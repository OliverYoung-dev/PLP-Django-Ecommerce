from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('register/', views.signup, name='register'),
    path('login/', views.login, name='login'),
    path('cart/', views.cart, name='cart_detail'),
    path('add_to_cart/int:product_id/', views.add_to_cart, name='add_to_cart'),


    path('remove-from-cart/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.signup, name='register'),
    path('login/', views.login, name='login'),
]
