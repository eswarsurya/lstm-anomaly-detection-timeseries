# LSTM Anomaly Detection Timeseries

Time-series anomaly detection project using LSTM modelling concepts and sequence-based analysis. The project explores how repeated behaviour over time can be learned, reviewed, and used to highlight unusual periods for further investigation.

## Why I Built This

Many analytics problems are sequential: transport demand, system traffic, transactions, sensor readings, and service usage all change hour by hour. Standard row-based analysis can miss the importance of order, seasonality, and recent behaviour.

I built this project to show that I can work with time-dependent data, prepare it for machine learning, and explain anomaly detection in a way that is useful for monitoring and operational review.

## Analytics Question

Can a time-series workflow learn normal behaviour and identify unusual periods that should be reviewed by an analyst?

## Dataset Context

The public project uses an NYC taxi time-series sample with two fields:

- `timestamp`: observation time
- `value`: activity level for that time interval

The full working sample contains 10,320 half-hourly records from July 2014 to January 2015. A smaller public sample is included so the repository can be reviewed quickly without large raw files.

## Tools Used

- Python
- Pandas and NumPy
- TensorFlow / Keras concepts for LSTM modelling
- Rolling-window time-series review
- Jupyter Notebook workflow
- Matplotlib-style output review

## What I Implemented

- Prepared timestamped data for time-series modelling.
- Created sequence windows for LSTM-style input.
- Reviewed rolling behaviour to identify unusual points for model validation.
- Exported public output tables showing dataset profile, daily volume, and anomaly review candidates.
- Added a clean public script and public notebook that document the reusable workflow without notebook clutter.
- Kept the repository public-safe by avoiding personal data and unnecessary raw files.

## Repository Guide

```text
data/
  README.md
  public_sample_nyc_taxi_timeseries.csv

notebooks/
  lstm_timeseries_public_workflow.ipynb

outputs/
  README.md
  dataset_profile.csv
  daily_volume_sample.csv
  top_anomaly_review_candidates.csv
  model_output_summary.md

src/
  lstm_timeseries_public_workflow.py

reports/
  report_summary.md

assets/
  daily_volume_sample.svg
  anomaly_review_candidates.svg
```

## Outputs And Results

The current public evidence shows:

- 10,320 time-series records reviewed in the working sample.
- Time range from 2014-07-01 to 2015-01-31.
- Daily volume summaries for trend review.
- Top anomaly review candidates ranked by deviation from recent rolling behaviour.
- A reusable script and public notebook showing the sequence-preparation and review process.

The anomaly candidate output is used as a transparent review layer. It supports the LSTM project by showing where unusual periods appear and where model output should be checked carefully.

## How To Review This Project

Start with the README for the project purpose. Then review:

1. `data/README.md` for dataset context.
2. `notebooks/lstm_timeseries_public_workflow.ipynb` for the clean notebook walkthrough.
3. `outputs/dataset_profile.csv` for scope.
4. `outputs/top_anomaly_review_candidates.csv` for unusual periods.
5. `src/lstm_timeseries_public_workflow.py` for the reusable script.
6. `reports/report_summary.md` for a short project explanation.

## Current Limitations And Next Improvements

The public repository focuses on safe evidence and clean explanation. A future version can add clearer model evaluation plots, threshold comparison, and a short dashboard-style visual summary.

## Recruiter Notes

This project demonstrates time-series thinking, sequence modelling exposure, anomaly detection workflow design, and the ability to explain machine learning work in a practical review format.
