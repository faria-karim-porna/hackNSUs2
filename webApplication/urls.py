"""webApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('tryAlert',views.tryAlert),
    # purchase url
    path('purchase_add', views.purchase_add),
    path('purchase_show', views.purchase_show),
    path('purchase_edit/<int:id>', views.purchase_edit),
    path('purchase_update/<int:id>', views.purchase_update),
    path('purchase_delete/<int:id>', views.purchase_delete),
    # stored product url
    path('stored_product_show', views.stored_product_show),
    # stock out product url
    path('stock_out_show', views.stock_out_show),
    # billing system url
    path('billing_show', views.billing_show),
    path('billing_edit/<int:id>', views.billing_edit),
    path('billing_update/<int:id>', views.billing_update),
    # sale product url
    path('sale_show', views.sale_show),
    # login signup url
    path('signup',views.handleSignup, name='handleSignup'),
    path('login',views.handleLogin, name='handleLogin'),
    path('logout',views.handleLogout)
]
