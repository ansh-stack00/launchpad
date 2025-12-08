import express from "express"
const app = express();
const PORT = 3000;


const HOSTNAME = process.env.HOSTNAME || "IronMan";

app.get("/api", (req, res) => {
  res.json({
    message: "Hello from backend service!",
    instance: HOSTNAME,
    timestamp: new Date().toISOString()
  });
});

app.listen(PORT, () => {
  console.log(`Backend running on port ${PORT} - Instance: ${HOSTNAME}`);
});
