from django.urls import path, include
from app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'expense', views.ExpenseViewSet)
router.register(r'expenseType', views.ExpenseTypeViewSet)
router.register(r'income', views.IncomeViewSet)
router.register(r'incomeType', views.IncomeTypeViewSet)

# router.register(r'getBalance', views.get_balance.)


urlpatterns = [
    path('', include(router.urls)),
    path('balance', views.Balance.as_view()),
    # path('taktTime/', views.TaktTimeView.as_view()),
    path('ba', views.get_balance),
    path('ex', views.get_expense),
    path('h_ex', views.get_higest_Expense),
    path('ava_ex', views.get_ava_ex),
    path('graph', views.analyze)
]
