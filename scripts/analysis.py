import pandas as pd
import matplotlib.pyplot as plt


# Load the cleaned dataset
analysis_df = pd.read_csv(
    "data/cleaned/brfss_sleep_mental_health_cleaned.csv"
)


# --------------------------------------------------
# 1. Explore sleep duration
# --------------------------------------------------

# View summary statistics for reported sleep hours
print("\nSleep Duration Summary:")
print(analysis_df["sleep_hours"].describe())

# Count respondents by reported hours of sleep
sleep_counts = analysis_df["sleep_hours"].value_counts().sort_index()

# Visualize the distribution of sleep duration
plt.figure(figsize=(10, 5))
plt.bar(sleep_counts.index, sleep_counts.values)

plt.xlabel("Hours of Sleep")
plt.ylabel("Number of Respondents")
plt.title("Distribution of Reported Sleep Duration")

plt.show()


# --------------------------------------------------
# 2. Explore poor mental health days
# --------------------------------------------------

# View summary statistics for poor mental health days
print("\nPoor Mental Health Days Summary:")
print(analysis_df["poor_mental_health_days"].describe())

# Count respondents by number of poor mental health days
mental_health_counts = (
    analysis_df["poor_mental_health_days"]
    .value_counts()
    .sort_index()
)

# Visualize the distribution of poor mental health days
plt.figure(figsize=(10, 5))
plt.bar(mental_health_counts.index, mental_health_counts.values)

plt.xlabel("Poor Mental Health Days")
plt.ylabel("Number of Respondents")
plt.title("Distribution of Poor Mental Health Days")

plt.show()


# --------------------------------------------------
# 3. Compare sleep duration with mental health
# --------------------------------------------------

# Calculate average poor mental health days for each sleep duration
sleep_mental_health = (
    analysis_df
    .groupby("sleep_hours")["poor_mental_health_days"]
    .mean()
    .reset_index()
)

print("\nMental Health by Sleep Duration:")
print(sleep_mental_health.round(2))

# Visualize the relationship
plt.figure(figsize=(10, 5))

plt.plot(
    sleep_mental_health["sleep_hours"],
    sleep_mental_health["poor_mental_health_days"],
    marker="o"
)

plt.xlabel("Hours of Sleep")
plt.ylabel("Average Poor Mental Health Days")
plt.title("Average Poor Mental Health Days by Sleep Duration")

plt.show()


# --------------------------------------------------
# 4. Feature engineering: create sleep categories
# --------------------------------------------------

# Group sleep hours into short, recommended, and long sleep
analysis_df["sleep_category"] = pd.cut(
    analysis_df["sleep_hours"],
    bins=[0, 7, 9, 25],
    labels=["Short Sleep", "Recommended Sleep", "Long Sleep"],
    right=False
)

# Check the number of respondents in each category
print("\nSleep Category Counts:")
print(analysis_df["sleep_category"].value_counts())


# Calculate average poor mental health days by sleep category
category_mental_health = (
    analysis_df
    .groupby("sleep_category", observed=True)["poor_mental_health_days"]
    .mean()
)

print("\nMental Health by Sleep Category:")
print(category_mental_health.round(2))

# Visualize the sleep category comparison
plt.figure(figsize=(8, 5))

plt.bar(
    category_mental_health.index,
    category_mental_health.values
)

plt.xlabel("Sleep Category")
plt.ylabel("Average Poor Mental Health Days")
plt.title("Poor Mental Health Days by Sleep Category")

plt.show()


# --------------------------------------------------
# 5. Feature engineering: create readable age groups
# --------------------------------------------------

# Convert BRFSS age codes into readable age categories
age_labels = {
    1: "18-24",
    2: "25-34",
    3: "35-44",
    4: "45-54",
    5: "55-64",
    6: "65+"
}

analysis_df["age_category"] = analysis_df["age_group"].map(age_labels)


# --------------------------------------------------
# 6. Compare sleep and mental health across age groups
# --------------------------------------------------

# Calculate average poor mental health days by age and sleep category
age_sleep_mental_health = (
    analysis_df
    .groupby(
        ["age_category", "sleep_category"],
        observed=True
    )["poor_mental_health_days"]
    .mean()
    .unstack()
)

print("\nMental Health by Age and Sleep Category:")
print(age_sleep_mental_health.round(2))

# Visualize the age comparison
age_sleep_mental_health.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.xlabel("Age Group")
plt.ylabel("Average Poor Mental Health Days")
plt.title("Poor Mental Health Days by Age and Sleep Category")
plt.xticks(rotation=0)
plt.legend(title="Sleep Category")

plt.tight_layout()
plt.show()