from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from app.hotels.router import get_hotels_by_location_and_date


router = APIRouter(prefix="/pages", tags=["Фронтенд"])

templates = Jinja2Templates(directory="app/frontend/templates")


@router.get("/hotels")
async def get_hotels_page(
    request: Request, hotels=Depends(get_hotels_by_location_and_date)
):
    return templates.TemplateResponse(
        name="hotels.html", context={"request": request, "hotels": hotels}
    )
