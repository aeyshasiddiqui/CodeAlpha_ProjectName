print("🤖 Welcome to the Basic Chatbot!")
print("Type 'bye' anytime to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm fine, thanks! How about you?")

    elif user == "what is your name":
        print("Bot: I am a simple Python chatbot.")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")