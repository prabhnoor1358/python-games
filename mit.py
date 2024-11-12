########################   Lecture 3   ############################

# Practice:
# Declare a variable n that stores an int. Print the sum of all digits in n.

""" n=int(input("Enter the no: "))
no=n
sum=0
while(n>0):
    last_dig=n%10
    sum=sum+last_dig
    n=n//10
print(f"The sum of digits of {no} is: {sum}") """

########################   Lecture 4   ############################

# Unique chars in string
""" s=input()
word=""
for char in s:
    if char in word:
        continue
    else:
        word=word+char
print(len(word)) """

# Guess And Check (Sq. Root)
""" flag=False
y=int(input("Enter the no: "))
for x in range(0,y+1):
    if x*x>y:
        break
    elif x*x==y:
        flag=True
        print(f"Square root of {y} is: {x}")
        break
if flag==False:
    print(f"Square root of {y} is not found") """
 
# Secret Code
""" ans=-10
flag=input(f"Is your secret {ans}: ")
if flag=='y':
print(f"Secret found: {ans}....")
print(".....ssh")
while(flag == 'n'):
ans=ans+1
flag=input(f"Is your secret {ans}: ")
if flag=='y':
    print(f"Secret found: {ans}....")
    print(".....ssh")
    break """

# Float problem 
""" x=0
for i in range(10):
    x=x+0.1
    print(x) """

# decimal to binary
""" num=int(input("Enter the no: "))
k=num
result=""
if num==0:
    result="0"
while num>0:
    bit=str(num%2)
    result=bit+result
    num=num//2           # Floor div: doesn't take remainder
print(f"{k} to binary is: {result}") """

# Write code that counts how many unique common characters there are between two strings
""" text1=input("Enter the 1st text: ")
text2=input("Enter the 2nd text: ")
word=""
count=0
for char in text1:
    if char in word or char==" ":
        continue
    elif char in text2:
        word=word+char
        count+=1
    else:
        word=word+char
print(f"Unique common characters between {text1} and {text2} are: {count}") """

########################   Lecture 5   ############################

# Approximation method
""" x=int(input("Enter the no: "))
guess=0
no_of_guesses=0
while(abs(guess**2-x)>=0.001 and guess**2<x):
    guess=guess+0.00001
    no_of_guesses+=1
ans=round(guess,3)
print(f"The approx square root of {x} is {ans}")
print(f"No of guesses took: {no_of_guesses}") """

#Approximation aliter
""" x=int(input("Enter the no: "))
guess=0
no_of_guesses=0
while(guess**2 < x):
    guess=guess+1
    no_of_guesses=no_of_guesses+1
while(guess**2-x > 0.001):
    guess=guess-0.00001
    no_of_guesses+=1
print(f"The approx square root of {x} is {round(guess,3)}")
print(f"No of guesses took: {no_of_guesses}") """

########################   Lecture 6   ############################

# Bisecction Search --Square Root

'''n=float(input("Enter the no: "))
epsilon=0.01
count=0
if n<1:
    start=n 
    end=1
else:
    start=0
    end=n
guess=(start+end)/2
while(abs(guess**2-n)>=epsilon):
    count+=1
    if guess**2>n:
        end=guess
        guess=(start+end)/2
    elif guess**2<n:
        start=guess
        guess=(start+end)/2
print(f"The square root of {n} is {guess}")
print("Count: ",count)'''

# Bisecction Search --Cube Root

'''n=float(input("Enter the no: "))
flag=False
if n<0:
    flag=True
n=abs(n)
if n<1:
    start=0
    end=1
else:
    start=0
    end=n
epsilon=0.01
guess=(start+end)/2
while(abs(guess**3-n)>=epsilon):
    if guess**3>n:
        end=guess
    elif guess**3<n:
        start=guess
    guess=(start+end)/2
if flag:
    print(f"Cube root of {n} is approximately {-guess}")
else:
    print(f"Cube root of {n} is approximately {guess}")'''


# Newton-Raphson method --Sqaure Root
# p(x)=x**2-num
# g=g-p(g)/p'(g)

""" x=float(input("Enter the no: "))
guess=float(input("Enter the guess: "))
epsilon=0.01
count=0
while(abs(guess**2-x)>=epsilon):
    count+=1
    guess=guess-((guess**2-x)/(2*guess))
print("Approximate sq. root of",x,"is",guess)
print("Count:",count) """

