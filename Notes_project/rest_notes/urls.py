from django.urls import path
from .views import UserAPIList, UserAPIDetailView

urlpatterns = [
    path('/api/v1/userlist/', UserAPIList.as_view(), name='rest_view'),
    path('/api/v1/userdetail/<int:pk>/', UserAPIDetailView.as_view()),
]