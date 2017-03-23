#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'The City of Toronto collects travel time data from Bluetooth and WiFi sensors on streets and highways across the City. Travel times are derived from individual point (i.e. single location) observations, generated when a vehicle or mobile device passes by a Bluetooth/WiFi sensor. Historical data (refreshed monthly) and a real-time feed are both available to the public.  Data is averaged into 5-minute snapshots based on a sample of detected vehicles. Availability of historical and real-time data are contingent on the installation date and on-going functionality of sensors on individual segments. '})
    app.run(port=8282)
