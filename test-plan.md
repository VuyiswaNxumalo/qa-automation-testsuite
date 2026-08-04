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

## 5. Test Environment
- API base URL: `https://reqres.in/api`
- Local machine running Python 3.x with `pytest` and `requests` installed
- No authentication required for target endpoints (public mock API)

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

*(This table will grow as more test cases are added throughout development.)*

## 9. Defect Management
Any bugs or inconsistencies found during testing will be logged in the `/bug-reports` folder of this repository, including:
- Steps to reproduce
- Expected vs actual behavior
- Severity/impact
- Screenshots or response payloads where relevant

## 10. Deliverables
- Automated test suite (`/tests`)
- This test plan (`test-plan.md`)
- Bug reports (`/bug-reports`, if applicable)
- Demo video walkthrough (linked in README)
- CI workflow (optional, via GitHub Actions)

## 11. Risks & Assumptions
- The public ReqRes API is a mock service; some "write" operations (POST/PUT/DELETE) do not persist data, which is accounted for in expected results
- API availability is assumed stable for the duration of testing; if downtime occurs, this will be noted in commit history/logs

---
*Author: Vuyiswa Nxumalo*
*Project: QA Solo Project – WeThinkCode_ Elective Specialization*