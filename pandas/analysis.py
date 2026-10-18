import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
print(df.head())
print(df.describe())

by_product = df.groupby("product")["revenue"].sum()
print(by_product)

by_product.plot(kind="bar", title="Revenue by product", rot=0)
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("chart.png")
plt.show()
