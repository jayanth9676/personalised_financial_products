# Dataset Generation Prompt for Personalized Loan Recommendation System

## Objective
Generate a realistic dataset of 10,000 rows for a bank's personalized loan recommendation system. This dataset will be used to train and test an AI model that provides customized loan offers to customers.

## Dataset Structure
Create a CSV file with the following columns:

1. customer_id: Unique identifier (e.g., LN001, LN002, etc.)
2. age: Integer between 18 and 80, with most customers between 25 and 65
3. annual_income: Integer between $20,000 and $500,000, correlated with age and education level
4. credit_score: Integer between 300 and 850
5. employment_status: 'Employed', 'Self-Employed', 'Unemployed', or 'Retired'
6. job_title: Realistic job titles correlated with income and education level
7. years_employed: Integer between 0 and 40, correlated with age
8. debt_to_income_ratio: Float between 0.0 and 1.0
9. savings_balance: Integer between $0 and $1,000,000
10. checking_balance: Integer between $0 and $50,000
11. home_ownership: 'Own', 'Rent', or 'Mortgage'
12. marital_status: 'Single', 'Married', 'Divorced', or 'Widowed'
13. num_dependents: Integer between 0 and 5
14. education_level: 'High School', 'Associate's', 'Bachelor's', 'Master's', or 'Doctorate'
15. loan_purpose: Various realistic purposes (e.g., 'Home Improvement', 'Debt Consolidation', 'Business Expansion', etc.)
16. requested_loan_amount: Integer between $1,000 and $500,000, correlated with income and credit score
17. existing_loans: Integer between 0 and 5
18. payment_history: 'Excellent', 'Good', 'Fair', or 'Poor'
19. loan_term: 12, 24, 36, 48, 60, 120, 180, or 360 (months)
20. interest_rate: Float between 3.0% and 25.0%, correlated with credit score and loan term
21. monthly_payment: Calculated based on loan amount, term, and interest rate
22. approval_status: 'Approved', 'Pending', or 'Rejected'

## Data Generation Guidelines

1. Maintain realistic relationships between fields:
   - Higher credit scores should generally lead to lower interest rates and higher approval chances
   - Higher debt-to-income ratios should decrease approval chances and increase interest rates
   - Loan amounts should be realistic given the customer's income and credit score
   - Monthly payments should be correctly calculated based on loan amount, term, and interest rate

2. Create a diverse range of scenarios:
   - Aim for approximately 60% approved, 25% pending, and 15% rejected loans
   - Include a mix of high-income and low-income customers, good and bad credit scores, and various loan purposes

3. Use realistic distributions for categorical variables:
   - Employment status: 70% Employed, 15% Self-Employed, 10% Unemployed, 5% Retired
   - Education level: 30% High School, 20% Associate's, 35% Bachelor's, 12% Master's, 3% Doctorate
   - Marital status: 45% Married, 35% Single, 15% Divorced, 5% Widowed

4. Ensure data consistency and realism:
   - Avoid impossible combinations (e.g., an 18-year-old with 20 years of employment)
   - Verify that all calculated fields (e.g., monthly_payment) are accurate
   - Confirm that the approval status makes sense given the customer's financial profile

## Validation and Summary

1. Perform a second pass to verify the realism and consistency of the generated data.
2. Provide a brief summary of the generated dataset, including:
   - Distribution of approval statuses
   - Average credit score, income, and loan amount
   - Any interesting patterns or insights observed in the data

## Output
Generate a CSV file named 'loan_recommendation_dataset.csv' containing 10,000 rows of data following the above guidelines. Ensure that the data is diverse, realistic, and suitable for training a personalized loan recommendation system.