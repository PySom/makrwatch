from django.shortcuts import render
from datetime import datetime
import requests
import environ
from rest_framework import status, request
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
# Get environment variable - My API Key is here
env = environ.Env()
environ.Env.read_env()
# Create your views here.

# Create cache for previous searched result
searched_videos = {}
api_key = env('API_KEY')


def get_time_estimate(seconds):
    if seconds < 60:
        return 'less than a minute ago'
    # check for less than an hour - for minutes
    elif seconds < 60 * 60:
        value = int(seconds//60)
        if value <= 1:
            rep = ' minute ago'
        else:
            rep = ' minutes ago'
        return str(value) + rep
    # check for less than a day - for hour
    elif seconds < 60 * 60 * 24:
        value = int(seconds//(60 * 60))
        if value <= 1:
            rep = ' hour ago'
        else:
            rep = ' hours ago'
        return str(value) + rep
    # check for less than a month - for day
    elif seconds < 60 * 60 * 24 * 30:
        value = int(seconds//(60 * 60 * 24))
        if value <= 1:
            rep = ' day ago'
        else:
            rep = ' days ago'
        return str(value) + rep
    # check for less than a year - for month
    elif seconds < 60 * 60 * 24 * 365:
        value = int(seconds//(60 * 60 * 24 * 30))
        if value <= 1:
            rep = ' month ago'
        else:
            rep = ' months ago'
        return str(value) + rep
    else:
        value = int(seconds//(60 * 60 * 24 * 365))
        if value <= 1:
            rep = ' year ago'
        else:
            rep = ' years ago'
        return str(value) + rep


def format_time(date):
    format = '%Y-%m-%dT%H:%M:%SZ'
    date_rep = datetime.strptime(date, format)
    today = datetime.now()
    total_seconds = (today - date_rep).total_seconds()
    return get_time_estimate(total_seconds)


def get_key(term, token):
    # Append token to term if there is any
    # This will serve as the key
    if token:
        key = term+token
    else:
        key = term

    return key


def get_local_search_term(key):
    return searched_videos.get(key)


def make_youtube_request(url, params):
    user_request = requests.get(
        'https://www.googleapis.com/youtube/v3/'+url, params=params, timeout=10)
    if user_request.status_code == 200:
        return user_request.json()
    else:
        raise Exception('An error occured')


@api_view(('GET',))
def youtube_api(request, term, token=None):
    key = get_key(term, token)
    value = get_local_search_term(key)
    # Use cached value if any
    if value:
        return Response(value, status=status.HTTP_200_OK)
    else:
        search_params = {
            'part': 'snippet',
            'maxResults': 20,
            'key': api_key,
            'type': 'video',
            'order': 'date',
            'pageToken': token,
            'q': term
        }
        video_param = {
            'part': 'statistics',
            'key': api_key,
        }
        try:
            data = make_youtube_request('search', params=search_params)
            # Get statistics for this video
            ids = [item['id']['videoId'] for item in data['items']]
            video_param['id'] = ','.join(ids)
            try:
                video_stat = make_youtube_request(
                    'videos', params=video_param)
                for index in range(0, len(data['items'])):
                    # Get formatted date
                    data['items'][index]['snippet']['publishedAt'] = format_time(
                        data['items'][index]['snippet']['publishedAt'])
                    # Assign statistics value
                    data['items'][index]['statistics'] = video_stat['items'][index]['statistics']
            except:
                pass
            # Add this result to cache
            searched_videos[key] = data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': err}, status=status.HTTP_400_BAD_REQUEST)
