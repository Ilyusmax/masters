from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, CheckConstraint
from sqlalchemy.orm import relationship

from database import Base

masters_category = Table('masters_category', Base.metadata,
                         Column('master_id', Integer, ForeignKey('masters.id')),
                         Column('category_id', Integer, ForeignKey('categories.id'))
                         )


class Masters(Base):
    __tablename__ = 'masters'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    phone_number = Column(String)
    city = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)

    # Establishing the relationship
    categories = relationship("Category", secondary=masters_category, back_populates="masters")

    __table_args__ = (
        CheckConstraint('price > 0', name='price_positive_constraint'),  # Constraint to ensure price is greater than 0
    )


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Establishing the relationship
    masters = relationship("Masters", secondary=masters_category, back_populates="categories")
