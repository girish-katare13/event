from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EventViewset,UserRegistrationView,UserLoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'events',EventViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name= 'login'),
]
