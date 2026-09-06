# Test Plan – QA Automation Test Suite

## 1. Project Overview
This test plan outlines the approach for testing the [ReqRes](https://reqres.in) public REST API as part of my Quality Assurance solo project for WeThinkCode_'s elective specialization.

The goal is to demonstrate practical QA skills: designing test cases, automating them, identifying edge cases and potential defects, and documenting findings clearly.

## 2. Objectives
- Verify that core API endpoints (Users, Registration, Login) behave as expected under normal, boundary, and invalid conditions
- Validate response structure, status codes, and data integrity
- Identify and document any inconsistencies or bugs found during testing
- Build an automated, repeatable test suite that can run via CI

## 3. Scope

### In Scope
- GET endpoints: list users, single user, user not found
- POST endpoints: create user, register user
- PUT/PATCH endpoints: update user
- DELETE endpoint: delete user
- Response validation: status codes, response schema, key fields, response time
- Negative/edge case testing: missing fields, invalid data types, invalid IDs, empty payloads

### Out of Scope
- Load/performance testing at scale
- Security penetration testing
- UI testing (this project is API-focused)

## 4. Test Approach
- **Type of testing**: Automated functional and negative API testing
- **Tooling**: Python, `pytest`, `requests`
- **Test data**: Static/predictable test data provided by the ReqRes mock API
- **Test levels**:
  - Positive tests — confirm expected behavior with valid input
  - Negative tests — confirm proper handling of invalid input (missing fields, wrong types, bad IDs)
  - Boundary tests — edge values (e.g. non-existent user ID, empty string fields)
  - Parametrized tests — the same test logic run against multiple inputs (e.g. a range of valid and invalid user IDs) to catch inconsistent behavior across values, without duplicating test code
  - Chained workflow tests — a sequence of dependent actions (create → update → delete) run as one flow, checking that each step's result is consistent with the step before it, rather than testing each action in total isolation

## 5. Test Environment
- API base URL: `https://reqres.in/api`
- Local machine running Python 3.x with `pytest` and `requests` installed
- **Authentication**: ReqRes requires an `x-api-key` header on all requests (discovered during development — see Section 11). The key is loaded from the `REQRES_API_KEY` environment variable via `tests/config.py`, and never hardcoded or committed.
- **CI environment**: Tests also run automatically via GitHub Actions on every push/PR to `main`, using a repository secret for the API key. See `.github/workflows/tests.yml`.

## 6. Entry Criteria
- Test environment set up (dependencies installed)
- API endpoints confirmed reachable
- Test cases documented before automation begins

## 7. Exit Criteria
- All planned test cases implemented and passing (or documented as known failures/bugs)
- No critical unaddressed defects
- Test suite runs cleanly via a single command
- Bug reports logged for any confirmed inconsistencies

## 8. Test Cases Summary

| ID | Endpoint | Type | Description | Expected Result |
|----|----------|------|--------------|------------------|
| TC01 | GET /users?page=2 | Positive | Retrieve list of users | 200 OK, valid list returned |
| TC02 | GET /users/2 | Positive | Retrieve single existing user | 200 OK, correct user data |
| TC03 | GET /users/23 | Negative | Retrieve non-existent user | 404 Not Found |
| TC04 | POST /users | Positive | Create a new user | 201 Created, response includes id and createdAt |
| TC05 | POST /users | Negative | Create user with missing fields | Appropriate error handling verified |
| TC06 | POST /register | Positive | Register with valid email and password | 200 OK, token returned |
| TC07 | POST /register | Negative | Register with missing password | 400 Bad Request, error message returned |
| TC08 | PUT /users/2 | Positive | Update existing user | 200 OK, updatedAt field present |
| TC09 | DELETE /users/2 | Positive | Delete existing user | 204 No Content |
| TC10 | GET /users/2 | Edge | Response time check | Response returns within acceptable threshold |
| TC11 | POST /login | Positive | Login with valid credentials | 200 OK, token returned |
| TC12 | POST /login | Negative | Login with missing email | 400 Bad Request, exact error message verified |
| TC13 | POST /login | Negative | Login with malformed email | Handled gracefully, no server error |
| TC14 | GET /users?page=0 | Edge | Invalid page number | 200 OK, no server error |
| TC15 | GET /users?page=9999 | Edge | Page far beyond available data | 200 OK, empty data list |
| TC16 | GET /users/abc | Negative | Non-numeric user ID | 404 Not Found |
| TC17 | POST /users | Negative | Wrong data type for a field | Handled gracefully, no server error |
| TC18 | GET /users?delay=3 | Edge | Delayed response | 200 OK despite delay |
| TC19 | GET /users?delay=3 | Edge | Response time under delay | Completes within timeout threshold |
| TC20 | GET /users/{id} | Parametrized | Valid user IDs (1, 2, 3, 6, 12) | 200 OK, correct ID returned for each |
| TC21 | GET /users/{id} | Parametrized | Invalid IDs (0, -1, 13, 999, "abc") | 404 Not Found, consistent across all values |
| TC22 | GET /users?page={n} | Parametrized | Valid pages (1, 2) | 200 OK, at least one user returned |
| TC23 | POST/PUT/DELETE /users | Chained workflow | Create → update → delete in sequence | Each step consistent with the step before it |

*(23 test cases implemented as of the latest update. Table reflects the current state of `tests/`.)*

## 9. Defect Management
Any bugs or inconsistencies found during testing will be logged in the `/bug-reports` folder of this repository, including:
- Steps to reproduce
- Expected vs actual behavior
- Severity/impact
- Screenshots or response payloads where relevant

## 10. Deliverables
- Automated test suite (`/tests`) — 23 test cases across functional, negative, edge, parametrized, and chained-workflow categories
- This test plan (`test-plan.md`)
- GitHub Issues documenting findings and their resolution
- Demo video walkthrough (linked in README)
- CI workflow via GitHub Actions (`.github/workflows/tests.yml`) — runs the full suite automatically on every push/PR to `main`

## 11. Risks & Assumptions
- The public ReqRes API is a mock service; some "write" operations (POST/PUT/DELETE) do not persist data, which is accounted for in expected results
- API availability is assumed stable for the duration of testing; if downtime occurs, this will be noted in commit history/logs

## 12. Findings & Adaptations

**Finding 1: API authentication requirement (resolved)**
During implementation, manual verification via `curl` revealed that ReqRes now requires an `x-api-key` header on every request — this was not the case when this plan was originally written, and caused the full test suite to fail. The issue was investigated, documented as a GitHub Issue with evidence, and resolved by loading the key from an environment variable (`REQRES_API_KEY`) rather than hardcoding it, keeping the secret out of version control. See closed Issue in this repository for the full investigation trail.

**Finding 2: TC12 assertion precision (resolved)**
While fixing the authentication issue, TC12's assertion was temporarily loosened from an exact error-message match to a generic "error key exists" check, as a shortcut. This was flagged and re-investigated separately: a fresh `curl` request confirmed the original exact error message (`"Missing email or username"`) was still accurate and had not changed. The assertion was tightened back to the precise match, since asserting on exact, stable error text is stronger verification than a loose existence check.

**Adaptation: Test data limitation in chained workflow (TC23)**
ReqRes does not persist data created via POST, so TC23's workflow test cannot verify deletion by re-fetching the created user afterward — doing so would return an unrelated existing demo user with a 200 status, producing a misleading pass rather than a real verification. This limitation is documented directly in the test code rather than worked around with an assertion that would look correct but not actually verify anything meaningful.

---
*Author: Vuyiswa Nxumalo*
