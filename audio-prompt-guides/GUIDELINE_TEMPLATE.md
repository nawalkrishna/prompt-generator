# Prompt Guideline Template

Use this template when building or reviewing prompts. This template is modality-agnostic and applies to text, audio, image, and video prompting.

---

## Prompt Specification Fields

| Field | Mandatory? | Purpose | Guidance |
|-------|-----------|---------|----------|
| **Goal** | YES | What the prompt should achieve | Be specific and measurable |
| **Audience / Persona** | YES | Who or what consumes the output | Include skill level, context, constraints |
| **Input constraints** | YES | Allowed inputs, size limits, formats | Define boundaries; avoid scope creep |
| **Output format** | YES | Expected output structure (schema, type, length) | Be precise; don't assume defaults |
| **Tone / Style** | CONDITIONAL | Voice, register, register, persona (for text/audio) | Omit only if not applicable to modality |
| **Core instructions** | YES | Step-by-step directions for the model | Clear, logical, sequenced |
| **Required fields** | YES | Critical attributes that must appear in output | Explicit list; no ambiguity |
| **Safety / Guardrails** | YES | Sensitive content checks, PII, consent, disallowed outputs | Document all constraints |
| **Examples** | YES | 2–3 good + 1 bad example with rationale | Show both success and failure modes |
| **Evaluation rubric** | YES | Quality criteria (clarity, completeness, accuracy, brevity) | Scored or categorical; reviewable |
| **Edge cases** | YES | Ambiguities and how to handle them | Anticipate common mistakes |

---

## LMS Submission Mapping

When submitting a prompt to the LMS, structure your submission as follows:

### Field: **Prompt** (LMS text area)
Map to template: Goal + Audience + Input constraints + Output format + Core instructions + Required fields + Examples.

**What to include in "Prompt":**
- State the goal (first sentence).
- Describe the audience and input format.
- Specify output format and required fields.
- Provide step-by-step core instructions.
- Include 2–3 good examples (show expected output).

**Example structure:**
```
Goal: Generate a concise social media caption.
Audience: Marketing team; posts to Instagram.
Input: Article headline and key takeaway.
Output format: Single paragraph, <280 characters, conversational tone.
Steps: 1) Extract key takeaway. 2) Craft engaging hook. 3) Add CTA.
Required: Hook + CTA + hashtag count ≤ 3.
Example 1 (good): "Discover the future of AI... [link]. #AI #Tech"
Example 2 (bad): [Shows over-long text with no CTA]
```

### Field: **Output** (LMS file upload or text area)
Map to template: Examples (actual model output or reference implementation).

**What to include in "Output":**
- If you ran the prompt through a system: paste the actual output.
- If demonstrating by hand: show 2–3 sample outputs from the prompt.
- Annotate with notes (e.g., "Output 1 meets spec: ✓ hook + CTA + hashtag count").

### Field: **Notes** (LMS text area)
Map to template: Safety / Guardrails + Edge cases + Evaluation rubric + Reflection.

**What to include in "Notes":**
- Safety constraints (PII handling, consent, disallowed content).
- Edge cases handled and how.
- Evaluation checklist (how will you know this prompt is working?).
- Self-reflection (why did you make these design choices?).

**Example structure:**
```
Safety: No customer data exposed. All examples anonymized.
Edge cases: Handles varying headline lengths; skips if input < 5 words.
Evaluation: 
  - Hook is engaging (subjective; human review).
  - Exactly ≤ 3 hashtags (objective).
  - CTA present (objective).
Reflection: Chose conversational tone to match platform norms (Instagram is informal).
```

---

## Mandatory Fields for LMS Submission

For any LMS submission to be accepted, the following **must** be present:

- ✓ **Goal** (explicit statement of what the prompt does)
- ✓ **Audience / Persona** (clear, specific)
- ✓ **Input constraints** (defined boundaries)
- ✓ **Output format** (unambiguous structure)
- ✓ **Core instructions** (step-by-step)
- ✓ **Required fields** (must-have output attributes)
- ✓ **Safety / Guardrails** (all relevant constraints documented)
- ✓ **Examples** (at least 2 good + 1 bad/edge case)
- ✓ **Evaluation rubric** (how to score this prompt's success)

**Optional fields** (omit only with documented reason):
- Tone / Style (N/A for some modalities)
- Edge cases (if none apply, state: "No known edge cases")

---

## Reviewer Checklist (Against This Template)

Use this checklist when reviewing submissions based on GUIDELINE_TEMPLATE.md:

| Field | Present? | Clear? | Complete? | Action |
|-------|----------|--------|-----------|--------|
| Goal | [ ] Yes [ ] No | [ ] Clear [ ] Vague | [ ] Complete [ ] Incomplete | ❌ REJECT if absent or vague |
| Audience / Persona | [ ] Yes [ ] No | [ ] Clear [ ] Vague | [ ] Complete [ ] Incomplete | ❌ REJECT if absent or too broad |
| Input constraints | [ ] Yes [ ] No | [ ] Clear [ ] Vague | [ ] Complete [ ] Incomplete | ❌ REJECT if absent or undefined |
| Output format | [ ] Yes [ ] No | [ ] Clear [ ] Vague | [ ] Complete [ ] Incomplete | ❌ REJECT if ambiguous |
| Core instructions | [ ] Yes [ ] No | [ ] Clear [ ] Vague | [ ] Complete [ ] Incomplete | ❌ REJECT if unclear or incomplete |
| Required fields | [ ] Yes [ ] No | [ ] Clear [ ] Vague | [ ] Complete [ ] Incomplete | ❌ REJECT if absent |
| Safety / Guardrails | [ ] Yes [ ] No | [ ] Clear [ ] Vague | [ ] Complete [ ] Incomplete | ❌ REJECT if inadequate for use case |
| Examples (2 good + 1 bad) | [ ] Yes [ ] No | [ ] Clear [ ] Vague | [ ] Complete [ ] Incomplete | ⚠️ REQUEST REVISION if < 3 examples |
| Evaluation rubric | [ ] Yes [ ] No | [ ] Clear [ ] Vague | [ ] Complete [ ] Incomplete | ⚠️ REQUEST REVISION if vague criteria |
| Edge cases (or "N/A") | [ ] Yes [ ] No | [ ] Clear [ ] Vague | [ ] Complete [ ] Incomplete | ⚠️ REQUEST REVISION if missing edge case handling |

**Decision:** All mandatory fields YES + CLEAR → **APPROVE**. Any field NO or VAGUE → **REQUEST REVISION or REJECT**.

---

## Authoring Best Practices

- **Be specific:** Avoid vague language ("good," "relevant," "appropriate"). Use measurable criteria.
- **Provide schema when structured output is required:** Use JSON, tables, or step-by-step format to clarify output expectations.
- **Include examples to reduce ambiguity:** Show both success and failure; annotate why each succeeds or fails.
- **Document safety first:** If sensitive, start with guardrails; don't append them as an afterthought.
- **Test your rubric:** Can a reviewer objectively score against it, or is it too subjective?
