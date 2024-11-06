from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from DuckFumApp import views
from DuckFumApp.views import login_view

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('login/', login_view, name='login'),
    path('registro/', views.register_view, name='registro'),
    path('carrito/', views.carrito, name='carrito'),
    path('admin/', views.admin, name='admin'),
    path('admin/create/', views.create, name='create'),
    path('detalle/', views.detalle, name="detalle")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
