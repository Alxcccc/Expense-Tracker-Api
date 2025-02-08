from fastapi import FastAPI

from src.app.infrastructure.database.database import DataBase
from src.app.expenses.infrastructure.routers.expense_router import router as expense_router

app = FastAPI(title=" FastApi - Expense Tracker API")

@app.on_event("startup")
def startup():
    DataBase.create_engin()

app.include_router(expense_router, prefix="/expense",tags=["Expenses"])
