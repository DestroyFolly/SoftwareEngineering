from sqlalchemy import create_engine, text
import asyncpg

engine = create_engine("postgresql+asyncpg://postgres:250803@localhost/fitnes", echo=True)

with engine.connect() as connection:
    result = connection.execute(text("select '2+5'"))
    print(result.scalar())