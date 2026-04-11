from fastapi import FastAPI
from src.routes.notes import router

app = FastAPI(
    title="Notes API",
    description="A simple API to manage notes",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to Notes API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)