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
import InputLabel from "@mui/material/InputLabel";
export default function Bulk() {
  const [condition, setCondition] = useState("");
  return (
    <div>
      <Container width="100%" height="100%" display="flex">
        <Paper maxWidth="1200px">
          <Stack direction="row" justifyContent="center">
            <Paper
              sx={{
                padding: 2,
                width: "30%",
                border: "1px solid #e0e0e0",
              }}
            >
              <Stack
                direction="column"
                spacing={2}
                justifyContent="center"
                alignItems="center"
              >
                <Container
                  sx={{
                    paddingTop: 2,
                  }}
                >
                  <Link to="/">
                    <Typography
                      sx={{
                        textDecoration: "underline",
                        color: "#70BDF9",
                      }}
                    >
                      Go back
                    </Typography>
                  </Link>
                </Container>
                <Typography p={2}>Select Websites</Typography>
                <FormGroup>
                  <FormControlLabel
                    control={<Checkbox />}
                    label="House of Cards"
                  />
                  <FormControlLabel
                    control={<Checkbox />}
                    label="Gauntlet Games"
                  />

                  <FormControlLabel
                    control={<Checkbox />}
                    label="Wizard's Tower"
                  />
                  <FormControlLabel
                    control={<Checkbox />}
                    label="Fusion Gaming"
                  />
                  <FormControlLabel control={<Checkbox />} label="401 Games" />

                  {/* CONDITION SELECTOR */}
                  <Typography p={2}>Worst acceptable condition</Typography>
                  <Select
                    value={condition}
                    onChange={(e) => setCondition(e.target.value)}
                    autoWidth
                  >
                    <MenuItem value="">
                      <em>None</em>
                    </MenuItem>
                    <MenuItem value={"NM"}>Near-mint</MenuItem>
                    <MenuItem value={"LP"}>Lightly played</MenuItem>
                    <MenuItem value={"MP"}>Moderately played</MenuItem>
                    <MenuItem value={"HP"}>Heavily played</MenuItem>
                  </Select>
                </FormGroup>
                <Button
                  variant="contained"
                  sx={{
                    maxWidth: "100px",
                  }}
                >
                  Submit
                </Button>
              </Stack>
            </Paper>
            <Paper
              sx={{
                padding: 2,
                width: "70%",
                border: "1px solid #ccc",
              }}
            >
              <Stack direction="column" spacing={2}>
                <Typography p={2}> Enter cards here</Typography>

                <TextField
                  placeholder="Enter one card per line..."
                  multiline
                  rows={20}
                  maxRows={100}
                  sx={{ width: "100%" }}
                />
              </Stack>
            </Paper>
          </Stack>
        </Paper>
      </Container>
    </div>
  );
}
