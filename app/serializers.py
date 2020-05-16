from rest_framework import serializers
from app import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AppUser
        fields = ['user', 'email']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Income
        fields = '__all__'


# class BalanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Balance
#         fields = '__all__'


class IncomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IncomeType
        fields = '__all__'


class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpenseType
        fields = '__all__'
