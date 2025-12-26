# Audio Prompting Module — README

## Module Overview

The **Audio Prompting Module** teaches interns and reviewers how to design effective prompts for audio AI systems. This module focuses on prompt engineering for voice synthesis, voice conversion, audio analysis, and voice-driven applications.

The module is **not** about generating audio outputs, deploying AI models, or writing application code. Instead, it provides a decision-making framework for specifying what you want from audio AI systems through well-structured prompts.

---

## Learning Goal

By completing this module, participants will be able to:

- Understand the six categories of audio prompts and when to use each
- Write clear, complete, and reusable audio prompts
- Apply voice attributes (emotion, pace, accent, age) appropriately
- Handle safety and consent requirements (especially voice cloning)
- Evaluate audio prompts against a quality standard
- Adapt prompts for different audiences and accessibility needs

---

## Reading Order

**Start here and follow in sequence:**

### 1. **This file (AUDIO_README.md)** — Entry point
   - Orients you to the module structure and goals.
   - Explains the relationship between files.

### 2. **AUDIO_GUIDELINES.md** — Scope & quality reference (~5 min read)
   - Defines what kinds of audio prompts exist.
   - Specifies mandatory prompt dimensions.
   - Lists the quality checklist.
   - **Purpose:** Understand the "what" and "why" before diving into detailed teaching.

### 3. **WEEK3_AUDIO_PROMPTING.md** — Core curriculum (~30–45 min study)
   - **THIS IS THE SOURCE OF TRUTH** for learning how to write audio prompts.
   - Covers Days 15–21 of the 1-month course.
   - Includes decision rules per prompt field.
   - Provides reusable prompt templates.
   - Includes evaluation checklist and reflection questions.
   - **Purpose:** Learn how to think and act while writing audio prompts.

---

## File Roles Explained

| File | Role | Read If You Want To... |
|------|------|------------------------|
| AUDIO_README.md (this file) | Entry point & navigation | Understand module structure and where to start |
| AUDIO_GUIDELINES.md | Governance & reference layer | Know the mandatory requirements and quality bar (management/review perspective) |
| WEEK3_AUDIO_PROMPTING.md | **Core curriculum (source of truth)** | **Learn HOW to write audio prompts** (intern/learner perspective) |

---

## Key Principles

1. **Complete prompts are reusable.** Every audio prompt should specify: use case, input, voice attributes, output format, and safety constraints.

2. **Safety and consent matter.** Voice cloning, speaker identification, and biometric features require explicit consent and documentation.

3. **Accessibility is mandatory.** Audio prompts for critical content (health, safety, instructions) must include slower-pace and transcript options.

4. **Emotion and pace are intentional choices.** Do not default to neutral or moderate; choose and justify each voice attribute based on use case.

5. **Model-agnostic design.** Prompts should work across different audio AI systems, not be tailored to one vendor.

---

## Daily LMS Submission Map

Each day, interns submit their work through the LMS. Here's what they submit and how WEEK3_AUDIO_PROMPTING.md guides that work:

- **Daily deliverable:** 1–2 complete audio prompts per submission (not partial drafts).
- **What each prompt includes:**
  - Structured prompt (use case, script, voice attributes, output format, safety constraints).
  - Notes explaining key decisions (e.g., "Why did I choose this emotion?" "How does this serve the learner?").
  - Reference to specific guideline section from WEEK3_AUDIO_PROMPTING.md (e.g., "Day 16 — Tone & Emotion; category: Podcast").
- **Quality expected:** Prompts are scored against AUDIO_GUIDELINES.md checklist; 80%+ of submissions must score ≥ 3.5 to advance.
- **Feedback loop:** Reviewers use AUDIO_GUIDELINES.md rejection criteria to assess submissions within 24 hours. Interns revise and resubmit.
- **Weekly review:** Lead instructor samples 2–3 prompts per intern, assigns peer review scores, and publishes aggregate report (see PRODUCTIVITY_METRICS.md).
- **Templates as guide:** Interns use the reusable templates in WEEK3_AUDIO_PROMPTING.md as starting points, then customize for their assigned audio category.

---

## How to Use This Module

### For Interns or Learners:
1. Read **AUDIO_GUIDELINES.md** (quick reference).
2. Study **WEEK3_AUDIO_PROMPTING.md** in detail (Days 15–21).
3. Use the prompt templates and checklists in WEEK3_AUDIO_PROMPTING.md to draft prompts.
4. Review your work against the quality checklist in both files.

### For Reviewers or Quality Checkers:
1. Consult **AUDIO_GUIDELINES.md** for the mandatory dimensions and quality bar.
2. Use the evaluation checklist in **WEEK3_AUDIO_PROMPTING.md** (Day 21 section) to assess submitted prompts.

### For Managers or Stakeholders:
1. Start with **AUDIO_GUIDELINES.md** to understand scope and governance.
2. Reference **WEEK3_AUDIO_PROMPTING.md** to understand curriculum depth and learner outcomes.

---

## Questions Answered Here

| Q | A |
|---|---|
| What is this module about? | Teaching how to write effective prompts for audio AI systems. |
| Where should I start? | Read this file, then AUDIO_GUIDELINES.md, then WEEK3_AUDIO_PROMPTING.md. |
| What is the source of truth? | WEEK3_AUDIO_PROMPTING.md — all detailed learning and templates are there. |
| What does AUDIO_GUIDELINES.md do? | It lists mandatory requirements and the quality checklist; it's a reference layer, not teaching. |
| Will I generate audio? | No. This module teaches prompt design, not audio generation or deployment. |
| Do I need coding skills? | No. This module is model-agnostic and does not require coding. |

---

## Next Steps

1. **Proceed to** [AUDIO_GUIDELINES.md](AUDIO_GUIDELINES.md) for a 5-minute overview of scope and requirements.
2. **Then study** [WEEK3_AUDIO_PROMPTING.md](WEEK3_AUDIO_PROMPTING.md) for detailed curriculum.
