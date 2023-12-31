from django.urls import path
from .views import ItemList, LocationList, ItemDetail, LocationDetail


# 4 end points along with primary key to access each item


urlpatterns = [
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
]
