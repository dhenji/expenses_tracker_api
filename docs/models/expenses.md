# Expenses Model

Represents a financial transaction or expense record.

---

## Description

The Expenses model stores all user spending records including amount, category, and metadata.

---

## Attributes

### id

- Type: UUID
- Description: Unique identifier for the expense

### user_id

- Type: UUID
- Description: Reference to the user who owns the expense

### category_id

- Type: integer
- Description: Reference to the category of the expense

### amount

- Type: decimal
- Description: Amount spent

### currency

- Type: string (ISO 4217)
- Description: Currency code used (e.g., PHP, USD)

### description

- Type: string (optional)
- Description: Notes or details about the expense

### merchant

- Type: string (not implemented)
- Description: Where the expense was made

### payment_method

- Type: string (not implemented)
- Description: Method used for payment (Cash, GCash, Card, etc.)

### expense_date

- Type: date
- Description: Date when the expense occurred

### location

- Type: string (not implemented)
- Description: Location of the transaction

### receipt_url

- Type: string (not implemented)
- Description: Link to receipt image or file

### created_at

- Type: datetime
- Description: Timestamp when the record was created

### updated_at

- Type: datetime
- Description: Timestamp when the record was last updated
