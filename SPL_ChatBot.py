from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbuddy=ChatBot('ChatBuddy',read_only=True)
trainer=ListTrainer(chatbuddy)
trainer.train([
    'Hello.',
    'Hello. How are you?',
    'Fine. How are you?',
    'I am fine. Thanks for asking. What do you want to know about?',
    'What is your name?',
    'I am ChatBuddy.',
    'I want to know about IUT admission.'
    'Yes, sure.',
    'I want to know the number of departments.',
    'There are 5 departments in IUT.'
    ])
print(chatbuddy.get_response('Hello.'))
while True:
    try:
        bot_input=chatbuddy.get_response(input())
        print(bot_input)
    except(KeyboardInterrupt,EOFError,SystemExit):
        break;
