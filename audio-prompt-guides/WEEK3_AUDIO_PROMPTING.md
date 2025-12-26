# Week 3 — Audio Prompting (Days 15–21)

This document provides model-agnostic prompt guidelines, templates, and decision rules for audio AI prompting. It is intended for interns learning to design prompts for audio outputs (voice synthesis, narration, and voice-driven systems). Focus on how to think and specify fields; do not include UI code, vendor names, or audio generation.

## Prompt Field Guidance (decision rules)

When constructing an audio prompt, treat each field as a tunable parameter. For each field below, ask the decision questions and follow the short rule to choose values.

- Text / Script
  - Decision questions: Who is the audience? Is this informational, persuasive, instructional, or narrative? Are there any words that need explicit pronunciation or spelling? Do you need structured output (timestamps, segments)?
  - Rule: Write natural, spoken-style text; keep sentences short for clarity. Prefer conversational phrasing for narration and imperative clarity for instructions. Note ambiguous words and provide phonetic hints if precise pronunciation is required.

- Accent
  - Decision questions: Does the target audience expect a regional accent? Will an accent affect intelligibility or inclusivity? Is accent required for character or locale authenticity?
  - Rule: Prefer a neutral, widely intelligible accent unless the use case requires regional flavor. Document why a regional accent is chosen and provide examples/references for the desired accent characteristics.

- Emotion
  - Decision questions: What is the primary communicative goal (inform, excite, reassure)? Should the voice convey subtext (sympathy, urgency)? Are multiple emotions present across sections?
  - Rule: Choose one primary emotion and at most one secondary emotion. Avoid conflicting emotional instructions within a single short script — break scripts into segments with their own emotion if needed.

- Pace
  - Decision questions: Is the content meant for careful comprehension (slow), general listening (moderate), or energetic delivery (fast)? Are there places that need deliberate pauses for emphasis or accessibility?
  - Rule: Specify overall pace (slow / moderate / fast) and mark explicit pause locations. Use relative descriptors (e.g., "30% slower than conversational speed") when precise control is required.

- Voice Gender
  - Decision questions: Does gender carry functional meaning for the use case (e.g., character role)? Could gender choice create bias or exclusivity?
  - Rule: Use gender only when relevant; otherwise prefer neutral descriptors (voice timbre, brightness) or offer multiple alternatives for inclusivity.

- Age Range
  - Decision questions: Should the voice sound like a child, young adult, middle-aged, or senior speaker? Is age important for credibility or empathy?
  - Rule: Specify an age band (child, teen, adult, middle-aged, senior) and provide guidance on timbre and energy to match that band.

- Use Case
  - Decision questions: Is this for narration, transactional messages, IVR menus, training content, or assistants? What are constraints (length, repetition, interactivity)?
  - Rule: State the use case clearly; this drives decisions about emotion, pace, and script style. Use-case should appear early in the prompt so the model treats other fields in context.

## Day 15 — Voice Synthesis Fundamentals

- What Text-to-Speech prompting is
  - High-level: the process of specifying a spoken output in text form using structured instructions for voice, emotion, pacing, and formatting.
  - Practical: prompts connect an authored script with metadata (voice properties) so the synthesizer produces consistent, predictable speech.

- How scripts should be written for spoken output
  - Use conversational sentence structure; write as you would speak aloud.
  - Keep sentences short (10–18 words) where comprehension is critical.
  - Break long paragraphs into smaller segments; indicate explicit breaks/pauses.
  - Mark specialized pronunciations: provide phonetic spellings or syllable emphasis when needed.
  - Indicate non-speech actions explicitly (e.g., [breath], [soft laugh], [pause 500ms]).

- Common mistakes when writing text for audio
  - Writing in dense, academic prose that reads poorly aloud.
  - Omitting punctuation or pause markers for long sentences.
  - Leaving ambiguous names/terms without pronunciation hints.
  - Mixing multiple unrelated instructions in one sentence (e.g., style + pacing + emotion without segmentation).

- Checklist for good voice synthesis prompts
  - Script written in spoken style and segmented.
  - Use case stated at the top.
  - Required voice properties listed (emotion, pace, accent, age, gender—or reasons to omit).
  - Pronunciations and pause locations annotated.
  - Output format specified (plain speech text, timestamped segments, or markup hints).

## Day 16 — Tone and Emotion Control

- Emotion taxonomy (practical set)
  - Neutral / Informative
  - Warm / Empathetic
  - Calm / Reassuring
  - Energetic / Excited
  - Serious / Authoritative
  - Urgent / Direct

