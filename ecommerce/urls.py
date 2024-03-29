from django.urls import path

from .views import home, register, user_login,products, to_cart,orders, logout_user,payments,profile_data

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('products/', products, name='products'),
    path('to_cart/<str:pk>', to_cart, name="cart"),
    path('oders/', orders, name="orders"),
    path('logout_user/', logout_user, name="logout"),
    path('payments/', payments, name="payments"),
    path('profile_data/', profile_data, name="profile"),
]