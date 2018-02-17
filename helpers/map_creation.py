import folium
import requests

from data.tokens import API_KEY


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
        my_icon = folium.features.CustomIcon(
            friend['profile_image_url'],
            icon_size=(25, 25)
        )
        fg.add_child(
            folium.Marker(
                location=[coordinates[0], coordinates[1]],
                popup=str(friend['name']) + my_icon,
                icon=my_icon
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
