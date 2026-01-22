import os
import google.generativeai as genai


# -----------------------------
# Configure Gemini
# -----------------------------
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

MODEL_NAME = "gemini-2.5-flash"
model = genai.GenerativeModel(MODEL_NAME)


def run_llm(prompt: str) -> str:
    """
    Sends the agent-generated prompt to Gemini
    and returns a natural language explanation.
    """
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 500,
        }
    )

    return response.text
