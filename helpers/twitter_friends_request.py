"""twitter_friends_request.py

The module provides functions to work with
data, which twitter's API returns

"""

import ssl
import urllib
import json

from data.tokens import TWITTER_URL
from helpers import twitter_url
from helpers.map_creation import create_map


def ignore_errors():
    """Ignore SSL certificate errors

    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def create_friends_list(json_file):
    """Creates the list of friends with some data

    (dict) -> (list[dict])

    """
    friends = list()
    for user in json_file['users']:
        temp = dict()
        temp['name'] = user['name']
        temp['location'] = user['location']
        temp['profile_image_url'] = user['profile_image_url']
        temp['screen_name'] = user['screen_name']
        friends.append(temp)
    return friends


def request_remaining(headers):
    """The function returns the number of remaining requests

    (dict) -> (str)

    """
    return headers['x-rate-limit-remaining']


def show_friends_on_the_map(user_account, count_of_friends):
    """The function shows user's friends on the map

    (string, string) -> (None)

    """
    url = twitter_url.get_friends_url(TWITTER_URL, user_account, count_of_friends)
    connection = urllib.request.urlopen(url, context=ignore_errors())
    data = connection.read().decode()
    js = json.loads(data)

    print('Remaining:', request_remaining(dict(connection.getheaders())))
    print(json.dumps(js, indent=2))

    friends = create_friends_list(js)
    create_map(friends)
