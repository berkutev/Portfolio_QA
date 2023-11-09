import configuration
import data
import requests
import json
import get_order_by_track_test

# Функция получения заказа по трек-номеру

def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_PATH, params={"t":track_number})





