import React from "react";
import { Button, Typography } from "@mui/material";
import { Link } from "react-router-dom";

export default function HomeLink() {
  return (
    <div>
      {" "}
      <Link to="/">
        <Button sx={{ margin: 2}}variant="contained" color="primary">
        <Typography
          sx={{
            textDecoration: "underline",
          }}
        >
           back
        </Typography>
        </Button>

      </Link>
    </div>
  );
}
