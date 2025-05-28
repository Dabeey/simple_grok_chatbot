import os
from typing import Optional
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class AIChatbot:
    def __init__(self):
        self.client = Groq(api_key=self._get_api_key())
        self.model = "llama3-70b-8192"  # Or "mixtral-8x7b-32768"
        self.exit_commands = ["exit", "quit", "bye"]

    def _get_api_key(self) -> str:
        """Load API key from environment variables with validation."""
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file")
        return api_key

    def get_ai_response(self, prompt: str) -> Optional[str]:
        """Get AI response with error handling."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7  # Balance creativity vs focus
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"⚠️  Error: {str(e)}")
            return None

    def run(self):
        """Main chat loop."""
        print("\n" + "=" * 40)
        print("🌟 AI Chatbot Activated".center(40))
        print("Type 'exit' to quit".center(40))
        print("=" * 40 + "\n")

        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue
                    
                if user_input.lower() in self.exit_commands:
                    print("\n🛑 Session ended")
                    break

                if response := self.get_ai_response(user_input):
                    print(f"\nAI: {response}\n")
                else:
                    print("AI: ❌ Failed to generate response")

            except KeyboardInterrupt:
                print("\n🛑 Session interrupted")
                break

if __name__ == "__main__":
    chatbot = AIChatbot()
    chatbot.run()