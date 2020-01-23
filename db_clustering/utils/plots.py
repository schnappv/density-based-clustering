import logging

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator
from pandas.plotting import register_matplotlib_converters

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


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
