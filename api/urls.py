from django.urls import path,include

urlpatterns=[
    path('user/',include('users.urls')),
    path('product/',include('products.urls')),
    path('cart/',include('carts.urls')),
    path('order/',include('orders.urls')),
]