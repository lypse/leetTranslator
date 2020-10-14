#!/usr/bin/python3

def translate(userText):
    inputText  = 'aAiIoOsSeEbBtTlL'
    outputLeet = '4411005533887711'

    conversion = userText.maketrans(inputText, outputLeet)

    return userText.translate(conversion)

print(translate(str(input('Insert your text: '))))
