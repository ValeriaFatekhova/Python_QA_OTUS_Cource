import requests
import pytest
from requests import HTTPError
import random

LIST_ALL_BREEDS = "/breeds/list/all"
SINGLE_RANDOM_IMAGE = "/breeds/image/random"
MULTIPLE_RANDOM_IMAGES = "/breeds/image/random/"


def test_list_all_breeds(base_url):
    r = requests.get(base_url + LIST_ALL_BREEDS)
    assert r.ok, "Request is not success"
    assert r.json().get("status") == "success", "Status field in JSON is not success"
    assert isinstance(r.json().get("message"), dict), "List of breeds is not presented in JSON"


def test_single_random_image(base_url):
    r = requests.get(base_url + SINGLE_RANDOM_IMAGE)
    assert r.ok, "Request is not success"
    assert r.json().get("status") == "success", "Status field in JSON is not success"
    assert r.json().get("message").split(".")[-1].lower() in ["jpg", "png", "jpeg", "gif"], "There is no image in JSON"


@pytest.mark.parametrize("breed", [
    "hound",
    "akita",
])
def test_single_random_image_positive(base_url, breed):
    r = requests.get(base_url + "/breed/" + str(breed) + "/images/random")
    assert r.ok, "Request is not success"
    assert r.json().get("status") == "success", "Status field in JSON is not success"
    assert r.json().get("message").split(".")[-1].lower() in ["jpg", "png", "jpeg", "gif"], "There is no image in JSON"


@pytest.mark.parametrize("breed", [
    "23234",
    "akita2",
])
def test_single_random_image_negative(base_url, breed):
    r = requests.get(base_url + "/breed/" + str(breed) + "/images/random")
    with pytest.raises(HTTPError):
        r.raise_for_status()
    assert r.json().get("status") == "error", "Status field in JSON is not error"
    assert "Breed not found (master breed does not exist)" in r.json().get("message"), "Incorrect error message in JSON"


@pytest.mark.parametrize("link", [
    SINGLE_RANDOM_IMAGE + "111",
    SINGLE_RANDOM_IMAGE.rsplit('/', 1)[0],
])
def test_incorrect_link(base_url, link):
    r = requests.get(base_url + str(link))
    with pytest.raises(HTTPError):
        r.raise_for_status()
    assert r.json().get("status") == "error", "Status field in JSON is not error"
    assert "No route found for" in r.json().get("message"), "Incorrect error message in JSON"


@pytest.mark.parametrize("image_num", [-1, 0, 10, 50, 60])
def test_multiple_random_images(base_url, image_num):
    r = requests.get(base_url + MULTIPLE_RANDOM_IMAGES + str(image_num))
    assert r.ok, "Request is not success"
    assert r.json().get("status") == "success", "Status field in JSON is not success"
    assert isinstance(r.json().get("message"), list), "List of breeds is not presented in JSON"
    num = random.randint(0, len(r.json().get("message"))-1)
    assert r.json().get("message")[num].split(".")[-1].lower() in ["jpg", "png", "jpeg", "gif"]


