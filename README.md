# QA Automation Test Suite

Automated API test suite built as my Quality Assurance solo project for WeThinkCode_'s elective specialization program.

This project tests the [ReqRes](https://reqres.in) public REST API, covering functional, negative, and edge-case scenarios across its Users, Registration, and Login endpoints.

## 🎯 Project Goal

To demonstrate practical QA skills: designing meaningful test cases, automating them, identifying edge cases and inconsistencies, and clearly documenting the reasoning behind each decision — not just writing scripts that pass.

## 🛠️ Tech Stack

- **Python 3**
- **pytest** — test framework
- **requests** — HTTP client for API calls

## 📁 Project Structure

```
qa-automation-testsuite/
├── tests/
│   └── test_users.py       # automated test suite
├── test-plan.md             # test strategy, scope, and test case design
├── certificates/            # QA course completion certificates
├── requirements.txt         # project dependencies
└── README.md
```

## 🚀 Getting Started

Clone the repo:
```bash
git clone git@github.com:VuyiswaNxumalo/qa-automation-testsuite.git
cd qa-automation-testsuite
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the test suite:
```bash
pytest tests/test_users.py -v
```

## ✅ What's Covered

- **GET** — list users, retrieve single user, handle non-existent user (404)
- **POST** — create user, register user (valid and invalid payloads)
- **PUT** — update existing user
- **DELETE** — remove existing user
- **Edge cases** — missing fields, invalid data, response time thresholds

See [`test-plan.md`](./test-plan.md) for the full test strategy and case-by-case breakdown.

## 🐛 Bugs & Findings

Any inconsistencies found during testing are logged as [GitHub Issues](../../issues) in this repository, including steps to reproduce and expected vs. actual behavior.

## 🎥 Demo Video

[Link to demo video — coming soon]

A 5–10 minute walkthrough covering the project's design decisions, a live test run, and an explanation of the testing approach.

## 📜 Certificates

Course completion certificates for the QA specialization are available in the [`certificates/`](./certificates) folder, and via [this Google Drive link] *(add link here)*.

## 📌 About This Project

Built as part of my QA elective at [WeThinkCode_](https://www.wethinkcode.co.za/), a tuition-free software engineering school. This project reflects steady, iterative development — see the commit history for the full build process.

---
*Author: Vuyiswa Nxumalo*

# My code:
WTC-YLZFENXH