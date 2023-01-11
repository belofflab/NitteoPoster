from fastapi import FastAPI
# from src.database.connection import database
from src.routers import items

app = FastAPI()

# @app.on_event("startup")
# async def startup():
#     if not database.is_connected:
#         await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     if database.is_connected:
#         await database.disconnect()


@app.get('/')
async def root(): 
    return {"status": "Project succesfully started "}

app.include_router(items.router, prefix="/api/v1", tags=['items'])


