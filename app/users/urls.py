from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'(?P<pk>\d+)$', views.UserViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update',
                                                      'delete': 'destroy'})),
    path('', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}))
]
