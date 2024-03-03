import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

masters = [
    {"name": "Ivan",
     "surname": "Trololo",
     "city": "Prague",
     "language": "Ru/Cz",
     "category": "Electric"},
    {"name": "Valera",
     "surname": "dededed",
     "city": "Prague",
     "language": "En/Cz",
     "category": "notarius"},
    {"name": "ededed",
     "surname": "dededed",
     "city": "Prague",
     "language": "En/Cz",
     "category": "notarius"}
]


@app.get("/masters")
async def get_all_master():
    return masters


@app.get("/masters/categories/{category}")
async def get_muster_by_cat(category: str):
    masters_cats = []
    for master in masters:
        if master["category"].lower() == category.lower():
            masters_cats.append(master)
    if len(masters_cats) == 0:
        raise HTTPException(status_code=404,
                            detail="The category is not found. "
                                   "Pls try next endpoint to see "
                                   "list of possible categories: /categories")
    return masters_cats


@app.get("/categories")
async def get_all_cats():
    s = []
    for master in masters:
        s.append(master["category"])
    return list(set(s))

if __name__ == '__main__':
    uvicorn.run("main:app",port=8001, reload=False)

