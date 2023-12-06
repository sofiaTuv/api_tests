import jsonschema
import pytest
import requests

from tests.utils import load_schema


def test_get_single_user_successfully():
    url = 'https://reqres.in/api/users/2'
    schema = load_schema('get_single_user.json')

    result = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


@pytest.mark.parametrize('id_', [1, 2, 3])
def test_get_single_user_id(id_):
    url = f"https://reqres.in/api/users/{id_}"

    result = requests.get(url)
    assert result.json()['data']['id'] == id_


def test_list_of_users_pagination():
    page = 2
    url = "https://reqres.in/api/users"

    result = requests.get(url, params={"page": page})

    assert result.json()["page"] == page


def test_list_of_users_per_page():
    page = 2
    per_page = 6
    url = "https://reqres.in/api/users"

    result = requests.get(
        url=url,
        params={"page": page, "per_page": per_page}
    )

    assert result.json()["per_page"] == per_page
    assert len(result.json()['data']) == per_page


def test_delete_user():
    url = 'https://reqres.in/api/users/2'
    result = requests.delete(url)

    assert result.status_code == 204


def test_create_user():
    url = 'https://reqres.in/api/users'
    schema = load_schema('create_user.json')

    result = requests.post(url,
                           {
                               "name": "morpheus",
                               "job": "leader"
                           })

    assert result.status_code == 201
    assert result.json()['name'] == 'morpheus'
    assert result.json()['job'] == 'leader'
    jsonschema.validate(result.json(), schema)


def test_put_update_user():
    url = 'https://reqres.in/api/users/2'
    schema = load_schema('put_apdate.json')
    result = requests.put(url,
                          {
                              "name": "morpheus",
                              "job": "zion resident"
                          })

    assert result.status_code == 200
    assert result.json()['name'] == 'morpheus'
    assert result.json()['job'] == 'zion resident'
    jsonschema.validate(result.json(), schema)


def test_get_single_user_not_found():
    url = "https://reqres.in/api/users/23"
    result = requests.get(url)
    assert result.status_code == 404
    assert result.json() == {}


def test_get_register_unsuccessful():
        url = 'https://reqres.in/api/register'
        schema = load_schema('register_user.json')

        result = requests.post(url,
                               json={
                                   "email": "eve.holt@reqres.in"
                               })

        assert result.status_code == 400
        assert result.json()['error'] == 'Missing password'







