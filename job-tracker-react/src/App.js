import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    fetch("/applied_jobs.json")
      .then((res) => res.json())
      .then((data) => {
        // Sort by date (most recent first)
        const sorted = data.sort((a, b) => {
          const d1 = new Date(a.date);
          const d2 = new Date(b.date);
          return d2 - d1;
        });
        setJobs(sorted);
      })
      .catch((err) => console.error("Failed to load jobs:", err));
  }, []);

  return (
    <div className="App">
      <h1>📋 My Applied Jobs</h1>
      <div className="job-list">
        {jobs.map((job, i) => (
          <div className="job-card" key={i}>
            <h3>{job.subject}</h3>
            <p><strong>Date:</strong> {formatDate(job.date)}</p>
            <p>{job.snippet}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

function formatDate(dateStr) {
  try {
    const date = new Date(dateStr);
    const options = { year: "numeric", month: "long", day: "numeric" };
    return date.toLocaleDateString(undefined, options);
  } catch (e) {
    return dateStr || "Unknown";
  }
}

export default App;
