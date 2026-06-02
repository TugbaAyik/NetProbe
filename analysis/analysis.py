import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

df = pd.read_csv(r"C:\Users\tugba\Desktop\NetProbe\logs\client_log.csv")

plt.bar(df["Metric"], df["Value"])
plt.title("NetProbe Performance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()