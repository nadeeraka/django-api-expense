from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import parse
from rest_framework.views import APIView
from rest_framework import viewsets, status, mixins, generics, views, permissions
from app import models, serializers
from rest_framework import filters, pagination
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from app.models import Expense, Income, Balance


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = serializers.IncomeSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = serializers.BalanceSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    pagination.PageNumberPagination.page_size_query_param = 'page_size'




class IncomeTypeViewSet(viewsets.ModelViewSet):
    queryset = models.IncomeType.objects.all()
    serializer_class = serializers.IncomeTypeSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class ExpenseTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ExpenseType.objects.all()
    serializer_class = serializers.ExpenseTypeSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    pagination.PageNumberPagination.page_size_query_param = 'page_size'
