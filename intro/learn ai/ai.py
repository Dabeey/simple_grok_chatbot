from groq import Groq  
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROK_API_KEY"))

def chat_with_llama(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",  # Free & fast
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
if __name__ == "__main__":
    while True:
        print("Welcome to the AI Chatbot! Type 'exit' to quit.")
        user_input = input('Your input here: ')
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Exiting...")
            break
        response = chat_with_llama(user_input)
        if response:
            print('AI: ', response)
        else:
            print('AI: No response received.')