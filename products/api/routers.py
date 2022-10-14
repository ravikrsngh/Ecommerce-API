from rest_framework import routers
from .api import *

router = routers.SimpleRouter()
router.register(r'category', CategoryAPI)
router.register(r'products', ProductAPI)
router.register(r'filteroptions', FilterOptionAPI)
router.register(r'filteroptionitems', FilterOptionItemsAPI)

urlpatterns = router.urls
