import logging
from typing import Optional, List
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator
from pandas.plotting import register_matplotlib_converters
from db_clustering.base_dbscan import BaseDBSCAN

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def plot_noise(
    dbscan_obj: BaseDBSCAN,
    title: Optional[str] = None,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None,
):
    """
    Plots the data and circles the points that are determined as outliers or
    anomalies
    Args:
        dbscan_obj: A fitted dbscan object
        x_label: a label for the x axis
        y_label: a label for the y axis
    Returns:
        fig, ax
    """
    outlier_x, outlier_y = dbscan_obj.outlier_report()
    fig, ax = _plot_params(title, x_label, y_label)
    plt.scatter(dbscan_obj.obs_x, dbscan_obj.obs_y, color="b", marker="x")
    plt.scatter(outlier_x, outlier_y, s=200, facecolors="none", edgecolors="r")
    plt.legend(["Observed", "Detected Noise"])
    return fig, ax


def plot_clusters(
    dbscan_obj: BaseDBSCAN,
    title: Optional[str] = None,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None,
    colors: Optional[List[str]] = None,
):
    """
    Plots the data and circles the different clusters and noise points
    Args:
        dbscan_obj: A fitted dbscan object
        x_label: a label for the x axis
        y_label: a label for the y axis
        colors: a list of strings representing colors to represent each cluster
    Returns:
        fig, ax
    """
    clusters = dbscan_obj.detect_clusters()
    outlier_x, outlier_y = dbscan_obj.outlier_report()
    n_clusters_ = len(set(clusters)) - (1 if -1 in clusters else 0)
    fig, ax = _plot_params(title, x_label, y_label)
    plt.scatter(dbscan_obj.obs_x, dbscan_obj.obs_y, color="k", marker="x")
    if colors is None:
        colors = ["b", "g", "orange", "purple", "gold"]
    for i in range(n_clusters_):
        ilocs = np.where(clusters == i)
        cluster_i_x = dbscan_obj.obs_x[ilocs]
        cluster_i_y = dbscan_obj.obs_y[ilocs]
        plt.scatter(
            cluster_i_x,
            cluster_i_y,
            s=200,
            facecolors="none",
            edgecolors=colors[i],
        )
    plt.scatter(outlier_x, outlier_y, s=200, facecolors="none", edgecolors="r")
    labels = ["Cluster {}".format(str(i + 1)) for i in range(n_clusters_)]
    labels = ["Observed"] + labels + ["Detected Noise"]
    plt.legend(labels)
    return fig, ax


def _plot_params(title: str, x_label: str, y_label: str):
    """
    Establishes parameters for the plots to all be consistent
    Args:
        title: a title for the plot
        x_label: a label for the x axis
        y_label: a label for the y axis
    Returns:
        fig, ax
    """
    sns.set_style("white")
    register_matplotlib_converters()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.tick_params(bottom=True, left=True, labelleft=True, labelbottom=True)
    if x_label is not None:
        plt.xlabel(x_label, fontsize=15, color="k")
    if y_label is not None:
        plt.ylabel(y_label, fontsize=15, color="k")
    if title is not None:
        plt.title(title, fontsize=20, color="k")
    return fig, ax
