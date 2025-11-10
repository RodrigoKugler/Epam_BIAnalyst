# BI Analyst Training – Quality Plan
This plan enforces consistent execution for the BI Analyst training project. Each phase defines activities, required artifacts, and explicit quality gates to guarantee flawless delivery.

## Phase 1 – Setup & Calibration
- **Activities**
  - Confirm subject inventory matches scope (review `README.md` and folder tree).
  - Draft the quality checklist in `shared/quality_checklist.md`.
  - Run a pilot prompt; iterate on `prompts/base_prompt_template.md` until output matches expectations.
- **Artifacts**
  - `shared/quality_checklist.md`
  - Calibrated prompt template (`prompts/base_prompt_template.md`)
  - Pilot `draft.md`
- **Quality Gate 1**
  - Checklist approved and stored.
  - Pilot draft satisfies all required sections and tone.
  - Prompt template version recorded in `prompts/run_history.md`.
  - ✅ Gate owner documents sign-off in table below.

## Phase 2 – Draft Production
- **Activities (per subject)**
  1. Define subtopics, depth, tooling notes (optional `notes.md`).
  2. Run prompt and save output to `draft.md`.
  3. Log run details (date, parameters, template version) in `prompts/run_history.md`.
  4. Perform self-review via checklist; revise immediately if gaps exist.
- **Artifacts**
  - `subject/draft.md`
  - `prompts/run_history.md` entry
  - (Optional) `subject/notes.md`
- **Quality Gate 2**
  - Draft contains all mandatory sections.
  - Markdown passes lint/basic validation.
  - Self-review documented (note outcome in draft front matter or notes).
  - ✅ Sign-off recorded in `content_reviews/<subject>.md`.

## Phase 3 – Peer Review & QA
- **Activities**
  - Assign reviewer; capture in `content_reviews/<subject>.md`.
  - Reviewer checks accuracy, clarity, and example validity.
  - Track issues with severity tags (Critical/Major/Minor) until resolved.
- **Artifacts**
  - Updated `draft.md`
  - `content_reviews/<subject>.md`
- **Quality Gate 3**
  - No unresolved critical or major issues.
  - Reviewer approval logged (initials + date).
  - ✅ Summarize gate completion in review file and `prompts/run_history.md`.

## Phase 4 – Harmonization
- **Activities**
  - Cross-check tone, terminology, and formatting across subjects.
  - Centralize shared assets (glossary, diagrams) in `shared/`.
  - Update references to point to shared materials.
- **Artifacts**
  - Harmonized drafts
  - `shared/glossary.md`, `shared/templates/`
- **Quality Gate 4**
  - Style guide rules met (headings, voice, terminology).
  - Shared assets referenced consistently; no duplication.
  - ✅ Sign-off documented in this plan.

## Phase 5 – Publication Preparation
- **Activities**
  - Copy approved drafts to `docs/<structure>/index.md`.
  - Add front matter/navigation metadata if needed for GitHub Pages.
  - Build `docs/index.md` landing page and navigation files (`_config.yml`, `_sidebar.md` as applicable).
- **Artifacts**
  - `docs/` content set
  - Navigation configuration files
- **Quality Gate 5**
  - File hierarchy verified; links and anchors tested locally.
  - Markdown lint passes for `docs/`.
  - ✅ Gate entry added to table below.

## Phase 6 – Automation & Release
- **Activities**
  - Configure linting/CI scripts (optional but recommended).
  - Initialize git repository; commit with clear messages.
  - Configure GitHub Pages and perform end-to-end walkthrough as learner.
- **Artifacts**
  - CI configuration (if used)
  - Git log
  - Feedback summary from walkthrough
- **Quality Gate 6**
  - CI status green (if present).
  - Walkthrough validates completeness and flow.
  - Launch checklist completed (README, CONTRIBUTING updated).
  - ✅ Release metadata entered below.

## Gate Sign-off Log
| Gate | Date | Owner | Evidence/Notes |
|------|------|-------|----------------|
| 1 | 2025-11-09 | GPT-5 Codex | Inventory confirmed, checklist published, pilot SQL draft ready |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

## Change Management
- Update this plan when phases or gates change.
- Record modifications in `shared/changelog.md`.
