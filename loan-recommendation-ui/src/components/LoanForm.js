import React, { useState } from 'react';
import { Box, Button, Grid, TextField, Typography } from '@mui/material';

function LoanForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    age: '',
    annual_income: '',
    credit_score: '',
    debt_to_income_ratio: '',
    savings_balance: '',
    checking_balance: '',
    employment_status: '',
    years_employed: '',
    home_ownership: '',
    marital_status: '',
    num_dependents: '',
    education_level: '',
    existing_loans: '',
    requested_loan_amount: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 3 }}>
      <Typography variant="h6" gutterBottom>
        Enter Your Information
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={6}>
          <TextField
            required
            fullWidth
            label="Age"
            name="age"
            type="number"
            value={formData.age}
            onChange={handleChange}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            required
            fullWidth
            label="Annual Income"
            name="annual_income"
            type="number"
            value={formData.annual_income}
            onChange={handleChange}
          />
        </Grid>
        {/* Add more form fields for other attributes */}
      </Grid>
      <Button
        type="submit"
        fullWidth
        variant="contained"
        sx={{ mt: 3, mb: 2 }}
      >
        Get Loan Recommendation
      </Button>
    </Box>
  );
}

export default LoanForm;