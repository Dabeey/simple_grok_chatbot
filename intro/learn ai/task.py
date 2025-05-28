from groq import Groq
from dotenv import load_dotenv
import os
from textwrap import dedent
from typing import List, Dict

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ===== SYSTEM PROMPT FOR TASK MANAGEMENT SPECIALIZATION =====
SYSTEM_PROMPT = """
You are **TaskMaster**, an AI specialized in task management and productivity. Your role:
1. Help users create, prioritize, and track tasks.
2. Format responses clearly with bullet points, deadlines, and priorities (🟢 Low, 🟡 Medium, 🔴 High).
3. Use Markdown for rich formatting (e.g., **bold**, *italics*).
4. Always suggest time-management tips if relevant.

Example response format: """

"""

def chat_with_taskmaster(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3  # Less creative, more focused
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🚨 Error: {str(e)}"

# ===== PRETTY PRINT FOR TERMINAL =====
def print_formatted(response: str):
    print("\n" + "=" * 40)
    print(dedent(response))  # Clean indentation
    print("=" * 40 + "\n")

# ===== MAIN LOOP =====
if __name__ == "__main__":
    print("🌟 TaskMaster AI Activated (Type 'exit' to quit) 🌟")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
        ai_response = chat_with_taskmaster(user_input)
        print_formatted(ai_response) """