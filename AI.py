print("FreakAI: Hello, I am FreakAI!")
def ask():
    global message
    message = input("")
ask()
while True:
    if (message == "Are you freaky?"):
        print("FreakAI: Yes, I am freaky, as I am a large language model from Freakybob Team.")
        ask()
    if (message == "boom" or "Boom"):
        print("FreakAI: No more Malaysia")
        ask()
    if (message == "freaky" or "Freaky"):
        print("I'm currently with your mother.")
        ask()
    else:
        print("FreakAI: I'm sorry, but I do not understand what you are saying. Try again later!")
        ask()