import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data_path = "/Users/abc/Downloads/creditcard.csv"
df = pd.read_csv(data_path)

# Data Exploration
print(df.info())
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print(df.columns)
print(df.dtypes)

print(df.isnull().sum())

fraud_count = df[df['Class'] == 1].shape[0]
legitimate_count = df[df['Class'] == 0].shape[0]
fraud_percentage = (fraud_count / len(df)) * 100

print(f"Number of fraudulent transactions: {fraud_count}")
print(f"Number of legitimate transactions: {legitimate_count}")
print(f"Percentage of fraudulent transactions: {fraud_percentage:.2f}%")

print(df['Amount'].describe())

max_amount = df['Amount'].max()
is_fraudulent_max = df[df['Amount'] == max_amount]['Class'].values[0]

print(f"Maximum transaction amount: ${max_amount:.2f}")
print(f"Is the maximum transaction fraudulent? {is_fraudulent_max == 1}")

# Visualizations
plt.figure(figsize=(8, 6))
sns.countplot(x='Class', data=df)
plt.xlabel('Transaction Class (0: Legitimate, 1: Fraudulent)')
plt.ylabel('Count')
plt.title('Distribution of Fraudulent vs. Legitimate Transactions')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df['Amount'], bins=30, edgecolor='black')
plt.xlabel('Transaction Amount ($)')
plt.ylabel('Frequency')
plt.title('Distribution of Transaction Amounts')
plt.show()

numerical_cols = df.select_dtypes(include=[np.number])
correlation = numerical_cols.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Numerical Features')
plt.show()