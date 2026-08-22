# Expenses Tracker API

FastAPI-based expense tracking API in development. Uses layered architecture with CQS pattern: write operations through a Unit of Work, read operations through direct queries.

## Tech Stack

- **Runtime:** Python 3.13, FastAPI, Uvicorn
- **ORM:** SQLAlchemy 2.0 + psycopg3 (PostgreSQL 16)
- **Migrations:** Alembic (SQLAlchemy migrations)
- **Auth:** Argon2 password hashing via pwdlib
- **Dev env:** Docker Compose (primary workflow), uv for package management

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (package manager)
- Docker & Docker Compose (for the primary dev workflow)

## Environment Setup

`.env` is gitignored — you need to create it manually after cloning.

### `.env`

Copy the template below into `.env` at the project root and adjust as needed:

```env
APP_NAME=Expenses_Tracker_API
ENVIRONMENT=development
APP_PORT=8000

DB_PG_HOST=localhost
DB_PG_PORT=5432
DB_PG_USER=exp_track_user
DB_PG_DB_NAME=exp_track_db
DB_PG_USER_PASSWORD=your_password_here
```

- `DB_PG_USER_PASSWORD` is the DB password, set directly here for development.
- When using Docker Compose, `DB_PG_HOST` must be `postgres` (the service name), not `localhost`.

> **Deployment:** for non-development environments, the password is injected by your own tooling (e.g. a cloud secrets manager / orchestrator secret) as the `DB_PG_USER_PASSWORD` env var. The app falls back to a Docker secret file mounted at `/run/secrets/pg_user_password` if the env var is unset.

## Quick Start

### Local development

```bash
uv sync --frozen
uv run pytest
uv run alembic upgrade head
uvicorn expenses_tracker_api.main:app --reload
```

### Docker Compose (primary workflow)

```bash
docker compose -f docker-compose.dev.yml up -d postgres app
DB_PG_HOST=localhost uv run alembic upgrade head
docker compose -f docker-compose.dev.yml run test
```

Migrations run from the host against the published Postgres port, hence the `DB_PG_HOST=localhost` override (inside containers the host is `postgres`).

## API Endpoints

All routes under `/api/v1`.

| Method | Path | Description |
|--------|------|-------------|
| POST | `/users/` | Create user |
| GET | `/users/` | List users |
| GET | `/users/{user_id}` | Get user by ID |
| GET | `/users/by-email/{email}` | Get user by email |
| PATCH | `/users/{user_id}` | Update user |
| DELETE | `/users/{user_id}` | Delete user |
| POST | `/categories/` | Create category |
| GET | `/categories/` | List categories |
| GET | `/categories/{category_id}` | Get category by ID |
| GET | `/categories/by-name/{name}` | Get category by name |
| DELETE | `/categories/{category_id}` | Delete category |
| POST | `/expenses/` | Create expense |
| GET | `/expenses/` | List expenses |
| GET | `/expenses/{expense_id}` | Get expense by ID |
| DELETE | `/expenses/{expense_id}` | Delete expense |

## Project Structure

```
src/
├── expenses_tracker_api/
│   ├── main.py                  # FastAPI app entrypoint
│   ├── api/                     # Routes + DI wiring
│   │   ├── router.py
│   │   ├── deps.py
│   │   └── v1/
│   │   ├── users.py
│   │   ├── categories.py
│   │   └── expenses.py
│   ├── core/                    # Config, database, security, UoW
│   ├── shared/                  # Exceptions, repo utils
│   ├── user/                    # User domain (model, DTO, schema, repo, service)
│   ├── category/                # Category domain
│   └── expense/                 # Expense domain (create, list, get, delete)
├── tests/                       # Test suite
alembic/
├── env.py                       # Alembic env wired to app settings (DB URL from core/config.py)
└── versions/
    ├── 9b04f42c35dd_init_schema.py                    # tables: users, categories, expenses
    └── ed4ac8f928f4_seed_default_expense_categories.py # idempotent category seed
```

## Development Notes

- **Migrations:** Alembic. Create revisions with `uv run alembic revision -m "..."` into `alembic/versions/` and apply with `uv run alembic upgrade head`. Seed data lives in data migrations using raw SQL guarded by `ON CONFLICT DO NOTHING`. Never edit an applied revision — add a new one instead.
- **Pre-Alembic databases:** if your database was created back when migrations ran via Flyway, adopt it once with `uv run alembic stamp 9b04f42c35dd` before running `upgrade head`.
- **Secrets:** DB password is set via the `DB_PG_USER_PASSWORD` env var from `.env` in development. For deployment, inject it with your own tooling; the app falls back to a Docker secret at `/run/secrets/pg_user_password`. Tests mock the secret reader.
- **Tests:** `uv run pytest` or `docker compose -f docker-compose.dev.yml run test`.

## Status

- **Implemented:** User CRUD; category create/list/get/delete; expense create/list/get/delete; database schema + seed data
- **In progress:** Expense update, category update, authentication/authorization
