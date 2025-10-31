#  Nobel Prize Data Analysis

A small Python project that fetches, cleans, and analyzes Nobel Prize data from the official Nobel Prize API (https://api.nobelprize.org/).
The goal is to provide reproducible, inspectable insights about prize counts, laureate counts, and category distributions through a combination of tabular summaries and simple visualizations.

## Motivation
Public historical data about Nobel Prizes holds value for exploratory data analysis, curriculum examples, and small reproducible research projects. The official Nobel Prize API exposes structured records for prizes, laureates, years, and categories; this project demonstrates how to fetch that data, transform it into analysis-ready tables, compute summary statistics, and visualize trends over time.

##  Features
- Fetches live data from the Nobel Prize API
- Normalizes and flattens prize and laureate records into pandas DataFrames.
- Computes summary statistics:
  - prizes per year
  - total awardee per year
  - awardee per category
  - Generates a yearly prize/ laureate distribution bar chart (Matplotlib).
  - CLI options to filter by year range and category; optional CSV export.
- Design overview
 - Data acquisition: call API endpoints and collect JSON payloads.
 - Data normalization: convert nested JSON (prizes → laureates) into row-oriented tables.
 - Analysis: derive time-series and category aggregates.
 - Visualization: produce a time-series bar chart (prizes per year) and optional stacked chart (categories).
 - Output: print summary tables and optionally save CSV / PNG.  

##  How to Run

```bash
pip install -r requirements.txt
python main.py
