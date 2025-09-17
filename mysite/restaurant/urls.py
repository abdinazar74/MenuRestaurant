from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, CategoryViewSet, MenuItemViewSet, OrderViewSet

router = DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('categories', CategoryViewSet)
router.register('menuitems', MenuItemViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
