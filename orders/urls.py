from django.urls import path
from .views import OrderListAndCreateView,OrderRetrieveUpdateAndDestroyView


urlpatterns=[
    path('',OrderListAndCreateView.as_view()),

    path('<int:pk>/',OrderRetrieveUpdateAndDestroyView.as_view())
]