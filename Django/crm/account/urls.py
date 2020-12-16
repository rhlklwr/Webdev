from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customers/<str:id>', views.customers, name='customers'),
    path('create_order/<str:id>', views.createOrder, name='create_order'),
    path('update_order/<str:id>', views.updateOrder, name='update_order'),
    path('delete_order/<str:id>', views.deleteOrder, name='delete_order'),
]