# Users Model

Represents an account in the expense tracking system.

---

## Description

The Users model stores authentication and profile information for each user of the application.

---

## Attributes

### id

- Type: UUID
- Description: Unique identifier for the user

### name

- Type: string
- Description: Display name of the user

### email

- Type: string
- Description: Unique email used for login and communication

### password_hash

- Type: string
- Description: Encrypted password for authentication

### created_at

- Type: datetime
- Description: Timestamp when the user was created

### updated_at

- Type: datetime
- Description: Timestamp when the user was last updated
