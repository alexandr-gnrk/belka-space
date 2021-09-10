import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.v1.api import router


app = FastAPI(title='Belka Space API')
app.include_router(router)


@app.get('/')
async def root():
    return {"message": "Hello World!"}


register_tortoise(
    app,
    # db_url="sqlite://hollow.db",
    db_url="sqlite://:memory:",
    modules={"models": ['app.core.models.models']},
    generate_schemas=True,
    add_exception_handlers=True,)


if __name__ == "__main__":
    uvicorn.run("app:main", host="127.0.0.1", port=5000, log_level="info")
