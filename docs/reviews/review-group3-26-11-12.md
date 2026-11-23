# Review template (inspection / technical review)

**Project / product:** FocusFlow by group 3  
**Review object(s):** app.md, requirements.md, quality.md, backend?  
**Review type:** walkthrough  
**Date (planned / actual):** 12.November 2026  
**Moderator:** Max
**Protokollant:** Isabel  
**Author(s):** group 3  
**Reviewers:** group 2

---

## 1. General instructions

Use this template together with the review process you selected from the presented ones in the course. The phases below describe a typical inspection-style workflow (adapt terminology to your chosen review type if needed).

| type | reason|
| walkthrough | we intend to review some of the technical soundness and overall consensus of the project (see review objects), but due to the time limit and the fact we only want to do a static review with no tests a walkthrough seemed the most appropriate, it also seemed more time-efficient to have the project also explained by an author present |

**Terminology**

| Acronym | Meaning |
|--------|---------|
| **MP** | Master Plan |
| **DS** | Data Summary |
| **LoF** | List of Findings |
| **RR** | Review Report |

### Phases of a review / inspection

| Phase | Description |
|-------|-------------|
| **Planning** | The moderator checks whether the **entry criteria** are met (e.g. the review object is in a reviewable state). The review is planned: reviewers and dates are fixed, invitations are sent, etc. The moderator completes the **Master Plan (MP)** and identifies suitable inspection tasks. |
| **Individual preparation** | Each reviewer examines the review object for defects and other issues. Findings and their quality are reported to the moderator. The moderator consolidates findings into one document, prepares the review meeting, and derives key figures for the **Data Summary (DS)**. |
| **Walkthrough Meeting** | The author of the project meets with the reviewers and walks them through the project, the files, setup, etc. The reviewers present their initial findings and document further findings that appear through the walkthrough. |
| **Final Documentation** | The reviewers finalize their findings and documentation. |


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
| 1 | project description app.md | APP |
| 2 | requirements.md | REQ |
| 3 | quality.md | QUA |
| 4 | unit tests | UNI |
| 5 | gherkin feature files| GHE |
| 6 | backend | BAC |

### 2.3 Reference documents

<!-- List materials reviewers need for context (requirements baseline, architecture, API spec, course brief). Use Abbr. for cross-references. -->

| # | Reference documents | Abbr. |
|---|---------------------|-------|
| 1 | focus flow product brief | BRI |
| 2 | focus flow product description | DES |

### 2.4 Checklists / scenarios

<!-- Specify which checklists, reading guides, or test scenarios reviewers should follow (course checklist, OWASP skim, API contract checks). -->

| # | Checklists / scenarios |
|---|-------------------------|
| 1 | use cases for gherkin and feature files use-cases.md |
| 2 | Consistency check across documents: terms, statuses (Offen / In Arbeit / Fertig) and the external dependency (e-mail) in app.md, requirements.md, quality.md and the code must match |
| 3 | Unit tests checked against requirements.md and test-strategy.md (are the requirements covered, do the tests check the right behaviour) |

### 2.5 Reviewer assignment

<!-- Up to 10 reviewers: assign names and which chapters, objects, or checklists each person covers. Use Abbr. for initials or short IDs. -->

| Reviewer | Names (and chapters / checklists or scenarios assigned to the review) | Abbr. |
|:--------:|---------------------------------------------------------------------------|-------|
| 1 | Max, app.md | MA |
| 2 | Isabel, requirements.md, quality.md | IS |
| 3 | Fabian, unit tests (UNI): `FocusFlow.Tests/Models/*`, `UnitTest1.cs`, checked against `Models/*.cs`, `Service/TaskService.cs`, requirements.md, test-strategy.md | FA |
| 4 | Manuel, Gherkin feature files (GHE)| MH |
| 5 | Sefa | <!--  --> |


### 2.6 Kick-off

<!-- Optional but recommended: align on scope, Master Plan, and context before individual preparation. -->

| Date / time / location |
|------------------------|
| No joint kick-off. The Master Plan was agreed informally in the team; each reviewer prepared individually. |

### 2.7 Individual preparation

<!-- Planning figures for the preparation phase. “Optimal” rows support effort estimation (rate × time ≈ size). For documents without NLOC, substitute pages or words and state that in the Size unit cell. -->

| Individual preparation | Value | Unit |
|------------------------|-------|------|
| Submission of findings by | 48h before deadline | — |
| Size of review objects | 14446 | NLOC |
| Optimal inspection rate | ~500 | NLOC/h |
| Optimal inspection time | 6 | h |

### 2.8 Review meeting

