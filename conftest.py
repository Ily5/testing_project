import pytest
import json
import os
from fixture.api_helper import ApiHelper

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def api(request):
    with open(request.config.getoption("--config")) as cfg:
        config = json.load(cfg)
        fixture = ApiHelper(
            url=config["base_url"],
            payload=config["base_payload"],
            headers=config["base_headers"]
        )
        yield fixture
        for i in os.listdir(ROOT_DIR + f"/model/data/"):
            if ".yaml" in i:
                os.remove(ROOT_DIR + "/model/data/" + i)
        fixture.reset()


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default=ROOT_DIR + "/config.json")
