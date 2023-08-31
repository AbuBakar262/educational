from django.urls import path
from .views import UserViewSet, UserLoginViewSet

urlpatterns = [
    # endpoints for users
    path('create_user', UserViewSet.as_view({'post': 'create_user'})),
    path('login', UserLoginViewSet.as_view({"post": "login"}), name='login'),
]
