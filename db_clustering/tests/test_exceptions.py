import logging

import pytest
from db_clustering.base_dbscan import BaseDBSCAN

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def test_init_exception_list(x, y):
    x, y = list(x), list(y)
    with pytest.raises(AttributeError):
        BaseDBSCAN(x, y)


def test_eps_distance_exception(x, y, float_neighbors):
    dbscan_obj = BaseDBSCAN(x, y)
    with pytest.raises(TypeError):
        dbscan_obj.eps_distances(float_neighbors)
