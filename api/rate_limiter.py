"""
Simple in-memory rate limiter for Flask API.
For production, use Redis-backed rate limiting.
"""

import time
from functools import wraps
from flask import request, jsonify
from collections import defaultdict, deque


class RateLimiter:
    """
    Token bucket rate limiter implementation.
    Tracks requests per IP address.
    """

    def __init__(self, max_requests=60, window_seconds=60):
        """
        Initialize rate limiter.

        Args:
            max_requests: Maximum requests allowed in time window
            window_seconds: Time window in seconds
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(deque)

    def is_allowed(self, key):
        """
        Check if request is allowed for given key (e.g., IP address).

        Args:
            key: Identifier for rate limiting (usually IP address)

        Returns:
            bool: True if request is allowed, False otherwise
        """
        now = time.time()
        cutoff = now - self.window_seconds

        # Remove old requests outside the window
        while self.requests[key] and self.requests[key][0] < cutoff:
            self.requests[key].popleft()

        # Check if under limit
        if len(self.requests[key]) < self.max_requests:
            self.requests[key].append(now)
            return True

        return False

    def get_remaining(self, key):
        """
        Get remaining requests for key.

        Args:
            key: Identifier for rate limiting

        Returns:
            int: Number of remaining requests
        """
        now = time.time()
        cutoff = now - self.window_seconds

        # Clean up old requests
        while self.requests[key] and self.requests[key][0] < cutoff:
            self.requests[key].popleft()

        return max(0, self.max_requests - len(self.requests[key]))

    def get_reset_time(self, key):
        """
        Get time until rate limit resets.

        Args:
            key: Identifier for rate limiting

        Returns:
            int: Seconds until limit resets
        """
        if not self.requests[key]:
            return 0

        oldest_request = self.requests[key][0]
        reset_time = oldest_request + self.window_seconds
        return max(0, int(reset_time - time.time()))


# Global rate limiter instance
_rate_limiter = None


def get_rate_limiter(max_requests=60, window_seconds=60):
    """Get or create rate limiter instance."""
    global _rate_limiter
    if _rate_limiter is None:
        _rate_limiter = RateLimiter(max_requests, window_seconds)
    return _rate_limiter


def rate_limit(max_requests=60, window_seconds=60):
    """
    Decorator to rate limit Flask routes.

    Usage:
        @app.route('/endpoint')
        @rate_limit(max_requests=10, window_seconds=60)
        def my_endpoint():
            return 'Hello'

    Args:
        max_requests: Maximum requests per window
        window_seconds: Time window in seconds
    """

    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            limiter = get_rate_limiter(max_requests, window_seconds)

            # Get client identifier (IP address)
            client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
            if client_ip:
                # Handle multiple IPs in X-Forwarded-For
                client_ip = client_ip.split(",")[0].strip()

            # Check rate limit
            if not limiter.is_allowed(client_ip):
                remaining = limiter.get_remaining(client_ip)
                reset_time = limiter.get_reset_time(client_ip)

                response = jsonify(
                    {
                        "error": "Rate limit exceeded",
                        "message": f"Too many requests. Please try again in {reset_time} seconds.",
                    }
                )
                response.status_code = 429
                response.headers["X-RateLimit-Limit"] = str(max_requests)
                response.headers["X-RateLimit-Remaining"] = str(remaining)
                response.headers["X-RateLimit-Reset"] = str(reset_time)
                response.headers["Retry-After"] = str(reset_time)

                return response

            # Request allowed - add rate limit headers
            remaining = limiter.get_remaining(client_ip)
            response = f(*args, **kwargs)

            # Add rate limit headers to response
            if hasattr(response, "headers"):
                response.headers["X-RateLimit-Limit"] = str(max_requests)
                response.headers["X-RateLimit-Remaining"] = str(remaining)

            return response

        return wrapped

    return decorator


def sanitize_input(text, max_length=2000, allow_newlines=True):
    """
    Sanitize text input to prevent injection attacks.

    Args:
        text: Input text to sanitize
        max_length: Maximum allowed length
        allow_newlines: Whether to allow newline characters

    Returns:
        str: Sanitized text
    """
    if not isinstance(text, str):
        return ""

    # Trim to max length
    text = text[:max_length]

    # Remove null bytes
    text = text.replace("\x00", "")

    # Optionally remove newlines
    if not allow_newlines:
        text = text.replace("\n", " ").replace("\r", " ")

    # Remove excessive whitespace
    text = " ".join(text.split())

    return text.strip()


def sanitize_payload(payload, max_text_length=2000):
    """
    Sanitize entire payload dictionary.

    Args:
        payload: Dictionary of form data
        max_text_length: Maximum length for text fields

    Returns:
        dict: Sanitized payload
    """
    if not isinstance(payload, dict):
        return {}

    sanitized = {}

    for key, value in payload.items():
        if isinstance(value, str):
            sanitized[key] = sanitize_input(value, max_text_length)
        elif isinstance(value, (int, float)):
            sanitized[key] = value
        elif isinstance(value, list):
            # Sanitize list items if they're strings
            sanitized[key] = [
                sanitize_input(item, max_text_length)
                if isinstance(item, str)
                else item
                for item in value
            ]
        else:
            # Skip unsupported types
            continue

    return sanitized
