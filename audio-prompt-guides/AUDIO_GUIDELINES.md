# Audio Prompt Guidelines — Scope & Quality Reference

**Purpose:** This document defines the scope, quality expectations, and mandatory dimensions for all audio prompts in this repository. It serves as the **quality gate for reviewing LMS submissions**—not a teaching guide. Reviewers use this document to accept or reject learner and content team submissions. For detailed curriculum content, see [WEEK3_AUDIO_PROMPTING.md](WEEK3_AUDIO_PROMPTING.md).

---

## Audio Prompt Taxonomy

All audio prompts fall into one of these categories:

| Category | Purpose | Primary Output |
|----------|---------|-----------------|
| Voice Synthesis | Generate spoken audio from text | Audio file (WAV, MP3, etc.) |
| Audio Analysis | Extract or understand audio content | Transcript, metadata, insights |
| Voice Conversion | Modify voice characteristics (emotion, accent, timbre, pace) | Audio file (modified) |
| Sound Design | Compose background, SFX, or spatial audio | Audio file (composited) |
| Audio-to-Text | Convert audio to structured text | Transcript, segmentation, metadata |
| Voice Agents | Multi-turn spoken interaction | Dialog logs, audio responses |

---

## Mandatory Prompt Dimensions

Every audio prompt **must** specify:

1. **Use Case** — What will the audio be used for (e.g., IVR menu, podcast narration, training module)?
2. **Input / Source** — What is the input (text, audio file, script)?
3. **Voice Attributes** — Emotion, pace, accent, gender/age (or explicit omission with rationale).
4. **Output Format** — Desired codec, sample rate, channels, duration, or delivery mechanism.
5. **Safety & Consent** — PII handling, voice cloning consent, licensing rights, accessibility requirements.

---

## Audio Prompt Quality Checklist

All audio prompts must meet these criteria before acceptance:

- ✓ Use case is explicitly stated and justified.
- ✓ All voice attributes are specified (or omissions are reasoned).
- ✓ Input type and output format are unambiguous.
- ✓ Pronunciation hints and pause markers are provided where needed.
- ✓ Safety constraints are documented (e.g., PII scrubbing, consent for voice cloning, licensing).
- ✓ Accessibility options are included (slower pace variant, transcript, captions).
- ✓ Prompt is reusable and parameterized (not a one-off script).
- ✓ Examples and acceptance tests are provided or referenced.

---

## When to REJECT a Prompt

A prompt **must be rejected** if it violates any of the following:

### 1. Missing or Unclear Use Case
- **Reject if:** No use case stated, or use case is vague (e.g., "general narration").
- **Example:** ❌ "Script: Welcome to our service. Please speak clearly." [No use case, unclear output format]
- **Acceptable:** ✓ "Use case: IVR main menu for financial services. Voice: neutral, slow pace. Output: segmented with 500ms pauses between options."

### 2. Unsafe Voice Cloning Without Consent
- **Reject if:** Prompt uses voice cloning, speaker identification, or biometric voice features **without documented explicit consent**.
- **Example:** ❌ "Clone the voice of [Person's Name] for this script." [No consent documentation provided]
- **Acceptable:** ✓ "Voice synthesis: Adult male, neutral accent (no cloning). Consent: not applicable. Output format: MP3, 44.1kHz."

### 3. PII Exposure Without Handling Plan
- **Reject if:** Prompt includes or implies PII (names, phone numbers, addresses) without explicit handling instructions.
- **Example:** ❌ "Script: Thank you, John. Your account number is 5551234567." [No mention of PII scrubbing or anonymization]
- **Acceptable:** ✓ "Script: Thank you, [CUSTOMER_NAME]. Your account number is [ACCT_NUM]. Safety: All PII redacted before training data use. Output will not be logged."

### 4. Critical Content Without Accessibility
- **Reject if:** Prompt is for health, safety, emergency, or compliance content **without slower-pace and transcript options**.
- **Example:** ❌ "Medical instruction: Fast pace, no transcript variant." [Violates accessibility mandate]
- **Acceptable:** ✓ "Use case: Medical device instructions. Pace: slow (clear for non-native speakers). Accessibility: Slower pace variant included; full transcript and captions required."

