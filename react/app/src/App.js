import { createTheme, ThemeProvider } from '@mui/system';
import './App.css';
import React from "react";
import CardDisplay from './components/CardDisplay';

function App() {
  return (
    <div className="App">
        <CardDisplay/>
    </div>
  );
}

export default App;
