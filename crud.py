from sqlalchemy.orm import Session, joinedload
import db_models


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Category).offset(skip).limit(limit).all()


def get_masters(db: Session):
    return db.query(db_models.Masters).options(joinedload(db_models.Masters.categories)).all()


def get_masters_by_category_db(db: Session, category: str):
    return db.query(db_models.Category).filter(db_models.Category.name == category).options(joinedload(db_models.Category.masters)).all()
