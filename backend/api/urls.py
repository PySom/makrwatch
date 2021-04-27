from django.urls import path
from .views import youtube_api
urlpatterns = [
    path('youtube/<content>', youtube_api, name='youtube_api')
]
