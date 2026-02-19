# OrangeHRM Automation Test Strategy
Author: Alice_Nguyen
Framework: Playwright + Pytest (Python)
Project Type: Web Application (Business Flow Testing)
Target: https://opensource-demo.orangehrmlive.com/

---

## 1. Project Objective

The goal of this automation project is to:

- Design a scalable automation framework using Playwright (Python)
- Automate core business flows of OrangeHRM
- Implement smoke and regression test suites
- Integrate with GitLab CI for merge request validation
- Demonstrate production-ready QA engineering practices

---

## 2. Scope of Automation

### In Scope
- Role-based login
- Employee Management (PIM)
- Leave Management
- Business End-to-End HR Flow

### Out of Scope
- Performance testing
- Security testing
- Cross-browser compatibility matrix
- Mobile testing

---

## 3. Test Levels

### 3.1 Smoke Tests

Purpose:
- Validate system stability
- Verify core business functionality
- Run on every Merge Request

Characteristics:
- 5–8 test cases
- Covers only happy paths
- Execution time < 7 minutes

Includes:
- Admin login
- Create employee
- Apply leave
- Approve leave

---

### 3.2 Regression Tests

Purpose:
- Validate full functionality
- Run nightly or before release

Includes:
- Validation tests
- Negative scenarios
- Role restrictions
- Data integrity checks
- Edge cases

---

## 4. Test Tagging Strategy

- @smoke
- @regression
- @business
- @role
- @validation

Example:
@pytest.mark.smoke
@pytest.mark.business

---

## 5. Test Isolation Strategy

- Each test must be independent
- No shared state between tests
- Random data generation
- Cleanup after execution (if applicable)

---

## 6. Test Data Strategy

- Use dynamic test data
- Generate unique employee names
- Avoid hardcoded values
- Environment-based config (dev/staging)

---

## 7. Cleanup Strategy

- Delete created employee if required
- Or use unique data to avoid collision

---

## 8. Execution Strategy

### Merge Request Pipeline
- Run smoke tests only
- Block merge if failure

### Nightly Pipeline
- Run full regression
- Generate full report

---

## 9. Retry Strategy

- 1 retry for flaky tests
- Capture screenshot on failure
- Capture trace for debugging

---

## 10. Reporting Strategy

- HTML report
- Artifact upload in GitLab
- Screenshot on failure
- Optional: Allure integration

---

## 11. Test Pyramid Model

UI Tests: Majority
API Tests: Optional extension
Unit Tests: Out of scope (Dev responsibility)

---

## 12. Risks & Mitigation

Risk: Flaky UI element
Mitigation: Proper wait strategy, locator stability

Risk: Data collision
Mitigation: Random test data

Risk: Slow execution
Mitigation: Parallel execution
