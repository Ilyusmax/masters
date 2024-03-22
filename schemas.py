from pydantic import BaseModel


class MasterBase(BaseModel):
    id: int
    name: str
    phone_number: int
    city: str
    description: str
    price: float
    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class MasterBaseOut(MasterBase):
    categories: list[CategoryBase]


class CategoryBaseOut(CategoryBase):
    masters: list[MasterBase]
