# Productivity Metrics — LMS Content Team

**Purpose:** Measure contribution quality fairly and objectively. Metrics reflect both output volume and prompt quality. Emphasis is on **reusable, well-documented prompts**, not raw task count.

**Data Source:** All metrics are derived from LMS submissions. Learners submit prompts daily via the LMS; reviewers assess these submissions and record scores in the LMS. Metrics are aggregated from LMS data weekly.

---

## LMS Submission Data Flow

- **Daily submissions:** Learners submit 1–2 prompts per day via LMS (Prompt field, Output field, Notes field).
- **Reviewer assessment:** Within 24 hours, assigned reviewer scores the submission using `AUDIO_GUIDELINES.md` checklist and `GUIDELINE_TEMPLATE.md` rubric.
- **Iteration tracking:** LMS shows revision history. Iteration count = number of resubmissions before approval.
- **Time tracking:** Learner timestamps (LMS auto-records submission time). Lead reviewer notes estimated effort in LMS comments.
- **Weekly aggregation:** Friday 17:00 — lead reviewer exports metrics from LMS and populates weekly report.

---

## Core Metrics (Tracked Weekly)

### 1. Tasks Claimed / Completed
- **What it measures:** Ownership and follow-through.
- **Data source:** LMS submission log (task ID + completion status).
- **Good performance:** Claim 1–2 tasks per week; complete within due date.
- **Poor performance:** Claim tasks but don't complete; miss deadlines without communication.
- **Note:** Quality matters more than quantity; one excellent prompt beats three mediocre ones.

### 2. Average Prompt Iterations (Draft → Final)
- **What it measures:** Efficiency and self-sufficiency in prompt refinement.
- **Data source:** LMS revision history per submission. Iteration count = resubmissions before final approval.
- **Good performance:** 2–3 iterations to approval (showing thoughtful initial work).
- **Concerning performance:** > 5 iterations (suggests unclear requirements or lack of planning).
- **Exceptional:** 1–2 iterations (rare; indicates deep understanding of requirements).
- **Formula:** (Total iterations across all prompts) / (Number of prompts submitted).

### 3. Peer Review Score (1–5)
- **What it measures:** Quality as perceived by reviewers.
- **Data source:** LMS reviewer notes field. Peer scores are recorded in LMS comments using `GUIDELINE_TEMPLATE.md` rubric (Clarity, Completeness, Robustness, Reusability, Safety).
- **1–2:** Incomplete, unsafe, or unclear; major revisions needed.
- **3:** Acceptable; meets minimum requirements; minor improvements suggested.
- **4:** Good; meets all requirements; demonstrates strong decision-making.
- **5:** Excellent; goes beyond requirements; reusable, well-documented, accessible.
- **Sampling method:** Lead reviewer samples 2–3 submissions per person per week (rotating basis). Sample is scored; aggregate becomes weekly peer score.

### 4. Time Spent per Task (Hours)
- **What it measures:** Realistic effort allocation and workload balance.
- **Data source:** LMS timestamp metadata + reviewer notes. Lead reviewer estimates effort based on submission timestamps and notes burden level (e.g., "10 hours" or "quick refinement").
- **Baseline:** 4–8 hours per prompt (varies by category and complexity).
- **Outliers:** < 2 hours suggests rushing; > 12 hours suggests unclear scope or blocker.
- **Action:** If outlier, discuss in 1:1 to identify root cause (scope creep, unclear requirements, etc.).

### 5. Reusability Score (% of Prompts Meeting Template Standard)
- **What it measures:** Adherence to standards and future reusability.
- **Data source:** LMS reviewer checklist (does submission follow `GUIDELINE_TEMPLATE.md`?). Recorded as YES/NO in LMS.
- **Good performance:** ≥ 80% of submitted prompts follow approved template structure.
- **Prompts deemed reusable if:** They include use case, voice attributes, output format, safety constraints, and accessibility options (verified via LMS checklist).
- **Formula:** (Reusable prompts submitted) / (Total prompts submitted) × 100.

