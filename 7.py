import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a simulated dataset with three columns
np.random.seed(42)  # Set a seed for reproducibility
data = pd.DataFrame({
    "column1": np.random.normal(loc=100, scale=15, size=1000),
    "column2": np.random.uniform(low=50, high=200, size=1000),
    "column3": np.random.poisson(lam=5, size=1000)
})

# Visualize histograms
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.hist(data["column1"], bins=20)
plt.title("Histogram of Column 1")

plt.subplot(1, 3, 2)
plt.hist(data["column2"], bins=20)
plt.title("Histogram of Column 2")

plt.subplot(1, 3, 3)
plt.hist(data["column3"], bins=20)
plt.title("Histogram of Column 3")
plt.show()

# Visualize boxplots
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
sns.boxplot(data["column1"])
plt.title("Boxplot of Column 1")

plt.subplot(1, 3, 2)
sns.boxplot(data["column2"])
plt.title("Boxplot of Column 2")

plt.subplot(1, 3, 3)
sns.boxplot(data["column3"])
plt.title("Boxplot of Column 3")
plt.show()

# Visualize scatter plots
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(data["column1"], data["column2"])
plt.xlabel("Column 1")
plt.ylabel("Column 2")
plt.title("Scatter Plot of Column 1 vs. Column 2")

plt.subplot(1, 2, 2)
plt.scatter(data["column1"], data["column3"])
plt.xlabel("Column 1")
plt.ylabel("Column 3")
plt.title("Scatter Plot of Column 1 vs. Column 3")
plt.show()
