from pathlib import Path
import pytest
import json


@pytest.fixture(scope="session")
def baseurl():
    return "https://jsonplaceholder.typicode.com/posts"


@pytest.fixture(scope="session")
def post():
    with Path(__file__).parent.parent.joinpath("main", "posts.json").open("r") as f:
        return json.load(f)

