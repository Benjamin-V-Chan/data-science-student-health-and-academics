import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("../outputs/cleaned_data.csv")

# Define variables to visualize
variables = ["Gender", "Mobile Phone", "Daily usages", "Health rating"]

for var in variables:
    plt.figure(figsize=(8, 5))
    df[var].value_counts().plot(kind="bar", color="skyblue")
    plt.title(f"Distribution of {var}")
    plt.xlabel(var)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.savefig(f"../outputs/{var}_distribution.png")
    plt.close()
