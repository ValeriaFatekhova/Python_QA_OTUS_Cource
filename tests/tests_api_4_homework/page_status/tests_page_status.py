import requests


def test_url_status_code(url, status_code):
    r = requests.get(url)
    assert r.status_code == int(status_code), f"Incorrect status code for {url}"
