# using dictionary

response = { "hi":"hello",
            "hii":"hello",
            "hey":"hello",
            "hello":"hello",
            "what is your name":"My name is Chatbot",
            "what can you do?" : "I can help you with a variety of things. Just tell me what you need!",
            "bye": "Goodbye!",
            "goodbye": "See you later!",
            "thanks":"You're welcome!",
            "thankyou":"You're welcome!",
            "how are you":"I am fine"
        }


print("Hello! I'm Chatbot. How can I help you today?")

i = 1
while(i == 1):
    x = input("you: ")

    if response.get(x):
        print("Chatbot: ",response[x])
    else:
        print("Chatbot: I'm sorry, I didn't understand. Can you please rephrase that?")


# using nltk library

# import nltk
# import random
# from nltk.chat.util import Chat, reflections

# # Define the patterns and responses for the chatbot
# patterns = [
#     (r"hi|hello|hey", ["Hello!", "Hi there!"]),
#     (r"what is your name?", ["My name is Chatbot. What's yours?"]),
#     (r"my name is (.*)", ["Hello, %1! How can I help you today?"]),
#     (r"what can you do?", ["I can help you with a variety of things. Just tell me what you need!"]),
#     (r"bye|goodbye", ["Goodbye!", "See you later!"]),
#     (r"thanks|thank you", ["You're welcome!", "No problem!"]),
#     (r"(.*)", ["I'm sorry, I didn't understand. Can you please rephrase that?"])
# ]

# # Create the chatbot
# chatbot = Chat(patterns, reflections)

# # Start the chatbot
# print("Hello! I'm Chatbot. How can I help you today?")
# chatbot.converse()


# # if pip not  working use command py -m pip install nltk
   