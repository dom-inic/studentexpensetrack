from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from . models import Expense


class ExpenseManager:
    @staticmethod
    def create_expense(user, card, category, expense_date, amount, notes=None):
        """
        Creates a new expense record.
        """
        new_expense = Expense.objects.create(
            user=user,
            card=card,
            category=category,
            expense_date=expense_date,
            amount=amount,
            notes=notes,
        )
        return new_expense

    @staticmethod
    def get_user_expenses(user):
        """
        Retrieves all expenses for a specific user.
        """
        return Expense.objects.filter(user=user)

    @staticmethod
    def get_expense_by_id(expense_id):
        """
        Retrieves an expense by its ID.
        """
        return Expense.objects.get(pk=expense_id)

    @staticmethod
    def update_expense(expense_id, card=None, category=None, expense_date=None, amount=None, notes=None):
        """
        Updates an existing expense record.
        """
        expense = Expense.objects.get(pk=expense_id)
        if card:
            expense.card = card
        if category:
            expense.category = category
        if expense_date:
            expense.expense_date = expense_date
        if amount:
            expense.amount = amount
        if notes is not None:
            expense.notes = notes
        expense.save()
        return expense

    @staticmethod
    def delete_expense(expense_id):
        """
        Deletes an expense record by its ID.
        """
        expense = Expense.objects.get(pk=expense_id)
        expense.delete()