########################   Lecture 7   ############################

# Add all odd integers b/w and including a and b

""" def isOdd(x):
    return x%2 != 0

def odd_bw(a,b):
    sum=0
    for i in range(a,b+1):
        if isOdd(i):
            sum=sum+i
    return sum

a=int(input("Enter the 1st no: "))
b=int(input("Enter the 2nd no: "))
output=odd_bw(a,b)
print(f"Sum of no b/w {a} and {b} is: {output}") """

# Palindrome String

""" def is_palindrome(s):
    word=""
    for i in range(len(s)-1,-1,-1):
        word=word+s[i]
    if word==s:
        return True
    else:
        return False

print(is_palindrome("madam")) """

# Return consonant words from str

""" vowels="aeiouAEIOU"
def keep_consonants(word):
    for i in range(0,len(word)):
        if word[i] in vowels:
            continue
        else:
            print(word[i])

keep_consonants("babas") """

# Write code that satisfies the following specs:

""" def first_to_last_diff(s, c):

    # s is a string, c is single character string
    #     Returns the difference between the index where c first
    #     occurs and the index where c last occurs. If c does not 
    #     occur in s, returns -1. 
   
    if c not in s:
        return -1
    else:
        # Searching from start
        for i in range(0,len(s)):
            if s[i]==c:
                start_index=i
                break
        # Searching from start
        for j in range(len(s)-1,-1,-1):
            if s[j]==c:
                stop_index=j
                break
        # Printing the result
        return (stop_index-start_index)   

print(first_to_last_diff('aaaa', 'a'))  # prints 3
print(first_to_last_diff('abcabcabcb','b'))  # prints 6
print(first_to_last_diff('abcabcabc', 'd'))  # prints -1    """

########################   Lecture 8   ############################

# Triangular No

""" def is_triangular(n):
    count=0
    for i in range(n+1):
        count=count+i
        if count==n:
            return True
        else:
            continue
    return False
print(is_triangular(1)) """

# Problem Quesstion

""" def count_nums_with_sqrt_close_to(n, epsilon):
    # n is an int > 2
    #     epsilon is a positive number < 1
    # Returns how many integers have a square root within epsilon of n
    # your code here

    def bisection_root(x):
        start=0
        if x<1:
            end=1
        else:
            end=x
        guess=(start+end)/2
        while(abs(guess**2-x)>epsilon):
            if guess**2>x:
                end=guess
            elif guess**2<x:
                start=guess
            guess=(start+end)/2
        return guess

    for i in range(n**3):
        if abs(bisection_root(i)-n)>epsilon:
            continue
        else:
            print(f"Sqrt of {i} is {bisection_root(i)}")
            print(f"Epsilon diff. {abs(bisection_root(i)-n)}")
            print("==========================================")

count_nums_with_sqrt_close_to(10,0.1) """

# note: In a function, we can access a variable defined outside but we con't modify them
""" def f(y):
    print(x)
    # error: 
    # x=x+1
    z=x
    z=z+1
    print(z)
x=2
f(x) """

# Problem Question

""" def apply(criteria,n):
    # criteria is a function that takes in a number and returns a Boolean
    #     n is an int
    # Returns how many ints from 0 to n (inclusive) match the criteria 
    # (i.e. return True when criteria is applied to them)
    
    count=0
    for i in range(n+1):
        if criteria(i):
            count+=1
    return count


def is_even(x):
    return x%2==0

how_many = apply(is_even,10)
print(how_many) """

# Problem Question

""" def f_yields_palindrome(n, f):
    # n is a positive int
    #     f is a function that takes in an int and returns an int
    # Returns True if applying f on n returns a number that is a
    # palindrome and False otherwise. 
    # your code here
    return is_palindrome(f(n))

def is_palindrome(n):
    x=n
    word=""
    while(n>0):
        last_dig=n%10
        word=word+str(last_dig)
        n=n//10
    return str(x)==word

# For example:
def f(x):
    return x+1

def g(x):
    return x*2

def h(x):
    return x//2

print(f_yields_palindrome(2, f))   # prints True
print(f_yields_palindrome(76, f))   # prints True
print(f_yields_palindrome(11, g))   # prints True
print(f_yields_palindrome(123, h))   # prints False """

########################   Lecture 9   ############################

# Lambda function
# Can only be used one time
""" y = (lambda x:x%2==0)(8)
print(y) """

# Tuples
""" t=()
print(type(t))
a=(5)
print(type(a))
b=(5,)
print(type(b))
t=(2,"mit",3)
print(t[1][1])
t=t+(5,6)
print(t)
t=t+() """
# note: we can't change elements of tuple
# Error: t[0]=3

# Can be used to swap variables
""" x=1
y=2
(x,y)=(y,x)
print(x)
print(y) """
# Can be used to return multiple elements from an function 
# Problem Question

""" def char_counts(s):
    # s is a string of lowercase chars 
    # Returns a tuple where the first value is the 
    # number of vowels in s and the second value 
    # is the number of consonants in s 
   
    vowel=""
    consonant=""
    for char in s:
        if char in "aeiouAEIOU":
            vowel=vowel+char
        else:
            consonant=consonant+char
    return (len(vowel),len(consonant))

print(char_counts("abcd"))  # prints (1,3)
print(char_counts("zcght"))  # prints (0,5) """

# Can be used to pass 'variable no of arguments' in a function
# Example:

""" def mean(* args):        # * paramameters is used to pass variable args
    sum=0
    for no in args:
        sum=sum+no
    return (sum/len(args))

print(mean(1,2,3,4,5,6))
print(mean(6,0,9)) """

# Problem Question
""" def max_of_both(n, f1, f2):
    # n is an int
    #     f1 and f2 are functions that take in an int and return a float
    # Applies f1 and f2 on all numbers between 0 and n (inclusive). 
    # Returns the maximum value of all these results.
    # your code here
    max1=0
    max2=0
    for i in range(0,n+1):
        if f1(i)>max1:
            max1=f1(i)
        if f2(i)>max2:
            max2=f2(i)
    return (max(max1,max2))

print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20 """

# Problem Question
""" def sublist_sum(L):
    # L is a list whose elements are lists with int elements
    # Returns the sum of all int elements.
    # your code here
    sum=0
    for i in range(0,len(L)):
        for j in range(0,len(L[i])):
            sum=sum+L[i][j]
    return sum

print(sublist_sum([[1,2], [4,5,6]])) # prints 18 """

########################   Lecture 10   ############################

# Lists are mutable (can be changed) 
# lst.append(a)         **adds a to end of the list
#                       **return value None
#                       **lst=lst.append(a) is wrong and lst=None

# Problem Question
""" def make_ordered_list(n):
    # n is a positive int
    # Returns a list containing all ints in order 
    # from 0 to n (inclusive)
   
    # your code here
    lst=[]
    for i in range(0,n+1):
        lst.append(i)
    return lst

print(make_ordered_list(6))  # prints [0, 1, 2, 3, 4, 5, 6] """

# Problem Question
""" def remove_elem(L, e):
    # L is a list
    # Returns a new list with elements in the same order as L
    # but without any elements equal to e. 
    # your code here
    newList=[]
    for ele in L:
        if e!=ele:
            newList.append(ele)
    return newList

L = [1,2,2,2]
print(remove_elem(L, 2))    # prints [1]
L = [1,2,2,2]
print(remove_elem(L, 1))    # prints [2,2,2]
L = [1,2,2,2]
print(remove_elem(L, 0))    # prints [1,2,2,2] """

# Problem Question
""" def count_words(sen):
    # sen is a string representing a sentence 
    # Returns how many words are in sen (i.e. a word is a 
    # a sequence of characters between spaces.
    # your code here
    newstr=sen.split(" ")
    return len(newstr)

s = "Hello it's me"
print(count_words(s))   # prints 3
s = "I just took a DNA test turns out I'm 100% splitting strings"
print(count_words(s))   # prints 12 """

# Problem Question
""" def sort_words(sen):
    # sen is a string representing a sentence 
    # Returns a list containing all the words in sen but
    # sorted in alphabetical order.
    # your code here
    lst=sen.split(" ")
    lst.sort()
    return lst

s = "look at this photograph"
print(sort_words(s))    # prints ['at', 'look', 'photograph', 'this']
s = "now this is a story all about how my life got flipped turned upside down"
print(sort_words(s)) """

# Tricy Example
""" L=[1,2]
for i in L:
    L=L+L        # This does noy go to infinity bcz L lost its binding but i doesn't
    print(i)
    print(L) """

