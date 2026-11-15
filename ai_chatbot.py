
# Simple AI Chatbot - Beginner Project

def chatbot():
    print("AI Chatbot: Hello! I am your beginner AI assistant.")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "exit":
            print("Bot: Goodbye! Have a great day!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I help you?")

        elif "name" in user_input:
            print("Bot: I am a Python-based chatbot.")

        elif "ai" in user_input:
            print("Bot: AI stands for Artificial Intelligence.")

        elif "machine learning" in user_input:
            print("Bot: Machine learning helps computers learn from data.")

        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking.")

        else:
            print("Bot: Interesting! Tell me more.")

if __name__ == "__main__":
    chatbot()
  
