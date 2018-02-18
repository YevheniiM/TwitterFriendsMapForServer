"""twitter_url.py

The module provides functions to access twitter API

"""

from helpers import oauth
from data import tokens


def augment(url, parameters):
    """The function generates appropriate url
    to access twitter's API

    """
    consumer_information = tokens.auth()
    consumer = oauth.OAuthConsumer(
        consumer_information['consumer_key'],
        consumer_information['consumer_secret']
    )
    token = oauth.OAuthToken(
        consumer_information['token_key'],
        consumer_information['token_secret']
    )

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(
        consumer,
        token=token,
        http_method='GET',
        http_url=url,
        parameters=parameters
    )
    oauth_request.sign_request(
        oauth.OAuthSignatureMethod_HMAC_SHA1(),
        consumer,
        token
    )

    return oauth_request.to_url()


def get_friends_url(twitter_url, name, count):
    """The function helps to form the url in easiest way

    """
    return augment(
        twitter_url,
        {
            'screen_name': name,
            'count': count
        }
    )
