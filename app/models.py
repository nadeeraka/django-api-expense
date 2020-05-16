from datetime import datetime
from typing import List, Tuple
from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='app_user')
    email = models.EmailField()


class Income(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    income_type = models.ForeignKey("IncomeType", default='', on_delete=models.CASCADE, related_name="incomes")
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    created_time = models.DateTimeField(default=datetime.now, blank=True)
    update_time = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['id']


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    expense_type = models.ForeignKey("ExpenseType", on_delete=models.CASCADE, related_name="expenses")
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    created_time = models.DateTimeField(default=datetime.now, blank=True)
    update_time = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['id']


class Saving(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    selection = models.ForeignKey('SavingType', on_delete=models.CASCADE, related_name="savings")
    amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    created_time = models.DateTimeField(default=datetime.now, blank=True)
    rate = models.DecimalField(max_digits=100, decimal_places=4, default=0)
    update_time = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['id']


class ExpenseType(models.Model):
    id = models.AutoField(primary_key=True)
    selection_type = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']


class SavingType(models.Model):
    id = models.AutoField(primary_key=True)
    selection_type = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']


class IncomeType(models.Model):
    id = models.AutoField(primary_key=True)
    selection_type = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']


# class Balance(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.CharField(max_length=100, blank=True)
#     amount = models.DecimalField(max_digits=100, decimal_places=4, default=0)
#     update_time = models.DateTimeField(default=datetime.now, blank=True)
#     created_time = models.DateTimeField(default=datetime.now, blank=True)
#
#     class Meta:
#         ordering = ['id']