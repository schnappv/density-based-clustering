import logging

import numpy as np
from sklearn.preprocessing import StandardScaler

import db_clustering.version_ as v
from db_clustering.base_dbscan import BaseDBSCAN

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class TimeSeriesDBSCAN(BaseDBSCAN):
    """
    A DBSCAN class meant for time series data
    """

    __version__ = v.__version__

    def __init__(self, observed_ts: np.ndarray, observed_dates: np.ndarray):
        """
        Args:
            observed_ts (np.ndarray): an observed time series
            observed_dates (np.ndarray): dates that correspond the time series
        """
        try:
            self.obs_x = observed_dates.reshape(-1, 1)
            self.obs_y = observed_ts.reshape(-1, 1)

        except (AttributeError, Exception) as e:
            logger.error("{}:".format(type(e)), exc_info=True)
            raise

        self.x, self.y = self.__preprocess_ts()

        self.detection_model = None
        self.c_labels = None

    def __preprocess_ts(self):
        """
        Sets up the data and scales it to fit the model. Switches axis for the
        DBSCAN that will be switched back at the end

        Args:
            *None*

        Returns:
            x (np.ndarray), y (np.ndarray)
        """
        dates_i = np.arange(len(self.obs_x))

        x = StandardScaler().fit_transform(self.obs_y).reshape(-1, 1)
        y = dates_i.reshape(-1, 1)

        return x, y
