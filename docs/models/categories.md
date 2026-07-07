# Categories Model

Represents expense categories used for grouping transactions.

---

## Description

Categories help organize expenses into meaningful groups such as Food, Transport, and Utilities.

---

## Attributes

### id

- Type: Serial
- Description: Unique identifier for the category

### user_id

- Type: UUID (optional)
- Description: Owner of the category (null means global category)

### name

- Type: string
- Description: Name of the category (e.g., Food, Transport)

### created_at

- Type: datetime
- Description: Timestamp when the category was created
