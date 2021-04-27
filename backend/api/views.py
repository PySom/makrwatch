from django.shortcuts import render
import requests
from rest_framework import status, request
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

# Create your views here.

# Create cache for previous searched result
searched_videos = {}
api_key = 'AIzaSyCs6bjpUgW-sKvkK3a3_TzZlr7urWFysPc'


@api_view(('GET',))
def youtube_api(request, term, token=None):
    # Append token to term if there is any
    # This will serve as the key
    if token:
        key = term+token
    else:
        key = term
    value = searched_videos.get(key)
    if value:
        return Response(value, status=status.HTTP_200_OK)
    else:
        params = {
            'part': 'snippet',
            'maxResults': 20,
            'key': api_key,
            'type': 'video',
            'order': 'date',
            'pageToken': token,
            'q': term
        }
        user_request = requests.get(
            'https://www.googleapis.com/youtube/v3/search', params=params, timeout=10)
        if user_request.status_code == 200:
            data = user_request.json()
            # Add this result to cache
            searched_videos[key] = data
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'error'}, status=user_request.status_code)
