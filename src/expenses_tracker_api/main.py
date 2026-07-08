from .core.config import Settings, get_settings


def main():
    setting: Settings = get_settings()
    print(setting.db_pg_port)


if __name__ == "__main__":
    main()
