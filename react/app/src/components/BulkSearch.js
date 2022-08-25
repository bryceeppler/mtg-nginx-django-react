import {
  Button,
  CircularProgress,
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
import axios from "axios";
import HomeLink from "./HomeLink";

export default function BulkSearch({ data, setData }) {
  const [condition, setCondition] = useState("");
  const [gauntlet, setGauntlet] = useState(false);
  const [four01, setFour01] = useState(false);
  const [houseOfCards, setHouseOfCards] = useState(false);
  const [fusion, setFusion] = useState(false);
  const [kanatacg, setKanatacg] = useState(false);
  const [cardList, setCardList] = useState("");
  const [loading, setLoading] = useState(false);
  const [cardName, setCardName] = useState("");

  const handleChange = (event, val, setVal) => {
    setVal(event.target.checked);
  };

  const handleClick = () => {
    // get list of websites to search
    let websites = [];
    if (gauntlet) websites.push("gauntlet");
    if (four01) websites.push("four01");
    if (houseOfCards) websites.push("houseOfCards");
    if (fusion) websites.push("fusion");
    if (kanatacg) websites.push("kanatacg");

    console.log("Clicked");
    const cardArray = cardList.split("\n");
    setLoading(true);
    axios
      .post("/bulk/", {
     
          cardNames: cardArray,
          websites: websites,
          condition: condition,
       
      })
      .then((res) => {
        console.log("setting response data: ", res.data);
        setData(res.data);
      })
      .catch((err) => console.log(err))
      .finally(() => {
        setLoading(false);
      });
  };
  return (
    <div>
      {!loading ? (
        <Stack 
          direction="row" 
          justifyContent="center"
          spacing={2}
        >
          <Paper
            elevation={3}
            sx={{
              padding: 2,
              width: "30%",
              // border: "1px solid #e0e0e0",
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
              ></Container>
              <Typography p={2}>Select Websites</Typography>
              <FormGroup>
                <FormControlLabel
                  control={<Checkbox />}
                  label="401 Games"
                  onChange={(e) => handleChange(e, four01, setFour01)}
                />

                <FormControlLabel
                  control={<Checkbox />}
                  label="Fusion Gaming"
                  onChange={(e) => handleChange(e, fusion, setFusion)}
                />
                <FormControlLabel
                  control={<Checkbox />}
                  label="Gauntlet Games"
                  onChange={(e) => handleChange(e, gauntlet, setGauntlet)}
                />

                <FormControlLabel
                  control={<Checkbox />}
                  label="House of Cards"
                  onChange={(e) =>
                    handleChange(e, houseOfCards, setHouseOfCards)
                  }
                />

                <FormControlLabel
                  control={<Checkbox />}
                  label="Wizard's Tower"
                  onChange={(e) => handleChange(e, kanatacg, setKanatacg)}
                />

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
              <Button variant="contained" onClick={handleClick}>
                Submit
              </Button>
            </Stack>
          </Paper>
          <Paper
            elevation={3}
            sx={{
              padding: 2,
              width: "70%",
              // border: "1px solid #ccc",
            }}
          >
            <Stack direction="column" spacing={2}>
              <Paper
                elevation={5}
                sx={{ backgroundColor: "#011a3b", padding: "2rem" }}
              >
                <Typography>
                  This is the bulk card search beta. Here you can search for up
                  to 100 cards at a time, across whichever websites you choose.
                  The goal is to come up with the most affordable decklist
                  across those sites, while still browsing cards of acceptable
                  condtion. The list of cards will return the cheapest price for
                  each card.
                </Typography>
              </Paper>
              <Typography p={2}> Enter cards here</Typography>

              <TextField
                placeholder="Enter one card per line..."
                multiline
                rows={20}
                sx={{ width: "100%" }}
                onChange={(e) => setCardList(e.target.value)}
              />
            </Stack>
          </Paper>
        </Stack>
      ) : (
        <Container
          sx={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
        <CircularProgress/>
        <Typography p={2}>Loading... this may take a minute</Typography>
        </Container>
      )}
    </div>
  );
}
