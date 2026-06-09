"""
Database setup using SQLAlchemy.

SQLAlchemy gives you an ORM (Object-Relational Mapper): you write Python
classes and it turns them into SQL tables automatically.  Think of it as
Python objects ↔ database rows.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config import DATABASE_URL


# DeclarativeBase is the parent class all DB models inherit from
class Base(DeclarativeBase):
    pass


# The engine is the actual connection to the SQLite file
engine = create_engine(DATABASE_URL, echo=False)

# Session factory — each request gets its own session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def init_db():
    """Create all tables defined in schemas.py (if they don't exist yet)."""
    from . import schemas  # noqa: F401 — import schemas so Base knows about them
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Context-manager style DB session for use in Flask routes.

    Usage:
        with get_db() as db:
            db.query(...)

    TODO: yield a SessionLocal() and close it in a finally block.
    This is the standard SQLAlchemy session lifecycle pattern.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
