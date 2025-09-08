#File: homework1.py

# --- Variables and Data Types ---
a = 10 #int, whole number no decimals
b = 1.5 #float, number with decimal
c = 3j #complex number, think a+bi where i is imaginary number
d = "hello" #string, text (list of characters)
e = [1, 2, 3] #list, set of multiple values stored together
f = {"name": "Ellen", "favorite fruit": "strawberry"} #dictionary, key:value pair list
g = (1, 2) #tuple, immutable collection of items
h = ["apple", "banana", "strawberry"] #another list, this time of strings
i = True #boolean, true or false
j = None #NoneType, just doesnt have/do anything
k = [True, "blue", 12] #List, lists are not required to store only one kind of data
l = str(14) #string "14", casted by the str() command
m = 1e4 #float, uses scientific notation

#script to print all (lazy writing)
all = [a,b,c,d,e,f,g,h,i,j,k,l,m]
for z in all:
    print(z)
    print(type(z))

#Questions:
#1. 9
#2. int, float, complex, string, list, dictionary, tuple, boolean, NoneType
#3. d, k, and e are all lists and l and d are both strings
#4. str makes whatever it is given a string
#5. set, cannot have duplicates

n = {1,2,3}
print(n)
print(type(n))

# --- Booleans ---
print(10 > 9) #True, 10 is more than 9
print(10 == 9) #false, 10 isnt 9
print(10 <= 9) #False, 10 isnt less than or equal to 9
print(bool('abc')) #true, not empty
print(bool(123)) #true, not zero
print(bool(["apple", "cherry", "banana"])) #true, not empty
print(bool(True)) #true is true
print(bool(False)) #false is false
print(bool(0)) #false, zero
print(bool("")) #false, empty
print(bool(" ")) #True, not empty
print(bool(())) #False, empty
print(bool([])) #False, empty
print(bool({})) #False, empty
print(bool(True and False)) #False, one is true but not both
print(bool(True and True)) #true, both true
print(bool(False and False)) #false, both false
print(bool(True or False)) #true, one of two true so or satisfied
print(bool(True or True)) #true, both right
print(bool(False or False)) #false, neither true means false
print(bool(not(False))) #true, not false is true
print(bool(not(True))) #false, not true is false

#Questions
#1. empty things are false "filled" values are true
#2. the " " one, thought it would count as empty
#3. 1 == 1, 1 is equal to 1
#4. 1 != 2, 1 is not equal to false

# --- Operators ---
print(10 + 5)   # 15, + performs addition
print(10 - 5)   # 5, - performs subtraction
print(2 * 4)    # 8, * performs multiplication
print(6 / 3)    # 2.0, / performs division and returns a float
print(5 % 2)    # 1, % gives the remainder of division
print(3 ** 2)   # 9, ** raises to a power
print(15 // 2)  # 7, // performs floor division
print(5 == 2)   # False, == checks equality
print(10 != 10) # False, != checks inequality
print(2 < 5)    # True, < checks if less than
print(12 > 5)   # True, > checks if greater than
print(5 <= 6)   # True, <= checks if less than or equal
print(1 >= 10)  # False, >= checks if greater than or equal

x = 5
x += 5 #10
x -= 4 #6
x *= 3 #18

#Questions 3.3.4
#1. and returns true if both inputs are true, otherwise false
#2. or is true if one or both inputs are true
#3. not returns the opposite of what it is given (false->true and opposite)

#More Questions
#1. / is normal division, // is integer division (no decimal)
#2. % returns remainder of division
#3. %, 3 % 2 = 1
#4. Act on the variable's current value and what's given (x+=1 same as x=x+1)

# --- Strings ---
my_string = "hello"
print(my_string) #hello
print(my_string[0]) #h first character
print(my_string[1]) #e second
print(my_string[2]) #l third
print(my_string[3]) #l fourth
print(my_string[4]) #o fifth
print(my_string[-1]) #o last
print(my_string[1:3]) #el indexes 1 & 2
print(my_string[0:5:2]) #hlo indexes 0, 2 and 5 in order
print(len(my_string)) #5 length of string
print(my_string + "goodbye") #hellogoodbye adds the strings
print(my_string * 7) # hellohellohellohellohellohellohello prints string 7 times

#Questions
#1. Taking a "substring" by 'cutting out' parts of a string based on their index. It was used in 2-9
#2. "Hello, my name is Oski" -> adds the two strings together with a space between
#3. "Hello, my name is Oski" -> same thing, but this time the name was added inside the string
#4. formatted string vs normal method -> formatted strings allow for expressions to be embedded using curly braces

# --- Terminal Commands ---

#1. cd
#Changes directories. Use it to move from one folder to another
#Example: cd Desktop

#2. ls
#shows files and folders in the current directory
#Example: ls

#3. ls -a
#Lists all files, including hidden ones
#Example: ls -a

#4. mkdir
#Makes a new folder
#Example: mkdir projects

#5. cat
#Prints contents of file to the terminal
#Example: cat notes.txt

#6. pwd
#Shows full path of current working directory
#Example: pwd

#7. cd ..
#Go back to previous directory
#Example: cd ..

#8. cd .
#refers to current directory
#Example: cd .

#9. cd ~
#return to home directory
#Example: cd ~

#10. cp
#duplicates files/folders
#Example: cp notes.txt backup.txt

#11. mv
#move/rename files/folders
#Example mv draft.txt final.txt

#12. rm
#Delete files permanently
#rm old.txt

#13. clear
#empty terminal screen
#Example: clear

#14. grep
#find text pattern in file
#grep "error" log.txt

#Questions:
#1. touch - makes empty file or updates timestamp, man - opens documentation for a command, history - shows list of recently used commands
#2. ls shows only visible files/folders, ls -a includes hidden ones
#3. hidden files start with a ., to avoid clutter
#4. ls -l - list in long format, ls -h - shows file sizes, rm -r - recursively deletes folder contents