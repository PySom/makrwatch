import requests


class YoutubeRepository:

    def __init__(self):
        self.__path = 'https://crowdexpress.ng/api/users'
        self.results = {}

    def get_youtube_data(self, term):
        if self.__results.has_key(term):
            return self.results[term]
        user_request = requests.get(
            'https://crowdexpress.ng/api/users', timeout=10)
        if user_request.status_code == 200:
            data = user_request.json()
            self.results[term] = data
            return data
        else:
            raise Exception('An error occured')
