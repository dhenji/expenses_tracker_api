from unittest.mock import Mock

from expenses_tracker_api.core.config import Settings


def test_db_pg_url_encodes_credential() -> None:
    settings = Settings(
        app_name="expenses-tracker-api",
        environment="test",
        db_pg_host="localhost",
        db_pg_port=5432,
        db_pg_user="test_user",
        db_pg_db_name="test_db",
    )

    settings.__dict__["_secrets"] = Mock()
    settings.__dict__["_secrets"].read.return_value = "test_password"

    assert settings.db_pg_url == (
        "postgresql+psycopg://test_user:test_password@localhost:5432/test_db"
    )
