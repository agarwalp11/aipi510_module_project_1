import pandas as pd
import numpy as np


# Load the raw BRFSS dataset
raw_data_path = "data/raw/LLCP2025.XPT"
df = pd.read_sas(raw_data_path, format="xport")


# Select variables used for the analysis
columns = [
    "SLEPTIM1",
    "MENTHLTH",
    "_AGE_G",
    "SEXVAR",
    "GENHLTH"
]

sleep_df = df[columns].copy()

# Clean special BRFSS response codes

# 77 = Don't know/Not sure, 99 = Refused
sleep_df["SLEPTIM1"] = sleep_df["SLEPTIM1"].replace({
    77: np.nan,
    99: np.nan
})

# 77 = Don't know/Not sure, 88 = None, 99 = Refused
sleep_df["MENTHLTH"] = sleep_df["MENTHLTH"].replace({
    77: np.nan,
    88: 0,
    99: np.nan
})

# 7 = Don't know/Not sure, 9 = Refused
sleep_df["GENHLTH"] = sleep_df["GENHLTH"].replace({
    7: np.nan,
    9: np.nan
})

# Keep respondents with valid sleep and mental health responses
analysis_df = sleep_df.dropna(
    subset=["SLEPTIM1", "MENTHLTH"]
).copy()


# Rename columns for readability
analysis_df = analysis_df.rename(columns={
    "SLEPTIM1": "sleep_hours",
    "MENTHLTH": "poor_mental_health_days",
    "_AGE_G": "age_group",
    "SEXVAR": "sex",
    "GENHLTH": "general_health"
})


# Save the cleaned dataset
output_path = "data/cleaned/brfss_sleep_mental_health_cleaned.csv"
analysis_df.to_csv(output_path, index=False)

print(f"Cleaned dataset saved to: {output_path}")
print(f"Rows in cleaned dataset: {len(analysis_df)}")