def detect_intent(user_message):
    message = user_message.lower()

    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    inquiry_words = [
        "price", "pricing", "plan", "plans",
        "feature", "features", "cost",
        "refund", "support"
    ]
    high_intent_words = [
        "buy", "signup", "sign up",
        "subscribe", "purchase",
        "want pro", "i want"
    ]

    # Greeting check
    for word in greetings:
        if word in message:
            return "greeting"

    # High-intent check
    for word in high_intent_words:
        if word in message:
            return "high_intent"

    # Inquiry check
    for word in inquiry_words:
        if word in message:
            return "inquiry"

    return "unknown"