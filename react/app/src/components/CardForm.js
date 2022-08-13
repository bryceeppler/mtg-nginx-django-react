import React from "react";
import TextField from "@mui/material/TextField";
import axios from "axios";
import { Box, Button, Stack } from "@mui/material";

// changing buttons custom styles
//https://smartdevpreneur.com/override-textfield-border-color-in-material-ui/#Outlined_Variant

export default function CardForm({
  setLoading,
  setData,
  setCardName,
  cardName,
}) {
  const handleSubmit = (e) => {
    setLoading(true);
    e.preventDefault();
    axios
      .get("/", { params: { name: cardName } })
      .then((res) => setData(res.data))
      .catch((err) => console.log(err))
      .finally(() => {
        setCardName("");
        setLoading(false);
      });
  };

  const handleChange = (e) => {
    setCardName(e.target.value);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <Stack spacing={2} direction="row" justifyContent='center'>
          <TextField
            variant="outlined"
            onChange={handleChange}
            value={cardName}
            autoComplete="off"
            size="small"
            spellCheck="false"
          />
          <Button size="small" type="submit" variant="outlined">
            Search
          </Button>
        </Stack>
      </form>
    </div>
  );
}
