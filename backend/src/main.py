from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.users.router import router as user_router
from src.data.router import router as data_router
from src.swagger.router import create_swagger_router
from src.reviews.router import router as review_router

app = FastAPI(title="IP_belkin", docs_url=None, redoc_url=None, openapi_url=None)
PORT=9000
HOST = "0.0.0.0"

app.include_router(user_router)
app.include_router(data_router)
app.include_router(create_swagger_router(app))
app.include_router(review_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000",
                   "http://212.192.127.152:9090"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run('src.main:app', host = HOST, port=PORT, reload = True)