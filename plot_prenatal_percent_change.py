import pandas as pd
import matplotlib.pyplot as plt

def load_long(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    df.rename(columns={df.columns[0]: "County"}, inplace=True)
    df = df[df["County"].str.lower() != "county summary"]
    long = df.melt(id_vars="County", var_name="Year", value_name="Visits")
    long["Year"] = long["Year"].astype(int)
    long["Visits"] = long["Visits"].astype(str).str.replace(",", "", regex=False).astype(float)
    return long

r_long = load_long("data/prenatal_timeseries_rural.csv")
nr_long = load_long("data/prenatal_timeseries_suburban.csv")

r_mean = r_long.groupby("Year")["Visits"].mean().reset_index()
nr_mean = nr_long.groupby("Year")["Visits"].mean().reset_index()

base_r = r_mean.iloc[0]["Visits"]
base_nr = nr_mean.iloc[0]["Visits"]

r_mean["PctChange"] = r_mean["Visits"] / base_r
nr_mean["PctChange"] = nr_mean["Visits"] / base_nr

plt.figure(figsize=(10,6))
plt.plot(r_mean["Year"], r_mean["PctChange"], marker="o", linewidth=2, label="Rural", color="#2a6fbb")
plt.plot(nr_mean["Year"], nr_mean["PctChange"], marker="o", linewidth=2, label="Non-Rural", color="#c72c41")

plt.axhline(1.0, linestyle="--", color="gray", linewidth=1)
plt.title("Relative Change in Inadequate Prenatal Care\n(<5 Visits) — 2018 Baseline")
plt.xlabel("Year")
plt.ylabel("2018-Normalized Level (1.0 = baseline)")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
