from django.urls import path
from .views import CartListAndAddView,CartUpdateOrDeleteOrRetrieveView

urlpatterns=[
    path('',CartListAndAddView.as_view()),
    path('<int:pk>/',CartUpdateOrDeleteOrRetrieveView.as_view()), 
]