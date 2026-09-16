# QA Automation Test Suite

[![Run QA Test Suite](https://github.com/VuyiswaNxumalo/qa-automation-testsuite/actions/workflows/tests.yml/badge.svg)](https://github.com/VuyiswaNxumalo/qa-automation-testsuite/actions/workflows/tests.yml)
![Tests](https://img.shields.io/badge/tests-23%20passing-4ADE80)

Automated API test suite built as my Quality Assurance solo project for WeThinkCode_'s elective specialization program.

This project tests the [ReqRes](https://reqres.in) public REST API, covering functional, negative, edge-case, parametrized, and chained-workflow scenarios across its Users, Registration, and Login endpoints.

## 🎯 Project Goal

To demonstrate practical QA skills: designing meaningful test cases, automating them, identifying edge cases and inconsistencies, and clearly documenting the reasoning behind each decision — not just writing scripts that pass.

## 🛠️ Tech Stack

- **Python 3**
- **pytest** — test framework
- **requests** — HTTP client for API calls

## 📁 Project Structure

```
qa-automation-testsuite/
├── .github/
│   └── workflows/
│       └── tests.yml         # CI: runs the suite on every push/PR
├── tests/
│   ├── config.py             # base URL + auth header (key via env var)
│   ├── test_users.py         # core CRUD test cases (TC01-TC10)
│   ├── test_extra_cases.py   # login, pagination, edge cases (TC11-TC19)
│   └── test_advanced.py      # parametrized + chained workflow (TC20-TC23)
├── test-plan.md               # test strategy, scope, and findings
├── certificates/               # QA course completion certificates
├── requirements.txt            # project dependencies
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

Set your ReqRes API key (get a free one at [app.reqres.in/api-keys](https://app.reqres.in/api-keys)):
```bash
export REQRES_API_KEY="your_key_here"
```

Run the full test suite:
```bash
pytest tests/ -v
```

## ✅ What's Covered

**23 test cases** across four categories:
- **Functional (CRUD)** — GET, POST, PUT, DELETE across users, registration, and login
- **Negative** — missing fields, invalid data types, malformed input
- **Edge cases** — non-existent resources, out-of-range pagination, delayed responses, response time thresholds
- **Parametrized & chained workflow** — the same test logic run across multiple inputs, plus a full create → update → delete lifecycle test

See [`test-plan.md`](./test-plan.md) for the full test strategy, case-by-case breakdown, and a **Findings & Adaptations** section documenting a real API change discovered and resolved during development.

## 🐛 Bugs & Findings

Any inconsistencies found during testing are logged as [GitHub Issues](../../issues) in this repository, including steps to reproduce and expected vs. actual behavior.

## 🎥 Demo Video

[Link to demo video — coming soon]

A 5–10 minute walkthrough covering the project's design decisions, a live test run, and an explanation of the testing approach.

## 📜 Certificates

Course completion certificates for the QA specialization are available in the [`certificates/`](./certificates) folder, and via [this Google Drive link] *(add link here)*.



# My code:
WTC-YLZFENXH