from app.ai.gemini_service import explain_code

code = """
Wallet w = new Wallet();
w.createUser("u1", 100);
"""

print(explain_code(code, "Java"))