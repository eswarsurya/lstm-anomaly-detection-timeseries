# Model Output Summary

This file summarises the public-facing output for the LSTM anomaly detection timeseries project.

## Project Output

The project reviews an NYC taxi time-series sample and identifies unusual periods that should be checked during anomaly detection review. The public output focuses on transparent evidence: dataset profile, daily activity summaries, and top anomaly review candidates.

## Dataset Profile

- Records reviewed in working sample: 10,320
- Fields used: `timestamp`, `value`
- Time range: 2014-07-01 to 2015-01-31
- Minimum observed value: 8
- Maximum observed value: 39,197
- Mean observed value: 15,137.57

## Review Candidate Output

`top_anomaly_review_candidates.csv` lists the strongest unusual periods based on deviation from recent rolling behaviour. This supports the modelling workflow by showing which points deserve analyst attention and model validation.

This is intentionally presented as a review layer, not as a final production alerting system. It keeps the project honest and makes the result easier to understand.

## Analysis Focus

The workflow focuses on:

- Time-series ordering and cleaning
- Sequence window creation for LSTM-style modelling
- Rolling baseline comparison
- Deviation-based anomaly candidate review
- Public-safe output documentation

## Business Value

This type of workflow can support monitoring use cases such as demand forecasting, transport activity, website traffic, operations data, and sensor-based review. It shows how unusual behaviour can be surfaced for investigation instead of being buried inside raw time-series data.

## Public Sharing Note

The repository includes a smaller public sample and aggregated outputs. Large experimental notebooks and raw working files can be added later after cleaning and file-size checks.
