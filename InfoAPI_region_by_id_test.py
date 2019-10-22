"""
Получение информации о регионе внутри страны, по идентификатору региона
Описание метода API:
http://sr-app01-t12-02.test-s02.uniservers.ru:1010/help/index.html#Countries-GetRegion
"""
import requests
import pytest
import jsonschema
import json


api_method = '/api/v1/countries/RUS/regions/'  # Вызов InfoAPI для получения данных региона по идентификатору
id = 289  # Идентификатор региона

@pytest.fixture
def response(info_api_app):
    """Производим запрос к API"""
    return requests.get(info_api_app + api_method + str(id))


@pytest.fixture()
def json_validator(response):
    """Получаем схему JSON из файла и сравниваем ответ сервиса со схемой JSON в файле InfoAPI_region_by_id_schema.json"""
    json_schema = open("InfoAPI_region_by_id_schema.json").read()
    json_validator = jsonschema.validate(response.json(), json.loads(json_schema))
    print(json_validator)
    return json_validator


def test_status_code(response):
    """HTTP-код ответа 200. Запрос успешен."""
    print(response.text)
    assert response.status_code == 200


def test_json_schema(json_validator):
    """Полученный JSON соответствует схеме."""
    try:
        json_validator
    except json_validator.SchemaError as schemaError:
        print(schemaError)
    assert json_validator is None


# def test_id(response):
#     """В ответ получен тот же идентификатор"""
#     print(response.json()['id'])
#     assert response.json()['id'] == id
#
#
# def test_country_code(response):
#     """В ответ получен верный код региона"""
#     print(response.json()['countryCode'])
#     assert response.json()['countryCode'] == "RUS"
#
#
# def test_name(response):
#     """В ответ получено верное название города"""
#     print(response.json()['name'])
#     assert response.json()['name'] == "Крымск"
#
#
# def test_currencies(response):
#     """В ответ получен верный список валют (для России пустой) """
#     print(response.json()['currencies'])
#     assert response.json()['currencies'] == []
#
#
# def test_subway(response):
#     """В ответ получены верные данные о наличии метро"""
#     print(response.json()['subway'])
#     assert response.json()['subway'] is False
#
#
# def test_links(response):
#     """В JSON-ответе имеется верный объект _links"""
#     print(response.json()['_links'])
#     assert response.json()['_links'] == {
#         "self": "/api/v1/countries/RUS/regions/" + str(id)
#     }
