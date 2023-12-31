from django.urls import path
from .views import (
    IntroductionViewSet, PartViewSet,
    AboutUsViewSet, ContactInfoViewSet,
    CompilerViewSet, SubPartViewSet,
    ContactUsViewSet
)

urlpatterns = [
    # introduction urls
    path('create_intro', IntroductionViewSet.as_view({'post': 'create'})),
    path('update_intro/<int:pk>', IntroductionViewSet.as_view({'put': 'update'})),
    path('get_intro/<int:pk>', IntroductionViewSet.as_view({'get': 'retrieve'})),
    path('list_intro', IntroductionViewSet.as_view({'get': 'list'})),
    # part urls
    path('create_part', PartViewSet.as_view({'post': 'create'})),
    path('update_part/<int:pk>', PartViewSet.as_view({'put': 'update'})),
    path('get_part/<int:pk>', PartViewSet.as_view({'get': 'retrieve'})),
    path('list_part', PartViewSet.as_view({'get': 'list'})),
    # sub part urls
    path('create_sub_part', SubPartViewSet.as_view({'post': 'create'})),
    path('update_sub_part/<int:pk>', SubPartViewSet.as_view({'put': 'update'})),
    path('get_sub_part/<int:pk>', SubPartViewSet.as_view({'get': 'retrieve'})),
    path('list_sub_part', SubPartViewSet.as_view({'get': 'list'})),
    path('get_by_part_id', SubPartViewSet.as_view({'get': 'get_by_part'})),
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
    # compiler urls
    path('execute_code/<int:pk>', CompilerViewSet.as_view({'get': 'execute_code'})),
    path('list_codes', CompilerViewSet.as_view({'get': 'list'})),
    path('create_codes', CompilerViewSet.as_view({'post': 'create'})),
    # address of contact us urls
    path('create_contact_us', ContactUsViewSet.as_view({'post': 'create'})),
    path('update_contact_us/<int:pk>', ContactUsViewSet.as_view({'put': 'update'})),
    path('get_contact_us/<int:pk>', ContactUsViewSet.as_view({'get': 'retrieve'})),
    path('list_contact_us', ContactUsViewSet.as_view({'get': 'list'})),
]
