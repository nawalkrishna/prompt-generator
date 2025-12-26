# LMS Course Outlines — 1-month and 4-month

**Purpose:** Define learning pathways for two course durations (1-month intensive, 4-month comprehensive) across two learner profiles (coders and non-coders). These outlines map to modality-specific curriculum modules (text, audio, image, video) in the `prompt-guides/` directory.

**Execution Model:** Each week/month focuses on ONE modality. Learners complete that modality's guideline documents, submit prompts **daily via the LMS**, and receive peer review before advancing. Modality modules are self-contained and can be assembled in any order or deployed independently.

---

## Execution Framework: LMS & Repository Relationship

- **LMS is the submission and feedback platform.** All learner work (prompts, outputs, notes) is submitted daily through the LMS course interface. Learners do not interact with this repository.
- **Repository documents are reference standards.** Curriculum modules (e.g., `WEEK3_AUDIO_PROMPTING.md`) and evaluation checklists (e.g., `AUDIO_GUIDELINES.md`) live in this repository. Learners access these via the LMS (embedded or linked).
- **Assessment standards are repository-based.** Reviewers use `AUDIO_GUIDELINES.md`, `PRODUCTIVITY_METRICS.md`, and `GUIDELINE_TEMPLATE.md` to evaluate LMS submissions. Peer review scores are recorded in the LMS.
- **Daily cadence:** Learners submit 1–2 prompts per day via LMS; reviewers assess within 24 hours and provide feedback in LMS.

---

## 1-Month Intensive Course — Coders

**Target:** Software engineers, developers, technical founders  
**Delivery:** Live + async  
**Assessment:** Weekly peer review + capstone project  

| Week | Focus | Learning Objectives | Reference Documents | Deliverables |
|------|-------|--------------------|--------------------|--------------|
| 1 | **Foundations** | Understand prompt engineering paradigms; learn template structure; apply decision framework | `GUIDELINE_TEMPLATE.md`, `AUDIO_GUIDELINES.md` (or chosen modality) | 3–5 reusable prompt templates |
| 2 | **Modality Deep-Dive** (Choose ONE: Audio, Text, Image, or Video) | Master voice/style attributes, edge cases, safety constraints for chosen modality | `WEEK3_AUDIO_PROMPTING.md` (or equivalent modality module) | 5–8 prompts per category; peer score ≥ 3.5 |
| 3 | **Integration & Testing** | Chain prompts across modalities; build evaluation harness; test edge cases | Chosen modality module + `ASSIGNMENT_TRACKER.md` patterns | Working prompt chain; test suite; documentation |
| 4 | **Capstone** | Design end-to-end multi-prompt system; code review and peer feedback | All reference docs + `PRODUCTIVITY_METRICS.md` | Capstone project + code repo + reflection |

**Prerequisites:** None (but familiarity with APIs or scripting assumed).  
**Grading:** Peer review scores (see `PRODUCTIVITY_METRICS.md`); capstone rubric TBD.  
**Certificate:** Awarded on completion of all weeks + capstone approval (score ≥ 3.5).

---

## 1-Month Intensive Course — Non-Coders

**Target:** Content creators, marketers, product managers, support teams  
**Delivery:** Live + async with guided tools  
**Assessment:** Weekly practical assignments + portfolio  

| Week | Focus | Learning Objectives | Reference Documents | Deliverables |
|------|-------|--------------------|--------------------|--------------|
| 1 | **Concepts & Examples** | Understand what prompts do; learn safety/ethics; see real-world examples | `GUIDELINE_TEMPLATE.md`, `AUDIO_GUIDELINES.md` (or chosen modality) | Summary notes on 1 use case |
| 2 | **Hands-On: Chosen Modality** (Choose ONE: Audio, Text, Image, or Video) | Write 3–5 prompts using LMS tools; get peer feedback; iterate | `WEEK3_AUDIO_PROMPTING.md` (or equivalent modality module); templates provided | 3–5 completed prompts; no code required |
| 3 | **Templates & Workflows** | Reuse and adapt prompts for real scenarios (marketing, support, training) | Templates from Week 2 + `ASSIGNMENT_TRACKER.md` | 3 workflow prompt sets (e.g., "Email marketing", "Customer support") |
| 4 | **Portfolio & Certification** | Assemble 5 best prompts; prepare job-ready portfolio; present | Completed prompts from Weeks 2–3 + portfolio template | Portfolio deck + 5 polished prompts |

**Prerequisites:** None (no coding or technical skills required).  
**Grading:** Completeness of prompts; peer feedback positive/neutral; portfolio presentation.  
**Certificate:** Awarded on completion of all weeks + portfolio approval.

---

## 4-Month Comprehensive Course — Coders

