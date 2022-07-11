import os
from chatterbot import ChatBot
chatbot = ChatBot("Chappie")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there! My name is Chappie.",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)


while True:
    question = input("You: ")
    response = chatbot.get_response(question)
    if float(response.confidence) > 0.5:
        print('Chappie: ',response)
    else:
        print('Chappie: I still dont know how to answer this question')