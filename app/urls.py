from django.urls import  path , include
from app import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'user', views.UserViewSet)
router.register(r'expense', views.ExpenseViewSet)
router.register(r'expenseType', views.ExpenseTypeViewSet)
router.register(r'income', views.IncomeViewSet)
router.register(r'incomeType', views.IncomeTypeViewSet)
router.register(r'balance', views.BalanceViewSet)
#router.register(r'expenseType', views.ExpenseTypeViewSet)




urlpatterns = [
       path('', include(router.urls)),
]
