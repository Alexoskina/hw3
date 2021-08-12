import pytest
import requests



def test_accessibility(baseurl):
    resp = requests.get(f"{baseurl}/breeds/list/all")
    assert resp.status_code == 200


def test_get_random_photo(baseurl):
    random_photo1 = requests.get(f"{baseurl}/breeds/image/random").json()
    random_photo2 = requests.get(f"{baseurl}/breeds/image/random").json()
    assert random_photo2["message"] != random_photo1["message"]


def test_breed_list_json(baseurl):
    resp = requests.get(f"{baseurl}/breeds/list/all", verify=False)
    body = resp.json()
    assert type(body) is dict
    assert "message" in body


@pytest.mark.parametrize("breed", ["corgi", "collie", "husky"])
def test_breed_in_breeds(baseurl, breed):
    resp = requests.get(f"{baseurl}/api/breed//images").json()
    assert len(resp["message"]) > 0


@pytest.mark.parametrize("setter", ["english", "gordon", "irish"])
def test_subbreads(baseurl, setter):
    resp = requests.get(f"{baseurl}/breed/setter/list", verify=False)  # получаем список подпород, задаем переменную
    subbreeds = resp.json().get('message', {})
    assert setter in subbreeds
