import React from 'react';
import { Box, Typography, Paper, Grid } from '@mui/material';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function RecommendationResult({ recommendation }) {
  const {
    approval_probability,
    recommended_interest_rate,
    recommended_loan_term,
    estimated_monthly_payment,
    feature_importance,
  } = recommendation;

  return (
    <Box mt={4}>
      <Typography variant="h5" gutterBottom>
        Loan Recommendation
      </Typography>
      <Paper elevation={3} sx={{ p: 3 }}>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6}>
            <Typography variant="h6">Approval Probability</Typography>
            <Typography variant="h4">{(approval_probability * 100).toFixed(2)}%</Typography>
          </Grid>
          <Grid item xs={12} md={6}>
            <Typography variant="h6">Recommended Interest Rate</Typography>
            <Typography variant="h4">{recommended_interest_rate.toFixed(2)}%</Typography>
          </Grid>
          <Grid item xs={12} md={6}>
            <Typography variant="h6">Recommended Loan Term</Typography>
            <Typography variant="h4">{recommended_loan_term} months</Typography>
          </Grid>
          <Grid item xs={12} md={6}>
            <Typography variant="h6">Estimated Monthly Payment</Typography>
            <Typography variant="h4">${estimated_monthly_payment.toFixed(2)}</Typography>
          </Grid>
        </Grid>
      </Paper>
      <Box mt={4}>
        <Typography variant="h6" gutterBottom>
          Feature Importance
        </Typography>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={feature_importance}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="feature" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="importance" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </Box>
    </Box>
  );
}

export default RecommendationResult;