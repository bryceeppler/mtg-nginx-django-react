import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';

const root = ReactDOM.createRoot(document.getElementById('root'));

const theme = createTheme({
        palette: {
                mode: 'dark',
                primary: {
                        // main: '#8C67AB',
                        // main: '#3401A9',
                        // main: '#00B0F0',
                        main: '#ECA35B',


                },
        },
})


root.render(
        <ThemeProvider theme={theme}>
                <CssBaseline/>
                <App />
        </ThemeProvider>
);
