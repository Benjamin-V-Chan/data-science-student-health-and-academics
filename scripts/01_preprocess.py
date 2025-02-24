import pandas as pd

# Load the dataset
df = pd.read_csv("../data/Impact_of_Mobile_Phone_on_Students_Health.csv")

# Handling missing values by filling with mode
df.fillna(df.mode().iloc[0], inplace=True)

# Convert categorical values to a standardized format (e.g., lowercase)
df = df.applymap(lambda x: x.strip().lower() if isinstance(x, str) else x)

# Save cleaned dataset
df.to_csv("../outputs/cleaned_data.csv", index=False)
