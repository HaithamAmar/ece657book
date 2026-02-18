# Write-up Tasks (Optional Continuity Enrichment)

- Date: 2026-02-18
- Purpose: help you add *authorial* continuity glue (beyond strict reference correctness) without me guessing
  your course intent. The manuscript's cross-references are structurally consistent, but some of the narrative
  "promises" in the Introduction would feel richer if we add a few short payoffs later (especially for the
  camera case study and for the fuzzy->evolutionary tuning bridge).

## Where we stand (current situation)

- A rolling-window reference audit exists at:
  - `notes_output/review/rolling_window_reference_audit_20260218.md`
- Structural check: all `\Cref{chap:*}` references in `lecture_1_intro.tex` point to chapter labels that exist
  in the book (no broken chapter-label promises).
- What is still missing (optional): a few *semantic* callbacks that make the book feel like it is "closing loops"
  on earlier motivating examples (camera system; thermostat design-to-tuning arc).

## My intent (what I want to do with your write-ups)

If you provide the prose requested below, I will:

1) Insert it into the LaTeX chapters as short, consistent callout boxes (likely `tcolorbox` with `summarybox`)
   at natural "handoff" points (near chapter openings/closings, or just before the relevant worked examples).
2) Keep the content lean and non-repetitive: each callback should serve a distinct pedagogical role
   (motivation, audit habit, or transfer cue), not re-teach the whole chapter.
3) Preserve all numeric walkthroughs (and only change numeric values if verified by Python).
4) Re-run production checks and log results in `notes_output/review/editorial_issue_plan_20260216.md`.

## How to respond (write-up style)

- Please write directly under each task heading (complete prose paragraphs), in one pass per task.
- This is intentionally a write-up task, not a Q&A form.
- Use your preferred voice for this textbook (direct, technical, classroom-friendly).
- Avoid citations unless you really want them; these are continuity/pedagogy bridges.
- If you want, you can include 1-2 short "phrases you want repeated" across the book (e.g., "budgeted optimizer",
  "audit hooks", "preview -> formalization -> checklist") so we can reuse them consistently.

## Task A: Camera case study payoffs (4 micro-callouts)

Write four short callouts (each 120–180 words) that explicitly revisit the Introduction’s industrial camera system
and connect it to later parts.

Where these will go:
- One box near the end (or "Where we head next" region) of each target chapter below.

Each callout should:

- Start with a one-sentence reminder of the camera system goal (restricted-zone human detection + escalation).
- Name the chapter/toolkit it connects to, and state what that toolkit contributes (and what it does *not* solve).
- Include one concrete “audit hook” (what would you log/plot/check).
- End with a one-sentence forward/backward pointer (how it connects to the preceding/following chapter).

Callout targets (one each):

1) CNNs (`lecture_6.tex`): perception stack and false-negative/latency constraints.
2) Sequence models / masking (`lecture_7.tex` or `lecture_transformers.tex`): temporal smoothing, event prediction,
   and the risk of leakage (future info) in evaluation.
3) Fuzzy reasoning (`lecture_8_part_ii.tex` or `lecture_10_part_ii.tex`): auditable escalation policies and
   the “degrees of truth” interface to human concepts.
4) Evolutionary optimization (`lecture_11.tex`): tuning thresholds/memberships under noisy evaluations and
   discrete constraints (placement, rule weights, penalty weights).

Idea bank (optional) to spark brainstorming:
- CNN payoff angles: false negatives vs latency; dataset shift by lighting/camera angle; calibration vs thresholding;
  slice audits (night vs day, PPE vs no PPE); "what is the failure mode, not just the metric?"
- Sequence payoff angles: tracking + smoothing; alert "debounce" windows; mask/leakage analogy (future frames);
  evaluation protocol (time-based splits); caching/state bugs.
- Fuzzy payoff angles: escalation logic as rules you can explain; membership shapes as "policy knobs";
  monotonicity and edge-case tests; degrees of truth vs probabilities.
- Evolutionary payoff angles: discrete knobs (camera placement, frame rate, rule set selection) + noisy sims;
  budgeted evaluation; multi-seed reporting; feasibility-first constraints (privacy, retention, safety).

## Task B: A realistic “tuning objective” vignette for Part IV

Write 250–400 words describing one real controller/decision policy you care about tuning (it can be the thermostat,
the camera escalation logic, or a different system you teach). Include:

- Decision variables to tune (at least 5; a mix of discrete + continuous is ideal).
- The objective metric(s) and how they are measured (include noise/variance sources if any).
- Constraints (hard vs soft) and what “feasible-first” would mean.
- Evaluation budget (e.g., “each simulation run is 5 minutes; we can afford 200 evaluations total”).
- What would count as “premature convergence” in this setting and one diversity mechanism you would tolerate.

This will be used to enrich the Part IV opening motivation and/or the GA “risk & audit” discussion.

Idea bank (optional) to spark brainstorming:
- Good decision variables to include (mix discrete + continuous):
  - detection threshold(s), NMS threshold, tracking association threshold, alert debounce window length,
    camera pan/tilt gain limits, membership breakpoints, rule weights, penalty weights, evaluation horizon length,
    sampling/frame rate, model-choice toggle (small vs large detector), "feasible-first" repair toggles.
- Good objective definitions:
  - minimize false negatives subject to latency; maximize utility = true positives - cost(false alarms) - compute cost;
    multi-objective (FNR, FPR, latency, energy) with a Pareto front story.
- Natural noise sources:
  - stochastic simulation seeds, environment randomness, annotation noise, non-deterministic hardware timing,
    rare-event variance.

## Task C: Your preferred “course voice” for recap paragraphs

Write a single short style sample (120–180 words) in the tone you want for end-of-chapter recap paragraphs in this book.
Aim for:

- Direct, technical, non-salesy voice.
- One explicit learning transfer cue (“this same habit will be reused when…”).
- One explicit warning about a common student misconception.

We will use this sample to align recap voice when we do future rolling-window passes.

Idea bank (optional) to spark brainstorming:
- Helpful recurring moves for recaps:
  - 1 sentence: "What problem did we solve?"
  - 2-3 sentences: "What are the knobs, and what do they trade off?"
  - 1 sentence: "What would you plot/log to debug it?"
  - 1 sentence: "What transfers to the next chapter?"
- Common misconceptions worth warning about (examples):
  - "fitness is probability"; "membership degree is probability"; "one run proves optimality";
    "attention implies memory"; "good loss implies good decisions without calibration".