# Problem Question
""" def apply_to_each(L, f):
    # L is a list of numbers 
    #     f is a function that takes in a number and returns a number
    # Mutate L such that you apply function f to every element in L
    # your code here
    for i in range(len(L)):
        L[i]=f(L[i])

test = [1,-2,3]
apply_to_each(test, lambda x: x**2)
print(test)   # prints [1,4,9]

test = [-7, 8, 5, -8, -3]
apply_to_each(test, abs)
print(test)   # prints [7, 8, 5, 8, 3] """

########################   Lecture 11   ############################

# Problem Question
""" def remove_all(L, e):
    # L is a list
    # Mutates L to remove all elements in L that are equal to e
    # Returns None.
    # your code here
    Lcopy=L[:]
    L.clear()
    for k in Lcopy:
        if e != k:
            L.append(k) 
    
Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin)    # prints [1] """

# Problem Question
""" def repeat(L, n):
    # L is a list of ints
    #     n is a positive int
    # Mutates L to contain whatever elements L has right now repeated n times.
    # your code here 
    Lcopy=L[:]
    L.clear()
    for i in Lcopy:
        for j in range(n):
            L.append(Lcopy[j])
    
Lin = [1,2,3]
repeat(Lin, 3)
print(Lin)    # prints [1, 2, 3, 1, 2, 3, 1, 2, 3] """

########################   Lecture 12   ############################

# Problem Question
## Write a list comprehension expression that uses a list named L.
# It makes a new list whose elements are the middle 
# character of strings whose length is 3. 

# If L = ['abc', 'm', 'p', 'xyz', '123', 57]
# It makes ['b', 'y', '2']
""" L = ['abc', 'm', 'p', 'xyz', '123', 57]
L = [e[1] for e in L if (type(e)==str and len(e)==3)]
print(L) """

########################   Lecture 13   ############################

# Problem Question
""" def pairwise_div(Lnum, Ldenom):
    # Lnum and Ldenom are non-empty lists of 
    #     equal lengths containing numbers
    # Returns a new list whose elements are the pairwise 
    # division of an element in Lnum by an element in Ldenom. 
    # Raise a ValueError if Ldenom contains 0.
    # your code here
    # challenge: write this with list comprehension!
    assert (len(Lnum)!=0 and len(Lnum)==len(Ldenom)),"len(L1 or L2)=0 || len(L1)!=len(L2)"
    try:
        Lcopy=[Lnum[i]/Ldenom[i] for i in range(len(Lnum))]
        return Lcopy
    except:
        raise ValueError("Div by 0")

L1 = [4,5,6]
L2 = [1,2,3]    
print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]
L1 = [4,5,6]
L2 = [1,0,3]    
print(pairwise_div(L1, L2))  # raises a ValueError
L1 = [4,5,6,7,8]
L2 = [1,8,3]    
print(pairwise_div(L1, L2))  # raises an AssertionError
L1 = []
L2 = []    
print(pairwise_div(L1, L2))  # raises an AssertionError """

########################   Lecture 14   ############################

# Problem Question
""" def find_grades(grades, students):
    # grades is a dict mapping student names (str) to grades (str)
    #     students is a list of student names 
    # Returns a list containing the grades for students (in the same order)
    # your code here
    lst=[]
    for name in students:
        if name in d:
            lst.append(d[name])
    return lst

d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A'] """

# Problem Question
""" def find_in_L(Ld, k):
    # L is a list of dicts
    #     k is an int
    # Returns True if k is a key in any dicts of L and False otherwise
    # your code here
    for i in range(len(Ld)):
        if k in Ld[i]:
            return True
    return False

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
print(find_in_L([d1, d2, d3], 2))  # returns True
print(find_in_L([d1, d2, d3], 25))  # returns False """

# Problem Question
""" def count_matches(d):
    # d is a dict
    # Returns how many entries in d have the key equal to its value
    # your code here
    count=0
    lst=list(d.items())
    for [k,v] in lst:
        if k==v:
            count+=1
    return count

d = {1:2, 3:4, 5:6}
print(count_matches(d))   # prints 0
d = {1:2, 'a':'a', 5:5}
print(count_matches(d))   # prints 2 """

# Problem Question
""" def is_inverse(d1, d2):
    # d1 and d2 are dicts 
    # Assume values of d1 and d2 are unique and immutable
    # Returns True if d1's keys are values in d2 and d1's 
    # values are keys in d2
    if len(d1)!=len(d2):
        return False
    for k1 in d1.keys():
        if k1 not in d2.values():
            return False
    return True

d1 = {1:2, 3:4}
d2 = {2:1, 4:3}
print(is_inverse(d1, d2))  # prints True
d1 = {1:2, 3:4}
d2 = {2:1, 4:3, 5:6}
print(is_inverse(d1, d2))  # prints False
d1 = {1:2, 3:4}
d2 = {1:2, 2:1}
print(is_inverse(d1, d2))  # prints False """

# Problem Question
""" def add_to_d(d, L):
    # d is a dict
    #     L is a list of tuples
    # Mutates d with new entries whose key is the first element of a 
    # tuple in L and the associated value is the second element of a 
    # tuple in L. If the key is already in d, do nothing to its value. 
    # If the key cannot be added, raise a ValueError. Returns None.
    try:
        for i in range(len(L)):
            if L[i][0] not in d:
                d[L[i][0]]=L[i][1]
            elif L[i][0] in d:
                continue
    except:
        raise ValueError

d = {1:1}
L = [(1,2), (3,4)]
add_to_d(d, L)
print(d)   # d is mutated to be {1: 1, 3: 4}
d = {1:1}
L = [(3,4), ([1,2,3], 5)]
add_to_d(d, L)   
# raises a ValueError because its trying to add a list (mutable obj) as key """

########################   Lecture 16   ############################

# Problem Question
# Code to return the total length of all strings inside L:     
""" def total_len_recur(L):
    if len(L) == 1:
        return len(L[0])
    else:
        return len(L[0]) + total_len_recur(L[1:])
test = ["ab", "c", "defgh"]
print(total_len_recur(test))  # should print 8 """

# Problem Question
""" def in_lists_of_list(L, e):
    # L is a list whose elements are lists containing ints
    # Returns True if e is an element within the lists of L
    # and False otherwise. 
    # Hint, the in operator is useful here, i.e. e in something
    # your code here
    if len(L)==1:
        for i in L[0]:
            if e==i:
                return True
        return False
    else:
        return ( e in L[0]) or in_lists_of_list(L[1:],e)

test = [[1,2], [3,4], [5,6,7]]
print(in_lists_of_list(test, 3))  # prints True
test = [[1,2], [3,4], [5,6,7]]
print(in_lists_of_list(test, 0))  # prints False """

# Problem Question
# Memoize the code to find possible scores in basketball
""" def score_count(x, d):
    if x in d:
        return d[x]
    else:
        ans = score_count(x-1,d) + score_count(x-2,d) + score_count(x-3,d)
        d[x]=ans
        return ans
d = {1:1, 2:2, 3:3}
print(score_count(4, d))  # prints 6
print(score_count(6, d))  # prints 20
print(score_count(13, d))  # prints 1431 """

# Problem Question
""" def in_list_of_lists_mod(L, e):
    # L is a list whose elements are either
    #     * lists containing ints or
    #     * ints
    # Returns True if e is an element within L or 
    # sublists of L and False otherwise. 
    # your code here
    if len(L)==1:
        if type(L[0])==list:
            return (e in L[0])
        else:
            return (e == L[0])
    else:
        if type(L[0])==list:
            return (e in L[0]) or in_list_of_lists_mod(L[1:],e) 
        else:
            return (e == L[0]) or in_list_of_lists_mod(L[1:],e)

test = [[1,2],3,4,5,6,7]
print(in_list_of_lists_mod(test, 3))  # prints True
test = [[1,2],[3,4,5],6,7]
print(in_list_of_lists_mod(test, 3))  # prints True
test = [[1,2],[3,4,5],6,7]
print(in_list_of_lists_mod(test, 10))  # prints False """

# Problem Question
""" def my_deepcopy(L): 
    # L is a list, containing lists or list of lists, etc.
    # Returns a new list with the same structure as L that 
    # contains copies (recursively) of every sublist 
    # your code here
    newL=[]
    if len(L)==1:
        if type(L[0])==list:
            newL.append(my_deepcopy(L[0]))
        else:
            newL.append(L[0])
            return [L[0]]
    else:
        if L[0]==list:
            return my_deepcopy(L[0]) + my_deepcopy(L[1:])
        else:
            return [L[0]] + my_deepcopy(L[1:])
    return newL

myL = ["abc", ['d'], ['e', ['f', 'g']]]
my_newL = my_deepcopy(myL)
print(myL)
print(my_newL)
myL[2][1][0] = 1
print(myL)      # should be ['abc', ['d'], ['e', [1, 'g']]]
print(my_newL)  # should be ['abc', ['d'], ['e', ['f', 'g']]] """

