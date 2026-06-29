# 🤖 Code Matri

An AI-powered Chrome extension that helps developers analyze code from any webpage.

---

## 🚀 Project Overview

AI Code Mentor is a browser extension that can detect the current webpage, read selected code, and prepare it for AI analysis.

---

## ✅ Features Completed (Phase 1)

- Chrome Extension setup
- Popup UI
- Manifest V3 configuration
- Background script
- Content script
- Current page title detection
- Current page URL detection
- Selected code detection
- Error handling
- Project folder structure

---

## 📁 Folder Structure

```
AI-Code-Mentor/
├── backend/
├── docs/
├── extension/
├── screenshots/
├── README.md
└── .gitignore
```

---

## 🛠 Technologies Used

- JavaScript
- HTML
- CSS
- Chrome Extension Manifest V3
- Python (Backend - Phase 2)
- FastAPI (Phase 2)

---

## 📷 Screenshots

Add screenshots of:
- Extension popup
- Chrome extension page
- Project folder structure (add soon)

---

## 📌 Version

Phase 1 - Browser Extension Foundation
Version 1.0.0



# 🚀 Phase 2 - AI Backend Completed

## 📌 Overview

Phase 2 introduces a FastAPI backend with a modular architecture and Gemini AI integration. The backend receives requests from the browser extension, builds prompts, sends them to Gemini, and returns AI-generated responses.

---

## ✨ Features

- FastAPI Backend
- Google Gemini AI Integration
- Modular Project Structure
- Prompt Engine
- Explain Code
- Find Bugs
- Optimize Code
- Generate Comments
- Translate Code
- Environment Variable Support
- Automatic Retry for AI Requests
- Error Handling

---

## 🏗 Backend Structure

```
backend/
│
├── app/
│   ├── api/
│   ├── ai/
│   ├── prompts/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── tests/
├── requirements.txt
└── .env
```

---

## 🧠 AI Features

- Explain Code
- Detect Bugs
- Optimize Code
- Generate Comments
- Translate Code

---

## 🛠 Technologies Used

- Python
- FastAPI
- Google Gemini API
- Chrome Extension (Manifest V3)
- HTML
- CSS
- JavaScript
- Git & GitHub

---

## 🔐 Environment Variables

Create a `.env` file inside the backend folder.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📌 Current Progress

- ✅ Phase 1 - Browser Extension Foundation
- ✅ Phase 2 - AI Backend & Gemini Integration
- 🚧 Phase 3 - Extension ↔ Backend Communication

---

## 📷 Screenshots

Add screenshots of:

- Extension Popup
- Backend Folder Structure
- FastAPI Running
- AI Response

---
