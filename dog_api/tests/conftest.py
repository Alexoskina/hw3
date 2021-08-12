from pathlib import Path
import pytest
import json


@pytest.fixture(scope="session")
def baseurl():
    return "https://dog.ceo/api"


@pytest.fixture(scope="session")
def dogsbreeds():
    with Path(__file__).parent.parent.joinpath("main", "sub_breeds.json").open("r") as f:
        return json.load(f)
