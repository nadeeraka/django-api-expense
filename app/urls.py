from django.urls import  path , include
from app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)




urlpatterns = [
       path('', include(router.urls)),
]
