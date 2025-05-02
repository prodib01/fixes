from django.urls import path
from .views import SchoolListCreateAPIView, SchoolDetailAPIView, CampusDetailAPIView, CampusListCreateAPIView

urlpatterns = [
    path('schools/', SchoolListCreateAPIView.as_view(), name='school-list-create'),
    path('schools/<int:pk>/', SchoolDetailAPIView.as_view(), name='school-detail'),
    path('campuses/', CampusListCreateAPIView.as_view(), name='campus-list-create'),
    path('campuses/<int:pk>/', CampusDetailAPIView.as_view(), name='campus-detail'),
]