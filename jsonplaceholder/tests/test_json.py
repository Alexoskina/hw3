import pytest
import requests


def test_len(baseurl):
    responce = requests.get(baseurl).json()
    assert len(responce) == 100


def test_status(baseurl):
    resp = requests.get(baseurl)
    assert resp.status_code == 200


@pytest.mark.parametrize('id', [100, 10, 1])
def test_filter_by_id(baseurl, id):
    resp = requests.get(baseurl, params={'id': id})
    for x in range(len(resp.json())):
        assert resp.json()[x]['id'] == id


def test_new_post(baseurl):
    json_new_post = {
        "title": "test",
        "body": "It is just a test",
        "userId": 666
    }
    resp = requests.post(baseurl, json=json_new_post).json()
    assert resp["userId"] == json_new_post["userId"]
    assert resp["title"] == json_new_post["title"]
    assert resp["body"] == json_new_post["body"]


@pytest.mark.parametrize('title', ['t1', 't2', 't3'])
@pytest.mark.parametrize('body', ['b1', 'b2', 'b3'])
@pytest.mark.parametrize('userid', [9, 10, 11])
def test_post(baseurl, title, body, userid):
    res = requests.post(baseurl, json={'title': title, 'body': body, 'userId': userid})
    res_json = res.json()
    assert res_json