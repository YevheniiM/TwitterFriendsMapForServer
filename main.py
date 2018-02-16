import ssl
import json
import twurl
import folium
import requests
import urllib.request
import urllib.parse
import urllib.error

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
API_KEY = "AIzaSyAgddL1nFKDhUNuiEAPFNUD-kNktOratbU"


def ignore_errors():
    """Ignore SSL certificate errors

    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def create_friends_list(json_file):
    friends = list()
    for user in json_file['users']:
        temp = dict()
        temp['name'] = user['name']
        temp['location'] = user['location']
        friends.append(temp)
    return friends


def request_remaining(headers):
    return headers['x-rate-limit-remaining']


def get_coordinates(address):
    """(string) -> (tuple[float, float])

    The functions finds actual coordinates of
    the place, which is given as a string and
    returns them in the tuple of floats

    """
    link = 'https://maps.googleapis.com/maps/api/geocode/'
    api_response = requests.get(
        link + 'json?address={0}&key={1}'.format(address, API_KEY)
    )
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        lat = api_response_dict['results'][0]['geometry']['location']['lat']
        lon = api_response_dict['results'][0]['geometry']['location']['lng']
        return lat, lon
    else:
        return 0, 0


def add_friends_layer(my_map, friends):
    """(folium.Map, list[tuple[string, int, string]]) -> (None)

    The function adds the layer with films to
    the map, which is given as an argument

    """
    fg = folium.FeatureGroup(name='Friends')

    for friend in friends:
        coordinates = get_coordinates(friend['location'])
        # if coordinates == (0, 0):
        #     continue
        fg.add_child(
            folium.Marker(
                location=[coordinates[0], coordinates[1]],
                popup=str(friend['name'])
            )
        )

    my_map.add_child(fg)


def create_map(friends):
    """(list[tuple[string, int, string]]) -> (None)

    The function creates map with a few
    layers, which are needed.

    """
    _map = folium.Map()

    add_friends_layer(_map, friends)

    _map.add_child(folium.LayerControl())
    _map.save("templates/FriendsMap.html")


def test_set_friends(user_account, count_of_friends):

    url = twurl.get_friends_url(TWITTER_URL, user_account, count_of_friends)

    connection = urllib.request.urlopen(url, context=ignore_errors())
    data = connection.read().decode()

    js = json.loads(data)

    print('Remaining:', request_remaining(dict(connection.getheaders())))

    friends = create_friends_list(js)
    create_map(friends)
