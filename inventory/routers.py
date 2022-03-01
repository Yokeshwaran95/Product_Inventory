from prod_app.viewsets import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product',ProductViewSet)