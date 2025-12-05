import express from "express";
import mongoose from "mongoose";
import cors from "cors";

const app = express();
app.use(express.json());
app.use(cors());

const MONGO_URL = process.env.MONGO_URL || "mongodb://localhost:27017/feedback";

mongoose
  .connect(MONGO_URL)
  .then(() => console.log("Connected to MongoDB"))
  .catch((err) => console.error("MongoDB connection error:", err));

const FeedbackSchema = new mongoose.Schema({
  name: { type: String, required: true },
  message: { type: String, required: true }
});

const Feedback = mongoose.model("Feedback", FeedbackSchema);

// Routes
app.get("/", (req, res) => {
  res.send("Feedback API is running...");
});

app.post("/feedback", async (req, res) => {
  try {
    const entry = await Feedback.create(req.body);
    res.json(entry);
  } catch (err) {
    res.status(400).json({ error: "Invalid data" });
  }
});

app.get("/feedback", async (req, res) => {
  const allFeedback = await Feedback.find();
  res.json(allFeedback);
});

const PORT = 5000;
app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));
