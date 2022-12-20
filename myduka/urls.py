"""myduka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "MyDuka Administrator"
admin.site.site_title = "MyDuka Admin Portal"
admin.site.index_title = "Welcome to MyDuka Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cart", include("cart.urls", namespace="cart")),
    path("orders", include("orders.urls", namespace="orders")),
    path("payment/", include("payment.urls", namespace="payment")),
    # add others before since they are more restrictive
    path("", include("duka.urls", namespace="dukani")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
