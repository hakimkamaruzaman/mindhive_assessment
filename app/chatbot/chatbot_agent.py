from langchain_core.runnables import RunnableLambda
from langchain_core.messages import AIMessage

from app.planner.planner import detect_intent, plan_response
import requests


def create_chatbot():
    def _chat_logic(inputs):
        user_input = inputs["input"]
        context = inputs.get("context", {})

        print(f"[DEBUG] User said: {user_input}")
        intent = detect_intent(user_input)
        print(f"[DEBUG] Detected intent: {intent}")

        if intent == "product_info":
            try:
                r = requests.get("http://127.0.0.1:8000/product_info", params={"query": user_input})
                if r.status_code == 200:
                    return AIMessage(content=r.json()["result"])
                else:
                    return AIMessage(content="Product not found.")
            except Exception as e:
                print(f"[ERROR] Product info error: {e}")
                return AIMessage(content="Something went wrong while fetching product info.")

        elif intent == "calculate":
            try:
                r = requests.get("http://127.0.0.1:8000/calculate", params={"expression": user_input})
                if r.status_code == 200:
                    return AIMessage(content=f"The result is {r.json()['result']}")
                else:
                    return AIMessage(content="Invalid calculation.")
            except Exception as e:
                print(f"[ERROR] Calculation error: {e}")
                return AIMessage(content="Something went wrong while calculating.")

        else:
            message = plan_response(intent, user_input, context)
            return AIMessage(content=message)

    return RunnableLambda(_chat_logic)
