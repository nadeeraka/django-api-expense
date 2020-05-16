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
import functools



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

    @action(detail=True, methods=['get'])
    def delT(self, request, *args, **kwargs):
        # print(self.request.user)
        # id = request.data['id']
        # print(id)
        return Response(data='success', status=status.HTTP_200_OK)


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


# @action(detail=True, methods=['get'])
# def get(self, request, *args, **kwargs):
#     income = Income.object.amount
#     print(income)
#     return Response(data='success', status=status.HTTP_200_OK)

@api_view(['GET'])
def get_balance(self):
    def getCount(array):
        count = 0
        for i in array:
            count += i
        return count
    # serializer = serializers.UserSerializer(request.user)
    # serializer = serializers.ExpenseSerializer
    expenseArray = Expense.objects.values_list('amount', flat=True).order_by('id') #get only one field in list
    incomeArray = Income.objects.values_list('amount',flat=True)

    #print('count',balance)
    try:
        balance = functools.reduce(lambda a, b: a + b, incomeArray) - functools.reduce(lambda a, b: a + b, expenseArray)
    except Exception as e: return Response(data=expenseArray, status=status.HTTP_400_BAD_REQUEST)

    # data = serializers.serialize('json', self.get_queryset())
    return Response(data=balance, status=status.HTTP_200_OK)


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
