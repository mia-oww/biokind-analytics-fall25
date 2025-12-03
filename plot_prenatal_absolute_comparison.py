import pandas as pd
import matplotlib.pyplot as plt

rural = pd.read_csv("late_noprenatal_rural - Sheet1.csv")
nonrural = pd.read_csv("late_no-prenatal care nonrural - Sheet1.csv")

# standardize column names
for df in (rural, nonrural):
    df.columns = df.columns.str.strip()
    df.rename(columns={df.columns[0]: "County"}, inplace=True)
    df.dropna(subset=["County"], inplace=True)
    df = df[df["County"].str.lower() != "county summary"]

# long format
r_long = rural.melt(id_vars="County", var_name="Year", value_name="Visits")
nr_long = nonrural.melt(id_vars="County", var_name="Year", value_name="Visits")

# Convert types
r_long["Year"] = r_long["Year"].astype(int)
nr_long["Year"] = nr_long["Year"].astype(int)
r_long["Visits"] = r_long["Visits"].astype(str).str.replace(",", "", regex=False).astype(float)
nr_long["Visits"] = nr_long["Visits"].astype(str).str.replace(",", "", regex=False).astype(float)

# Group by year
r_mean = r_long.groupby("Year")["Visits"].mean().reset_index()
nr_mean = nr_long.groupby("Year")["Visits"].mean().reset_index()

# Plot
fig, axes = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# --- Rural (ZOOMED) ---
axes[0].plot(r_mean["Year"], r_mean["Visits"], marker="o", linewidth=2, color="#2a6fbb")
axes[0].set_title("Rural Average Count (Late or No Prenatal Visits)")
axes[0].set_ylabel("Avg Count (Late or No Visits)")
axes[0].set_ylim(r_mean["Visits"].min() - 1, r_mean["Visits"].max() + 1)
axes[0].text(0.02, 0.9, "Zoomed scale", transform=axes[0].transAxes, fontsize=10, color="gray")

# --- Non-Rural (full scale) ---
axes[1].plot(nr_mean["Year"], nr_mean["Visits"], marker="o", linewidth=2, color="#c72c41")
axes[1].set_title("Non-Rural Average Count (Late or No Prenatal Visits)")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Avg Count (Late or No Visits)")
# scales to actual nonrural values

plt.suptitle("Comparison of Late or No Prenatal Care — GA Counties (2018–2024)")
plt.tight_layout(rect=[0,0,1,0.95])
plt.show()
