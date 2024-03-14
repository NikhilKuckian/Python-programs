import os
print("Welcome to Robo Speaker - Text to Speech")
while True:
    x=input("What do you want me to say?")
    if x == "quit":
        print("Exiting loop")
        break
    else:
        command = f"say {x}"
        os.system(command)
os.system("say -v {voice} Bye Bye Friend")