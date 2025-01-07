# Credit Card Fraud Detection - Exploratory Data Analysis

This repository contains the code and findings from an Exploratory Data Analysis (EDA) conducted on a credit card transactions dataset. The goal of this project is to identify patterns and anomalies that may indicate fraudulent activity.

**Key Findings:**

* **Dataset:** 
    - Consists of 284,807 transactions with 31 features, including 'Time', 'Amount', and 28 principal component features (V1-V28).
    - No missing values were found in the dataset.
    - The dataset exhibits severe class imbalance, with only 0.17% of transactions classified as fraudulent.
* **Transaction Amounts:**
    - The maximum transaction amount is significantly higher than the mean, suggesting the presence of outliers. 
    - The distribution of transaction amounts needs further investigation.

**Libraries Used:**

- **pandas:** For data manipulation and analysis.
- **matplotlib:** For basic plotting.
- **seaborn:** For enhanced visualizations.
- **NumPy:** For numerical operations.

**Key Analyses Performed:**

- Data loading and initial exploration.
- Analysis of fraudulent vs. legitimate transactions.
- Statistical summary of transaction amounts.
- Creation of visualizations:
    - Bar chart of fraudulent vs. legitimate transactions.
    - Histogram of transaction amounts.
    - Correlation heatmap of numerical features.

This project provides a foundation for further analysis and the development of machine learning models to effectively detect and prevent credit card fraud.
