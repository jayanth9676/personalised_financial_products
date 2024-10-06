import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib
import shap
import matplotlib.pyplot as plt

# Load the preprocessed data
df = pd.read_csv('preprocessed_loan_data.csv')

# Prepare features and target variables
features = ['age', 'annual_income', 'credit_score', 'debt_to_income_ratio', 'savings_balance', 'checking_balance', 'employment_status', 'years_employed', 'home_ownership', 'marital_status', 'num_dependents', 'education_level', 'existing_loans', 'credit_score_category', 'dti_category']
X = df[features]
y_approval = df['approval_status']
y_interest_rate = df['interest_rate']
y_loan_term = df['loan_term']

# Encode categorical variables
le = LabelEncoder()
categorical_columns = ['employment_status', 'home_ownership', 'marital_status', 'education_level', 'credit_score_category', 'dti_category']
for col in categorical_columns:
    X[col] = le.fit_transform(X[col])

# Split the data into training and testing sets
X_train, X_test, y_approval_train, y_approval_test, y_interest_train, y_interest_test, y_term_train, y_term_test = train_test_split(X, y_approval, y_interest_rate, y_loan_term, test_size=0.2, random_state=42)

# Hyperparameter tuning for approval model
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_approval_train)
approval_model = grid_search.best_estimator_

# Train interest rate model
interest_model = RandomForestRegressor(n_estimators=100, random_state=42)
interest_model.fit(X_train, y_interest_train)

# Train loan term model
term_model = RandomForestRegressor(n_estimators=100, random_state=42)
term_model.fit(X_train, y_term_train)

# Evaluate models
approval_accuracy = accuracy_score(y_approval_test, approval_model.predict(X_test))
approval_report = classification_report(y_approval_test, approval_model.predict(X_test))
interest_mse = mean_squared_error(y_interest_test, interest_model.predict(X_test))
term_mse = mean_squared_error(y_term_test, term_model.predict(X_test))

print(f"Approval Model Accuracy: {approval_accuracy:.2f}")
print("Approval Model Classification Report:")
print(approval_report)
print(f"Interest Rate Model MSE: {interest_mse:.2f}")
print(f"Loan Term Model MSE: {term_mse:.2f}")

# Save models
joblib.dump(approval_model, 'approval_model.joblib')
joblib.dump(interest_model, 'interest_model.joblib')
joblib.dump(term_model, 'term_model.joblib')

# Generate SHAP values for model interpretability
explainer = shap.TreeExplainer(approval_model)
shap_values = explainer.shap_values(X_test)

# Plot SHAP summary
shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
plt.savefig('shap_summary.png')
plt.close()

def generate_loan_recommendation(customer_data):
    # Load models
    approval_model = joblib.load('approval_model.joblib')
    interest_model = joblib.load('interest_model.joblib')
    term_model = joblib.load('term_model.joblib')
    
    # Prepare customer data
    customer_features = pd.DataFrame([customer_data])
    
    # Define mapping for categorical variables
    categorical_mapping = {
        'employment_status': {'Employed': 1, 'Unemployed': 0, 'Self-employed': 2},
        'home_ownership': {'Own': 1, 'Rent': 0, 'Mortgage': 2},
        'marital_status': {'Married': 1, 'Single': 0, 'Divorced': 2},
        'education_level': {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3},
        'credit_score_category': {'Poor': 0, 'Fair': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4},
        'dti_category': {'Low': 0, 'Medium': 1, 'High': 2}
    }
    
    # Encode categorical variables in customer data
    for col, mapping in categorical_mapping.items():
        if col in customer_features.columns:
            customer_features[col] = customer_features[col].map(mapping)
            if customer_features[col].isnull().any():
                raise ValueError(f"Invalid value for {col}")
    
    # Ensure all required features are present
    required_features = ['age', 'annual_income', 'credit_score', 'debt_to_income_ratio', 'savings_balance', 
                         'checking_balance', 'employment_status', 'years_employed', 'home_ownership', 
                         'marital_status', 'num_dependents', 'education_level', 'existing_loans', 
                         'credit_score_category', 'dti_category']
    for feature in required_features:
        if feature not in customer_features.columns:
            raise ValueError(f"Missing required feature: {feature}")
    
    # Reorder columns to match the model's expected input
    customer_features = customer_features[required_features]
    
    # Make predictions
    approval_prob = approval_model.predict_proba(customer_features)[0][1]
    interest_rate = interest_model.predict(customer_features)[0]
    loan_term = term_model.predict(customer_features)[0]
    
    # Calculate estimated monthly payment
    loan_amount = customer_data['requested_loan_amount']
    monthly_rate = interest_rate / 1200
    monthly_payment = (loan_amount * monthly_rate * (1 + monthly_rate) ** loan_term) / ((1 + monthly_rate) ** loan_term - 1)
    
    # Get feature importance
    explainer = shap.TreeExplainer(approval_model)
    shap_values = explainer.shap_values(customer_features)
    feature_importance = pd.DataFrame({
        'feature': customer_features.columns,
        'importance': np.abs(shap_values[1][0]).mean()
    }).sort_values('importance', ascending=False)
    
    recommendation = {
        'approval_probability': approval_prob,
        'recommended_interest_rate': interest_rate,
        'recommended_loan_term': loan_term,
        'estimated_monthly_payment': monthly_payment,
        'feature_importance': feature_importance.to_dict('records')
    }
    
    return recommendation

print("Loan recommendation engine created and models saved.")