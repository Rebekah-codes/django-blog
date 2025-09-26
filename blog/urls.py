
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # Add any more specific blog paths here before the catch-all
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),  # More specific
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # Catch-all, must be last
]
