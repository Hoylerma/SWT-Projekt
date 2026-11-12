# Review template (inspection / technical review)

**Project / product:** FocusFlow by group 3  
**Review object(s):** app.md, requirements.md, quality.md, backend?  
**Review type:** informal technical review  
**Date (planned / actual):** 12.November 2026  
**Moderator:** Max
**Protokollant:** Isabel  
**Author(s):** group 3  
**Reviewers:** group 2

---

## 1. General instructions

Use this template together with the review process you selected from the presented ones in the course. The phases below describe a typical inspection-style workflow (adapt terminology to your chosen review type if needed).

| type | reason|
| technical review | we intend to review the technical soundness and overall consensus of the project(see review objects), but due to the time limit and the fact we only want to do a static review with no tests, the techncial review is more informal with also no author present |
walkthrough | we intend to review some of the technical soundness and overall consensus of the project(see review objects), but due to the time limit and the fact we only want to do a static review with no tests, the review is a author present

**Terminology**

| Acronym | Meaning |
|--------|---------|
| **MP** | Master Plan |
| **DS** | Data Summary |
| **LoF** | Level of Findings |
| **RR** | Review Report |

### Phases of a review / inspection

| Phase | Description |
|-------|-------------|
| **Planning** | The moderator checks whether the **entry criteria** are met (e.g. the review object is in a reviewable state). The review is planned: reviewers and dates are fixed, invitations are sent, etc. The moderator completes the **Master Plan (MP)** and identifies suitable inspection tasks. |
| **Individual preparation** | Each reviewer examines the review object for defects and other issues. Findings and their quality are reported to the moderator. The moderator consolidates findings into one document, prepares the review meeting, and derives key figures for the **Data Summary (DS)**. |


---

## 2. Master Plan (MP)

### 2.1 Masterplan — header

<!-- Fill the table below during planning. Redundant with the document header above is OK if you copy values here for a self-contained MP export. -->

| Field | Value |
|-------|-------|
| Review No. | REV-2026-001 |
| Project | FocusFlow |
| Project manager | group 3 |
| Quality expert / manager | — |
| Moderator | Max |
| Author(s) | Florian Claus |

### 2.2 Review objects

<!-- List the specific artefacts under review (files, modules, documents, commits). Use Abbr. as a short label for each row (used in findings and assignments). Add rows if needed. -->

| # | Review objects | Abbr. |
|---|----------------|-------|
| 1 | project description app.md | app |
| 2 | requirements.md | reqs |
| 3 | quality.md | quali |
| 4 | unit tests | unit-test |
| 5 | gherkin feature files| gherkin |
| 6 | irgendwa sim backend | backend |

### 2.3 Reference documents

<!-- List materials reviewers need for context (requirements baseline, architecture, API spec, course brief). Use Abbr. for cross-references. -->

| # | Reference documents | Abbr. |
|---|---------------------|-------|
| 1 | focus flow product brief | brief |
| 2 | focus flow product description | desc |

### 2.4 Checklists / scenarios

<!-- Specify which checklists, reading guides, or test scenarios reviewers should follow (course checklist, OWASP skim, API contract checks). -->

| # | Checklists / scenarios |
|---|-------------------------|
| 1 | use cases for gherkin and feature files use-cases.md |
| 2 | <!-- e.g. REST error-handling scenario list. --> |

### 2.5 Reviewer assignment

<!-- Up to 10 reviewers: assign names and which chapters, objects, or checklists each person covers. Use Abbr. for initials or short IDs. -->

| Reviewer | Names (and chapters / checklists or scenarios assigned to the review) | Abbr. |
|:--------:|---------------------------------------------------------------------------|-------|
| 1 | Max, app.md | MA |
| 2 | Isabel, requirements.md, quality.md | IRQ |
| 3 | Fabian | <!--  --> |
| 4 | Manuel | <!--  --> |
| 5 | Sefa | <!--  --> |


### 2.6 Kick-off

<!-- Optional but recommended: align on scope, Master Plan, and context before individual preparation. -->

| Date / time / location |
|------------------------|
| <!-- e.g. 2026-04-22 14:00 CET, Room X / video link --> |

### 2.7 Individual preparation

<!-- Planning figures for the preparation phase. “Optimal” rows support effort estimation (rate × time ≈ size). For documents without NLOC, substitute pages or words and state that in the Size unit cell. -->

| Individual preparation | Value | Unit |
|------------------------|-------|------|
| Submission of findings by | <!-- Enter the deadline by which each reviewer submits findings to the moderator (date/time or rule such as “72h after kick-off”). --> | — |
| Size of review objects | <!-- Enter the total Non-Comment Lines of Code (NLOC) for code; for specification-only reviews, use pages or words and note the unit here. --> | NLOC |
| Optimal inspection rate | <!-- Target or measured inspection speed (e.g. NLOC per hour per reviewer). --> | NLOC/h |
| Optimal inspection time | <!-- Planned total inspection time in hours (placeholder 0.00 until estimated or measured). --> | h |

