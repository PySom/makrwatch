import requests


class YoutubeRepository:

    def __init__(self):
        self.__path = 'https://crowdexpress.ng/api/users'

    def get_youtube_data(self):
        user_request = requests.get(
            'https://crowdexpress.ng/api/users', timeout=10)
        if user_request.status_code == 200:
            return user_request.json()
        else:
            raise Exception('An error occured')
