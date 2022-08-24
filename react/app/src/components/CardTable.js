import React from "react";
import { DataGrid, GridToolbar, GridToolbarContainer, GridToolbarColumnsButton, GridToolbarFilterButton, GridToolbarDensitySelector } from "@mui/x-data-grid";
import { Button, Container } from "@mui/material";
import { useState } from "react";

const gauntletImage =
  "http://cc-client-assets.s3.amazonaws.com/store/gauntletgamesvictoria/7c8176e703db451bad3277bb6d4b8631/medium/Transparent_logo.png";
const hocImage =
  "https://i.ibb.co/JdGh6x9/Screen-Shot-2022-08-09-at-1-43-13-PM-removebg-preview.png";
const wtImage =
  "https://i.ibb.co/hm3qKWc/wizardstower-removebg-preview.png";

const fusionImage = 
  "https://cc-client-assets.s3.amazonaws.com/store/fusiongamingonline/e85497a0877911e79bd1b58786c09dea/large/fusiongamingonline_logo2.png";

const four01Image =
  'https://cdn.shopify.com/s/files/1/1704/1809/files/Logo_For_Website_260x_b5b9ece0-d6a5-4807-9427-0d488c650cb7_320x.png?v=1582044237';

const renderBuyNowBtn = (params) => {
  return (
    <Button
      variant="contained"
      size="small"
      onClick={() => handleClick(params)}
    >
      Buy
    </Button>
  );
};

const handleClick = (params) => {
  window.open(params.link, "noopener,noreferrer");
};

function CustomToolbar() {
  return (
    <GridToolbarContainer>
      <GridToolbarColumnsButton />
      <GridToolbarFilterButton />
      <GridToolbarDensitySelector />
    </GridToolbarContainer>
  );
}

const columns = [
  {
    field: "image",
    headerName: "Image",
    width: 80,
    renderCell: (params) => {
      return <img src={params.row.image} height={90} />;
    },
    align: "center",
    headerAlign: "center",

  },
  { field: "name", headerName: "Name", flex: 1, align: "center", headerAlign: 'center' },
  { field: "set", headerName: "Set", flex:1, align: "center", headerAlign: 'center' },
  { field: "price", headerName: "Price", width: 70, align: "center", headerAlign: 'center', },
  { field: "condition", headerName: "Condition", width: 90, align: "center", headerAlign: 'center' },
  {
    field: "websiteLogo",
    headerName: "Vendor",
    width: 110,
    renderCell: (params) => {
      return <img src={params.row.websiteLogo} width={80} />;
    },
    align: "center",
    headerAlign: 'center',
  },

  {
    field: "buynow  ",
    headerName: "Buy Now",
    renderCell: (params) => {
      return renderBuyNowBtn(params.row);
    },
    align: "center",
    headerAlign: 'center',
  },
];

export default function CardTable({ data }) {
  function uuidv4() {
    return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
      (
        c ^
        (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
      ).toString(16)
    );
  }

  const [pageSize, setPageSize] = useState(5);


  const rows = [];
  for (const website in data) {
    var websiteLogo;
    if (website === "gauntlet") {
      websiteLogo = gauntletImage;
    } else if (website === "houseOfCards") {
      websiteLogo = hocImage;
    } else if (website === "kanatacg") {
      websiteLogo = wtImage;
    } else if (website === "fusion") {
      websiteLogo = fusionImage;
    } else if (website === 'four01') {
      websiteLogo = four01Image;
    }

    for (const card of data[website]) {
      for (const condition of card.stock) {
        if (website === 'fusion') {
          console.log('card found on fusion', card)
        };
        rows.push({
          name: card.name,
          set: card.set,
          image: card.image,
          link: card.link,
          price: condition[1],
          website: website,
          websiteLogo: websiteLogo,
          condition: condition[0],
        });
      }
    }
  }
  const rows2 = data;

  return (
    <div>
        
        <DataGrid
        components={{ Toolbar: CustomToolbar }}
          columns={columns}
          rows={rows}
          pageSize={pageSize}
          onPageSizeChange={(newPage) => setPageSize(newPage)}
          rowsPerPageOptions={[5, 10, 25, 50]}
          getRowId={(row) => uuidv4()}
          rowHeight={100}
          sx={{backgroundColor: '#222222'}}
          autoHeight
        />

    </div>
  );
}
