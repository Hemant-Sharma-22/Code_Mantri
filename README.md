# 🤖 AI Code Mentor

> An AI-powered Chrome Extension that analyzes code directly from websites like GitHub, LeetCode, CodeChef, and more using Google's Gemini AI.

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/Python-FastAPI-green)
![JavaScript](https://img.shields.io/badge/JavaScript-Chrome%20Extension-yellow)
![Gemini](https://img.shields.io/badge/AI-Gemini-red)

---

## 🚀 Features

- 🧠 Explain Code
- 🐞 Find Bugs
- ⚡ Optimize Code
- 💬 Generate Comments
- 🌍 Translate Code
- 📊 Time Complexity Analysis
- 💾 Space Complexity Analysis
- 🔍 Platform Detection
- 💻 Language Detection
- 📄 Page Context Analysis

---

# 🏗 Architecture

```
Chrome Extension
        │
        ▼
Content Script
        │
        ▼
Background Script
        │
        ▼
FastAPI Backend
        │
        ▼
Prompt Engine
        │
        ▼
Gemini API
        │
        ▼
Structured JSON
        │
        ▼
Popup UI
```

---

# 🛠 Tech Stack

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

# 📂 Folder Structure

```
AI-Code-Mentor
│
├── backend
│   ├── app
│   │   ├── ai
│   │   ├── api
│   │   ├── prompts
│   │   ├── schemas
│   │   ├── services
│   │   ├── utils
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── extension
│   ├── popup
│   ├── background
│   ├── content
│   ├── assets
│   ├── styles
│   └── manifest.json
│
└── README.md
```

---

# 📸 Screenshots

## 🖥 Extension Interface

![Extension UI](screenshots/extension-home.png)

---

## 📄 Code Selection

![Code Selection](screenshots/code-selection.png)

---

## ⚙ Backend API

![Swagger](screenshots/swagger-api.png)

---

## 🚀 Backend Running

![Backend](screenshots/backend-running.png)

---

## 🤖 AI JSON Response

![AI Response](screenshots/ai-response.png)

---

# 🚀 Current Progress

| Phase | Status |
|---------|---------|
| Project Foundation | ✅ |
| Extension UI | 🟡 |
| Code Extraction | ✅ |
| Backend | ✅ |
| Gemini Integration | ✅ |
| AI Features | ✅ |
| Project Audit | ⏳ |
| Refactoring | ⏳ |
| UI/UX | ⏳ |
| Deployment | ⏳ |

### Overall Progress

████████▌░░ **85%**

---

# ⚡ AI Features

| Feature | Status |
|-----------|---------|
| Explain Code | ✅ |
| Find Bugs | ✅ |
| Optimize Code | ✅ |
| Generate Comments | ✅ |
| Translate Code | ✅ |
| Complexity Analysis | ✅ |
| Platform Detection | ✅ |
| Language Detection | ✅ |

---

# 🔄 Workflow

```
User selects code

        │

        ▼

Chrome Extension

        │

        ▼

FastAPI Backend

        │

        ▼

Prompt Engine

        │

        ▼

Gemini AI

        │

        ▼

JSON Response

        │

        ▼

Beautiful Analysis UI
```

---

# ⚙ Installation

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

2. Go to

```
chrome://extensions
```

3. Enable Developer Mode

4. Click

```
Load Unpacked
```

5. Select

```
extension/
```

---

# 📅 Upcoming

- Better UI
- Dark / Light Theme
- Export PDF
- Export Markdown
- Analysis History
- Settings Page
- Chrome Web Store Deployment

---

# 👨‍💻 Author

**Hemant Sharma**

GitHub

https://github.com/Hemant-Sharma-22

---

# ⭐ Star this Repository

If you like this project, consider giving it a ⭐ on GitHub.
