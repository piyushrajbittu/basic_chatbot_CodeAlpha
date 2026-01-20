def chatbot():
    print("🤖 Chatbot: Hey there! I'm ChatPy 😄")
    print("🤖 Chatbot: You can say 'hello', 'how are you', 'help', or 'bye'")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hello! Nice to meet you 😊")

        elif user_input == "how are you":
            print("🤖 Chatbot: I'm doing great! Thanks for asking 🌟")

        elif user_input == "help":
            print("🤖 Chatbot: Try typing 'hello', 'how are you', or 'bye' 👍")

        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a wonderful day 👋✨")
            break

        else:
            print("🤖 Chatbot: Hmm 🤔 I don't understand that yet.")

# Start the chatbot
chatbot()