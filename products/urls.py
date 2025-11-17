from django.urls import path
from .views import ListAndAddProductView,RetrieveAndUpdateAndDestroyProductView

urlpatterns=[
    path('<int:pk>/',RetrieveAndUpdateAndDestroyProductView.as_view()),
    path('',ListAndAddProductView.as_view()),
]