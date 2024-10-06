import React, { useState } from 'react';
import { ThemeProvider, CssBaseline, Container, Typography, Box } from '@mui/material';
import { createTheme } from '@mui/material/styles';
import Header from './components/Header';
import LoanForm from './components/LoanForm';
import RecommendationResult from './components/RecommendationResult';
import Footer from './components/Footer';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

function App() {
  const [recommendation, setRecommendation] = useState(null);

  const handleSubmit = async (formData) => {
    try {
      const response = await fetch('http://localhost:5000/api/loan-recommendation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      setRecommendation(data);
    } catch (error) {
      console.error('Error fetching loan recommendation:', error);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Header />
      <Container maxWidth="lg">
        <Box my={4}>
          <Typography variant="h4" component="h1" gutterBottom>
            Personalized Loan Recommendation
          </Typography>
          <LoanForm onSubmit={handleSubmit} />
          {recommendation && <RecommendationResult recommendation={recommendation} />}
        </Box>
      </Container>
      <Footer />
    </ThemeProvider>
  );
}

export default App;