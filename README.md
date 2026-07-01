# 🤖 AI Code Mentor

> An AI-powered Chrome Extension that analyzes code directly from websites like GitHub, LeetCode, CodeChef, and more using Google's Gemini AI.

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/Python-FastAPI-green)
![JavaScript](https://img.shields.io/badge/JavaScript-Chrome%20Extension-yellow)
![Gemini](https://img.shields.io/badge/AI-Gemini-red)

---

# 📌 Features

### 🧠 AI Code Analysis
- ✅ Explain Code
- ✅ Detect Bugs
- ✅ Optimize Code
- ✅ Generate Comments
- ✅ Translate Code
- ✅ Time & Space Complexity Analysis
- ✅ Unit Test Generation

---

# 🌐 Supported Platforms

- GitHub
- LeetCode
- CodeChef
- Generic Websites (Extensible)

---

# ⚙️ Tech Stack

## Frontend
- HTML
- CSS
- JavaScript
- Chrome Extension (Manifest V3)

## Backend
- Python
- FastAPI
- Google Gemini API

---

# 🏗️ Project Architecture

```
Chrome Extension
│
├── Popup UI
├── Background Script
├── Content Script
│
▼

FastAPI Backend
│
├── API Routes
├── AI Service
├── Prompt Engine
├── Schemas
│
▼

Gemini API
│
▼

Structured JSON Response
│
▼

Chrome Extension UI
```

---

# 📂 Folder Structure

```
AI-Code-Mentor
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── ai
│   │   ├── prompts
│   │   ├── schemas
│   │   ├── services
│   │   ├── utils
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── extension
│   ├── popup
│   ├── background
│   ├── content
│   ├── settings
│   ├── styles
│   ├── assets
│   └── manifest.json
│
└── README.md
```

---

# 🚀 Current Progress

| Phase | Status |
|--------|--------|
| Project Foundation | ✅ |
| Extension UI | 🟡 |
| Code Extraction | ✅ |
| Backend | ✅ |
| Gemini Integration | ✅ |
| AI Features | ✅ |
| Project Audit | ⏳ |
| Refactoring | ⏳ |
| UI/UX Upgrade | ⏳ |
| Advanced Features | ⏳ |
| Deployment | ⏳ |
| Portfolio | ⏳ |

Overall Progress

**85% Complete**

---

# ✨ AI Features

| Feature | Status |
|----------|--------|
| Explain Code | ✅ |
| Bug Detection | ✅ |
| Code Optimization | ✅ |
| Generate Comments | ✅ |
| Translate Code | ✅ |
| Complexity Analysis | ✅ |
| Unit Test Generation | ✅ |

---

# 🔥 How It Works

1. User selects code on a supported website.
2. Chrome Extension captures:
   - Selected Code
   - Page Title
   - URL
   - Page Context
   - Programming Language
   - Platform
3. Data is sent to the FastAPI backend.
4. Backend builds an AI prompt.
5. Gemini generates a structured JSON response.
6. Extension displays the analysis.

---

# 🛠 Installation

## Clone Repository

```bash
git clone https://github.com/Hemant-Sharma-22/Code_Mantri.git
```

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Chrome Extension

1. Open Chrome
2. Go to `chrome://extensions`
3. Enable Developer Mode
4. Click **Load Unpacked**
5. Select the `extension` folder

---

# 📸 Screenshots

> Add screenshots here.

- Popup UI
- AI Analysis
- GitHub Analysis
- LeetCode Analysis

---

# 🚧 Upcoming Features

- Analysis History
- Export PDF
- Export Markdown
- Export JSON
- Light & Dark Theme
- Chrome Web Store Release
- Settings Page
- AI Model Selector

---

# 📈 Roadmap

- ✅ Chrome Extension
- ✅ FastAPI Backend
- ✅ Gemini AI Integration
- ✅ Seven AI Features
- 🔄 Project Audit
- 🔄 UI/UX Improvement
- 🔄 Deployment
- 🔄 Chrome Web Store

---

# 👨‍💻 Author

**Hemant Sharma**

GitHub:
https://github.com/Hemant-Sharma-22

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
