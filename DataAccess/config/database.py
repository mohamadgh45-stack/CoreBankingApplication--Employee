import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

load_dotenv()


def build_connection_url():
    server = os.getenv("DB_SERVER")
    database_name = os.getenv("DB_NAME")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    driver = os.getenv("DB_DRIVER", "").replace("+", " ")

    query = {"driver": driver, "TrustServerCertificate": "yes"}

    if username and password:
        # SQL Server Authentication
        return URL.create(
            "mssql+pyodbc",
            username=username,
            password=password,
            host=server,
            database=database_name,
            query=query,
        )

    # Windows Authentication

    query["Trusted_Connection"] = "yes"
    return URL.create(
        "mssql+pyodbc",
        host=server,
        database=database_name,
        query=query,
    )


connection_url = build_connection_url()
engine = create_engine(connection_url, echo=True)

session_maker = sessionmaker(engine)


@contextmanager
def create_session():
    session = session_maker()
    try:
        yield session
    except Exception as ex:
        session.rollback()
        print(f"Database Exception -> {ex.args[0]}")
        raise
    else:
        session.commit()
    finally:
        session.close()
