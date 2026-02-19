# OrangeHRM Automation Test Cases

---

## LOGIN MODULE

| Test ID | Title | Type | Priority | Description |
|---------|-------|------|----------|-------------|
| TC-LOGIN-01 | Valid Admin Login | Smoke | High | Admin login with valid credentials |
| TC-LOGIN-02 | Invalid Password | Regression | High | Incorrect password validation |
| TC-LOGIN-03 | Empty Username | Regression | Medium | Required field validation |
| TC-LOGIN-04 | Logout | Regression | Medium | Verify logout functionality |

---

## ROLE-BASED ACCESS

| Test ID | Title | Type | Priority | Description |
|---------|-------|------|----------|-------------|
| TC-ROLE-01 | Employee cannot access Admin | Regression | High | Access restriction |
| TC-ROLE-02 | Admin sees full menu | Regression | Medium | Verify role-based UI |

---

## PIM MODULE

| Test ID | Title | Type | Priority |
|---------|-------|------|----------|
| TC-PIM-01 | Create Employee (Happy Path) | Smoke | High |
| TC-PIM-02 | Missing First Name | Regression | High |
| TC-PIM-03 | Duplicate Employee ID | Regression | High |
| TC-PIM-04 | Search Employee | Regression | Medium |
| TC-PIM-05 | Delete Employee | Regression | Medium |

---

## LEAVE MODULE

| Test ID | Title | Type | Priority |
|---------|-------|------|----------|
| TC-LEAVE-01 | Apply Leave | Smoke | High |
| TC-LEAVE-02 | Invalid Date | Regression | Medium |
| TC-LEAVE-03 | Approve Leave | Smoke | High |
| TC-LEAVE-04 | Reject Leave | Regression | Medium |
| TC-LEAVE-05 | Leave Balance Update | Regression | High |

---

## BUSINESS FLOW

| Test ID | Title | Type | Priority |
|---------|-------|------|----------|
| TC-BUSINESS-01 | End-to-End HR Flow | Regression | Critical |
