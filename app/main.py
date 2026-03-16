from fastapi import FastAPI
from app.api.health_routes import router as health_router


app=FastAPI(title="ChartGPT API", description="API for ChartGPT, a tool for generating charts from natural language queries.")
app.include_router(health_router)

@app.get("/")
def route():
    return {"message":"The backend server is running"}