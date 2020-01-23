# `density-based-clustering` v 0.0.3

A package of density-based clustering methods for anomaly detection.

The respo is located [here](https://github.boozallencsn.com/wcp/density-based-clustering).

## About

The method of focus is __Density-based spatial clustering of applications with noise (DBSCAN)__ which will be applied to time series data.

DBSCAN detects clusters based on an epsilon distance measure between points and a minimum cluster size to identify points outside of clusters as _noise_. These noise points are then considered to be anomalous.

Click [here](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html) for further understanding of the `scikit-learn` DBSCAN package that is being used.

## Quickstart

```bash
pip install -r requirements.txt

python setup.py install
```

## Usage

Please see notebooks for more complete examples using the WCP data.

The following example requires time series data to use `TimeSeriesDBSCAN`:

```python
from db_clustering.ts_dbscan import TimeSeriesDBSCAN

# Instantiate TimeSeriesDBSCAN object
# obs_ts is a numpy array with the observed time series data
# obs_dates is a numpy array of the corresponding time series dates
ts_dbscan = TimeSeriesDBSCAN(obs_ts, obs_dates)

# Fit the model using determined parameters
dbscan.fit(eps=0.5, metric="euclidean", min_samples=10, n_jobs=-1)

# Identify the clusters
clusters = dbscan.detect_clusters()

# Identify the anomalous points
outlier_dates, outlier_values = dbscan.outlier_report()
```

## Test

To run tests: 

```bash
py.test -v
```

If you're on Windows

```bash
python -m pytest -v
```

## Feature Requests and Bug Reporting

Please open an issue on GitHub.
