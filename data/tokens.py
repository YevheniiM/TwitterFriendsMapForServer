"""tokens.py

The module provides the data to the program.

"""


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
API_KEY = "AIzaSyAgddL1nFKDhUNuiEAPFNUD-kNktOratbU"


def auth():
    """The function provides data to access twitter API

    () -> (dict)

    """
    return {
        "consumer_key": "Aj5UJ2bxhDcT4HYwUiVGvM3iH",
        "consumer_secret": "oKUW2JAkdoXqybXABpdDD2fDgvPLl7qtkUFyE6mdb9El3AyApg",
        "token_key": "964111790434119681-ITLPnBt3Stx1s3EMKRzHSmD29CvwBs8",
        "token_secret": "gGbyfdw5PT87FDBby9shoXWAbRuaVFT7Ok2gXaJTUg0Rl"
    }