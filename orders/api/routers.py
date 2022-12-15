from rest_framework import routers
from .api import *

router = routers.SimpleRouter()
router.register(r'order', OrderAPI)
urlpatterns = router.urls
