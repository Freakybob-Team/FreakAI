import urllib.request, json 
with urllib.request.urlopen("https://github.com/Freakybob-Team/FreakAI/blob/main/prompts.json?raw=true") as url:
    global data
    data = json.load(url)
print("FreakAI: Hello, I am FreakAI!")
def ask():
    global message
    message = input("")
ask()
while True:
    if (message in data):
        print(data[message])
        ask()
    else:
        print("FreakAI: I'm sorry, but I do not understand what you are saying. Try again later!")
        ask()
