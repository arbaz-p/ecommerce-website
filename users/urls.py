from django.urls import path
from .views import RegisterView,ManagerView
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns=[
    path('register/',RegisterView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('manager/',ManagerView.as_view())
]