- Mapping emotion to use cases
  - Neutral / Informative: news reading, documentation narration.
  - Warm / Empathetic: customer support callbacks, training modules with sensitive content.
  - Calm / Reassuring: healthcare instructions, safety announcements.
  - Energetic / Excited: ads, trailers, social snippets.
  - Serious / Authoritative: legal notices, policy updates.
  - Urgent / Direct: safety alerts, emergency instructions.

- Conflicting emotion scenarios to avoid
  - Mixing "energetic" with "reassuring" in the same short segment.
  - Switching emotions mid-sentence — prefer segment-level changes.

- Prompt guidance for emotional consistency
  - Set a primary emotion for the whole prompt.
  - If different sections require different emotions, label sections and attach emotion field per section.
  - Provide short examples of desired phrasing: show one sentence exhibiting the emotion and one that does not.

## Day 17 — Pacing and Rhythm

- Definitions
  - Slow: deliberate, clear enunciation; used for comprehension-sensitive content.
  - Moderate: everyday conversational speed; default for most narration.
  - Fast: higher words-per-minute for energetic content or short announcements.

- When to use pauses
  - After key information (e.g., phone numbers, steps).
  - To separate clauses that would otherwise run together.
  - To let the listener process complex instruction (long lists, steps).

- Accessibility considerations
  - Slow pace and explicit pauses improve access for non-native speakers and hearing-impaired listeners.
  - Include options for transcript and timestamped captions.
  - Avoid fast pace for content with dense information.

- Prompt rules for pacing control
  - Specify overall pace and annotate pause points: e.g., "Pace: moderate; pause 600ms after each step." 
  - Use numeric pause durations when precise timing matters.
  - For long-form content, allow natural variation: "moderate with slightly longer pauses between sections."

## Day 18 — Accent and Language Variation

- When accent selection matters
  - Audience comprehension and authenticity (character voices, regional content).
  - Accessibility: accents can increase or decrease intelligibility for certain audiences.

- Neutral vs regional accents
  - Neutral accent: default choice for broad intelligibility and professional content.
  - Regional accent: use for character authenticity or region-specific content; document rationale and provide references.

- Multilingual considerations
  - Provide language codes and transliteration instructions.
  - For mixed-language scripts, mark language boundaries and give pronunciation cues.
  - Specify whether code-switching is allowed and how it should be pronounced.

- Risks of accent mismatch
  - Miscommunication and perceived inauthenticity.
  - Unintended bias or stereotyping — avoid caricatured accents.

## Day 19 — Audio Content Creation: Prompt Categories

For each category below: recommended script style, emotion, pace, and accent considerations.

- Podcast narration
  - Script style: conversational, first-person or host-to-guest phrasing; include segment markers.
  - Emotion: warm / engaged; natural inflection.
  - Pace: moderate, with planned pauses for ad breaks and transitions.
  - Accent: neutral or audience-appropriate; consistency across hosts.

- Audiobooks
  - Script style: narrative prose with character labels; mark chapter and scene breaks.
  - Emotion: varies by scene — use section-level emotion tags.
  - Pace: moderate to slightly slow for complex prose; adapt for dialogue tempo.
  - Accent: character-based accents may be used sparingly and with sensitivity.

- Announcements (public addresses, transit)
  - Script style: concise, direct sentences; avoid idioms.
  - Emotion: neutral / authoritative.
  - Pace: moderate to slow; enforce clear enunciation.
  - Accent: neutral preferred for broad understanding.

- IVR systems (menus)
  - Script style: terse, action-oriented prompts; number-based options clearly separated.
  - Emotion: neutral / friendly.
  - Pace: slow to moderate; include clear pauses between options.
  - Accent: neutral; ensure high intelligibility.

- Training content (corporate learning)
  - Script style: instructive, stepwise; include examples and recap markers.
  - Emotion: calm / encouraging.
  - Pace: slow to moderate; add deliberate pauses after examples.
  - Accent: match learner population or neutral.

- News reading
  - Script style: factual, third-person; headlines first, detail next.
  - Emotion: neutral / serious.
  - Pace: moderate; allow slight acceleration for breaking updates but keep clarity.
  - Accent: neutral to match the outlet's style.

- Voice assistants (short responses)
  - Script style: short, confirmatory, and context-aware.
  - Emotion: neutral / friendly.
  - Pace: moderate to fast for brief replies.
  - Accent: configurable per user preference; default to neutral.

## Day 20 — Sound Design Integration

