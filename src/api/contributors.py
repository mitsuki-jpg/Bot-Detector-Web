from fastapi import APIRouter, Request

from src.core.config import CONFIG, templates

router = APIRouter()


@router.get("/")
async def contributors(request: Request):
    return templates.TemplateResponse("pages/contributors.html", {"request": request})
