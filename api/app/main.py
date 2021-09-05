from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI(title='Belka Space API')


@app.get('/')
async def root():
    return {"message": "Hello World!"}


register_tortoise(
    app,
    db_url="sqlite://hollow.db",
    modules={"models": ['core.models.database']},
    generate_schemas=True,
    add_exception_handlers=True,)
