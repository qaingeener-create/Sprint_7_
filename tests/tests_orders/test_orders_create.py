import requests
import allure
from urls import Urls
import data

import json
import requests
from allure import step, title, description

class TestOrderCreate:
    @title('Проверка создания заказа с разными параметрами цвета')
    @description('Согласно требованиям, система должна позволять указать в заказе один цвет самоката, выбрать '
                 'сразу оба или не указывать совсем. В тест по очереди передаются наборы данных с разными '
                 'параметрами: серый, черный, оба цвета, цвет не указан. Проверяются код и тело ответа.')
    def test_order_create_color_parametrize_success(self):
        # Список данных для тестирования
        test_data = [
            {"color": "grey"},
            {"color": "black"},
            {"color": ["grey", "black"]},
            {}
        ]

        for param in test_data:
            # Преобразование данных в JSON-формат для отправки
            order_data_json = json.dumps(param)
            # Установка заголовков для JSON-запроса
            headers = {'Content-Type': 'application/json'}

            with step('Отправка POST запроса на создание заказа'):
                response = requests.post(Urls.URL_orders_create, data=order_data_json, headers=headers, timeout=5)

            # Проверка успешного создания заказа (код 201) и наличия track-номера
            assert response.status_code == 201 and 'track' in response.text
