# Expenses Tracker API

FastAPI-based expense tracking API in development. Uses layered architecture with CQS pattern: write operations through a Unit of Work, read operations through direct queries.

## Tech Stack

- **Runtime:** Python 3.13, FastAPI, Uvicorn
- **ORM:** SQLAlchemy 2.0 + psycopg3 (PostgreSQL 16)
- **Migrations:** Flyway (plain SQL)
- **Auth:** Argon2 password hashing via pwdlib
- **Dev env:** Docker Compose (primary workflow), uv for package management

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (package manager)
- Docker & Docker Compose (for the primary dev workflow)

## Environment Setup

Both `.env` and `secrets/` are gitignored — you need to create them manually after cloning.

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

SECRETS_PATH=/run/secrets
```

- `SECRETS_PATH` points to the directory where the DB password file lives. Set it to `./secrets` when running locally outside Docker.
- When using Docker Compose, `DB_PG_HOST` must be `postgres` (the service name), not `localhost`.

### `secrets/pg-user-password.txt`

The DB password is stored separately as a Docker secret file. Create it with your own password:

```bash
mkdir -p secrets
echo "your_password_here" > secrets/pg-user-password.txt
```

This file is mounted at `/run/secrets/pg_user_password` inside containers and read by the app at startup.

## Quick Start

### Local development

```bash
uv sync --frozen
uv run pytest
uvicorn expenses_tracker_api.main:app --reload
```

### Docker Compose (primary workflow)

```bash
docker compose -f docker-compose.dev.yml up -d postgres flyway app
docker compose -f docker-compose.dev.yml run test
```

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

## Project Structure

```
src/
├── expenses_tracker_api/
│   ├── main.py                  # FastAPI app entrypoint
│   ├── api/                     # Routes + DI wiring
│   │   ├── router.py
│   │   ├── deps.py
│   │   └── v1/
│   │       ├── users.py
│   │       └── categories.py
│   ├── core/                    # Config, database, security, UoW
│   ├── shared/                  # Exceptions, repo utils
│   ├── user/                    # User domain (model, DTO, schema, repo, service)
│   └── category/                # Category domain
├── tests/                       # Test suite
db/
└── migrations/                  # Flyway SQL migrations
```

## Development Notes

- **Migrations:** Add new files to `db/migrations/` as `V<number>__<description>.sql`. Run via Flyway in Docker.
- **Secrets:** DB password is in `secrets/pg-user-password.txt`, mounted as a Docker secret at `/run/secrets/pg_user_password`. Not in `.env`. Tests mock the secret reader.
- **Tests:** `uv run pytest` or `docker compose -f docker-compose.dev.yml run test`.

## Status

- **Implemented:** User CRUD, category creation, database schema + seed data
- **Planned:** Expenses CRUD, category read/update/delete, authentication/authorization
