import requests
import pytest
from requests import HTTPError
from jsonschema import validate


schema = {
    "type": "object",
    "properties": {
        'id': {"type": ["string", "null"]},
        'name': {"type": ["string", "null"]},
        'brewery_type': {"type": ["string", "null"]},
        'street': {"type": ["string", "null"]},
        'address_2': {"type": ["string", "null"]},
        'address_3': {"type": ["string", "null"]},
        'city': {"type": ["string", "null"]},
        'state': {"type": ["string", "null"]},
        'county_province': {"type": ["string", "null"]},
        'postal_code': {"type": ["string", "null"]},
        'country': {"type": ["string", "null"]},
        'longitude': {"type": ["string", "null"]},
        'latitude': {"type": ["string", "null"]},
        'phone': {"type": ["string", "null"]},
        'website_url': {"type": ["string", "null"]},
        'updated_at': {"type": ["string", "null"]},
        'created_at': {"type": ["string", "null"]}
    },
    "required": ["id"]
}


@pytest.mark.parametrize("brewery", [
    "madtree-brewing-cincinnati",
])
def test_get_single_brewery(base_url, brewery):
    r = requests.get(base_url + "/" + brewery)
    assert r.ok, "Request is not success"
    validate(instance=r.json(), schema=schema)
    assert r.json()["id"] == brewery


@pytest.mark.parametrize("brewery", [
    "111",
    12121,
])
def test_get_single_brewery_negative(base_url, brewery):
    r = requests.get(base_url + "/" + str(brewery))
    with pytest.raises(HTTPError):
        r.raise_for_status()
    assert "Couldn't find Brewery" in r.json().get("message")


@pytest.mark.parametrize("name", [
    "cooper",
    "",
    "gdfgertrthyjfgdgrteyg",
])
def test_get_breweries_by_name(base_url, name):
    r = requests.get(base_url, params={"by_name": name})
    assert r.ok, "Request is not success"
    for brewery in r.json():
        validate(instance=brewery, schema=schema)
        assert name in brewery["name"].lower()


@pytest.mark.parametrize("search_str", [
    "dog",
    "mason"
])
def test_search_breweries(base_url, search_str):
    r = requests.get(base_url + "/search", params={"query": search_str})
    assert r.ok, "Request is not success"
    for brewery in r.json():
        validate(instance=brewery, schema=schema)


@pytest.mark.parametrize("search_str", [
    "dog",
    "mason"
])
def test_autocomplete_search_breweries(base_url, search_str):
    r = requests.get(base_url + "/autocomplete", params={"query": search_str})
    assert r.ok, "Request is not success"

    schema_for_test = {
        "type": "object",
        "properties": {
            'id': {"type": "string"},
            'name': {"type": "string"}
        },
        "required": ["id", "name"]
    }

    for brewery in r.json():
        validate(instance=brewery, schema=schema_for_test)



