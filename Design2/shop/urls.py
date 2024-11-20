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
from shop import views
from django.urls import path
app_name="shop"


urlpatterns = [
    path('', views.Home, name='Home'),
    path('products/<int:i>',views.Products,name='products'),
    path('detail/<int:i>',views.ProductDetail,name='detail'),
    path('u_login',views.u_login,name='login'),
    path('register',views.register,name='register'),
    path('u_logout',views.u_logout,name='logout'),
    path('addcategories',views.addcategories,name='addcategories'),
    path('addproducts',views.addproducts,name='addproducts'),
    path('addstock/<int:i>', views.addstock, name='addstock'),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)