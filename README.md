# Chennai Metro Station Activity Analysis

## Project Overview

This project performs exploratory data analysis on Chennai Metro
station activity data using Python, Pandas and NumPy.

The analysis focuses on passenger activity, waiting times,
complaints, delays, parking availability and station-level
operational indicators.

## Objectives

- Identify stations in specific zones
- Find stations with high daily passenger entries
- Analyze peak-hour load
- Identify stations with high complaints
- Analyze parking availability
- Calculate weekly delays
- Handle missing values
- Compare station performance across zones
- Rank stations based on daily entries
- Identify stations requiring operational attention

## Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook

## Dataset

The dataset contains information about Chennai Metro stations,
including:

- Station name
- Zone
- Daily entries
- Daily exits
- Peak-hour load percentage
- Average waiting time
- Monthly complaints
- Parking availability
- Weekday delays
- Weekend delays

## Analysis Performed

### 1. Data Filtering

Filtered stations based on:

- Zone
- Daily entries
- Peak-hour load
- Monthly complaints
- Parking availability

### 2. Data Cleaning

Handled missing values using:

- Mean imputation for average waiting time
- Median imputation for monthly complaints

### 3. Grouped Analysis

Calculated zone-level:

- Average waiting time
- Maximum daily entries
- Number of stations
- Average entries
- Average exits
- Total complaints

### 4. NumPy Analysis

Converted Pandas columns into NumPy arrays to calculate:

- Entry-exit differences
- Maximum entry-exit difference
- Total entries
- Total exits
- Overall entry-exit ratio

### 5. Station Ranking

Stations were ranked according to daily passenger entries.

### 6. Problem Stations

Identified stations with:

- More than 20 monthly complaints
- Average waiting time greater than 3 minutes

### 7. Operational Attention Score

Created an experimental attention score using station rankings
based on:

- Daily entries
- Monthly complaints
- Average waiting time

The score is used as an exploratory indicator to identify stations
that may deserve further investigation.

## Key Skills Demonstrated

- Data loading
- Data filtering
- Boolean indexing
- Missing-value handling
- `groupby()`
- Aggregation
- Sorting
- Ranking
- NumPy arrays
- Basic exploratory data analysis
- Feature creation

## Project Structure

```text
chennai-metro-station-analysis/
│
├── README.md
├── data/
│   └── challenge_dataset_chennai_metro_station_activity.csv
│
├── notebooks/
│   └── metro_station_analysis.ipynb
│
├── src/
│   └── metro_analysis.py
│
├── results/
│   └── analysis_summary.md
│
├── requirements.txt
└── .gitignore