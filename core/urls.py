from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/',  views.logout_view ,name='logout'),
    path('add_to_cart/<item_id>/',views.add_to_cart,name="add_to_cart"),
    path('cart/',views.view_cart,name="cart"),
    path('cart/delete/<int:id>/', views.cart_delete, name='cart_delete'),
    # path('order_placed/',views.order_placed,name="order_placed"),

]
