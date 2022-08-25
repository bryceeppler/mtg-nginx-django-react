import {
  Button,
  Container,
  MenuItem,
  Paper,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import React from "react";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import { useState } from "react";
import { Link } from "react-router-dom";
import Select from "@mui/material/Select";
import BulkSearch from "./components/BulkSearch";
import BulkResults from "./components/BulkResults";
import HomeLink from "./components/HomeLink";
export default function Bulk() {
  const [data, setData] = useState(null);
  return (
    <div>
      <Container width="100%" height="100%" sx={{ padding: 2 }}>
        <Paper
        
          maxWidth="1200px"
          sx={{
            padding: 2,
          }}
        >

          <HomeLink />
          {!data && <BulkSearch data={data} setData={setData} />}
          {data && <BulkResults data={data} setData={setData} />}
        </Paper>
      </Container>
    </div>
  );
}
