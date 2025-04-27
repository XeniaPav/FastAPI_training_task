from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random
import string

router = APIRouter()

# Хранилище для сокращенных URL
url_storage = {}

class UrlRequest(BaseModel):
    url: str


def generate_random_id(length=6):
    """Генерирует случайный идентификатор заданной длины."""
    characters = string.ascii_letters + string.digits  # Буквы и цифры
    return "".join(random.choice(characters) for _ in range(length))


@router.post("/", status_code=201)
async def shorten_url(url_request: UrlRequest):
    """Сокращает переданный URL и возвращает его идентификатор."""
    url_id = generate_random_id()
    while url_id in url_storage:
        url_id = generate_random_id()
    url_storage[url_id] = url_request.url
    return {"shortened_url_id": url_id}


@router.get("/{shorten_url_id}", status_code=307)
async def get_original_url(shorten_url_id: str):
    """Возвращает оригинальный URL по идентификатору."""
    original_url = url_storage.get(shorten_url_id)
    if original_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"location": original_url}