### 6. Delivery On-Time Rate (%)
- **What it measures:** Reliability and commitment to deadlines.
- **Data source:** LMS submission timestamps + task due date. Calculated as: (Submissions by due date) / (Total submissions due) × 100.
- **Good performance:** ≥ 90% of tasks completed by due date.
- **Acceptable:** 75–89% (with documented blockers or communication).
- **Concerning:** < 75% (suggests planning or estimation issues).
- **Note:** Communication about delays (logged in LMS notes) counts toward reliability; silence does not.

---

## Prompt Quality Rubric (Detailed)

All submitted prompts are scored 1–5 on each dimension:

| Dimension | 1 (Poor) | 3 (Acceptable) | 5 (Excellent) |
|-----------|----------|----------------|---------------|
| **Clarity** | Instructions are ambiguous or incomplete. | Instructions are clear; most edge cases handled. | Instructions are precise, unambiguous; all edge cases addressed. |
| **Completeness** | Missing critical metadata (use case, voice attributes, safety). | Includes required metadata; some reasoning omitted. | All required metadata present; reasoning documented for every choice. |
| **Robustness** | Prompt fails for common variations; hard-coded assumptions. | Prompt works for standard inputs; parameterized. | Prompt works across input variations; handles errors gracefully. |
| **Reusability** | One-off script; not adaptable. | Adaptable for similar use cases; partial template structure. | Reusable template; easily adapted by others; modular design. |
| **Safety** | No safety constraints mentioned; misses PII/consent issues. | Basic safety constraints present; may miss some edge cases. | Comprehensive safety plan (PII, consent, accessibility); documented rationale. |

**Average across dimensions becomes the Peer Review Score (1–5).**

---

## Weekly Report Template

Submit by **Friday 17:00** to lead reviewer.

| Person | Tasks Claimed | Tasks Completed | Avg Iterations | Peer Score (1–5) | Reusability % | Hours Spent | On-Time Rate | Blockers / Notes |
|--------|---------------|-----------------|-----------------|------------------|---------------|-------------|--------------|-----------------|
| Jane   | 2             | 2               | 2.5             | 4.2              | 100%          | 10          | 100%         | All on track     |
| Marcus | 2             | 1               | 4.0             | 3.5              | 75%           | 14          | 50%          | Waiting on design feedback for Task #5 |
| Alex   | 1             | 1               | 1.0             | 4.8              | 100%          | 6           | 100%         | Completed early; quality excellent |

---

## Interpretation Guidelines

### Green Flags (Strong Performance)
- Peer score ≥ 4.0
- Reusability ≥ 80%
- 2–3 iterations average
- On-time rate ≥ 90%
- Clear, concise notes

### Yellow Flags (Needs Support)
- Peer score 2.5–3.5
- Reusability 50–79%
- > 4 iterations average
- 50–89% on-time rate
- Recurring blockers

### Red Flags (Intervention Required)
- Peer score < 2.5
- Reusability < 50%
- > 6 iterations average
- On-time rate < 50%
- Frequent missing deadlines without communication

---

## Weekly Review Process

1. **LMS data export:** Lead reviewer exports submission data from LMS (Friday 17:00).
2. **Sampling and scoring:** Lead reviewer samples 2–3 prompts per learner. Uses `GUIDELINE_TEMPLATE.md` rubric and `AUDIO_GUIDELINES.md` checklist to score. Records peer scores in LMS.
3. **Metrics aggregation:** Calculate week's metrics from LMS data and sample scores.
4. **1:1 sync (if needed):** If yellow/red flags present, discuss root cause and adjustments. Reference specific LMS submissions.
5. **Team report:** Lead publishes summary of team performance by Monday (aggregate + individual flagged items).

---

## Principles

- **Quality over quantity:** One excellent prompt (5/5) is worth more than three mediocre ones (2/5 each).
- **Transparency:** Metrics are visible to team; no surprises in reviews.
- **Fair assessment:** Blockers and external factors are considered; not punitive for unavoidable delays.
- **Growth mindset:** Low scores trigger support, not punishment; goal is improvement.
- **Consistency:** Same rubric applied to all team members.
