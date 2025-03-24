import random, os, time
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

choices = [stone, paper, scissors]

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

def move(choice, steps, rev=False):
    obj = choice[:]
    for i in range(len(obj)):
        for _ in range(steps):
            if i == 1 or i == len(obj)-1:
                if rev:
                    obj[i] += "-"
                else:
                    obj[i] = "-" + obj[i]
            else:
                if rev:
                    obj[i] += " "
                else:
                    obj[i] = " " + obj[i]
    return obj

line()
print("\tRULES")
print("1. Press", colored("0", "red", attrs=['bold']), "for", colored("stone", "red", attrs=['bold']))
print("2. Press", colored("1", "red", attrs=['bold']), "for", colored("paper", "red", attrs=['bold']))
print("3. Press", colored("2", "red", attrs=['bold']), "for", colored("scissors", "red", attrs=['bold']))
line()

time.sleep(3)
os.system("cls")

line()
user = int(input("Enter your input... "))
if user not in [0,1,2]:
    print(colored("Invalid input! Using default choice (Stone)", "red"))
    user = 0
    time.sleep(1)
userChoice = choices[user]
robo = random.randint(0, 2)
roboChoice = rev(choices[robo])

for i in range(0,6):
    print(userChoice[i], "\t\t", roboChoice[i])

won = None

# Animation part
def animate(won):
    max_width = 54  # Total terminal width to maintain
    
    if won == "Robo":
        for i in range(0, 12):
            frame_lines = []
            for j in range(0, 6):
                user_line = userChoice[j]
                robo_line = move(roboChoice, i, True)[j]
                
                # Calculate dynamic spacing
                spacing = max(0, max_width - len(user_line) - len(robo_line))
                
                # Combine into one line
                combined = user_line + " " * spacing + robo_line
                frame_lines.append(combined)
            
            print('\n'.join(frame_lines))
            time.sleep(0.1)
            os.system("cls")
        print("\n".join(frame_lines))
    
    elif won == "User":
        for i in range(0, 20):
            frame_lines = []
            for j in range(0, 6):
                moved_user_line = move(userChoice, i)[j]
                robo_line = roboChoice[j]
                spacing = max(0, max_width - len(moved_user_line) - len(robo_line))
                combined = moved_user_line + " " * spacing + robo_line
                frame_lines.append(combined)
            
            print('\n'.join(frame_lines))
            time.sleep(0.1)
            os.system("cls")
        print("\n".join(frame_lines))

if user == robo:
    animate(won)
    print("\n\t\t", colored("MATCH TIE !!!", "red", attrs=['bold', 'underline']))
elif (user == 0 and robo == 2) or (user == 1 and robo == 0) or (user == 2 and robo == 1):
    won = "User"
    animate(won)
    print("\n\t\t", colored("YOU WON !!!", "red", attrs=['bold', 'underline']))
else:
    won = "Robo"
    animate(won)
    print("\n\t\t", colored("ROBO WON !!!", "red", attrs=['bold', 'underline']))
line()
