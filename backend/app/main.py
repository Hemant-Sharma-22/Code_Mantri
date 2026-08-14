from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.analyze import router as analyze_router
from app.api.bugs import router as bugs_router
from app.api.optimize import router as optimize_router
from app.api.comments import router as comments_router
from app.api.translate import router as translate_router
from app.api.complexity import router as complexity_router
from app.api.tests import router as tests_router
from app.api.generate import router as generate_router

app = FastAPI(
    title="AI Code Mentor API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router)
app.include_router(bugs_router)
app.include_router(optimize_router)
app.include_router(comments_router)
app.include_router(translate_router)
app.include_router(complexity_router)
app.include_router(tests_router)
app.include_router(generate_router)


@app.get("/", response_class=HTMLResponse)
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🤖 AI Code Mentor - Live Backend & Extension Launcher</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #090d16;
            --card-bg: rgba(18, 24, 38, 0.75);
            --border-color: rgba(255, 255, 255, 0.1);
            --primary-glow: #6366f1;
            --accent-glow: #a855f7;
            --cyan-glow: #06b6d4;
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 15% 20%, rgba(99, 102, 241, 0.18) 0%, transparent 45%),
                radial-gradient(circle at 85% 80%, rgba(168, 85, 247, 0.18) 0%, transparent 45%);
        }

        .container {
            width: 90%;
            max-width: 900px;
            margin: 40px auto;
            text-align: center;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.3);
            color: #34d399;
            padding: 6px 16px;
            border-radius: 9999px;
            font-size: 0.9rem;
            font-weight: 500;
            margin-bottom: 24px;
        }

        .badge-dot {
            width: 8px;
            height: 8px;
            background-color: #34d399;
            border-radius: 50%;
            box-shadow: 0 0 10px #34d399;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
        }

        h1 {
            font-size: 3rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 50%, #c084fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 16px;
        }

        p.subtitle {
            font-size: 1.2rem;
            color: var(--text-muted);
            max-width: 650px;
            margin: 0 auto 32px;
            line-height: 1.6;
        }

        .actions {
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            justify-content: center;
            margin-bottom: 48px;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 14px 28px;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.25s ease;
        }

        .btn-primary {
            background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
            color: #ffffff;
            box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
            border: none;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(168, 85, 247, 0.5);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.05);
            color: var(--text-main);
            border: 1px solid var(--border-color);
            backdrop-filter: blur(10px);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
            border-color: rgba(255, 255, 255, 0.25);
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 20px;
            text-align: left;
        }

        .card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            backdrop-filter: blur(12px);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .card:hover {
            transform: translateY(-4px);
            border-color: rgba(99, 102, 241, 0.4);
        }

        .card-icon {
            font-size: 2rem;
            margin-bottom: 12px;
        }

        .card h3 {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 8px;
            color: #f3f4f6;
        }

        .card p {
            font-size: 0.9rem;
            color: var(--text-muted);
            line-height: 1.5;
        }

        /* Modal Popup Styling */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(5, 7, 13, 0.75);
            backdrop-filter: blur(12px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }

        .modal-overlay.active {
            opacity: 1;
            pointer-events: auto;
        }

        .modal-box {
            background: #111827;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            width: 90%;
            max-width: 580px;
            padding: 32px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
            transform: scale(0.9);
            transition: transform 0.3s ease;
            position: relative;
            text-align: left;
        }

        .modal-overlay.active .modal-box {
            transform: scale(1);
        }

        .modal-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .modal-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .close-btn {
            background: rgba(255, 255, 255, 0.08);
            border: none;
            color: #9ca3af;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-size: 1.2rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }

        .close-btn:hover {
            background: rgba(255, 255, 255, 0.2);
            color: #fff;
        }

        .steps-list {
            display: flex;
            flex-direction: column;
            gap: 16px;
            margin-bottom: 24px;
        }

        .step-item {
            display: flex;
            gap: 14px;
            align-items: flex-start;
        }

        .step-num {
            background: linear-gradient(135deg, #6366f1, #a855f7);
            color: #fff;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 0.85rem;
            flex-shrink: 0;
            margin-top: 2px;
        }

        .step-content h4 {
            font-size: 0.95rem;
            font-weight: 600;
            color: #f3f4f6;
            margin-bottom: 4px;
        }

        .step-content p {
            font-size: 0.85rem;
            color: #9ca3af;
            line-height: 1.4;
        }

        code {
            font-family: 'Fira Code', monospace;
            background: rgba(255, 255, 255, 0.08);
            color: #a5b4fc;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.82rem;
        }

        .modal-footer {
            display: flex;
            gap: 12px;
            justify-content: flex-end;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 20px;
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="badge">
            <span class="badge-dot"></span> AI Code Mentor Backend Active
        </div>

        <h1>AI Code Mentor</h1>
        <p class="subtitle">Elevate your coding experience on GitHub, LeetCode, GeeksforGeeks, and CodeChef with AI-driven explanations, bug detection, and code optimization.</p>

        <div class="actions">
            <button class="btn btn-primary" onclick="openModal()">
                🚀 Start Extension
            </button>
            <a href="/docs" class="btn btn-secondary" target="_blank">
                📚 API Swagger Docs
            </a>
            <a href="https://github.com/Hemant-Sharma-22/Code_Mantri" class="btn btn-secondary" target="_blank">
                🐙 GitHub Repo
            </a>
        </div>

        <div class="features-grid">
            <div class="card">
                <div class="card-icon">📖</div>
                <h3>Explain Code</h3>
                <p>Instant logic breakdown, step-by-step analysis, and complexity breakdown.</p>
            </div>
            <div class="card">
                <div class="card-icon">🐞</div>
                <h3>Find Bugs</h3>
                <p>Locate subtle logical errors, edge case failures, and security vulnerabilities.</p>
            </div>
            <div class="card">
                <div class="card-icon">⚡</div>
                <h3>Optimize Code</h3>
                <p>Transform brute-force code into optimal time and space complexity solutions.</p>
            </div>
            <div class="card">
                <div class="card-icon">💡</div>
                <h3>Solve Problems</h3>
                <p>Generates Brute Force, Better, and Optimal solutions with interview guidance.</p>
            </div>
        </div>
    </div>

    <!-- Interactive Extension Launcher Modal -->
    <div class="modal-overlay" id="popupModal">
        <div class="modal-box">
            <div class="modal-header">
                <div class="modal-title">
                    <span>🧩</span> How to Launch AI Code Mentor
                </div>
                <button class="close-btn" onclick="closeModal()">&times;</button>
            </div>
            
            <div class="steps-list">
                <div class="step-item">
                    <div class="step-num">1</div>
                    <div class="step-content">
                        <h4>Download Extension Source</h4>
                        <p>Clone or download the repository from GitHub into your local folder.</p>
                    </div>
                </div>

                <div class="step-item">
                    <div class="step-num">2</div>
                    <div class="step-content">
                        <h4>Open Chrome Extensions Page</h4>
                        <p>In Chrome browser, navigate to <code>chrome://extensions</code></p>
                    </div>
                </div>

                <div class="step-item">
                    <div class="step-num">3</div>
                    <div class="step-content">
                        <h4>Enable Developer Mode & Load</h4>
                        <p>Toggle <strong>Developer mode</strong> in top-right corner & click <strong>Load unpacked</strong>. Select the <code>extension/</code> folder.</p>
                    </div>
                </div>

                <div class="step-item">
                    <div class="step-num">4</div>
                    <div class="step-content">
                        <h4>Ready to Use!</h4>
                        <p>Open GitHub, LeetCode, or GeeksforGeeks, highlight any code, and click the AI Code Mentor extension icon!</p>
                    </div>
                </div>
            </div>

            <div class="modal-footer">
                <a href="https://github.com/Hemant-Sharma-22/Code_Mantri" target="_blank" class="btn btn-primary" style="padding: 10px 20px; font-size: 0.9rem;">
                    📥 Download Project
                </a>
                <button class="btn btn-secondary" onclick="closeModal()" style="padding: 10px 20px; font-size: 0.9rem;">
                    Got It!
                </button>
            </div>
        </div>
    </div>

    <script>
        function openModal() {
            document.getElementById('popupModal').classList.add('active');
        }

        function closeModal() {
            document.getElementById('popupModal').classList.remove('active');
        }

        // Auto-open modal popup when user visits the site
        window.addEventListener('DOMContentLoaded', () => {
            setTimeout(() => {
                openModal();
            }, 400);
        });

        // Close modal when clicking outside box
        document.getElementById('popupModal').addEventListener('click', (e) => {
            if (e.target === document.getElementById('popupModal')) {
                closeModal();
            }
        });
    </script>
</body>
</html>"""


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }