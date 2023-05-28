def greet():
    print("Chatbot: Hello! How can I assist you today?")


def goodbye():
    print("Chatbot: Thank you for chatting with me. Goodbye!")


def process_input(user_input):
    if user_input.lower() == "hello":
        print("Chatbot: Hi there!")
    elif user_input.lower() == "help":
        print("Chatbot: I'm here to help you. How can I assist you?")
    elif user_input.lower() == "who is our pm?":
        print("Chatbot: Narendra Damodardas Modi")
    elif user_input.lower() == "bye":
        goodbye()
        return True
    else:
        print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?")


def start_chat():
    greet()
    while True:
        user_input = input("User: ")
        should_exit = process_input(user_input)
        if should_exit:
            break


# Start the chatbot
start_chat()
