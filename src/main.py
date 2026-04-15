import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.routes.notes import router
from src.storage.memory import NoteStorage

# Initialize storage
storage = NoteStorage()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Storage is initialized
    print("Storage initialized")
    yield
    # Shutdown: Cleanup if needed
    print("Shutting down")

app = FastAPI(
    title="Notes API",
    description="A simple API to manage notes",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to Notes API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)