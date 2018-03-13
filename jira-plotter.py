import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.style.use("ggplot")

df = pd.read_csv("jira-export.csv")

vals = df["Status"].value_counts().sort_values()
norm_vals = np.round(df["Status"].value_counts(normalize=True).sort_values() * 100, 2)

total = vals.sum()

ax = vals.plot("barh")

for p in ax.patches:
    n = p.get_width()
    percent = round(n/total * 100, 1)
    ax.annotate(str(n) + ", " + str(percent) + "%", (p.get_width() * 1.005, p.get_y() * 1.005))

plt.title("Status Distribution")
plt.ylabel("Status")
plt.xlabel("Count")

plt.savefig("jira-plot.png", bbox_inches="tight")


all_info = pd.concat([vals, norm_vals], axis=1, keys=["Count", "Percentage"])
all_info.index.name = "Status"
all_info.to_csv("out.csv")
