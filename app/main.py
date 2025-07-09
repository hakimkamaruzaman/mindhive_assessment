# app/main.py

from app.chatbot.chatbot_agent import create_chatbot

def main():
    print("Agentic Planner Bot is running. Type 'exit' to quit.\n")
    bot = create_chatbot()
    context = {}

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        print(f"[DEBUG] User said: {user_input}")
        response = bot.invoke({"input": user_input, "context": context})

        # Save intent in context
        context["last_user_input"] = user_input
        context["last_intent"] = response.additional_kwargs.get("intent", None)

        print(f"Bot: {response.content}")

if __name__ == "__main__":
    main()
