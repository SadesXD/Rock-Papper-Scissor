import random
import os 

options = ["rock","papper","scissor"]
pilih = random.choice(options)
enabled = True
bot = 0
me = 0

def cls():
    try:
        os.system('cls')
    except:
        os.system('clear')

def process(input):
    global me,bot
    opti = ["rock","papper","scissor"]
    opsi = random.choice(opti)
    if input.lower() == opsi:
        print(f"My Options is {opsi}\nYou're options is: {input}\nSo we are draw")
    
    if input.lower() == "rock":
        if opsi.lower() == "papper":
            cls()
            bot += 1
            print(f"My Options is {opsi}\nYou're options is: {input}\nSo i won")
        else:
            cls()
            me += 1
            print(f"My Options is {opsi}\nYou're options is: {input}\nSo You won")
    elif input.lower() == "papper":
        if opsi.lower() == "rock":
            cls()
            me += 1
            print(f"My Options is {opsi}\nYou're options is: {input}\nSo You won")
        else:
            cls()
            bot += 1
            print(f"My Options is {opsi}\nYou're options is: {input}\nSo i won")
    elif input.lower() == "scissor":
        if opsi.lower() == "rock":
            cls()
            me += 1
            print(f"My Options is {opsi}\nYou're options is: {input}\nSo You won")
        else:
            cls()
            bot += 1
            print(f"My Options is {opsi}\nYou're options is: {input}\nSo i won")
    else:
        cls()
        print(f"Can't found your selection: [ {input} ]")

def play():
    global enabled
    while enabled:
        if bot >= 5:
            cls()
            enabled = False
            print(f'Bot Score: {bot}\nYour Score: {me}\nSo i won')
        elif me >= 5:
            cls()
            enabled = False
            print(f'Bot Score: {bot}\nYour Score: {me}\nSo You won')
        else:
            print(f"\n[ Score ]\nYour Score: {me}, Bot Score: {bot}\n")
            main = input("[!]Type your selection [ Rock, Papper, Scissor ]: ")
            process(main)

def menu():
    cls()
    teks = '[ Rock, Papper, Scissor ]\n\n-type [ PLAY ] for playing a games\n-type [ INFO ] for show information about RPS games\n-type [ EXIT ] for exit the program\n'
    print(teks)
    opt = input("Select Your Options: ")
    if opt.lower() == "play":
        cls()
        enabled = True
        play()
    elif opt.lower() == "info":
        cls()
        info = '[ Rock, Papper, Scissor ]\n\n-Github URL: https://github.com/SadesXD/Rock-Papper-Scissor\n-Join Discord: https://discord.gg/FGsTcss'
        print(info)
        back()
    elif opt.lower() == "exit":
        quit()
    else:
        cls()
        print("[!] Can't found your selection\n")
        back()

def back():
    teks = "\n-type [ BACK ] for back to main menu\n-type [ EXIT ] for exit the program\n"
    print(teks)
    ok = input("Type your selection: ")
    if ok.lower() == "back":
        menu()
    elif ok.lower() == "exit":
        quit()
    else:
        cls()
        print("[!] Can't find your selection\n")
        back()

menu()