import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
# подключение к базе данных
DATABASE_URL = f'postgresql+asyncpg://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@localhost/{os.getenv("POSTGRES_DB")}'

try:
    engine = create_async_engine(DATABASE_URL)
except Exception as e:
    print(f"Ошибка при создании соединения: {e}")
    raise

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


#
# def init_db():
#     """Инициализация базы данных: создание всех таблиц."""
#     Base.metadata.create_all(bind=engine)
