from unittest.mock import Mock

from expenses_tracker_api.core.config import Settings


def test_db_pg_url_encodes_credential() -> None:
    settings = Settings(
        app_name="expenses-tracker-api",
        environment="test",
        db_pg_host="postgres",
        db_pg_port=5432,
        db_pg_user="test_user",
        db_pg_db_name="test_db",
        db_pg_user_password=None,
    )

    settings.__dict__["_secrets"] = Mock()
    settings.__dict__["_secrets"].read.return_value = "test_password"

    assert settings.db_pg_url == (
        "postgresql+psycopg://test_user:test_password@postgres:5432/test_db"
    )


def test_db_pg_url_prefers_env_password_over_secret() -> None:
    settings = Settings(
        app_name="expenses-tracker-api",
        environment="test",
        db_pg_host="postgres",
        db_pg_port=5432,
        db_pg_user="test_user",
        db_pg_db_name="test_db",
        db_pg_user_password="env_password",
    )
    settings.__dict__["_secrets"] = Mock()
    settings.__dict__["_secrets"].read.return_value = "file_password"

    assert settings.db_pg_url == (
        "postgresql+psycopg://test_user:env_password@postgres:5432/test_db"
    )
    settings._secrets.read.assert_not_called()
