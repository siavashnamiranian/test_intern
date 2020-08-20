from django.urls import path, include

from products.views import home_page, product_detail

urlpatterns = [
    path('home/', home_page),
    path('<int:pk>/', product_detail)
]