| Date / time / location |
|------------------------|
| 12 November 2026: walkthrough with group 3 (the author presented the project, reviewers presented their findings). No separate internal team meeting to consolidate findings. |



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
| F-009 | quality.md, section qualitätsmodell | unclear definition of the messbar cell of wartbarkeit | suggestion | minor | open | - | author agreed |
| F-010 | all `Gherkin-Szenarien/*.feature` | German keywords (Angenommen, Wenn, Dann) are used without a `# language: de` header; with the default English parser the step lines are read as scenario description, so the scenarios would contain no executable steps and the 7 "passed" BDD tests would verify nothing  | defect | major | open | - | - |
| F-011 | Gherkin-Szenarien, use-cases.md | Several use cases have no scenarios: "Nutzer anmelden", "Aufgabe zuweisen" and most of "Eingaben prüfen"  | defect | major | open | - | - |
| F-012 | Gherkin-Szenarien, quality.md "Zuverlässigkeit" / "Testbarkeit" | No scenario covers the external dependency (e-mail notifications / reminders) or its simulated outage| defect | major | open | - | - |
| F-013 | Task_verschieben.feature, requirements.md, use-cases.md | Scenarios use the statuses "To Do" / "In Progress" / "Overdue", while requirements.md and use-cases.md use "Offen" / "In Arbeit" / "Fertig"; the transition to "Done" is not covered | defect | minor | open | - | - |
| F-014 | all .feature files, StepDefinitions/*.cs | Scenarios describe UI behavior , but the step definitions only check the service / in-memory repository, so e.g. "auf dem Dashboard angezeigt" is never actually verified | defect | minor | open | - | - |
| F-015 | Task_verschieben.feature, Task_erstellen.feature, Kommentar_ergänzen.feature | Given steps are narrative instead of preconditions "Brille nicht an", "Aufgabe falsch verstanden" and contain asserts; test values (51 / 201 characters) are hidden in the step code instead of a Scenario Outline with Examples | suggestion | minor | open | - | - |
| F-016 | all .feature files | Incomplete sentences "gültige Werte in das Formular eingetragen", "flasch", "kommplett", "aktuallisiert" | defect | editorial | open | - | - |
| F-017 | `TaskItemTest.cs` test `TaskItem_WithoutDueDate_IsInvalid`, `Models/TaskItem.cs` | In requirements.md the due date is optional. But in the model the due date is required, and the unit test checks that a task without a due date is invalid. So the test checks the wrong behaviour | defect | major | open | - | - |
| F-018 | `Service/TaskService.cs`, `Service/NotesService.cs` | There are no unit tests for the services. The service does not check the allowed status changes from requirements.md, for example a task can go directly from "To Do" to "Done". No test would find this. The mock library NSubstitute is installed but not used, although test-strategy.md says that unit tests use mocks | defect | major | open | - | - |
| F-019 | `TaskItemTest.cs`, `Service/TaskService.cs` | The unit tests use the status "Open". But the service only accepts "To Do", "In Progress" and "Done", so it would reject "Open". requirements.md uses other names again ("Offen", "In Arbeit", "Fertig"). Related to F-007 and F-013 | defect | minor | open | - | - |
| F-020 | `Models/TaskItem.cs`, `TaskItemTest.cs` | Priority and status can be any text, for example `Priority = "xyz"` is accepted. requirements.md defines fixed values, but there is no check and no unit test for wrong values | defect | minor | open | - | - |
| F-021 | `UnitTest1.cs` | This test is empty and has no assert, so it always passes. It makes the number of passed tests look higher. It should be deleted | defect | minor | open | - | - |

---

## 4. Data Summary (DS)

<!-- Key metrics for this review. Fill after preparation and/or after rework. -->

| Metric | Value | Notes |
|--------|-------|-------|
| Size of review object | 185 dateien, 92 ordner | focus-flow zip file |
| Number of findings (initial) | 21 | 5 major, 12 minor, 4 editorial; by type: 14 defects, 5 suggestions, 2 questions |
| Number of findings after meeting | not determined | No consolidation meeting was held; the findings were not re-rated after the walkthrough. |


---

## 5. Review Report (RR)
### 5.1 Summary

<!-- Short executive summary: object reviewed, outcome, overall quality impression. -->
The reviewed project is an application for managing tasks. The outcome contained some minor erros and mistakes that could overall be easily fixed and only provide minor disturbances. The impression of the quality left on the reviewers was altogether good. The documents (F-001 to F-009) only have minor or editorial issues. In the tests (Gherkin files and unit tests) we found 5 major findings (F-010, F-011, F-012, F-017, F-018), for example the missing language header in the feature files and a unit test that checks the wrong behaviour. The author seemed to know their project and what they want to achieve with it.


### 5.2 Review outcome

- **Review object state after review:** unchanged<!-- e.g. accepted with changes, requires re-inspection, not accepted -->
- **Major risks or themes:** the BDD and unit tests are weaker than they look: the scenarios may contain no executable steps (F-010), use cases and the external dependency are not covered (F-011, F-012), and the services are not unit tested (F-018)<!-- bullet list -->

### 5.3 Decisions and follow-up

| Topic | Decision | Responsible | Due date |
|-------|----------|-------------|----------|
| All findings | Handed over to group 3 as feedback. No follow-up meeting was held, so no decisions or due dates were agreed. | group 3 (author) | - |

### 5.4 Positive observations (optional)

<!-- What was done well; good practices worth keeping. -->
struktur von den aufgaben wurd egut eingehalten

### 5.5 Lessons learned (optional)

<!-- Process improvements for the next review. -->

---

<!-- End of template -->
