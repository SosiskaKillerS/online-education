from fastapi import FastAPI
import uvicorn
from app.api.router_registry import api_router

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="localhost",
        port=8000,
        reload=True
    )