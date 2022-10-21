from django.urls import path
from . import views
from rest_framework import routers


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register(r'api/registeruser', views.RegisterUserAPI)
router.register(r'api/address', views.UserAddressAPI)

urlpatterns = [
    path('',views.start),
    path('',views.test),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls
