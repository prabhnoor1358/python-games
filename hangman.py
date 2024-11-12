import random

def actualWord_and_guessedWord(word,guessedWord):
    print("\t============================")
    print(f"\t| Actual Word:   {word}     |")
    print(f"\t| Guessed Word:  {guessedWord}     |")
    print("\t============================")


def scorecard(guesses_took,correct_guesses):
    incorrect_guesses=guesses_took-correct_guesses
    print("\t==============================")
    print("\t        SCORECARD ")
    print("\t==============================")
    print("\tNo Of Guesses Took:",guesses_took)
    print("\tCorrect Guesses:   ",correct_guesses)
    print("\tIncorrect Guesses: ",incorrect_guesses)

def start():
    print("\t==============================")
    print("\tWELCOME TO THE GAME OF HANGMAN")
    print("\t==============================")
    print("\t       ------------")
    print("\t            |")
    print("\t          -----")
    print("\t          | O |")
    print("\t          -----")
    print("\t   	   / \\")
    print("\t    	    |")
    print("\t   	   / \\")
    print("\t         -------")
    print("\t          |   |")

def win():
    print("\t==============================")
    print("\t   CONGRATULATIONS !!!!!!!!")
    print("\t\t    ^_^")
    print("\t       You Saved The Man")
    print("\t==============================")
    print("\t            O  ")
    print("\t   	   \\ /")
    print("\t    	    |")
    print("\t   	   / \\")

def lose():
    print("\t==============================")
    print("\t  SORRY! YOU LOST THE GAME ")
    print("\t==============================")
    print("\t       ------------")
    print("\t            |")
    print("\t          -----")
    print("\t          |*_*|")
    print("\t          -----")
    print("\t   	   / \\")
    print("\t    	    |")
    print("\t   	   / \\")

def play_game():
    wordList=["word","tiger","rat","joker","people","theatre","bat","yolk"]

    word=wordList[random.randint(0,len(wordList)-1)]
    guessedWord=""

    print(f"\tI'm thinking of a word with {len(word)} characters")
    for i in range(0,len(word)):
        guessedWord=guessedWord+"*"

    allowedWords="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    str_guessedChars=""
    no_of_guesses=10

    while(word!=guessedWord):
        if no_of_guesses==0:
            break
        else:
            print(f"\tNo of guesses left: {no_of_guesses}")
            print("\t"+guessedWord)
            guessedChar=input("\tEnter the char: ")
            print("\t===============================")
            if (len(guessedChar) != 1) or guessedChar not in allowedWords:
                print("\tInvalid character entered")
            elif guessedChar in str_guessedChars:
                print("\tThe char has been already guessed")
            else:
                flag=False
                str_guessedChars=str_guessedChars+guessedChar
                list_guessedWord=list(guessedWord)
                for i in range(0,len(word)):
                    if word[i]==guessedChar:
                        flag=True
                        list_guessedWord[i]=guessedChar
                        guessedWord="".join(list_guessedWord)
                if flag==True:
                    print("\tThe character exists in word !")
                elif flag==False:
                    print("\tThe character doesn't exists in word !")
                    no_of_guesses=no_of_guesses-1
                
    if no_of_guesses != 0:
        win()
        actualWord_and_guessedWord(word,guessedWord)
        scorecard(len(str_guessedChars),len(word))
    else:
        count=0
        for i in guessedWord:
            if i != '*':
                count+=1

        lose()
        actualWord_and_guessedWord(word,guessedWord)
        scorecard(len(str_guessedChars),count)


start()
play_game()
