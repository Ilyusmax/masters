import uvicorn
from fastapi import FastAPI

from database import engine

import db_models
from routers.categories import categories_router
from routers.masters import masters_router

db_models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(categories_router)
app.include_router(masters_router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8001, reload=False)
