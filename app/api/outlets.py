from fastapi import APIRouter, Query, HTTPException

@router.get("/")
async def search_products(query: str = Query(...)):
    try:
        # Your actual logic
        return {"result": f"You asked about: {query}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
