
from django.urls import path
from .views import *
urlpatterns = [
    path('create/', MarketFormView.as_view(), name='create'),
    path('list/', MarketListView.as_view(), name='list'),
    path('detail/<int:pk>/', MarketDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', MarketDeleteView.as_view(), name='delete'),
]
