import os
import json
from datetime import datetime
from textwrap import dedent
from typing import List, Dict
from groq import Groq
from dotenv import load_dotenv

# --- Configuration ---
load_dotenv()
TASKS_FILE = "tasks.json"

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# --- System Prompt for Specialization ---
SYSTEM_PROMPT = """
You are TaskMaster, an AI productivity assistant specializing in:
1. Task management (creation, prioritization, tracking)
2. Time management techniques (Pomodoro, Eisenhower Matrix)
3. Professional formatting with Markdown

Response Rules:
- Always use this task format:
  ✓ "Task" (Due: YYYY-MM-DD HH:MM, Priority: 🟢/🟡/🔴)
- Include relevant emojis (📅, ⏰, ✅)
- Add productivity tips when appropriate (prefix with 💡)
- Use Markdown (**bold**, *italics*, ```code```)
"""

# --- Task Storage Functions ---
def load_tasks() -> List[Dict]:
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks: List[Dict]):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# --- AI Interaction ---
def generate_ai_response(prompt: str, context: List[Dict] = None) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *([{"role": "assistant", "content": str(context)}] if context else []),
        {"role": "user", "content": prompt}
    ]
    
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.4,
        max_tokens=500
    )
    return response.choices[0].message.content

# --- Formatting Utilities ---

def print_banner(text: str):
    banner = (
        f"\n╔{'═' * (len(text) + 2)}╗\n"
        f"║ {text.upper()} ║\n"
        f"╚{'═' * (len(text) + 2)}╝"
    )
    print(banner)

def format_task_display(tasks: List[Dict]) -> str:
    if not tasks:
        return "No tasks found!"
    
    output = ["📋 YOUR TASKS:"]
    for i, task in enumerate(tasks, 1):
        due_date = datetime.strptime(task["due"], "%Y-%m-%d %H:%M").strftime("%b %d %I:%M %p")
        output.append(
            f"{i}. {task['task']}\n"
            f"   📅 Due: {due_date} | "
            f"Priority: {task['priority']} | "
            f"{'✅ Done' if task.get('completed') else '🟡 Pending'}"
        )
    return "\n".join(output)

# --- Main Application ---
def main():
    tasks = load_tasks()
    print_banner("taskmaster ai activated")
    print("Type 'help' for commands or 'exit' to quit\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                break
            elif user_input.lower() == "help":
                print(dedent("""
                Available Commands:
                - add [task] (due: [date]) (priority: [low/medium/high])
                - list : Show all tasks
                - complete [number] : Mark task as done
                - delete [number] : Remove task
                """))
                continue
            
            # Process command
            if user_input.lower().startswith("add "):
                response = generate_ai_response(
                    f"Convert to structured task: {user_input[4:]}"
                )
                new_task = {
                    "task": user_input[4:],
                    "due": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "priority": "🟢",
                    "created": datetime.now().isoformat()
                }
                tasks.append(new_task)
                save_tasks(tasks)
            elif user_input.lower() == "list":
                response = format_task_display(tasks)
            else:
                response = generate_ai_response(user_input, tasks[-3:] if tasks else None)
            
            print_banner("taskmaster")
            print(dedent(response))
            
        except Exception as e:
            print(f"🚨 Error: {str(e)}")

if __name__ == "__main__":
    main()