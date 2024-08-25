from ChatBot import ChatBot, GenAIEkception
from dotenv import load_dotenv
import os
import sys


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get the API key from environment variables
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise GenAIEkception("API key not found in environment variables")

    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()

    print(f"Welcome to {chatbot.CHATBOT_NAME}! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            sys.exit("Exiting...")
        try:
    a        response = chatbot.send_prompt(user_input)  # Corrected method name
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except GenAIEkception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
