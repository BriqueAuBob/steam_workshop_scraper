from requests import get

from Exceptions import HttpException


class Request:
    BASE_URL = 'https://steamcommunity.com/id/'

    @staticmethod
    def make(url):
        response = get(Request.BASE_URL + url)
        if response.status_code != 200:
            raise HttpException
        return response.text