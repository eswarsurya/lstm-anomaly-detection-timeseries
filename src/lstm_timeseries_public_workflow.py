"""Public workflow outline for LSTM time-series anomaly detection.

This script keeps the GitHub version readable and safe to review. The original
notebook includes experimentation; this version shows the reusable steps behind
the project: load the series, create sequence windows, and produce anomaly
review candidates using a rolling baseline that supports model validation.
"""

from __future__ import annotations

import pandas as pd

DATA_PATH = "../data/public_sample_nyc_taxi_timeseries.csv"


def load_timeseries(path: str = DATA_PATH) -> pd.DataFrame:
    """Load timestamp/value data and keep observations in time order."""
    data = pd.read_csv(path, parse_dates=["timestamp"])
    return data.sort_values("timestamp").reset_index(drop=True)


def create_sequences(values, window_size: int = 48):
    """Create fixed-length windows for sequence modelling."""
    return [values[start : start + window_size] for start in range(len(values) - window_size)]


def build_review_candidates(data: pd.DataFrame, window: int = 48, top_n: int = 10) -> pd.DataFrame:
    """Rank observations that differ most from the recent rolling pattern."""
    reviewed = data.copy()
    reviewed["rolling_mean_48"] = reviewed["value"].rolling(window, min_periods=12).mean()
    reviewed["rolling_std_48"] = reviewed["value"].rolling(window, min_periods=12).std()
    reviewed["deviation_score"] = (
        (reviewed["value"] - reviewed["rolling_mean_48"]) / reviewed["rolling_std_48"]
    ).abs()
    return reviewed.dropna().sort_values("deviation_score", ascending=False).head(top_n)


if __name__ == "__main__":
    series = load_timeseries()
    sequences = create_sequences(series["value"].to_numpy())
    candidates = build_review_candidates(series)

    print("Records reviewed:", len(series))
    print("Sequence windows created:", len(sequences))
    print("Top review candidates:")
    print(candidates[["timestamp", "value", "rolling_mean_48", "deviation_score"]])
