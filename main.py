from fastapi import FastAPI

from src.app.infrastructure.database.database import DataBase
from src.app.expenses.infrastructure.routers.expense_router import router as expense_router
from src.app.users.infrastructure.routers.user_router import router as user_router

app = FastAPI(title=" FastApi - Expense Tracker API")

@app.on_event("startup")
def startup():
    DataBase.create_engin()

app.include_router(expense_router, prefix="/expense",tags=["Expenses"])
app.include_router(user_router, prefix="/user",tags=["Users"])
