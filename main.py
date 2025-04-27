from fastapi import FastAPI
from app.routers.url_router import router as url_router
from app.routers.async_request import router as async_router

app = FastAPI()

# Подключаем роутеры
app.include_router(url_router)

app.include_router(async_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
