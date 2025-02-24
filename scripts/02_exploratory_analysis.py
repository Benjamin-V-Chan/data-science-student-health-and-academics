import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../outputs/cleaned_data.csv")

# Summary statistics
summary = df.describe(include="all").transpose()

# Save summary statistics
summary.to_csv("../outputs/summary_statistics.txt", sep="\t")
