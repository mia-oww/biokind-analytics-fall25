import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (only RURAL counties)
df = pd.read_csv("ruralbirths_w_less_than_5_visits.csv")

long_df = df.melt(
    id_vars="County",
    var_name="Year",
    value_name="Visits_LT5"
)
# Convert wide -> long format
long_df["Year"] = long_df["Year"].astype(str).str.strip().astype(int)
long_df["Visits_LT5"] = (
    long_df["Visits_LT5"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Group to average by year
grouped = long_df.groupby("Year")["Visits_LT5"].mean().reset_index()
# Plot mean trend only
plt.figure(figsize=(10,6))
plt.plot(
    grouped["Year"],
    grouped["Visits_LT5"],
    marker="o",
    linewidth=2,
    color="#2a6fbb"
)

y_min = grouped["Visits_LT5"].min() - 2
y_max = grouped["Visits_LT5"].max() + 2
plt.ylim(y_min, y_max)

plt.title("Average Births with <5 Prenatal Care Visits\nRural Georgia Counties (2018–2024)")
plt.xlabel("Year")
plt.ylabel("Average Count (<5 visits)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()