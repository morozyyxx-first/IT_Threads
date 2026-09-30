import uvicorn
import os
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from routers import router

app = FastAPI(title = "IT Threads")
# Do not need lifespan because db is already initialized

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host = str(os.getenv("FASTAPI_HOST")), port = int(os.getenv("FASTAPI_PORT")))