# Problem Question
""" def f(L):
    # L is a non-empty list of lowercase letters.
    # Returns the letter earliest in the alphabet.
    if len(L) == 1:
        return L[0]
    else:
        if L[0] < f(L[1:]):
            return L[0]
        else:
            return f(L[1:])
        
print(f(['z', 'a', 'b', 'c', 'd']))  # should print 'a' """

# Problem Question
""" def g(L, e):
    # L is list of ints, e is an int
    # Returns a count of how many times e occurrs in L 
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        if e == L[0]:
            return 1
        else:
            return 0
    else:
        if L[0] == e:
            return 1+g(L[1:], e)
        else:
            return 0+g(L[1:],e)
    
print(g([1,2,3,1], 1))     # should print 2
print(g([1,1,2,3,1,1], 1)) # should print 4 """
    
# Problem Question
""" def h(L, e):
    # L is list, e is an int
    # Returns a count of how many times e occurrs in L or 
    # (recursively) any sublist of L
    if len(L) == 0:
        return 0
    else:
        if type(L[0])==int:
            if L[0] == e:
                return 1+h(L[1:], e)
            else:
                return h(L[1:], e)
        elif type(L[0])== list:
            return h(L[0],e) + h(L[1:], e)
    
print(h([[1,1],2,[3],1], 1))        # should print 
print(h([1,2,[3,1,[1,[1]]]], 1))  # should print 4 """

########################   Lecture 18   ############################

# Problem Question
# Add code to the init method to check that 
# * the type of center is a Coordinate obj and 
# * the type of radius is an int. 
# If either are not these types, raise a ValueError.
""" class Coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Circle(object):
    def __init__(self, center, radius):
        if type(center)==Coordinate and type(radius)==int:
            self.center = center
            self.radius = radius
        else:
            raise ValueError("type(center)!=Coordinate OR type(radius)!=int:")

# center = Coordinate(2, 2)
# my_circle = Circle(center, 2)   # no error
# my_circle = Circle(2, 2)    # raises ValueError
# my_circle = Circle(center, 'two')  # raises ValueError """

# Problem Question
# Implement the missing get_inverse and invert methods below
""" class SimpleFraction(object):
    # A number represented as a fraction
    def __init__(self, num, denom):
        # num and denom are integers
        self.num = num
        self.denom = denom
    def get_inverse(self):
        # Returns a float representing 1/self
        # your code here
        return self.denom/self.num
    def invert(self):
        # Sets self's numerator to its denominator and vice versa.
        #     Returns None.
        # your code here
        (self.num,self.denom)=(self.denom,self.num)
             
f1 = SimpleFraction(3,4)
print(f1.num, f1.denom)   # prints 3 4 
print(f1.get_inverse())   # prints 1.33333333 (note this one returns value)
f1.invert()               # acts on data attributes internally, no return
print(f1.num, f1.denom)   # prints 4 3  """

########################   Lecture 19   ############################

# Problem Question
""" class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def __str__(self):
        return "Animal Name: "+str(self.name)+" Age: "+str(self.age)
    def get_name(self):                 # getter
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,newName):          # setter
        self.name=newName
    def set_age(self,newAge):
        self.age=newAge

# Write a function that meets this spec.
def make_animals(L1, L2):
    # L1 is a list if ints and L2 is a list of str
    #     L1 and L2 have the same length
    # Creates a list of Animals the same length as L1 and L2.
    # An animal object at index i has the age and name
    # corresponding to the same index in L1 and L2, respectively.
    # your code here
    L_animals=[]
    for i in range(len(L1)):
        temp=Animal(L1[i])
        temp.set_name(L2[i])
        L_animals.append(temp)
    return L_animals

L1 = [2,5,1]
L2 = ["blobfish", "crazyant", "parafox"]
animals = make_animals(L1, L2)
print(animals)     # note this prints a list of animal objects
for i in animals:  # this prints the indivdual animals
    print(i) """

