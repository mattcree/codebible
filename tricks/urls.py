from django.urls import path

from .views import CodeTrickListView, CodeTrickCreateView

urlpatterns = [
    path('', CodeTrickListView.as_view(), name='index'),
    path('new', CodeTrickCreateView.as_view(), name='new')
]