**Target:** Engineers, AI specialists, product teams building prompt systems  
**Delivery:** Structured modules + self-paced labs  
**Assessment:** Monthly capstones + code reviews + group projects  

| Month | Focus | Learning Objectives | Modality Coverage | Reference Documents | Deliverables |
|-------|-------|--------------------|--------------------|---------------------|--------------|
| 1 | **Foundations & Frameworks** | Prompt engineering theory; decision trees; template patterns; safety frameworks | Intro (all modalities) | `GUIDELINE_TEMPLATE.md`; all modality `_GUIDELINES.md` files | Framework document + 2 starter templates |
| 2 | **Modality Mastery — First Pair** (Audio + Text, or Image + Video) | Deep dive into two modalities; advanced prompting patterns; edge case handling | Audio + Text (or Image + Video) | `WEEK3_AUDIO_PROMPTING.md` + text equivalent; `PRODUCTIVITY_METRICS.md` | 15+ prompts per modality; peer scores ≥ 4.0 |
| 3 | **Modality Mastery — Second Pair** (remaining modalities) | Second pair deep-dive; integration patterns; performance measurement | Video + Image (or Audio + Text) | `WEEK3_AUDIO_PROMPTING.md` + video/image equivalents | 15+ prompts; integration patterns document |
| 4 | **Capstone & Advanced Topics** | Build multimodal prompt system; evaluate at scale; document for production | Integration across all 4 modalities | All reference docs + optional advanced topics | Multimodal prompt system + monitoring dashboard + repo |

**Prerequisites:** Coding experience and familiarity with APIs.  
**Grading:** Monthly peer reviews; capstone code quality; team feedback.  
**Certificate:** Awarded on completion of all months + capstone approval (score ≥ 4.0).

---

## 4-Month Comprehensive Course — Non-Coders

**Target:** Content strategists, creative directors, learning designers, community managers  
**Delivery:** Cohort-based + hands-on labs  
**Assessment:** Monthly projects + peer critique + portfolio evolution  

| Month | Focus | Learning Objectives | Modality Coverage | Reference Documents | Deliverables |
|-------|-------|--------------------|--------------------|---------------------|--------------|
| 1 | **Foundations & Ethics** | Prompt design theory; taxonomy of use cases; safety/consent; accessibility | Intro (all modalities) | `GUIDELINE_TEMPLATE.md`; all modality `_GUIDELINES.md` files | Use case mapping document + 1 baseline prompt set |
| 2 | **Content Creation Labs — First Pair** (Audio + Text, or Image + Video) | Write prompts for marketing, support, learning; iterate with feedback; build templates | Audio + Text (or Image + Video) | `WEEK3_AUDIO_PROMPTING.md` + text equivalent | 12+ production-ready prompts per modality |
| 3 | **Content Creation Labs — Second Pair** (remaining modalities) | Second pair; advanced styling, persona control, workflow automation | Video + Image (or Audio + Text) | Modality modules + workflow templates | 12+ production-ready prompts; 2 workflow templates |
| 4 | **Portfolio & Deployment** | Curate portfolio; design client pitch; prepare certification project | All 4 modalities + client templates | Portfolio template + client pitch template | Portfolio (20+ best prompts) + pitch deck + certification project |

**Prerequisites:** None (no coding required; tools provided via LMS).  
**Grading:** Completeness of prompts; peer critique feedback; portfolio quality.  
**Certificate:** Awarded on completion of all months + certification project approval.

---

## Document Reference Map

| Document | Used In | Purpose |
|----------|---------|---------|
| `GUIDELINE_TEMPLATE.md` | All courses, Week/Month 1 | Onboarding: what every prompt needs |
| `AUDIO_GUIDELINES.md` | All courses | Scope and quality bar for audio prompts (management reference) |
| `WEEK3_AUDIO_PROMPTING.md` | All courses, audio modules | Core curriculum: how to write audio prompts |
| `ASSIGNMENT_TRACKER.md` | All courses | Task ownership and team coordination |
| `PRODUCTIVITY_METRICS.md` | All courses | Weekly peer review and performance measurement |

---

## Execution Notes

1. **Modular by design:** Each modality (audio, text, image, video) is a self-contained learning unit. Instructors can sequence them in any order based on cohort needs.

2. **Peer review cadence:** Weekly reports due Friday 17:00 (all learners). Lead instructor reviews and provides feedback by Monday.

3. **Template reuse:** Learners are expected to parameterize and reuse templates. Quality score rewards reusability (see `PRODUCTIVITY_METRICS.md`).

4. **Capstone scoping:** 1-month capstones are single-modality; 4-month capstones integrate multiple modalities and include deployment considerations.

5. **Certification:** Both certificates are work-product based (portfolio of prompts), not exam-based. Emphasis is on demonstrated competency, not test scores.
