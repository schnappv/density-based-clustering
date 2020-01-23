import logging
import json
import os

import numpy as np

import pytest

log_fmt = "[%(asctime)s %(levelname)-8s] [%(filename)s:%(lineno)s - %(funcName)s()] %(message)s"  # noqa
logging.basicConfig(level=logging.DEBUG, format=log_fmt)

logger = logging.getLogger(__name__)


here = dir_path = os.path.dirname(os.path.realpath(__file__))
test_data_dir = os.path.join(here, "test_data")


def load_json(f_name):
    with open(os.path.join(test_data_dir, f_name)) as f:
        data = json.load(f)
        return np.array(data)


@pytest.fixture(scope="session")
def x():
    return np.array(load_json("test_x.json"))


@pytest.fixture(scope="session")
def y():
    return np.array(load_json("test_y.json"))


@pytest.fixture(scope="session")
def float_neighbors():
    return 2.5


@pytest.fixture(scope="session")
def foo():
    return "foo"
