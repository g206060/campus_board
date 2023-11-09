from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
]