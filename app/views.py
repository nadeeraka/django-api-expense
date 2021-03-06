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
from app.models import Expense, Income ,Saving
import functools
from app.util import count
from app.helpers import saving_resolver
from app.core import main,normal_savings

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

    @action(detail=True, methods=['GET'])
    def test(self, request, pk=None, *args, **kwargs):
        # ex = Expense.objects.filter(id=)
        print(self.request.user)
        return Response(data='ok')


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = serializers.IncomeSerializer
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


class SavingTypeViewSet(viewsets.ModelViewSet):
    queryset = models.SavingType.objects.all()
    serializer_class = serializers.SavingTypeSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class SavingViewSet(viewsets.ModelViewSet):
    queryset = models.Saving.objects.all()
    serializer_class = serializers.SavingSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    pagination.PageNumberPagination.page_size_query_param = 'page_size'

    @action(detail=True, methods=['GET'])
    def savings(self, request, pk=None, *args, **kwargs):
        # ex = Expense.objects.filter(id=)
        s = models.Saving.objects.all()
        # savings = saving_resolver(s)
        print(self.request.user)

        return Response(data='ok')


class FixedDepositViewSet(viewsets.ModelViewSet):
    queryset = models.FixedDeposit.objects.all()
    serializer_class = serializers.FixedDepositSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


class LoanViewSet(viewsets.ModelViewSet):
    queryset = models.Loan.objects.all()
    serializer_class = serializers.LoanSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    pagination.PageNumberPagination.page_size_query_param = 'page_size'


# api views


@api_view(['GET'])
def get_balance(request):
    expenseArray = Expense.objects.filter(user_id=request.user.id) \
        .values_list('amount', flat=True)  # get only one field in list
    incomeArray = Income.objects.filter(
        user_id=request.user.id).values_list('amount', flat=True)
    if len(incomeArray) == 0:
        return Response(data={"balance": '000,00'}, status=status.HTTP_200_OK)

    if len(expenseArray) == 0:
        return Response(data={"balance": incomeArray}, status=status.HTTP_200_OK)

    try:
        income = functools.reduce(lambda a, b: a + b, incomeArray)
        expense = functools.reduce(lambda a, b: a + b, expenseArray)
        if income > expense:
            balance = income - expense
        else:
            return Response(data={"massage": "not sufficient income"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={"massage": "bad request", "error": e}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={"amount": balance}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_expense(request):
    expense_array = Expense.objects.filter(
        user_id=request.user.id).values_list('amount', flat=True)
    try:
        value = main.Generics.calculate(expense_array)
    except Exception as e:
        return Response(data={"massage": "bad request"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={"amount": value, }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_higest_Expense(request):
    try:
        ex = Expense.objects.filter(
            user_id=request.user.id).values_list('amount', flat=True)
        high = main.Generics.max_ex(ex)

        return Response(data={"amount": high}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"massage": "bad request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_minimun_Expense(request):
    try:
        ex = Expense.objects.filter(
            user_id=request.user.id).values_list('amount', flat=True)
        min = main.Generics.min_ex(ex)
        return Response(data={"amount": min}, status=status.HTTP_200_OK)
    except:
        return Response(data={"massage": "bad request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_normal_savings(request):
    try:
        savings_array = Saving.objects.filter(
            user_id=request.user.id).filter(selection_id=1).values_list('amount', flat=True)
        savings = normal_savings.Saving_resolver.get_normal_savings(savings_array, 12)
        return Response(data={"amount": savings}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"massage": "bad request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_ava_ex(request):
    ex = Expense.objects.filter(
        user_id=request.user.id).values_list('amount', flat=True)
    try:
        amount = functools.reduce(lambda a, b: a + b, ex)
        if len(ex) > 0:
            val = amount / len(ex)
            return Response(data={"amount": val}, status=status.HTTP_200_OK)
    except:
        return Response(data={"massage": "bad request"}, status=status.HTTP_400_BAD_REQUEST)


# get all expenses @ given range
# TODO
@api_view(['POST'])
def get_ex_filter_by_given_date(request):
    try:
        data = request.data['time_range']
    except:
        return Response(data={"massage": "bad request"}, status=status.HTTP_400_BAD_REQUEST)


# balance
class Balance(APIView):
    def get(self, request):
        print(self.request.user)
        expenseArray = Expense.objects.filter(user_id=self.user.id) \
            .values_list('amount', flat=True)  # get only one field in list
        print(expenseArray)
        incomeArray = Income.objects.filter(
            user_id=self.user.id).values_list('amount', flat=True)
        try:
            income = functools.reduce(lambda a, b: a + b, incomeArray)
            expense = functools.reduce(lambda a, b: a + b, expenseArray)
            if income > expense:
                balance = income - expense
            else:
                return Response(data={"massage": "not sufficient income"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={"massage": "bad request", "error": e}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"amount": balance}, status=status.HTTP_200_OK)


# ################################# ###############################################
###################################################################################
# forcast
####################################################################################

# graph data
# TODO
@api_view(['GET'])
def analyze(request):
    typeIdSet = list(Expense.objects.filter(
        user_id=request.user.id).values_list('expense_type', flat=True))
    expenseArray = Expense.objects.filter(user_id=request.user.id) \
        .values_list('amount', flat=True)  # get only one field in list
    print(expenseArray)
    incomeArray = Income.objects.filter(
        user_id=request.user.id).values_list('amount', flat=True)

    # uniqeval = set(typeIdSet)
    # for i in uniqeval:
    #     Expense.objects.filter(user_id=request.user.id).values_list('expense_type', flat=True)

    print(set(typeIdSet))
    return Response(data={"amount": 'value'}, status=status.HTTP_200_OK)

# class BalanceViewSet(viewsets.ModelViewSet):
#     queryset = Balance.objects.all()
#     serializer_class = serializers.BalanceSerializer
#     # permission_classes = [IsAuthenticated]
#     permission_classes = (permissions.AllowAny,)
#     pagination.PageNumberPagination.page_size_query_param = 'page_size'


# @action(detail=True, methods=['get'])
# def get(self, request, *args, **kwargs):
#     income = Income.object.amount
#     print(income)
#     return Response(data='success', status=status.HTTP_200_OK)

# @action(detail=True, methods=['get'])
# def delT(self, request, *args, **kwargs):
#     # print(self.request.user)
#     # id = request.data['id']
#     # print(id)
#     return Response(data='success', status=status.HTTP_200_OK)
