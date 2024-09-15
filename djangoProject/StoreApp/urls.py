from django.template.context_processors import static
from django.urls import path

from djangoProject import settings
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    # path('', views.registerUser),
    path('', views.home),
    path('home/shop/<int:product_id>/', views.productDetail),
    path('home', views.home),
    path('home/shop/indexProductDetail.htm', views.productDetail),
    path('home/shop/<int:product_id>/add-to-cart', views.add_to_cart),

    # path('',TemplateView.as_view(template_name='Front/notCorrectInfo.htm'))
]
