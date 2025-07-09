from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/calculate")
def calculate(expression: str = Query(..., description="Math expression to evaluate")):
    try:
        # Safe eval: allow only math expressions
        result = eval(expression, {"__builtins__": {}})
        return {"result": result}
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"error": f"Invalid expression: {str(e)}"}
        )
