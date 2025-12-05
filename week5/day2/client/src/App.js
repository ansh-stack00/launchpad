import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [feedback, setFeedback] = useState([]);
  const [form, setForm] = useState({ name: "", message: "" });

  // Fetch all feedback
  const fetchFeedback = async () => {
    try {
      const res = await axios.get("http://localhost:5000/feedback");
      setFeedback(res.data); 
    } catch (err) {
      console.error("Error fetching feedback:", err);
    }
  };

  // Submit form
  const submit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://localhost:5000/feedback", form);
      setForm({ name: "", message: "" });
      fetchFeedback();
    } catch (err) {
      console.error("Error submitting feedback:", err);
    }
  };

  useEffect(() => {
    fetchFeedback();
  }, []);

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>User Feedback</h1>

      <form onSubmit={submit} style={{ marginBottom: "2rem" }}>
        <input
          type="text"
          placeholder="Your Name"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
          required
          style={{ marginRight: "1rem" }}
        />

        <input
          type="text"
          placeholder="Your Message"
          value={form.message}
          onChange={(e) => setForm({ ...form, message: e.target.value })}
          required
          style={{ marginRight: "1rem" }}
        />

        <button type="submit">Submit</button>
      </form>

      <h3>Feedback Entries</h3>
      <ul>
        {feedback.map((item) => (
          <li key={item._id}>
            <strong>{item.name}</strong>: {item.message}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
