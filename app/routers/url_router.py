from app.service.url_service import generate_short_id
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.database import get_db
from app.models.url_models import URL
from app.schemas.url_schemas import URLCreate
import httpx

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_short_url(url_create: URLCreate, db: AsyncSession = Depends(get_db)):
    """Сокращает переданный URL и возвращает его идентификатор."""
    original_url_str = str(url_create.url)
    q = await db.execute(select(URL).where(URL.original_url == original_url_str))
    existing_url = q.scalars().first()
    if existing_url:
        return {"short_id": existing_url.short_id}

    # Generate unique short_id:
    while True:
        short_id = generate_short_id()
        q2 = await db.execute(select(URL).where(URL.short_id == short_id))
        if not q2.scalars().first():
            break

    new_url = URL(original_url=original_url_str, short_id=short_id)
    db.add(new_url)
    await db.commit()
    await db.refresh(new_url)
    return {"short_id": new_url.short_id}


@router.get("/{short_id}", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def redirect_to_original(short_id: str, db: AsyncSession = Depends(get_db)):
    """Возвращает оригинальный URL по идентификатору."""
    q = await db.execute(select(URL).where(URL.short_id == short_id))
    url_obj = q.scalars().first()
    if not url_obj:
        raise HTTPException(status_code=404, detail="URL not found")
    return Response(
        status_code=status.HTTP_307_TEMPORARY_REDIRECT,
        headers={"Location": url_obj.original_url},
    )


@router.get("/async-request")
async def async_request():
    return {"message": "This is async request"}


@router.get("/sync-request-for-test")
def sync_request_for_test():
    return {"message": "This is sync request"}
