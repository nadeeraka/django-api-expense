from django.urls import  path , include
from app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'expense', views.ExpenseViewSet)




urlpatterns = [
       path('', include(router.urls)),
]
