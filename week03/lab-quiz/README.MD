# Lab 03 - Order Approval Policy

## Test Table (Boundary Cases)

| Order Amount (TRY) | Available Stock | Requested Quantity | Is Member | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| **499.99** (Below) | 10 | 2 | Yes | Approved (No discount) - Final Price: 499.99 TRY |
| **500.00** (Exact) | 10 | 2 | Yes | Approved (10% Discount) - Final Price: 450.00 TRY |
| **500.01** (Above) | 10 | 2 | Yes | Approved (10% Discount) - Final Price: 450.009 TRY |
| **200.00** (Error) | 5 | 10 | Yes | Rejected (Insufficient stock) - No final price shown |

## Test & Revision Note

- **Test Executed:** Tested the 500 TRY threshold with 10 available stock, requested quantity of 2, and a member user.
- **Revision Made:** Initially, `requested_quantity <= 0` was not explicitly validated. Added a check during the validation phase to reject zero or negative quantities.
