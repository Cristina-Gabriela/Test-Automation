import requests


def get_data(poi):
    overpass_url = "https://overpass.kumi.systems/api/interpreter"
    overpass_query = ""
    [out: json];
node
    [amenity = cafe]
    (41.8949549, 12.4910693);
out;
    """
    overpass_query = '[out: json];node;(amenity = '+poi+')(41.8949549, 12.4910693);out;'
    response = requests.get(overpass_url, params={
        "data": overpass_query
    })
    return response.json()


if __name__ == '__main__':
    my_data = get_data("pub")
    print(my_data)
