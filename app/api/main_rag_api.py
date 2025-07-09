from fastapi import FastAPI
from app.api.products import router as products_router
from app.api.outlets import router as outlets_router

app = FastAPI(title="MindHive RAG + Tool API")

# Register routers
app.include_router(products_router, prefix="/products")
app.include_router(outlets_router, prefix="/outlets")
