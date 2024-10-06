import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('loan_recommendation_dataset_5000.csv')

# Display basic information about the dataset
print(df.info())
print(df.describe())

# Handle missing values
df = df.dropna()

# Encode categorical variables
le = LabelEncoder()
categorical_columns = ['employment_status', 'home_ownership', 'marital_status', 'education_level', 'loan_purpose', 'payment_history', 'approval_status']
for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

# Analyze correlations
correlation_matrix = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.close()

# Analyze approval status distribution
plt.figure(figsize=(8, 6))
df['approval_status'].value_counts().plot(kind='bar')
plt.title('Loan Approval Status Distribution')
plt.xlabel('Approval Status')
plt.ylabel('Count')
plt.savefig('approval_status_distribution.png')
plt.close()

# Analyze credit score vs. interest rate
plt.figure(figsize=(10, 6))
plt.scatter(df['credit_score'], df['interest_rate'])
plt.title('Credit Score vs. Interest Rate')
plt.xlabel('Credit Score')
plt.ylabel('Interest Rate')
plt.savefig('credit_score_vs_interest_rate.png')
plt.close()

# Analyze debt-to-income ratio vs. loan amount
plt.figure(figsize=(10, 6))
plt.scatter(df['debt_to_income_ratio'], df['requested_loan_amount'])
plt.title('Debt-to-Income Ratio vs. Requested Loan Amount')
plt.xlabel('Debt-to-Income Ratio')
plt.ylabel('Requested Loan Amount')
plt.savefig('dti_vs_loan_amount.png')
plt.close()

# Feature engineering
df['credit_score_category'] = pd.cut(df['credit_score'], bins=[0, 580, 670, 740, 800, 850], labels=['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'])
df['dti_category'] = pd.cut(df['debt_to_income_ratio'], bins=[0, 0.36, 0.43, 1], labels=['Good', 'Acceptable', 'High'])

# Save the preprocessed dataset
df.to_csv('preprocessed_loan_data.csv', index=False)

print("Data analysis completed. Visualizations and preprocessed data saved.")