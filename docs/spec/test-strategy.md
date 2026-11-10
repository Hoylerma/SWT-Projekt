KI-Nutzung: Entwurf vom Team. Claude Opus 5.5 (Anthropic) wurde zur Überarbeitung, Strukturierung, sprachlichen Korrektur und für inhaltliche Ergänzungen genutzt (CI-Stages, Begründung des Mockings, Limitationen).


# Test Strategy

## 1. Unit tests vs. BDD/acceptance tests

| | Unit tests | BDD / acceptance tests |
|---|---|---|
| **Purpose** | Verify that individual units (functions, classes) work correctly from a technical perspective | Verify that the application behaves as specified from the user's perspective (Gherkin scenarios) |
| **Scope** | One unit in isolation; collaborators are mocked or stubbed | Several components working together through a complete feature |
| **Execution time** | Milliseconds per test; the whole suite runs in seconds | Seconds per scenario; the suite takes minutes and grows with every feature |
| **Failure diagnosis** | Points directly to the faulty code | Shows *that* a feature is broken, but not *where* |

The two test types complement each other rather than replace each other. Unit tests tell us whether the code is correct; BDD tests tell us whether we built the right behavior.

## 2. Recommendation for our CI pipeline

We run the tests in two separate, sequential CI stages:

1. **Unit test stage** – runs on every push to any branch. It is fast and gives developers immediate feedback.
2. **BDD/acceptance stage** – runs only if the unit test stage passed (fail fast), on every pull request against `main` and on every merge into `main`.

Rationale:
- If unit tests already fail, the BDD tests would most likely fail as well, but with a much less precise error message. Skipping them saves CI time and points developers to the exact location of the bug.
- Separate stages make it visible in the CI report on which level a failure occurred.
- No feature reaches `main` without its acceptance criteria being verified.

Locally, developers run the unit tests after each change and the BDD suite before opening a pull request. As long as the BDD suite stays fast (see section 3), running it on every push would also be acceptable; we will revisit this decision if its runtime grows beyond a few minutes.

## 3. Impact of mocking the external dependency

The responses of our external dependency fall into a small number of categories:
- **Successful responses**, e.g. the current date, whether it is a holiday, the current season
- **Unsuccessful responses**, e.g. the service is unreachable, times out or returns an invalid response

We only need one scenario per category that leads to *different behavior* in our application (equivalence classes), not one per possible response. A mock provider returns exactly these predefined responses.

Using the mock provider makes acceptance tests feasible in CI because:
- **No live access is required:** the CI runner needs neither network access to the provider nor API credentials stored as secrets.
- **Tests are deterministic:** live data changes over time (date, holidays, season), which would make tests flaky. A scenario such as "Given today is a holiday" cannot be tested on demand against the live service, but it can with the mock.
- **Error cases are testable:** an unreachable or failing service can be simulated reliably, which is practically impossible with the real dependency.
- **Tests are fast and free:** there are no network latencies, rate limits or usage costs.
- **The pipeline is independent of the provider:** an outage on the provider's side does not break our build.

As a result, the BDD tests are fast and stable enough to run automatically on every pull request.

**Limitation:** the mock only verifies our *assumptions* about the dependency. If the provider changes its response format, the mocked tests will stay green. We therefore plan an optional small smoke test against the live service that runs manually or on a schedule (e.g. nightly) and does not block pull requests.
