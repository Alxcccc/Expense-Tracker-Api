from typing import List
from sqlmodel import Session, select
from sqlalchemy.exc import NoResultFound

# Entity
from src.app.expenses.domain.entities.expense import Expense

# Repository
from src.app.expenses.domain.repositories.expense_repository import ExpenseRepository

# Database
from src.app.infrastructure.database.database import DataBase

# DB model
from src.app.infrastructure.database.models.expense_model import ExpenseDatabase

# value objects
from src.app.expenses.domain.value_objects.expense_id import ExpenseId
from src.app.expenses.domain.value_objects.expense_title import ExpenseTitle
from src.app.expenses.domain.value_objects.expense_date import ExpenseDate
from src.app.expenses.domain.value_objects.expense_description import ExpenseDescription
from src.app.expenses.domain.value_objects.expense_category import ExpenseCategory
from src.app.expenses.domain.value_objects.expense_amount import ExpenseAmount
from src.app.expenses.domain.value_objects.expense_id_user import ExpenseIdUser

class ExpenseRepositoryImpl(ExpenseRepository):

    def format_expense(self, id_expense, expense_title, expense_date, description, category, amount, idUser):
        return Expense(
                        id_expense=ExpenseId(value=id_expense), 
                        expense_title=ExpenseTitle(value=expense_title),
                        expense_date=ExpenseDate(value=expense_date),
                        description=ExpenseDescription(value=description),
                        category=ExpenseCategory(value=category),
                        amount=ExpenseAmount(value=amount),
                        idUser=ExpenseIdUser(value=idUser)
                        )
    
    def get_all(self, id_user: int) -> List[Expense]:
        try:
            with Session(DataBase.engine) as session:
                statement = select(ExpenseDatabase).where(ExpenseDatabase.idUser == id_user)
                results = session.exec(statement).all()
                if not results:
                    return None
                result = list()
                for expense in results:
                    result.append(self.format_expense(expense.id_expense, expense.expense_title, expense.expense_date, expense.description, expense.category, expense.amount, expense.idUser))
                return result
            
        except Exception as e:
            raise Exception(str(e))
            
        except NoResultFound as e:
            raise ValueError(str(e))
    
    def get_by_id(self, id_user: int, id_expense: int) -> Expense:
        try:
            with Session(DataBase.engine) as session:
                statement = select(ExpenseDatabase).where(ExpenseDatabase.id_expense == id_expense).where(ExpenseDatabase.idUser == id_user)
                expense = session.exec(statement).one()
                if not expense:
                    return None
                return self.format_expense(expense.id_expense, expense.expense_title, expense.expense_date, expense.description, expense.category, expense.amount, expense.idUser)
    
        except Exception as e:
            raise Exception(str(e))
        
        except NoResultFound as e:
            raise ValueError(str(e))

    
    def create(self, id_user: int, expense: Expense) -> Expense:
        try:
            with Session(DataBase.engine) as session:
                new_expense = ExpenseDatabase(expense_title=expense.expense_title, expense_date=expense.expense_date, description=expense.description, category=expense.category, amount=expense.amount, idUser=id_user)
                statement = session.add(new_expense)
                session.commit()
        except Exception as e:
            raise Exception(str(e))
    
    def update(self, id_user: int, id_expense: int, new_expense: Expense) -> Expense:
        try:
            with Session(DataBase.engine) as session:
                statement = select(ExpenseDatabase).where(ExpenseDatabase.id_expense == id_expense).where(ExpenseDatabase.idUser == id_user)
                expense = session.exec(statement).one()
                if expense.expense_title != new_expense.expense_title.value:
                    expense.expense_title = new_expense.expense_title.value
                    
                if expense.expense_date != new_expense.expense_date.value:
                    expense.expense_date = new_expense.expense_date.value
                    
                if expense.description != new_expense.description.value:
                    expense.description = new_expense.description.value
                    
                if expense.category != new_expense.category.value:
                    expense.category = new_expense.category.value
                    
                if expense.amount != new_expense.amount.value:
                    expense.amount = new_expense.amount.value
                    
                session.add(expense)
                session.commit()
                session.refresh(expense)
                session.commit()
                
        except Exception as e:
            raise Exception(str(e))
    
    def delete(self, id_user: int, id_expense: int) -> bool:
        try:
            with Session(DataBase.engine) as session:
                statement = select(ExpenseDatabase).where(ExpenseDatabase.id_expense == id_expense).where(ExpenseDatabase.idUser == id_user)
                expense = session.exec(statement).one()
                session.delete(expense)
                session.commit()
        except Exception as e:
            raise Exception(str(e))