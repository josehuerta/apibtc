from rest_framework.routers import DefaultRouter
from .views import PrecioBtcView

router = DefaultRouter()

router.register(prefix='precio-btc-mxn', basename='precio-btc-mxn',
                viewset=PrecioBtcView)
