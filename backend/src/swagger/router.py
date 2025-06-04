from src.swagger.dependencies import check_auth
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.responses import JSONResponse


def create_swagger_router(app):
    router = APIRouter()

    @router.get("/docs")
    def swagger_ui(credentials: HTTPBasicCredentials = Depends(check_auth)):
        return get_swagger_ui_html(openapi_url="/openapi.json", title="Docs")

    @router.get("/redoc")
    def redoc_ui(credentials: HTTPBasicCredentials = Depends(check_auth)):
        return get_redoc_html(openapi_url="/openapi.json", title="ReDoc")

    @router.get("/openapi.json")
    def openapi_json(credentials: HTTPBasicCredentials = Depends(check_auth)):
        return JSONResponse(content=app.openapi())

    return router