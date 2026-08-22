# Expense Categories Documentation

This document defines the default expense categories used in the Expenses Tracker application.

## Categories

## 1. Housing

Expenses related to maintaining a home or living space.

**Examples:**

- Rent
- Mortgage
- Property tax
- Home insurance
- Repairs and maintenance
- Furniture
- Home improvements

---

## 2. Utilities

Recurring household services and essential bills.

**Examples:**

- Electricity
- Water
- Gas
- Internet
- Mobile phone
- Cable or streaming services
- Garbage collection

---

## 3. Food & Drinks

Expenses related to meals, groceries, and beverages.

**Examples:**

- Groceries
- Restaurants
- Fast food
- Coffee
- Food delivery
- Snacks

---

## 4. Transportation

Expenses related to commuting and vehicle usage.

**Examples:**

- Fuel
- Public transportation
- Taxi or rideshare
- Parking
- Tolls
- Vehicle maintenance
- Vehicle insurance

---

## 5. Healthcare

Medical and wellness-related expenses.

**Examples:**

- Doctor visits
- Dental care
- Prescriptions
- Medical tests
- Health insurance
- Therapy

---

## 6. Shopping

General purchases and personal items.

**Examples:**

- Clothing
- Shoes
- Electronics
- Accessories
- Household items
- General purchases

---

## 7. Entertainment

Expenses for leisure and recreational activities.

**Examples:**

- Movies
- Concerts
- Games
- Books
- Hobbies
- Music subscriptions

---

## 8. Travel

Expenses related to trips and vacations.

**Examples:**

- Flights
- Hotels
- Vacation activities
- Travel transportation
- Travel insurance

---

## 9. Education

Expenses related to learning and professional development.

**Examples:**

- Tuition fees
- Courses
- Books
- School supplies
- Certifications

---

## 10. Work & Business

Expenses related to employment or business activities.

**Examples:**

- Office supplies
- Software subscriptions
- Equipment
- Marketing
- Professional services

---

## 11. Personal Care

Expenses related to personal maintenance and wellness.

**Examples:**

- Haircuts
- Cosmetics
- Skincare
- Spa services
- Gym memberships

---

## 12. Family & Kids

Expenses related to family members and children.

**Examples:**

- Childcare
- School expenses
- Baby supplies
- Toys
- Allowances

---

## 13. Financial

Expenses related to financial obligations and money management.

**Examples:**

- Loan payments
- Credit card payments
- Bank fees
- Interest payments
- Investments
- Savings contributions

---

## 14. Gifts & Donations

Expenses related to giving and celebrations.

**Examples:**

- Birthday gifts
- Holiday gifts
- Wedding gifts
- Charity donations
- Religious contributions

---

## 15. Miscellaneous

Expenses that do not fit into other categories.

**Examples:**

- Unexpected expenses
- One-time purchases
- Uncategorized expenses
- Other expenses

---

# Implementation Notes

- Implemented as Alembic data migration: `alembic/versions/ed4ac8f928f4_seed_default_expense_categories.py` (idempotent via `ON CONFLICT (name) DO NOTHING`).
- Categories should be stored as configurable data instead of hardcoded values.
- Users should be able to customize, add, disable, or rename categories.
- Categories can optionally support subcategories for more detailed tracking (not included).

## Example Category Structure

```text
Food & Drinks
├── Groceries
├── Restaurants
├── Coffee
└── Food Delivery
```
