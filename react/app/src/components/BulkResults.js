import React from "react";
import BulkTable from "./BulkTable";

export default function BulkResults({ data }) {
  return (
    <div>
      <div style={{ height: 400, width: "100%", maxWidth: "1200px" }}>
        <div style={{ display: "flex", height: "100%" }}>
          <div style={{ flexGrow: 1 }}>
            <BulkTable data={data}/>
          </div>
        </div>
      </div>
    </div>
  );
}
