import json

def get_answer(user_message):
    with open("knowledge_base.json", "r") as file:
        data = json.load(file)

    message = user_message.lower()

    if "basic" in message:
        basic = data["pricing"]["Basic Plan"]
        return f"Basic Plan costs {basic['price']} with {basic['videos']} and {basic['resolution']} resolution."

    elif "pro" in message:
        pro = data["pricing"]["Pro Plan"]
        return f"Pro Plan costs {pro['price']} with {pro['videos']}, {pro['resolution']} resolution, and {pro['extra']}."

    elif "refund" in message:
        return data["policies"]["refund"]

    elif "support" in message:
        return data["policies"]["support"]

    else:
        return "Please ask about pricing, plans, refund policy, or support."