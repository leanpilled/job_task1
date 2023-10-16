from django.urls import path
from .views import get_files, post_file


urlpatterns = [
    path('files/', get_files),
    path('upload/', post_file),
]