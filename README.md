# Sleep and Mental Health Analysis

## Project Overview

This project explores the relationship between sleep duration and mental health using data from the CDC Behavioral Risk Factor Surveillance System (BRFSS).

The analysis focuses on reported hours of sleep and the number of poor mental health days reported during the past 30 days. I also explored whether the relationship between sleep and mental health differed across age groups.

The analysis found that respondents reporting 7–8 hours of sleep had fewer average poor mental health days than respondents reporting shorter or longer sleep durations.

## Dataset

The data comes from the CDC's 2025 Behavioral Risk Factor Surveillance System (BRFSS).

Source: Centers for Disease Control and Prevention (CDC), Behavioral Risk Factor Surveillance System.

The original BRFSS dataset is too large to include directly in this repository. It can be downloaded from the CDC BRFSS Annual Survey Data website.

A cleaned dataset used for the analysis is included in the `data/cleaned` folder.

## Project Structure

- `scripts/` - Python scripts used for data cleaning, preprocessing, EDA, and feature engineering
- `notebooks/` - Jupyter notebook used to explore and visualize the data
- `data/cleaned/` - Cleaned dataset used for analysis
- `requirements.txt` - Python packages needed to run the project

## How to Reproduce the Analysis

1. Download the 2025 BRFSS dataset from the CDC.
2. Place the raw `.XPT` file in `data/raw/`.
3. Install the required Python packages:

    pip install -r requirements.txt

4. Run the data cleaning script:

    python3 scripts/clean_data.py

5. Run the EDA/analysis script or notebook to reproduce the analysis and visualizations.

## Main Analysis

The analysis included:

- Cleaning and preprocessing the BRFSS data
- Exploring the distribution of reported sleep duration
- Exploring reported poor mental health days
- Comparing mental health across sleep durations
- Creating short, recommended, and long sleep categories through feature engineering
- Comparing sleep and mental health patterns across age groups

## Key Finding

Respondents reporting 7–8 hours of sleep had the lowest average number of poor mental health days across the sleep categories examined. This pattern was also observed across the age groups analyzed.

This analysis shows an association between sleep and mental health and does not establish causation.