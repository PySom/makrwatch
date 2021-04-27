from django.urls import path
from .views import youtube_api
urlpatterns = [
    path('youtube/term/<term>',
         youtube_api, name='youtube_api'),
    path('youtube/term/<term>/pageToken/<token>',
         youtube_api, name='youtube_api_with_page'),

]
