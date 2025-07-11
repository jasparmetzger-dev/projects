from datasets import load_dataset
import pandas as pd
from sklearn.model_selection import train_test_split
import os
# Load the dataset from Hugging Face
dataset = load_dataset("eduhuemar001/tinyllama-german-dataset-sentiment-temp-train")

# Convert the Hugging Face dataset to a pandas DataFrame
df = dataset["train"].to_pandas()

# Check the data
print(df.head())
print(df["sentiment"].value_counts())

# Stratified train/test split
df_train, df_test = train_test_split(
    df,
    test_size=0.2,
    stratify=df["sentiment"],
    random_state=42
)
train_p = os.path.join(os.getcwd(), "sentiment_analysis", "data", "train_data.csv")
test_p = os.path.join(os.getcwd(), "sentiment_analysis", "data", "test_data.csv")

df_train.to_csv(train_p, index=False)
df_test.to_csv(test_p, index=False)


