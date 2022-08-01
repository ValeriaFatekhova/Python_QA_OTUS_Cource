import pytest
import requests
from jsonschema import validate


POST_COMMENTS = "/comments"

schema = {
    "type": "object",
    "properties": {
        "userId": {"type": ["number", "string"]},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["id", "userId"]
}


def test_listening_all_resources(base_url):
    r = requests.get(base_url)
    assert r.ok, "Request is not success"
    for item in r.json():
        validate(instance=item, schema=schema)


@pytest.mark.parametrize("title", [
    "rrr",
    "",
])
@pytest.mark.parametrize("body", [
    "ttt",
    "",
])
@pytest.mark.parametrize("user_id", [
    1,
    -7,
])
def test_create_resource(base_url, title, body, user_id):
    data = {'title': title, 'body': body, 'userId': user_id}
    r = requests.post(base_url, data)
    assert r.ok, "Request is not success"
    validate(instance=r.json(), schema=schema)
    assert r.json().get('title') == title
    assert r.json().get('body') == body
    assert int(r.json().get('userId')) == user_id


@pytest.mark.parametrize("post", [
    1,
    100,
])
def test_delete_resource(base_url, post):
    r = requests.delete(base_url + "/" + str(post))
    assert r.ok, "Request is not success"
    print(r.json())


@pytest.mark.parametrize("post", [
    1,
    100,
    "aaa",
])
def test_post_comments(base_url, post):
    r = requests.get(base_url + "/" + str(post) + POST_COMMENTS)
    assert r.ok, "Request is not success"

    schema_for_test = {
        "type": "object",
        "properties": {
            "postId": {"type": "number"},
            "id": {"type": "number"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["postId", "id", "name", "body"]
    }

    for item in r.json():
        validate(instance=item, schema=schema_for_test)
        assert item.get("postId") == post


@pytest.mark.parametrize("user_id", [
    1,
    100,
    "aaa",
])
def test_posts_by_user(base_url, user_id):
    r = requests.get(base_url, params={"userId": user_id})
    assert r.ok, "Request is not success"
    for item in r.json():
        validate(instance=item, schema=schema)
        assert item.get("userId") == user_id
