from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/products/")
def query_product(query: str = Query(...)):
    return {"result": f"You asked about: {query}"}
