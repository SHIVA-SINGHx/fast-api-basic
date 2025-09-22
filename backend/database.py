from sqlalchemy.orm import create_engine
from sqlalchemy.orm import sessionmaker


db_url = "postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi"
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit= False, autoflush = False, bind=engine )