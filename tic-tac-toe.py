import time,os,random
from getkey import getkey,keys
from termcolor import cprint

class grid(object):
    """ Pass a list of values for each cell of the grid
    """
    def __init__(self,cells=[' ',' ',' ',' ',' ',' ',' ',' ',' ']):
        self.cell=[]
        for i in range(0,9):
            self.cell.append(cells[i])
    def getCell(self,i):
        return self.cell[i]
    def setCell(self,val,i):
        self.cell[i]=val
    def __str__(self):
        return f" {self.cell[0]} | {self.cell[1]} | {self.cell[2]} \n-----------\n {self.cell[3]} | {self.cell[4]} | {self.cell[5]} \n-----------\n {self.cell[6]} | {self.cell[7]} | {self.cell[8]} \n"

def won(A):
    for i in range(0,7,3):
        if (A.getCell(i)==A.getCell(i+1)==A.getCell(i+2) and (A.getCell(i) in ['O','X']) ):
            A.setCell('*',i)
            A.setCell('*',i+1)
            A.setCell('*',i+2)
            return True
    for i in range(0,3):
        if (A.getCell(i)==A.getCell(i+3)==A.getCell(i+6) and (A.getCell(i) in ['O','X']) ):
            A.setCell('*',i)
            A.setCell('*',i+2)
            A.setCell('*',i+4)
            return True
    if ( A.getCell(0)==A.getCell(4)==A.getCell(8) and (A.getCell(0) in ['O','X']) ):
        A.setCell('*',0)
        A.setCell('*',4)
        A.setCell('*',8)
        return True
    if ( A.getCell(2)==A.getCell(4)==A.getCell(6) and (A.getCell(2) in ['O','X']) ):
        A.setCell('*',2)
        A.setCell('*',4)
        A.setCell('*',6)
        return True
    return False

sampleGrid = grid([1,2,3,4,5,6,7,8,9])

def line():
    print("=============================================================")

def start():
    line()
    print("\t\tHOW TO PLAY\n")
    print("1. You are X, and the computer is O or vice-versa")
    print("2. Players take turns putting their marks in empty squares")
    print("3. First player to get 3 of marks in a row is the winner")
    line()
    print("\n")
    print("Enter x to choose 'X' or o to choose 'O' ")

    global userSymbol
    global roboSymbol

    userSymbol = input("Choose your symbol: ")
    if (userSymbol in ['o','O']):
        userSymbol = 'O'
        roboSymbol = 'X'
    elif (userSymbol in ['x','X']) :
        userSymbol = 'X'
        roboSymbol = 'O'
    else:
        print("Invalid Choice\nPlease Restart the game.....")
        exit(0)
    time.sleep(1)
    os.system('cls')

    line()
    print("\tEnter your marking-choice in the following manner\n")
    print(sampleGrid)
    line()
    print("\n")
    print("Press ENTER to continue: ")
    key = getkey()
    if key == keys.ENTER:
        time.sleep(0.7)
        os.system('cls')
    else:
        print("Invalid Choice\nPlease Restart the game.....")
        exit(0)

def tie(A):
    for i in range(0,9):
        if A.getCell(i) == '*':
            return False
        if A.getCell(i) == ' ':
            return False
    return True

start()

A = grid()

while( (not won(A)) and (not tie(A))):

    global wonBy

    print(A)
    user = int(input("Enter the cell no: "))
    while(A.getCell(user-1) != ' '):
        print("The cell is already occupied...")
        time.sleep(1.5)
        os.system('cls')
        print(A)
        user = int(input("Enter the cell no: "))
    A.setCell(userSymbol,user-1)
    wonBy = 'You'
    print(A)
    print("Thinking....")
    time.sleep(1.5)
    os.system('cls')

    if won(A) or tie(A):
        break

    robo = random.randint(1,9)
    while(A.getCell(robo-1) != ' '):
        robo = random.randint(1,9)   
    A.setCell(roboSymbol,robo-1)
    wonBy = 'Robo'
    print(A)
    time.sleep(1.5)
    os.system('cls')

print(A)
line()

if (tie(A)):
    cprint("\tMATCH TIE","red",attrs=['bold','underline'])
else:
    cprint(f"\t{wonBy} won the game !!!","red",attrs=['bold','underline'])

line()