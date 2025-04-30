from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    url: HttpUrl


class URLInfo(BaseModel):
    id: int
    original_url: HttpUrl
    short_id: str

    class Config:
        from_attributes = True


class AsyncServiceResponse(BaseModel):
    data: dict  # example generic response from async service call (can be adjusted)
