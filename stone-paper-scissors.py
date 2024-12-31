import random,os,time
from termcolor import colored

def line():
    print("============================================================")

stone = ["    _______    ",
        "---'   ____)   ",
        "    (______)   ",
        "    (______)   ",
        "    (______)   ",
        "---.__(___)    "]
paper =["    _______    ",
        "---'    ___)__ ",
        "        ______)",
        "       _______)",
        "       _______)",
        "---._________) "]
scissors =["    ______     ",
           "---'   ___)___ ",
           "        ______)",
           "    __________)",
           "    (_____)    ",
           "---.__(___)    "]

choices = [stone,paper,scissors]

def rev(choice):
    obj = choice[:]
    reversed_obj = []
    
    for line in obj:
        reversed_line = ""
        for j in range(len(line) - 1, -1, -1):
            char = line[j]
            if char == '(':
                reversed_line += ')'
            elif char == ')':
                reversed_line += '('
            else:
                reversed_line += char 
        reversed_obj.append(reversed_line)
    return reversed_obj

def move(choice,steps,rev=False):
    obj = choice[:]
    for i in range(0,len(obj)):
        for j in range(0,steps):
            if i==1 or i==len(obj)-1:
                if rev:
                    obj[i] = obj[i] + "-"
                else:
                    obj[i] = "-" + obj[i]
            else:
                if rev:
                    obj[i] = obj[i] + " "
                else:
                    obj[i] = " " + obj[i]
    return obj

line()
print("\tRULES")
print("1. Press",colored("0","red",attrs=['bold']),"for",colored("stone","red",attrs=['bold']))
print("2. Press",colored("1","red",attrs=['bold']),"for",colored("paper","red",attrs=['bold']))
print("3. Press",colored("2","red",attrs=['bold']),"for",colored("scissors","red",attrs=['bold']))
line()

time.sleep(3)
os.system("cls")

line()
user = int(input("Enter your input... "))
userChoice = choices[user]
robo = random.randint(0,2)
roboChoice = rev(choices[robo])

for i in range(0,6):
    print(userChoice[i],"\t\t",roboChoice[i])

if user == robo:
    print("\n\t\t",colored("MATCH TIE !!!","red",attrs=['bold','underline']))
elif (user == 0 and robo == 2) or (user == 1 and robo == 0) or (user == 2 and robo == 1):
    print("\n\t\t",colored("YOU WON !!!","red",attrs=['bold','underline']))
else:
    print("\n\t\t",colored("ROBO WON !!!","red",attrs=['bold','underline']))
line()

newstone=stone[:]

for i in range(0,8):
    for j in range(0,6):
        newstone = move(newstone,1)
        print(newstone[j])
    # time.sleep(1)
    # os.system('cls')
