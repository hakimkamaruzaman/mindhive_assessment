import requests

def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif "thank" in user_input:
        return "thanks"
    elif any(word in user_input for word in ["price", "cost", "color", "material", "capacity", "size"]):
        return "product_info"
    elif any(op in user_input for op in ["+", "-", "*", "/"]):
        return "calculate"
    elif "outlet" in user_input or "petaling jaya" in user_input:
        return "find_outlet"
    elif "ss2" in user_input or "ss 2" in user_input:
        return "outlet_detail"
    else:
        return "unknown"

def plan_response(intent, user_input, context):
    if intent == "greeting":
        return "Hello! How can I help you today?"
    elif intent == "thanks":
        return "You're welcome!"
    elif intent == "calculate":
        try:
            response = requests.get("http://127.0.0.1:8000/calculate", params={"expression": user_input})
            return response.json().get("result", "Calculation error.")
        except Exception:
            return "Something went wrong."
    elif intent == "find_outlet":
        return "Which outlet are you referring to?"
    elif intent == "product_info":
        try:
            response = requests.get("http://127.0.0.1:8000/product_info", params={"query": user_input})
            return response.json().get("result", "Product not found.")
        except Exception:
            return "Something went wrong."
    elif intent == "unknown":
        # Use context to resolve ambiguous replies
        if context.get("last_intent") == "find_outlet":
            outlet = user_input.strip().lower().replace(" ", "")
            if outlet in ["ss2", "ss 2"]:
                return "Thanks! The SS 2 outlet opens at 9:00AM."
            else:
                return f"Sorry, I couldn't find the outlet '{user_input}'."
    elif intent == "outlet_detail":
        return "Thanks! The SS 2 outlet opens at 9:00AM."
        
    return "Sorry, I didn't understand that."