# Problem Question
# Write the function according to this spec
""" class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def __str__(self):
        return "Animal Name: "+str(self.name)+" Age: "+str(self.age)
    def get_name(self):                 
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,newName):          
        self.name=newName
    def set_age(self,newAge):
        self.age=newAge

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        self.name=name
        self.friends=[]
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

def make_pets(d):
    # d is a dict mapping a Person obj to a Cat obj
    # Prints, on each line, the name of a person, 
    # a colon, and the name of that person's cat
    # your code here
    for k,v in d.items():
        print(k.name+":"+v.name)

p1 = Person("ana", 86)
p2 = Person("james", 7)
c1 = Cat(1)
c1.set_name("furball")
c2 = Cat(1)
c2.set_name("fluffsphere")
d = {p1:c1, p2:c2}
make_pets(d)  # prints ana:furball
              #        james:fluffsphere """

# Problem Question
# Write the class Employee as a subclass of Person
""" class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def __str__(self):
        return "Animal Name: "+str(self.name)+" Age: "+str(self.age)
    def get_name(self):                 
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,newName):          
        self.name=newName
    def set_age(self,newAge):
        self.age=newAge

class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        self.name=name
        self.friends=[]
    def add_friend(self,name):
        self.friends.append(name)
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

class Employee(Person):
    list_salaries=[]
    # An Employee contains an extra data attribute, salary as an int
    def __init__(self, name, age):
        # initializes self as a Person with a salary data attribute, initially 0
        Person.__init__(self,name,age)
        self.salary=0
        self.list_salaries.append(self.salary)
    def get_salary(self):
        # returns self's salary
        return self.salary
    def set_salary(self, s):
        # s is an int
        # Sets self's salary data attribute to s
        self.salary=s
        self.list_salaries.append(self.salary)
    def salary_change(self, n):
        # n is an int (positive or negative)
        # Adds n to self's salary. If the result is negative, sets 
        # self's salary to 0. Otherwise sets self's salary to the new value.
        self.salary=self.salary+n
        if self.salary<0:
            self.salary=0
        self.list_salaries.append(self.salary)
    def has_friends(self):
        # Returns False if self's friend list is empty and True otherwise
        if len(self.friends)==0:
            return False
        return True    
    def past_salaries_list(self):
        # Keeps track of all salaries self has had in the order they've changed. 
        # i.e. whenever the salary changes, keep track of it.
        # Hint: you may need to add an additional data attribute to Employee.
        # Returns a copy of the list of all salaries self has had, in order.
        return self.list_salaries
    def past_salary_freq(self):
        # Returns a dictionary where the key is a salary number and the 
        # value is how many times self's salary has changed to that number.
        d={}
        for ele in self.list_salaries:
            if ele in d:
                d[ele]=d[ele]+1
            else:
                d[ele]=1
        return d
        
# For example:
e = Employee("ana", 35)
print(e.get_salary())   # prints 0
e.set_salary(1000)
print(e.get_salary())   # prints 1000
e.salary_change(2000)
print(e.get_salary())   # prints 3000
e.salary_change(-50000)
print(e.get_salary())   # prints 0
print(e.has_friends())  # prints False
e.add_friend("bob")
print(e.has_friends())  # prints True
print(e.past_salaries_list())  # prints [0, 1000, 3000, 0]
print(e.past_salary_freq())  # prints {0: 2, 1000: 1, 3000: 1} """

# Problem Question
# Write a function that meets this specification
""" def counts(L):
    # L is a list of Employee and Person objects 
    # Returns a tuple of a count of:
    #   * how many Person objects are in L
    #   * how many Employee objects are in L 
    #   * the number of unique names among Employee and Person objects
    persons=0
    emps=0
    for ele in L:
        if type(ele)==Person:
            persons+=1
        elif type(ele)==Employee:
            emps+=1
    
    names=[]
    for ele in L:
        if ele.name not in names:
            names.append(ele.name)
    return (persons,emps,len(names))
            
# For example:
# make employees and people
L = []
L.append(Person('ana',8))
L.append(Person('bob',25))
L.append(Employee('ana',35))
L.append(Employee('cara',18))
L.append(Employee('dan',53))
# call function
print(counts(L))    # prints (2,3,4) """

########################   Lecture 20   ############################

