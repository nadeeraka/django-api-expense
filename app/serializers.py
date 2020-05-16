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
