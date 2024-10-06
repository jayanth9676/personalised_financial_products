import unittest
import pandas as pd
import numpy as np
from loan_recommendation_engine import generate_loan_recommendation

class TestLoanRecommendation(unittest.TestCase):
    def setUp(self):
        self.sample_customer_data = {
            'age': 35,
            'annual_income': 75000,
            'credit_score': 720,
            'debt_to_income_ratio': 0.3,
            'savings_balance': 50000,
            'checking_balance': 5000,
            'employment_status': 'Employed',
            'years_employed': 10,
            'home_ownership': 'Own',
            'marital_status': 'Married',
            'num_dependents': 2,
            'education_level': 'Bachelor',
            'existing_loans': 1,
            'credit_score_category': 'Good',
            'dti_category': 'Low',
            'requested_loan_amount': 25000
        }

    def test_generate_loan_recommendation(self):
        recommendation = generate_loan_recommendation(self.sample_customer_data)
        
        self.assertIsInstance(recommendation, dict)
        self.assertIn('approval_probability', recommendation)
        self.assertIn('recommended_interest_rate', recommendation)
        self.assertIn('recommended_loan_term', recommendation)
        self.assertIn('estimated_monthly_payment', recommendation)
        self.assertIn('feature_importance', recommendation)
        
        self.assertGreaterEqual(recommendation['approval_probability'], 0)
        self.assertLessEqual(recommendation['approval_probability'], 1)
        self.assertGreater(recommendation['recommended_interest_rate'], 0)
        self.assertGreater(recommendation['recommended_loan_term'], 0)
        self.assertGreater(recommendation['estimated_monthly_payment'], 0)
        self.assertGreater(len(recommendation['feature_importance']), 0)

    def test_generate_loan_recommendation_edge_cases(self):
        # Test with very low credit score
        low_credit_data = self.sample_customer_data.copy()
        low_credit_data['credit_score'] = 300
        low_credit_data['credit_score_category'] = 'Poor'
        low_credit_recommendation = generate_loan_recommendation(low_credit_data)
        self.assertLess(low_credit_recommendation['approval_probability'], 0.5)

        # Test with very high income
        high_income_data = self.sample_customer_data.copy()
        high_income_data['annual_income'] = 1000000
        high_income_recommendation = generate_loan_recommendation(high_income_data)
        self.assertGreater(high_income_recommendation['approval_probability'], 0.5)

    def test_feature_importance(self):
        recommendation = generate_loan_recommendation(self.sample_customer_data)
        self.assertIn('feature_importance', recommendation)
        self.assertIsInstance(recommendation['feature_importance'], list)
        self.assertGreater(len(recommendation['feature_importance']), 0)

    def test_model_consistency(self):
        # Test that the model gives consistent results for the same input
        recommendation1 = generate_loan_recommendation(self.sample_customer_data)
        recommendation2 = generate_loan_recommendation(self.sample_customer_data)
        self.assertEqual(recommendation1, recommendation2)

    def test_invalid_input(self):
        # Test with missing required field
        invalid_data = self.sample_customer_data.copy()
        del invalid_data['credit_score']
        with self.assertRaises(ValueError):
            generate_loan_recommendation(invalid_data)

    def test_invalid_categorical_value(self):
        # Test with an invalid employment status
        invalid_data = self.sample_customer_data.copy()
        invalid_data['employment_status'] = 'Invalid'
        with self.assertRaises(ValueError):
            generate_loan_recommendation(invalid_data)

if __name__ == '__main__':
    unittest.main()