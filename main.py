from contextlib import asynccontextmanager

from fastapi import FastAPI
from routers import router as tasks_router
from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tables()
    print('Очищено')
    await create_tables()
    print('Готово')
    yield
    # Clean up the ML models and release the resources
    print('Выключение')

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)









