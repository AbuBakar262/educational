from django.urls import path
from .views import (
    IntroductionViewSet, ContentViewSet,
    AboutUsViewSet, ContactInfoViewSet,
    CompilerViewSet,
)

urlpatterns = [
    # introduction urls
    path('create_intro', IntroductionViewSet.as_view({'post': 'create'})),
    path('update_intro/<int:pk>', IntroductionViewSet.as_view({'put': 'update'})),
    path('get_intro/<int:pk>', IntroductionViewSet.as_view({'get': 'retrieve'})),
    path('list_intro', IntroductionViewSet.as_view({'get': 'list'})),
    # content urls
    path('create_content', ContentViewSet.as_view({'post': 'create'})),
    path('update_content/<int:pk>', ContentViewSet.as_view({'put': 'update'})),
    path('get_content/<int:pk>', ContentViewSet.as_view({'get': 'retrieve'})),
    path('list_content', ContentViewSet.as_view({'get': 'list'})),
    # about us urls
    path('create_about', AboutUsViewSet.as_view({'post': 'create'})),
    path('update_about/<int:pk>', AboutUsViewSet.as_view({'put': 'update'})),
    path('get_about/<int:pk>', AboutUsViewSet.as_view({'get': 'retrieve'})),
    path('list_about', AboutUsViewSet.as_view({'get': 'list'})),
    # contact info urls
    path('create_contacts', ContactInfoViewSet.as_view({'post': 'create'})),
    path('update_contacts/<int:pk>', ContactInfoViewSet.as_view({'put': 'update'})),
    path('get_contacts/<int:pk>', ContactInfoViewSet.as_view({'get': 'retrieve'})),
    path('list_contacts', ContactInfoViewSet.as_view({'get': 'list'})),
    # complier urls
    path('create_compiler', CompilerViewSet.as_view({'post': 'post'})),
]
