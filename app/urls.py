from django.urls import path, include
from app import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'user', views.UserViewSet)
router.register(r'expense', views.ExpenseViewSet)
router.register(r'expenseType', views.ExpenseTypeViewSet)
router.register(r'income', views.IncomeViewSet)
router.register(r'incomeType', views.IncomeTypeViewSet)
#router.register(r'balance', views.BalanceViewSet)
# router.register(r'getBalance', views.get_balance.)


urlpatterns = [
    path('', include(router.urls)),
    # path('taktTime/', views.TaktTimeView.as_view()),
    path('get_ba', views.get_balance),
    path('get_ex', views.get_expense),
    path('h_ex', views.get_higest_Expense),
    path('ava_ex', views.get_ava_ex)
]
