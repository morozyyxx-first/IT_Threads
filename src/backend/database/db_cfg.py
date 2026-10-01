from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from db_settings import db_settings

engine = create_async_engine(db_settings.DB_URL)#, echo = True)
session_factory = async_sessionmaker(engine, expire_on_commit = False)
Base = declarative_base()

# Function of creating tables and initialization database
# async def db_start():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

# Function of getting session
async def session_maker():
    async with session_factory() as ses:
        return ses