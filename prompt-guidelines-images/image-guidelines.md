# Week 2 — Image Prompting (Days 8–14)

This document provides **model-agnostic prompt guidelines, templates, and decision rules** for image AI prompting.  
It is intended for interns learning to design prompts for **image generation outputs** (illustrations, photographs, renders, and visual narratives).

**Focus:** how to think and specify visual fields clearly.  
**Out of scope:** UI code, vendor names, or image generation APIs.

---

## Prompt Field Guidance (Decision Rules)

When constructing an image prompt, treat each field as a **controlled visual parameter**.  
For each field below, ask the decision questions and follow the rule to choose values.

---

### Subject / Scene Description

- **Decision questions**
  - What is the main subject (person, object, place)?
  - Is there one subject or multiple?
  - Which attributes are essential vs optional?
- **Rule**
  - Describe subjects using **literal nouns and visible attributes only**.
  - Avoid opinions, emotions, metaphors, or symbolism.
  - If multiple subjects exist, state their relationship clearly.

---

### Environment / Background

- **Decision questions**
  - Where is the subject located?
  - Is the background contextual or neutral?
- **Rule**
  - Use **concrete physical locations**.
  - Prefer simple environments unless complexity is required.
  - Avoid abstract descriptors like “professional” or “dreamy”.

---

### Style / Visual Domain

- **Decision questions**
  - Should the image look like a real photo or an artwork?
  - Is realism required for the use case?
- **Rule**
  - Choose **one primary style only**.
  - Do not mix styles unless explicitly required.
  - Use standard domains (photorealistic, illustration, anime, 3D render, sketch).

---

### Art Style / Photography Technique

- **Decision questions**
  - Is this closer to fine art or photography?
  - Does lighting or capture method matter?
- **Rule**
  - Select a **single art or photography approach**.
  - Keep descriptions short and factual.
  - Avoid stacking stylistic adjectives.

---

### Visual Mood

- **Decision questions**
  - Is emotional tone necessary for interpretation?
- **Rule**
  - Mood is optional.
  - If used, choose **one simple descriptor**.
  - Do not use mood to replace missing visual details.

---

### Composition / Layout

- **Decision questions**
  - How close is the camera?
  - Where should attention be focused?
- **Rule**
  - Always specify framing (close, medium, wide).
  - Default to centered composition unless deviation is intentional.

---

### Framing & Perspective

- **Decision questions**
  - From which angle is the subject viewed?
- **Rule**
  - Specify viewpoint explicitly (front, side, top, angled).
  - Avoid leaving perspective implicit.

---

### Character / Subject Consistency

- **Decision questions**
  - Will this subject appear in multiple images?
- **Rule**
  - Fix attributes early.
  - Reuse the same descriptors across prompts.
  - Avoid adding new details unintentionally.

---

### Negative Prompting (Exclusions)

- **Decision questions**
  - What common visual errors should be avoided?
- **Rule**
  - Explicitly list unwanted artifacts.
  - Use short exclusion tokens.
  - Avoid narrative phrasing.

---

### Advanced Parameters (Technical Controls)

- **Decision questions**
  - Does format or reproducibility matter?
- **Rule**
  - Specify aspect ratio and quality intent.
  - Treat seeds and low-level parameters as system-controlled.

---

## Day 8 — Visual Language Fundamentals

### Describing Images for AI Generation

- **What image prompting is**

  - High-level: translating visual intent into structured textual description.
  - Practical: prompts act as blueprints for what must appear and how it should be viewed.

- **How to describe images**

  - Use physical descriptors.
  - Name visible attributes.
  - Describe spatial relationships.

- **Common mistakes**

  - Emotional adjectives instead of visual facts.
  - Assuming implicit context.
  - Combining multiple ideas in one sentence.

- **Checklist**
  - Subject clearly named.
  - Environment specified.
  - No abstract language.

---

## Day 9 — Style and Aesthetic Control

### Art Styles, Photography Techniques, Visual Mood

- **Style taxonomy**

  - Photorealistic
  - Illustration
  - Anime
  - 3D render
  - Sketch

- **Rules**
  - Choose one style.
  - Keep style independent of subject.
  - Avoid encoding mood into style unless required.

---

## Day 10 — Composition and Layout

### Framing, Perspective, and Visual Balance

- **Framing definitions**

  - Close-up: detail emphasis
  - Medium shot: subject clarity
  - Wide shot: context emphasis

- **Balance rules**

  - Default to centered subjects.
  - Deviate only with purpose.

- **Prompt rules**
  - Framing must be explicit.
  - Composition must support clarity.

---

## Day 11 — Character and Subject Design

### Consistent Character Creation and Details

- **Consistency principles**

  - Characters must remain visually stable.
  - Attributes should not drift across prompts.

- **Required attributes**

  - Physical traits
  - Clothing
  - Accessories (if any)

- **Mistakes to avoid**
  - Changing clothes or features unintentionally.
  - Altering age or proportions without reason.

---

## Day 12 — Negative Prompting

### Excluding Unwanted Elements

- **Purpose**

  - Prevent common generative failures.

- **Typical exclusions**

  - Blur
  - Distortion
  - Extra limbs
  - Text or logos
  - Low resolution

- **Rules**
  - Use list format only.
  - Keep exclusions reusable and generic.

---

## Day 13 — Advanced Image Parameters

### Aspect Ratios, Seeds, and Technical Controls

- **Aspect ratios**

  - Square (1:1)
  - Landscape (16:9)
  - Portrait (9:16)

- **Seeds**

  - Used for reproducibility.
  - Treated as technical metadata.

- **Prompt rule**
  - Avoid overloading prompts with low-level controls.

---

## Day 14 — Image Prompting Capstone

### Complex Visual Narrative Creation

- **What a good final prompt includes**

  - Complete subject specification.
  - Single style.
  - Explicit composition.
  - Clear exclusions.

- **Capstone task**
  - Create a controlled image set:
    - Same subject
    - Same style
    - One changing variable (angle, pose, or lighting)

---

## Reusable Prompt Templates (Model-Agnostic)

### Basic Single-Image Template
