from fastapi import APIRouter, Request

from src.core.config import CONFIG, templates

router = APIRouter()


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})