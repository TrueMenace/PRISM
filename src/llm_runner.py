"""
LLM Runner
Uses Gemini 2.5 Flash to generate final AI explanation
"""

import os
from dotenv import load_dotenv
from agent_explain import explain
from google import genai

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

# -----------------------------
# Initialize Gemini Client
# -----------------------------
client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash"

def fallback_response(prompt: str) -> str:
    """
    Fallback response when Gemini API is unavailable.
    Ensures system never crashes.
    """
    return (
        "⚠️ Gemini is temporarily unavailable.\n\n"
        "Here is the retrieved explanation based on trusted context:\n\n"
        f"{prompt}"
    )

# -----------------------------
# Call LLM
# -----------------------------
def call_llm(prompt: str) -> str:
    try:
        print("🚀 Calling Gemini LLM...")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("✅ LLM called successfully")
        return response.text

    except Exception as e:
        print("⚠️ Gemini temporarily unavailable.")
        print(f"⚠️ Reason: {e}")

        return fallback_response(prompt)



# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    query = "How do habits become part of identity?"

    print("\n🔍 User Query:")
    print(query)

    agent_prompt = explain(query)

    print("\n🧠 Agent Generated Prompt:")
    print(agent_prompt)

    final_answer = call_llm(agent_prompt)

    print("\n🤖 Final AI Explanation:")
    print(final_answer)
