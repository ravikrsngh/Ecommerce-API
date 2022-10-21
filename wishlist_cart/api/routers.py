from rest_framework import routers
from .api import *

router = routers.SimpleRouter()
router.register(r'wishlist', WishlistAPI)
router.register(r'cart', CartAPI)
urlpatterns = router.urls
