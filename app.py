from agent_graph import graph

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    result = graph.invoke({
        "user_input": user_input
    })

    print("Agent:", result["response"])