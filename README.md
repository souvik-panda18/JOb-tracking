# 🧾 Job Tracker

A full-stack Job Tracker web application built with **React** and **Python**, designed to help users manage and monitor their job applications efficiently.

---

## 🚀 Features

- Add, edit, and delete job applications
- Track job status (Applied, Interview, Offer, Rejected)
- Store additional job details like company name, role, date, and notes
- Frontend built with **React**
- Backend powered by **Python**
- Persistent storage using local JSON or database (optional)
- Simple, responsive UI

---

## 🛠️ Tech Stack

**Frontend:**
- React
- HTML/CSS
- JavaScript

**Backend:**
- Python
- Flask *(optional, if you're using it for API routes)*

**Other:**
- JSON for temporary data storage (can be extended to DB)
- Git & GitHub for version control

---

## 📂 Project Structure

job-tracker/
├── job-tracker-react/ # React frontend
│ ├── public/
│ └── src/
│ ├── App.js
│ └── ...
├── Main.py # Python backend (entry point)
├── Credentials.json # API credentials (keep secret, ignored in .gitignore)
├── applied_jobs.json # Job data storage
└── .gitignore

yaml
Copy
Edit

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/souvik-panda18/JOb-tracking.git
cd job-tracker
2. Start the React Frontend
bash
Copy
Edit
cd job-tracker-react
npm install
npm start
This will start the React app at http://localhost:3000.

3. Start the Python Backend (Optional)
Make sure you have Python installed:

bash
Copy
Edit
python Main.py
