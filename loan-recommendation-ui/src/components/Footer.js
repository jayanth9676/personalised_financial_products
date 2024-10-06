import React from 'react';
import { Box, Typography } from '@mui/material';

function Footer() {
  return (
    <Box mt={8} py={3} bgcolor="primary.main" color="white">
      <Typography variant="body2" align="center">
        © 2023 AI-Powered Loan Recommendations. All rights reserved.
      </Typography>
    </Box>
  );
}

export default Footer;