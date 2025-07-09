from fastapi import APIRouter, Query, HTTPException
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def sample():
    return {"message": "Hello from outlets"}

@router.get("/")
async def search_products(query: str = Query(...)):
    try:
        # Your actual logic
        return {"result": f"You asked about: {query}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
