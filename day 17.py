import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
    "Month":   ["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales":   [1200, 1500, 1300, 1800, 2000, 1700],
    "Profit":  [200,  300,  250,  400,  500,  350],
    "Customers":[150, 180, 160, 220, 250, 200]
}
df = pd.DataFrame(data)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1 - Line — Sales و Profit مع بعض
axes[0,0].plot(data["Month"], data["Sales"], color="blue", marker="o", label="Sales")
axes[0,0].plot(data["Month"], data["Profit"], color="green", marker="s", label="Profit")
axes[0,0].set_title("Sales & Profit")
axes[0,0].legend()
axes[0,0].grid(True)

# 2 - Bar
axes[0,1].bar(data["Month"], data["Customers"], color="orange")
axes[0,1].set_title("Customers per Month")
axes[0,1].set_ylabel("Customers")

# 3 - Scatter
axes[1,0].scatter(data["Sales"], data["Profit"], color="purple", s=100)
axes[1,0].set_title("Sales vs Profit")
axes[1,0].set_xlabel("Sales")
axes[1,0].set_ylabel("Profit")

# 4 - Histogram
axes[1,1].hist(data["Sales"], bins=5, color="red", alpha=0.7)
axes[1,1].set_title("Sales Distribution")
axes[1,1].axvline(np.mean(data["Sales"]), color="black", label="Mean")
axes[1,1].legend()

plt.tight_layout()
plt.show()

