import urllib.request, json 
data = ""
print("Use prompts.json from internet (may be out of date)?")
h = input("Y/N: ")
if (h == "Y" or "Y"):
    with urllib.request.urlopen("https://github.com/Freakybob-Team/FreakAI/blob/main/prompts.json?raw=true") as url:
        data = json.load(url)
else:
    data = json.load("prompts.json")
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
