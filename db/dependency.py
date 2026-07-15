from db.session import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator

# Dependency to get DB session
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()