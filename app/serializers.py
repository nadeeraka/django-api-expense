from rest_framework import serializers
from app import models
from django.contrib.auth.models import User, Group


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AppUser
        fields = ['username']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = '__all__'

class SavingeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Saving
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

class FixedDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FixedDeposit
        fields = '__all__'

