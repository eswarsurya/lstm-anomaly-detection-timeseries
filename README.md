# LSTM Anomaly Detection Timeseries

**Status: Completed machine-learning project**

Time-series anomaly detection project using LSTM modelling concepts and sequence-based analysis. The project demonstrates how time-dependent behaviour can be prepared, reviewed, and used to surface unusual periods for analyst investigation.

## Analytics Question

Can a time-series workflow learn normal behaviour and identify unusual periods that deserve further investigation?

## Dataset Context

The working sample contains **10,320 half-hourly records** from **July 2014 to January 2015**, with `timestamp` and `value` fields.

## Tools Used

Python, Pandas, NumPy, TensorFlow / Keras concepts, Jupyter, rolling-window analysis, and visual output review.

## What I Implemented

- Prepared timestamped data for sequence modelling.
- Created sequence windows for LSTM-style input.
- Reviewed rolling behaviour and deviation from recent baselines.
- Produced public output tables for dataset profile, daily activity, and anomaly review candidates.
- Added a reusable Python workflow and clean public notebook.
- Kept the public repository free of unnecessary personal or sensitive data.

## Key Outputs

- 10,320 time-series records reviewed.
- Daily activity summaries for trend analysis.
- Ranked anomaly review candidates based on deviation from recent rolling behaviour.
- Reusable source code and a public notebook walkthrough.

The anomaly candidates are presented as an analyst review layer rather than an unsupported claim of production alerting.

## Repository Guide

```
data/
notebooks/
outputs/
src/
reports/
assets/
```

## How To Review

Start with `outputs/model_output_summary.md`, then inspect `notebooks/lstm_timeseries_public_workflow.ipynb`, `outputs/top_anomaly_review_candidates.csv`, and `src/lstm_timeseries_public_workflow.py`.

## Author

**Eswar Surya Danaboina** · MSc Data Analytics · Dublin, Ireland

Portfolio: https://eswardanaboina.vercel.app/  
LinkedIn: https://www.linkedin.com/in/eswarsurya76/
