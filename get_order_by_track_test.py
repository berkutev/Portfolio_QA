import sender_stand_request
import data
import configuration
import requests
import pytest
import json

# POST-запрос на создание нового заказа

def post_create_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER_PATH, json = order_body)

# Функция, которая в качестве параметра будет получать номер заказа

def get_order_track():
    track_number = post_create_new_order(data.order_body)
    return track_number.json()["track"]

# Беркут Екатерина, 10-я когорта - Финальный проект. Инженер по тестированию плюс
# Тест на получение заказа по треку заказа (приходит код 200)

def test_get_order_by_track():
    track_number = get_order_track()
    response = sender_stand_request.get_order_by_track(track_number)
    assert response.status_code == 200

