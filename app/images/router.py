from fastapi import APIRouter, UploadFile
import shutil

router = APIRouter(prefix="/images", tags=["Загрузка изображений"])


@router.post("/hotels")
async def add_hotel_img(name: int, file: UploadFile):
    with open(f"app/static/images/{name}.webp", "wb+") as img:
        shutil.copyfileobj(file.file, img)
