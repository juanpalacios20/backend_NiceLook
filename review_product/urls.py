from django.contrib import admin
from django.urls import path ,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('review_product', views.reviewProductViewSet, 'review_product.views')   

urlpatterns = [
    path('all/', include(router.urls)),
]