### 5. Non-Reusable, One-Off Script
- **Reject if:** Prompt is a one-off with hard-coded values; no parameterization for reuse.
- **Example:** ❌ "Script: Hello Sarah, your appointment is Tuesday at 2 PM." [Hard-coded name and time; not reusable]
- **Acceptable:** ✓ "Template: Hello [CUSTOMER_NAME], your appointment is [DATE] at [TIME]. Voice attributes: warm, moderate pace. Parameterized fields: CUSTOMER_NAME, DATE, TIME."

### 6. Vague or Missing Output Format
- **Reject if:** Output codec, sample rate, channels, or delivery mechanism is not specified.
- **Example:** ❌ "Output: audio file." [Ambiguous]
- **Acceptable:** ✓ "Output format: MP3, 128 kbps, 44.1 kHz, mono. Delivery: LMS streaming (< 10 sec latency)."

---

## Reviewer Checklist (Fast Review)

Use this checklist when reviewing submissions. If any criterion is failed, **REJECT and request revision**.

| Criterion | Required? | Present? | Reviewer Action |
|-----------|-----------|----------|-----------------|
| Use case explicitly stated | YES | [ ] Yes [ ] No | ❌ REJECT if No |
| Input source specified | YES | [ ] Yes [ ] No | ❌ REJECT if No |
| Voice attributes (E, P, A, G, Age) all specified OR reasoned omission | YES | [ ] Yes [ ] No | ❌ REJECT if No |
| Output format (codec, sample rate, channels) specified | YES | [ ] Yes [ ] No | ❌ REJECT if No |
| Safety constraints documented | YES | [ ] Yes [ ] No | ❌ REJECT if No |
| Consent documentation (if voice cloning) | CONDITIONAL | [ ] Yes [ ] N/A [ ] No | ❌ REJECT if voice cloning + No consent |
| Accessibility options included (for critical content) | CONDITIONAL | [ ] Yes [ ] N/A [ ] No | ❌ REJECT if critical content + No accessibility |
| Parameterized and reusable (not one-off) | YES | [ ] Yes [ ] No | ❌ REJECT if No |
| Examples or acceptance tests provided | YES | [ ] Yes [ ] No | ⚠️ REQUEST REVISION if No |

**Decision:** If all criteria are YES or N/A, **APPROVE**. If any critical criterion fails, **REJECT with specific reason and request revision**.

---

## Safety & Consent Requirements

### Voice Cloning and Synthesis
- **Explicit consent required:** Any prompt using voice cloning, speaker identification, or biometric voice features must include documented consent from the speaker or rights holder.
- **Licensing clarity:** Specify whether the output may be used commercially, in training, or in evaluation.
- **Disclosure:** Outputs containing synthesized or cloned voices must be labeled as such.

### PII Handling
- Prompts must define how personally identifiable information (names, phone numbers, addresses, etc.) in scripts or audio will be handled.
- Specify if PII should be redacted, anonymized, or excluded from training data.

### Accessibility
- Prompts targeting sensitive audiences (e.g., health, safety, emergency content) must include slower-pace and captioned variants.
- Audio quality and intelligibility are non-negotiable for critical content (e.g., medical instructions, safety alerts).

---

## For Detailed Teaching & Examples

For curriculum content, prompt templates, and step-by-step guidance on writing audio prompts, refer to:
**→ [WEEK3_AUDIO_PROMPTING.md](WEEK3_AUDIO_PROMPTING.md)**

This document covers Days 15–21, decision rules per prompt field, prompt categories with detailed guidance, and capstone evaluation rubrics.

---

## Questions This Document Answers

| Q | A |
|---|---|
| What kinds of audio prompts exist in this repository? | Six categories: Voice Synthesis, Audio Analysis, Voice Conversion, Sound Design, Audio-to-Text, Voice Agents |
| What must every audio prompt specify? | Use case, input, voice attributes, output format, safety & consent |
| What is the minimum quality bar? | All items in the Quality Checklist above must be met |
| Where do I learn to write audio prompts? | WEEK3_AUDIO_PROMPTING.md (curriculum) |
| What are the safety and consent rules? | Voice cloning requires explicit consent; PII handling must be defined; accessibility required for critical content |
