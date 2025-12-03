import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.DataFrame({
    "county_type": ["rural"]*50 + ["nonrural"]*50,
    "premature_rate": sns.load_dataset("tips")["total_bill"][:100] / 100
})

sns.boxplot(data=data, x="county_type", y="premature_rate")
plt.title("Rural vs. Urban Counties")
plt.ylabel("Proportion of premature births")
plt.xlabel("Type of county")
plt.show()
