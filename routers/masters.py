from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import get_masters
from database import get_db
from schemas import MasterBaseOut

masters_router = APIRouter(prefix="/masters",
                           tags=["Masters"], )


@masters_router.get("/masters", response_model=list[MasterBaseOut])
def get_all_masters(db: Session = Depends(get_db)):
    masters = get_masters(db)
    return masters
