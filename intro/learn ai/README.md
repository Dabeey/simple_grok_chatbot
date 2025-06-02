# AIChatbot

![GROQ AI CHATBOT! Banner](img/banner.png)

AIChatbot is a command-line conversational assistant powered by Groq's Llama 3 model. It enables natural language conversations, answers questions, and provides helpful responses—all with a simple and interactive interface.

## Features

- **Conversational AI:** Chat with an advanced language model in real time.
- **Customizable Exit Commands:** Easily end your session with commands like `exit`, `quit`, or `bye`.
- **Error Handling:** Graceful handling of API and environment errors.
- **Environment-Based Configuration:** Securely load your API key from a `.env` file.

## Setup

1. **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd FASTAPI LEARNING/intro/learn ai
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set your Groq API key:**
    - Create a `.env` file in the project directory:
        ```
        GROQ_API_KEY=your_groq_api_key_here
        ```

## Usage

Run the chatbot from the terminal:

```sh
python ai.py
```

### How It Works

- Type your message and press Enter to chat with the AI.
- To end the session, type `exit`, `quit`, or `bye`.
- If the AI cannot generate a response, you'll see an error message.

## Example

```
You: Hello, who are you?
AI: Hello! I'm an AI assistant powered by Groq's Llama 3 model. How can I help you today?

You: Tell me a productivity tip.
AI: 💡 Try the Pomodoro Technique: work for 25 minutes, then take a 5-minute break to boost your focus!

You: exit
🛑 Session ended
```

## Notes

- Requires a valid [Groq API key](https://console.groq.com/).
- The `.env` file must be in the same directory as `ai.py`.

## License

MIT License