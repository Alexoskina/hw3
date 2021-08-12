import pytest
import requests


def test_status(baseurl):
    resp = requests.get(baseurl)
    assert resp.status_code == 200


def test_breweries_json(baseurl):
    resp = requests.get(f"{baseurl}/breweries", verify=False)
    body = resp.json()
    assert type(body) is list


@pytest.mark.parametrize("city", ["Moscow", "Saint-P"])
def test_api_city(baseurl, city):
    resp = requests.get(f"{baseurl}/breweries", verify=False, params={"by_city": city})
    for x in range(len(resp.json())):
        assert resp.json()[x]["city"] == city


@pytest.mark.parametrize("page", range(3))
def test_pages(baseurl, page):
    resp = requests.get(f"{baseurl}/breweries", verify=False, params={"page": page})
    res = resp.json()
    assert res


@pytest.mark.parametrize("state", ["Texas", "Colorado", "Florida"])
def test_states(baseurl, state):
    resp = requests.get(f"{baseurl}/breweries", verify=False, params={"by_state": state})
    res = resp.json()
    assert res
