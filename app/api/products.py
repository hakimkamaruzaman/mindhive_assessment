rom fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi import APIRouter

app = FastAPI()

router = APIRouter()

@router.get("/some-path")
def sample():
    return {"message": "Hello"}

# Updated database (as above)
product_data = {
    "zus all-can tumbler": {
        "price": "RM39.90",
        "color": "Black & Gold",
        "material": "Stainless Steel",
        "capacity": "350ml"
    },
    "zus classic mug": {
        "price": "RM29.90",
        "color": "White",
        "material": "Ceramic",
        "capacity": "300ml"
    },
    "zus thermal flask": {
        "price": "RM59.90",
        "color": "Blue",
        "material": "Insulated Stainless Steel",
        "capacity": "500ml"
    }
}

@app.get("/product_info")
def get_product_info(query: str = Query(..., description="Name or detail request")):
    query_lower = query.lower()

    for name, info in product_data.items():
        if name in query_lower:
            if "price" in query_lower or "cost" in query_lower:
                return {"result": f"The {name.title()} is {info['price']}"}
            elif "color" in query_lower:
                return {"result": f"The {name.title()} comes in {info['color']}"}
            elif "material" in query_lower:
                return {"result": f"The {name.title()} is made of {info['material']}"}
            elif "capacity" in query_lower or "size" in query_lower:
                return {"result": f"The {name.title()} holds {info['capacity']}"}
            else:
                return {"result": f"The {name.title()} is {info['price']} and comes in {info['color']}, made of {info['material']}, capacity: {info['capacity']}."}

    return JSONResponse(status_code=404, content={"error": "Product not found."})