### 2.8 Review meeting

| Date / time / location |
|------------------------|
| <!-- e.g. 2026-04-25 10:00 CET, Room Y / video link --> |



---

## 3. List of findings (LoF)

Use one row per finding. Extend the table if your course requires extra columns.

Suggested values: **Type** — defect, question, suggestion; **Severity** — blocking, major, minor, editorial (define team scale); **Status** — open, accepted, rejected, deferred, fixed (update through meeting and rework).

| ID | Location (file / section / module) | Summary | Type | Severity | Status | Owner | Notes / meeting decision |
|----|-------------------------------------|---------|------|----------|--------|-------|--------------------------|
| F-001 | app.md, section external dependency | external dependency is marked as sms, but in further documents it was changed to e-mail | defect | minor | open | - | author knew of this |
| F-002 | app.md, section usecase | defined target audience doesn't equal the one from the brief | defect | minor | open | - | author knew of this |
| F-003 | app.md | intended implementation of login isn't dodumented | question | editorial | open | - | - |
| F-004 | requirements.md, section erinnerungen | it is only documented in the external dependency that reminders happen through a mail system, section reminders should also state that | suggestion | editorial | open | - | - |
| F-005 | requirements.md, section testnutzer | the list of required data for test users does not list passwords | defect | minor | open | - | - | 
| F-006 | requirements.md, section prioritäten | the usability of the priority is not documented | suggestion | editorial | open | - | - |
| F-007 | requirements.md & app.md  | Task-Zustände and checkTask define the same statuses with different labels | suggestion | minor | open | - | - |
| F-008 | quality.md, section qualitätsmodell | it is only stated that a secure hash is intended to be used, but no defintion of what secure means or by which standards a hash will be chosen | question | minor | open | - | author stated that database isn't implemented yet |
| F-008 | quality.md, section qualitätsmodell | unclear definition of the messbar cell of wartbarkeit | suggestion | minor | open | - | author agreed |
| F-009 | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> |
| F-010 | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> |
| F-010 | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> |
| F-010 | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> | <!-- --> |

---

## 4. Data Summary (DS)

<!-- Key metrics for this review. Fill after preparation and/or after rework. -->

| Metric | Value | Notes |
|--------|-------|-------|
| Size of review object | 185 dateien, 92 ordner | focus-flow zip file |
| Number of findings (initial) | 4 | muss noch angepast werden is bishe rnur von isi und max |
| Number of findings after meeting | <!-- --> | <!-- --> |


---

## 5. Review Report (RR)
4
### 5.1 Summary

<!-- Short executive summary: object reviewed, outcome, overall quality impression. -->


### 5.2 Review outcome

- **Review object state after review:** <!-- e.g. accepted with changes, requires re-inspection, not accepted -->
- **Major risks or themes:** <!-- bullet list -->

### 5.3 Decisions and follow-up

| Topic | Decision | Responsible | Due date |
|-------|----------|-------------|----------|
| <!-- --> | <!-- --> | <!-- --> | <!-- --> |

### 5.4 Positive observations (optional)

<!-- What was done well; good practices worth keeping. -->
struktur von den aufgaben wurd egut eingehalten

### 5.5 Lessons learned (optional)

<!-- Process improvements for the next review. -->

### 5.6 Sign-off

| Role | Name | Signature / date |
|------|------|------------------|
| Moderator | Max | <!-- --> |
| Author | Florian | <!-- --> |

---

<!-- End of template -->

## Lab 6.2 Retrospektive zum Review
Was hat gut funktioniert? 
Kommunikation mit gruppe 3
sehr gut verständlicher walkthrough

Was war schwierig?
nciht wirklich schwierig, aber sachen von vor mehreen wochen sich ohne nachschuaen zu erinnern, man musste halt nochmal in den labs nachlesen oder nachfragen
es war uns nicht imme rganz eindeutig wann welcher type und severity genau zutrifft, vorallem wenn es so grenzf"alle waren

Sind formale Reviews eine geeignete Methode für Ihr Team? Für welche Artefakte (Spezifikation, Design, Code) würden Sie sie erneut einsetzen?
für die größe unseres projektes wirkt ein vollumfängliches review ein wneig zu viel. aber vor allem für code implememtation ist eine formal wreview ausserhalb vom team ganz hilfreich auch um unstimmigkeiten zwischen vershciednene dokumenten zu finden, die einem sleber ncihmehr auffallen

Eine konkrete Verbesserung, die Sie für die nächste Review-Runde vornehmen würden.
bessere vorbereitungsphase vollziehen

