import React, { useState } from "react";
import axios from "axios";
import CardForm from "./CardForm";
import CardTable from "./CardTable";
import {
  Typography,
  Stack,
  Card,
  Paper,
  Container,
  Button,
  Modal,
} from "@mui/material";
import HelpCenterTwoToneIcon from "@mui/icons-material/HelpCenterTwoTone";
import { Box } from "@mui/system";

axios.defaults.baseURL = "http://54.225.140.11/api";


// modal styling temporarily
const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  boxShadow: 24,
  p: 4,
};


export default function CardDisplay() {
  // General app state
  const [cardName, setCardName] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  // Modal state
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    <div>
      <Stack
        direction={"column"}
        spacing={2}
        justifyContent="center"
        alignItems={"center"}
      >
        <Paper
          sx={{
            padding: 2,
            margin: 2,
            width: "400px",
            justifyContent: "center",
          }}
        >
          <Stack
            direction="row"
            spacing={4}
            justifyContent="center"
          >
            <Typography
              variant="h4"
              component="h1"
              color="primary"
              sx={{ fontWeight: "bold", marginBottom: 2 }}
            >
              bugbear
            </Typography>
            <HelpCenterTwoToneIcon
              color="primary"
              sx={{ "&:hover": { color: "white" } }}
              onClick={handleOpen}
            />
          </Stack>

          <CardForm
            setLoading={setLoading}
            setData={setData}
            setCardName={setCardName}
            cardName={cardName}
          />
        </Paper>

        <div style={{ height: 400, width: "100%", maxWidth: "900px" }}>
          <div style={{ display: "flex", height: "100%" }}>
            <div style={{ flexGrow: 1 }}>
              {loading ? <p>Loading...</p> : data && <CardTable data={data} />}
            </div>
          </div>
        </div>
      </Stack>

          <Modal
            open={open}
            onClose={handleClose}
            aria-labelledby="simple-modal-title"
            aria-describedby="simple-modal-description"
          >
            <Box sx={style}>
            <Typography id="modal-modal-title" variant="h6" component="h2">
            What is bugbear?
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            Bugbear was created to help Canadian MTG enthusiasts find the cheapest card
            prices from Canadian vendors. Currently, we support HouseofCards, Gauntlet Games,
            and WizardTower. If you would like to see another site indexed on bugbear, or encounter
            any bugs, email me at epplerdev@gmail.com.
          </Typography>

            </Box>
          </Modal>


    </div>
  );
}
