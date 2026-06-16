from os import getenv

DATABASE_URL = (
    f"postgresql://{getenv('POSTGRES_USER')}:{getenv('POSTGRES_PASSWORD')}"
    f"@postgres:5432/{getenv('POSTGRES_DB')}"
)
