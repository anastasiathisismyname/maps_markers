import requests
import json


def get_all_locations_by_coordinates(box):

    resp = requests.get("http://api.luftdaten.info/static/v2/data.json").json()

    latitude1, longitude1, latitude2, longitude2 = float(box[0]), float(box[1]), float(box[2]), float(box[3])

    all_locations = []
    for location in resp:
        latitude = location["location"]["latitude"]
        longitude = location["location"]["longitude"]
        if latitude and longitude:
            point = [float(latitude), float(longitude)]
            if latitude1 < point[0] < latitude2 and longitude1 < point[1] < longitude2:
                all_locations.append(latitude)

    return all_locations


locations = get_all_locations_by_coordinates([50.396297, 30.432512, 50.492814, 30.585666])
# locations = get_all_locations_by_coordinates([0.514863, 0.361576, 50.401778, 30.683505])
str_data = json.dumps(locations)
with open("result.json", "w") as file:
    file.write(str_data)

