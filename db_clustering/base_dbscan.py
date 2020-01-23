import logging

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN

import db_clustering.version_ as v

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class BaseDBSCAN(object):
    """
    Used to prepare data and run the DBSCAN method on
    """

    __version__ = v.__version__

    def __init__(self, x: np.ndarray, y: np.ndarray):
        """
        Args:
            x (np.ndarray): the independent variable
            y (np.ndarray): the dependent variable
        """
        try:
            self.obs_x = x.reshape(-1, 1)
            self.obs_y = y.reshape(-1, 1)

        except (AttributeError, Exception) as e:
            logger.error("{}:".format(type(e)), exc_info=True)
            raise

        self.x, self.y = self.__preprocess()

        self.eps = None
        self.detection_model = None
        self.c_labels = None

    def __preprocess(self):
        """
        Scales the data to be able to fit the model

        Args:
            *None*

        Returns:
            x (np.ndarray), y (np.ndarray)
        """
        x = StandardScaler().fit_transform(self.obs_x).reshape(-1, 1)
        y = self.obs_y

        return x, y

    def eps_distances(self, n_neighbors: int = 2):
        """
        Uses the distances between each point of the scaled indepenent
        variable to estimate the epsilon variable for the DBSCAN

        Args:
            n_neightbors (int): Number of neighbors to use by default for
            kneighbors queries

        Returns:
            distances (np.ndarray)
        """
        try:
            nn = NearestNeighbors(n_neighbors=n_neighbors)
            nbrs = nn.fit(self.x)
            distances, _ = nbrs.kneighbors(self.x)
            distances = distances[:, n_neighbors - 1]
            self.eps = np.max(distances)

            logger.info("Suggested EPS: {}".format(self.eps))
            logger.info("Plot distances for more information")

            return distances

        except (TypeError, Exception) as e:
            logger.error("{}:".format(type(e)), exc_info=True)
            raise

    def fit(
        self,
        eps: float = None,
        metric: str = "euclidean",
        min_samples: int = 5,
        n_jobs: int = -1,
        **kwargs,
    ):
        """
        Fitting the DBSCAN model based on the pre-determined variables

        Args:
            eps (float): The maximum distance between two samples for one to be
                considered as in the neighborhood of the other
            metric (str): The metric to use when calculating distance between
                instances in a feature array
            min_samples (int): The number of samples (or total weight) in a
                neighborhood for a point to be considered as a core point
            n_jobs (int): The number of parallel jobs to run.
                (-1 means using all processors)

        Returns:
            self
        """
        if eps is None:
            if self.eps is None:
                eps = 0.5
            else:
                eps = self.eps
        try:
            scanner = DBSCAN(
                eps=eps, metric=metric, min_samples=5, n_jobs=-1, **kwargs
            )
            self.detection_model = scanner.fit(self.x, self.y)

            return self

        except (ValueError, TypeError, Exception) as e:
            logger.error("{}:".format(type(e)), exc_info=True)
            raise

    def detect_clusters(self):
        """
        Estimates the detects the models clusters, which are  labels for each
        point in the dataset such that noisy samples are given the label -1

        Args:
            *None*

        Returns:
            clusters (list)
        """
        clusters = self.detection_model.labels_
        n_clusters_ = len(set(clusters)) - (1 if -1 in clusters else 0)
        n_noise_ = list(clusters).count(-1)
        self.c_labels = clusters

        logger.info("Estimated number of clusters: %d" % n_clusters_)
        logger.info("Estimated number of noise points: %d" % n_noise_)

        return clusters

    def outlier_report(self):
        """
        Reports the x and y values of the noise points (outliers)

        Args:
            *None*

        Returns:
            outlier_x_values (np.ndarray), outlier_y_values (np.ndarray)
        """
        cluster_i = np.where(self.c_labels == -1)
        outlier_x_values = self.obs_x[cluster_i]
        outlier_y_values = self.obs_y[cluster_i]

        return outlier_x_values, outlier_y_values
