# October 2026: Three Datasets, One Record

How far ahead of the old record three global temperature datasets put October 2026, and how that margin compares with other monthly records and with what a trend and El Niño would predict. The analysis is in [`notebooks/analysis.ipynb`](notebooks/analysis.ipynb).

## The problem

Copernicus reports October 2026 as the warmest October on record, with a strong El Niño under way. I wanted to know whether the datasets that measure global temperature agree on how far ahead of the old record it is, and whether that margin is unusual.

## What I did

I took the October values from NASA's GISTEMP, NOAA's global series and ERA5, rebased each to its own 1991 to 2020 average, and compared the record year and the margin over the previous best. I then measured the margin of every monthly record since 1950 in NASA's and ERA5's data to see where October 2026 sits, and fitted each dataset's Octobers from 1979 to 2025 on the year and the Oceanic Niño Index to see what the fit predicts for 2026. The notebook ends by recomputing the main figures with plain Python and stops if any of them differ.

## What it found

- October 2026 is the warmest October in all three datasets.
- The lead over the old record is 0.21°C in NASA's data, 0.08°C in NOAA's and 0.05°C in ERA5.
- Among monthly records since 1950, the NASA margin ranks 16th of 133 and the ERA5 margin 89th of 152.
- A fit on the year and the Oceanic Niño Index predicts 1.31°C for NASA, 1.30°C for NOAA and 0.76°C for ERA5, and October came in 0.24, 0.13 and 0.14°C above that. With the Relative Oceanic Niño Index the gaps are 0.30, 0.19 and 0.21°C.

## Data

| Layer | Source | Notes |
|---|---|---|
| Monthly global mean, 1880 to 2026 | NASA GISTEMP v4, land and ocean | Relative to 1951 to 1980 |
| October global mean, 1850 to 2026 | NOAA Climate at a Glance, global land and ocean | October only, relative to 1901 to 2000 |
| Daily global mean, 1940 to 2026 | ERA5, from the C3S Climate Pulse series at ECMWF | Daily anomalies against 1991 to 2020 |
| Oceanic Niño Index | NOAA Climate Prediction Center, ERSST version 5 | Three-month seasons since 1950 |
| Relative Oceanic Niño Index | NOAA Climate Prediction Center | The index CPC now uses for official ENSO monitoring |

`scripts/download_data.py` downloads all five into `data/raw`. No API keys are needed.

## Method

- **Monthly values.** ERA5 months are the mean of their daily anomalies, and only complete months are used.
- **Rebasing.** Each October series is shown relative to its own 1991 to 2020 average, which can't change a margin.
- **Margin.** The October 2026 value minus the best earlier October in the same dataset.
- **Record months.** Any month since 1950 that beat every earlier value for its calendar month, with the margin over the previous best.
- **El Niño fit.** Least squares on the year and the Oceanic Niño Index for August to October, fitted on 1979 to 2025 and applied to 2026. Fits with the June to August index and with the Relative index are in the notebook.

## Limitations

- The three groups build their global averages differently, and this notebook doesn't explain why the margins differ.
- HadCRUT5 ends in July 2026 and Berkeley Earth's file ends in 2024, so neither is used.
- NOAA's file holds October only, so the record-margin comparison uses two datasets.
- The El Niño fit is linear, uses 47 Octobers and one choice of season, and the two El Niño indices disagree on how strong this event is.
- One October says little about the long-term rate of warming.

## Run it

```
pip install -r requirements.txt
python3 scripts/download_data.py   # optional: the data in data/raw is from November 23, 2026
jupyter lab notebooks/analysis.ipynb
```

The notebook writes the files in `data/processed/` and the two charts in `charts/`.
