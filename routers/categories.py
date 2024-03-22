from enum import Enum
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from crud import get_masters_by_category_db, get_categories
from database import get_db
from schemas import CategoryBase, CategoryBaseOut

categories_router = APIRouter(prefix="/categories",
                              tags=["categories"], )


class Categories(str, Enum):
    electrician = "electrician"
    technician = "technician"


ENG_RUS_MAP: dict[Categories, str] = {
    Categories.electrician: "электрик",
    Categories.technician: "техник"
}


@categories_router.get("/categories", response_model=list[CategoryBase])
def get_masters_by_category(db: Session = Depends(get_db)):
    cats = get_categories(db)
    return cats


@categories_router.get("/categories/{cat_name}", response_model=list[CategoryBaseOut])
def get_masters_by_category(category: Categories,
                                  db: Session = Depends(get_db)):
    if category not in Categories:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Provided category doesn't exists: {category}")
    ru_category = ENG_RUS_MAP[category]
    cats = get_masters_by_category_db(db, ru_category)
    return cats
