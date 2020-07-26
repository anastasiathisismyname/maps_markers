from flask import Flask
from flask import request
from flask import jsonify
import requests


clustered_maps_markers = Flask(__name__)

# http://127.0.0.1:5000/get_locations?box=50.396297,30.432512,50.492814,30.585666
@clustered_maps_markers.route('/get_locations')
def get_clustered_maps_markers():

    resp = requests.get("http://api.luftdaten.info/static/v2/data.json").json()

    box = request.args.get('box').split(",")

    latitude1, longitude1, latitude2, longitude2 = float(box[0]), float(box[1]), float(box[2]), float(box[3])

    all_locations = []
    for location in resp:
        latitude = location["location"]["latitude"]
        longitude = location["location"]["longitude"]
        if latitude and longitude:
            point = [float(latitude), float(longitude)]
            if latitude1 < point[0] < latitude2 and longitude1 < point[1] < longitude2:
                all_locations.append(latitude)

    return jsonify(all_locations)
