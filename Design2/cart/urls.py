"""
URL configuration for ecommerceapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings
from cart import views
from django.urls import path
app_name="cart"


urlpatterns = [
    path('addtocart/<int:i>', views.addtocart, name='addtocart'),
    path('cart_view', views.cart_view, name='cart_view'),
    path('cart_remove/<int:i>', views.cart_remove, name='cart_remove'),
    path('Orderform', views.Orderform, name='Orderform'),
    path('paymentstatus/<str:p>', views.payment_status, name='paymentstatus'),
    path('vieworder',views.vieworder,name="vieworder"),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)