- Guidelines for background audio usage
  - Purpose-first: include background only if it supports comprehension or mood without masking speech.
  - Low-level: keep background audio low in relative level (SNR) compared to voice.
  - Consistency: maintain consistent background level across sections when used.

- When to include or avoid sound effects
  - Include when they aid navigation (e.g., success/failure cues) or realism (scene-setting).
  - Avoid when they distract from critical instructions, numbers, or names.

- Voice clarity vs background balance
  - Rule of thumb: speech should be at least 12 dB above background noise for clear intelligibility (document as guideline, not mandatory number).
  - If you cannot measure levels, require user-facing tests: ask for a listening check in quiet and noisy conditions.

- Prompting rules for clean audio output
  - Specify "voice-first" mixing: "Background: low, non-lyrical ambient; Voice: clear, centered; Reduce overlap with narration frequency bands." (keep technical language high-level)
  - If sound effects must align to speech, annotate timestamps or relative locations in the script.

## Day 21 — Audio Prompting Capstone

- What a “good” final audio prompt looks like
  - Includes: use case, complete script (segmented), voice attributes (emotion, pace, accent, gender, age), pause and pronunciation markers, and output expectations (format, segments).
  - Example structure (fill-in template):

  - Use case: [e.g., IVR menu for banking]
  - Script segment 1: "Welcome to Acme Bank. For accounts, press 1." [pause 600ms]
  - Voice attributes: Emotion=neutral; Pace=slow; Accent=neutral; Gender=any; Age=adult
  - Pronunciation notes: "Acme" -> [AK-me]
  - Deliverable: plain speech text with pause markers and timestamps

- Evaluation checklist for prompts
  - Use case specified and justified.
  - Script written in spoken style and segmented.
  - All voice attributes specified or reasoned omission present.
  - Pronunciations and pauses annotated where needed.
  - Accessibility considerations included (transcript, slower pace option).
  - Sound design instructions present if background audio is desired.

- Reflection questions for interns
  - Why did you choose the specified emotion and pace for this script?
  - What accessibility trade-offs did you consider?
  - How would you modify the prompt for a different audience (non-native speakers, older adults)?

- Criteria to judge prompt quality
  - Clarity: unambiguous instructions for the synthesizer.
  - Completeness: all necessary metadata present.
  - Robustness: prompt works across a range of inputs and can be segmented.
  - Inclusivity: avoids biased or exclusionary choices unless justified.
  - Testability: includes checks (sample inputs) to validate output.

## Reusable Prompt Templates (model-agnostic)

- Basic single-segment template

  - Use case: [SHORT DESCRIPTION]
  - Script: "[SCRIPT TEXT]"
  - Voice: Emotion=[emotion]; Pace=[slow|moderate|fast]; Accent=[neutral|region]; Gender=[male|female|neutral|other]; Age=[child|teen|adult|middle-aged|senior]
  - Pronunciation notes: [word -> phonetic]
  - Pauses: [locations and durations]
  - Output format: [plain text / segment timestamps / markup]

- Sectioned template (for multi-emotion or multi-pace scripts)

  - Use case: [SHORT DESCRIPTION]
  - Sections:
    - Section 1: name="Intro"; Script="..."; Emotion=[...]; Pace=[...]; Pause after=XXXms
    - Section 2: name="Main"; Script="..."; Emotion=[...]; Pace=[...]
  - Global: Accent=[...]; Voice gender/age=[...]
  - Sound design: Background=[none|ambient|music:style]; Level=[low|medium|high]
  - Deliverable: [detailed transcript with markup]

- IVR/menu template (concise)

  - Use case: IVR main menu
  - Script: "Welcome to [ORG]. For sales press 1. For support press 2." [pause 500ms between options]
  - Voice: Emotion=neutral; Pace=slow; Accent=neutral; Gender=any; Age=adult
  - Output: segmented lines with expected DTMF timings or natural pauses

## Quick Prompting Rules (summary)

- Always state the use case first.
- Use spoken-style script; break into segments.
- Choose one primary emotion; use per-section emotions when necessary.
- Specify overall pace and mark explicit pauses.
- Prefer neutral accent unless authenticity requires otherwise; document rationale.
- Include pronunciation hints for ambiguous terms.
- If background audio or SFX are required, include clear mixing intent and timestamps.

## Appendix — Short Validation Checklist (for interns to run)

- Read the prompt aloud: does it flow naturally?
- Check segment boundaries and pause markers.
- Verify pronunciation notes for unusual terms.
- Confirm use-case alignment with emotion/pacing choices.
- Ensure accessibility options are provided (slower variant and transcript).
