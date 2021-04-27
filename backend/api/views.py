from django.shortcuts import render
from rest_framework import status, request
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from .repository import YoutubeRepository
# Create your views here.


@api_view(('GET',))
def youtube_api(request, content):
    _repo = YoutubeRepository()
    try:
        data = _repo.get_youtube_data()
        return Response(data, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': err}, status=user_request.status_code)
