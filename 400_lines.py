print("Welcome to Mufakose")
print("Hello World")
print("I Love Sadza")
print("Actually I don't love Sadza, ndorida from time to time, maybe kana ndine nzara")
print("I Love my familly")
print("I Love Kelly")
print("Shamwari nzangu ndizvozvo,NO HOMO")
print("Need to have millions when l reach 25")
print("Need to keep working hard")
print("Need to have money muna September")

#Creating Variables
score = 0
life = 0
timer = 30
Grace = "Unlimited"
blessings = "everyday"
age = 19
hos = False
future_success = True
Nyanzvi = "Where Art Meets Technology"
Pray = "ALWAYS,NIGGA!"

#Printing Variables

print(score)
print(life)
print(timer)
print(Grace)
print(blessings)
print(age)
print(hos)
print(future_success)
print(Nyanzvi)
print(Pray)

#Printing Variables with string

# The output of print is string, so if you want to output other datat types while including string there are methods to do that
# Notice if we mix string and Integer

print()
print("he got a score of {score}")  # will output "he got a score of {score} since python is not sure what our variable is"

#Method 1: Use of comma

print()
print("he got a score of",score) # will output "he got a score of 0" Since variable of score is 0
print("he has a life of",life)
print("the timer reads",timer)
# It even works on string
print("Jehovah's grace is",Grace)
print("Jehovah's blessings are",blessings)
print("Weston is of age",age)
print("Does he have Hos?",hos)  #even works on boolean data types
print("True/False, Do you think Weston is going to be succesfull in the future",future_success)
print("The motto of Nyanzvi is",Nyanzvi)
print("Pray",Pray)


#Method 2: use of Formatted Strings(f)

print()
print(f"he got a score of {score}") # will output the same as method 1
print(f"he got a score of{score}")
print(f"he has a life of {life}")
print(f"the timer reads{timer}")
#This also works on string and other data types
print(f"Jehovah's grace is{Grace}")
print(f"Jehovah's blessings are {blessings}")
print(f"Weston is of Age {age}")
print(f"Does he have Hos?{hos}")
print(f"True/False, Do you think Weston is going to be successfull in the future{future_success}")
print(f"The motto of Nyanzvi is{Nyanzvi}")
print(f"Pray{Pray}")

#printing data of many data types

#using commas
print()
print("he got a score of",score,"and he has a life of",life)#Output=> he got a score of 0 and he has a life of 0
print("he has a life of ",life,"and the timer reads",timer)
print("the timer reads",timer,"and Jehovah's grace is",Grace)
print("Jehovah's grace is",Grace,"and Jehovah's blessings are",blessings)
print("Jehovah's blessings are",blessings,"and weston is of age",age)
print("Weston is of age",age,"and Does he have hos?",hos)
print("Does he have Hos?",hos,"and true/False, Do you think Weston is going to be successfull in the future",future_success)
print("True/False, Do you think Weston is going to be succesfull in the furure?",future_success,"and The motto of Nyanzvi is",Nyanzvi)
print("The motto of Nyanzvi is",Nyanzvi,"and Pray",Pray)
print("Pray",Pray)

#using formatted strings(f)
print()
print(f"he got a score of {score} and he has a life of {life}")
print(f"he has a life of {life} and the timer reads {timer}")
print(f"the timer reads {timer} and Jehovah's grace is {Grace}")
print(f"Jehovah's grace is {Grace} and Jehovah's blesings are {blessings}")
print(f"Jehovah's blessings are {blessings} and Weston is of age {age}")
print(f"Weston is of age {age} and Does he have hos?{ hos}")
print(f"Does he have hos? {hos} and True/False, Do you think Weston is going to be successfull? {future_success}")
print(f"True/False, Do you think Weston is going to be successfull in the future {future_success} and The motto of Nyanzvi is {Nyanzvi}")
print(f"The motto of Nyanzvi is {Nyanzvi} and Pray {Pray}")
print(f"Pray {Pray}")

#Since input always accepts string, we always have to make sure that is knows that our inputted data is and integer, float or other data type

#we use the int function meaning integer on the input to let python know that we're accepting integer data types and not string

##mark = int(input("What is your Mark?"))
##Grade = int(input("What Grade are you in? "))
##number = int(input("What is the number"))
##integer = int(input("Input example of integer"))
##year = int(input("What Year is it"))
##no_of_children = int(input("How many children are there?"))
##no_of_staff = int(input("How many staff members are there?"))
##number_plate = int(input("What is the number Plate of your vehicle"))
##no_of_days = int(input("How many days did you use this product?"))
##no_of_shoes = int(input("How many shoes would you like to order?"))


# Now when we print the above variables, The data of the users will be the output

##print()
##print(mark)
##print(Grade)
##print(number)
##print(integer)
##print(year)
##print(no_of_children)
##print(no_of_staff)
##print(number_plate)
##print(no_of_days)
##print(no_of_shoes)
##print()
##


# The same can also be done to float and other data types
##floate = float(input("any example of a float"))
##weight = float(input("What is your wieght?"))
##Height = float(input("What is your height"))
##Temperature = float(input("What is the temperature?"))
##speed = float(input("What was the speed of the car? "))
##distance = float(input("The distance moved by the car was: "))
##length = float(input("What was the length of the object? "))
##width = float(input("What is the width of the object? "))
##acceleration = float(input("What was the acceleration of the car? : "))
##BMI = float(input("What is your BMI? "))
##Heart_Rate = float(input("What is your heart rate? "))
##
##print("the float is ",floate)
##print(f"the weight is {weight} and the user's height is{Height}. The temperature is: {Temperature}",
##      f"The speed is{speed} and the distance is {distance} not talking about the length of the object which was{length}",
##      f"The speed of the car was {speed} and the distance travelled was {distance}",
##      f"The length of the car is{length} and the width is{width} and it was moving with an acceleration of {acceleration}",
##      f"Your Body Mass Index is :{BMI} and you have a heart rate of : {Heart_Rate}"
##      )
##
###The same can also be done to Booleans
##

Question = bool(input("Are you Male?, True/False Only"))
user_authentication = bool(input("Is Auntheticated = True/False: "))
Email_verification = bool(input("is verified = True/False: "))
User_Subscription = bool(input("is subscribed = True/False: "))
Error_handling = bool(input("has error = True/False : "))
is_raining = bool(input("Is it raining? (yes/no): ") =="yes" )
is_logged_in = bool(input("Are you logged in? (yes/no): ")) =="yes"
is_paid = bool(input("Has the payment been made? (true/false): ")) =="true"
is_checked = bool(input("Check the box if you agree: (checked/unchecked): "))=="checked"
is_accepted = bool(input("Do yo accept  the terms? (checked/unchecked): ")) == "checked"

print(Question)

# we program to solve real life problems
#which means the programs are meant for users
# Which means the programs created are usually meant for the users and not the developers

#This means that the users need to input their data so that they can helped 

#This is where input comes in

#e.g

##input("What is your Name: ") # The input function will help the user enter his/her name Though there is nothing right now he can  do to proceed
##input("What is your Age")
##input("What is your Gender")
##input("What is your age?")
##input("What is your score")
##input("What is your height")
##input("What is your weight")
##input("What is your skin color")
##input("What is your favorite food")
##input("What is your favorite sport")

#though the above help in the user inputting data, it is not stored meaning whatever answered is useless
#unless we use variables to store data
#e.g

Name = input("What is your Name?") # instead of already assigning a variable to an already available string, we let the user input his own name, storing the data in the variable called Name
# meaning everytime we print Name, the name of the user is what is going to be printed.
Age = input("What is your Age")
Gender = input("What is your Gender")
age = input("What is your age?")
score = input("What is your score")
height = input("What is your height")
weight=input("What is your weight")
color = input("What is your skin color")
food = input("What is your favorite food")
sport = input("What is your favorite sport")

#remember input always accepts the data as string, meaning that age and score will be in the form of string not integers/floats

print(Name)
print(Gender)
print(age)
print(Age)
print(score)
print(height)
print(weight)
print(color)
print(food)
print(sport)

#You can do mathematical Operations in python using +,/,-,*,% to name a few

#first creating variables to use for operations

x = 15 
y = 30
#addition
print(x)
print(y)
print("add",x + y) #output is 45
print(f"addition {x + y}") # output is 45
print(x+y)
#subtraction
print(x-y) #-15
print(y-x) #15
# float division
print(x/y) #o.5 Outputs a float
print(y/x) #2.0 outputs a float too
#Integer division
print(x//y) #0 still remains an integer
print(y//x) #2
#multiplication
print(x*y) #prints 450
#modulus
print(x%y) # divides x and 15 but only prints the remainder
print(x**y) # x to the powerof y, x=> base : y=> power
#conditional operators, greater than,smaller than etc
print(x<y) # True prints Boolean (True/False)
print(x>y) # False

#you can also use variables in the use of operators

add = x+y
sub = x-y
mult = x*y
F_div = x/y
I_div = x//y
power_of = x ** y 

# creating variables help to print the value as you have already done the math already

#e.g
print(add) # same answer since add holds the value x+y
print(sub)
print(mult)
print(F_div)
print(I_div)
print(power_of)

# Sets => creation of unique elements, mutable, you can ADD/ REMOVE DATA, 
#when we create stets in Python we use curly brackets,{}

#e.g creation of set pupils:

pupils = {"Matthew","John","Mary","Samantha"} #everytime we add data it is seperated by a comma
numbers = {1,2,3,4,5,}
floatse = {0.1,0.2,0.3}
binary = {0,1}
countries = {"Brazil","Zimbabwe","Uganda","Malawi","United Kingdoms"}
rooms = {9899,2634,7890}
schools = {"Mufakose 2 High","Mufakose 1 High","Mufakose 3 High","Gwinyiro Primary School"}
Teachers ={"Mr John","Mrs Mary","Mrs Kelly","Man like Jerry","Sir Harry"}
Buildings = {"Joina",}
cities = {"Kwekwe","Harare","Mavingo","Chitungwiza","Mutare"}
mulitples_of_10 = {10,100,1000,10000,100000}


print(pupils)
print(numbers)
print(floatse)
print(binary)
print(countries)
print(rooms)
print(schools)
print(Teachers)
print(Buildings)
print(cities)
print(mulitples_of_10)

# set doesn't have a fixed index order, that's why the output will have change almost everytime
# but sets also priotise other data types over another for example integers over strings
#And Yes we can also mix data types in strings

children = {1,"Matthew",2,"John",3,"Mary",4,"Samantha"}
sega = {"sonic","knuckles",1001,"no Hos",True,6<9,0.1} # a set called sega whith unique variables
# I don't think its possible to add a list inside a set, tried that, didin't work
set1 = {1,1,2,3,4,5,6,7,777}
# a set also doesn't allow duplication of data, that's why even if you input the same variables pver and over again only one will show.
set2 = {"John","John",1,"carries"}
set3 = {"bed","living room","jannie" > "jannie",9}
flavor = {10000,"peach","orange","banana",2.0}
beanz = {"sugar beans","Baked Beans","Half a Bean😎"}
odd_numbers = {1,3,5,7,9,11,13,17,...}
even_numbers = {2,4,6,8,10,12,14,16,18,20}
numbers = {0.1,0.5,200,2002}


print(children)
print(sega)
print(set1)
print(set2)
print(set3)
print(flavor)
print(beanz)
print(odd_numbers)
print(even_numbers)
print(numbers)

# there are also unqie ways to use our sets such as 

#1. Union
#2. Intersection
#3. Difference
#4. Symmetric Difference

#1. Union of sets

# Union of sets is the combining of two sets e.g A and B to A U B

A = {1,2,3,4,5,6,7}
B = {1,3,5,7,9,11}
C = {2,4,6,8,10}
D = {2,3,5,7,11}
E = {1,2,3,4,5,6,7,8,9,10,11}
F = {2,4,6,8,10,12}
G = {3,6,9,12}
H = {4,8,12}
I = {5,10}
J = {6,12}
# don't forget that sets don't do no duplicates

A|B # A Union B
print(A|B)
# to make it easier so that we don't have to type A union B everytime we create a variable of the union set

union_AB = A|B
union = A|C
union_2 = C|G
UNIONS = G|H
UNI = H|D
UNIA = B|C
union45 = J|J|H|D
union_z = A|D|F|I
uniza = F|J
ASD = F|D
AS = J|C|B

print(union_AB)
print(union)
print(union_2)
print(UNIONS)
print(UNI)
print(UNIA)
print(union45)
print(union_z)
print(uniza)
print(ASD)
print(AS)

#Intersection (&)

#Intersecting of sets means only taking what is common amongst the intersecting sets, for example both set A and B have 1,3,5,7 as the common values

# that means A & B(A intersecting B) => 1,3,5,7

inter = A&B
inte = A&C
secting = C&G
intersectingg = G&H
intersecter = H & D
interrr = B & C
iii = J & J & H & D
iee = A & D & F & I
iniza = F & J
init = F & D
Inisa = J & C & B


print(inter) # output is 1,3,5,7
print(inte)
print(secting)
print(intersectingg)
print(intersecter)
print(interrr)
print(iii)
print(iee)
print(iniza)
print(init)
print(Inisa)

# Difference of a set

diff = A - B
diffe = A - C
differ = C - G
differe = G - H
differen = H - D
differenc = B - C
differencee = J -J - H - D
fference = A - D - F - I
ff = F - J
ffe = F - D
ffer = J - C - B

print(diff)
print(diffe)
print(differ)
print(differe)
print(differen)
print(differenc)
print(differencee)
print(fference)
print(ff)
print(ffe)
print(ffer)

# Symmetric Difference

s = A ^ B
sy = A ^ C
sym = C ^ G
symm = G ^ H
symme = H ^ D
symmet = B ^ C
symmetr = J ^J ^ H ^ D
symmetri = A ^ D ^ F ^ I
symmetrice = F ^ J
m = F ^ D
mm = J ^ C ^ B

print(s)
print(sy)
print(sym)
print(symm)
print(symme)
print(symmet)
print(symmetr)
print(symmetri)
print(symmetrice)
print(m)
print(mm)

# as we mentioned on line 1 , sets are mutable meaning we can ADD/ REMOVE data

#1. Adding

A.add(12)
B.add(13)
C.add(14)
D.add(15)
E.add(11)
F.add(10)
G.add(100)
H.add(99)
I.add(10001)
J.add(16)
H.add(7)

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)
print(I)
print(J)
print(mm)

# you can also add many elements to a set using one method,
# it is called the update method

#2. Updating a set

A.update([13,14,15,16])
B.update([89,99,100])
C.update([12,24,54])
D.update([3456,5,56])
E.update([23,45,6])
F.update([6735,78])
G.update([56,67,3])
H.update([354,78,56])
I.update([78,45,2])
J.update([9,45,7,8])

# Since we can add values, we can also remove them

# there are two ways of removing elements in a set
#1. the. remove method => which causes an error if we are to look for a specific value
#2. the .discard method => which prevents errors from occuring even if we where to look for the value removed

##A.remove(2)
##B.remove(13)
##C.remove(14)
##D.remove(1) # outputs error cox there is no 1 in set D
##E.remove(11)
##F.remove(10)
##G.remove(100)
##H.remove(99)
##I.remove(16)
##J.remove(12)
##H.remove(6)

# to prevent that error we use the second method

#2. the .discard method

A.discard(2)
B.discard(13)
C.discard(14)
D.discard(1) 
E.discard(11)
F.discard(10)
G.discard(100)
H.discard(99)
I.discard(16)
J.discard(12)
H.discard(6)

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)
print(I)
print(J)
print(mm)

# If_statements
# If statements are conditional operators which want we want can only be achieved if there is a condition which needs to be met.

#If not, then the desired outcome will not happen.

# Simple If Statements
x = 6
y = 4
z = 0

if x > 5: 
 print(" x is greater than 5") # wil only execute if variable x is greater than 5

if y < 10 :
 print("y is less than 10")

if z == 0:
 print("z is equal to 0")

name = input("What is your name?")
if name == "john" :
 print("Hello, John!")

age = int(input("What is your Age?"))
if age > 18 :
 print("You are an adult")

score = int(input("What score did you get?"))

if score > 90:
 print("You got an A")

temp = int(input("What is the temperature in these parts? "))

if temp > 30:
 print("It's hot outside.")

city = input("Which city do you live in? ")
if city == "Harare":
 print("You are in the capital city of Zimbabwe")

country = input("Which country do you live in? : ")
if country == "Zimbabwe":
 print("Do you speak Shona?")

#If-Else Statements

# If maybe the condition of our value was not met, that is where the Else comes in
# If condition is false , Else is True

if x < 5 :
 print("x is smaller than 5")
else:
 print("X is greater than or equal to 5")

if y > 10 :
 print("y is less than 10")
else:
 print("y is greater than or equal to 10")

if z != 0 :
 print("z is not equal to 0")
else:
 print("Z is equal to 0")

if name == "John":
 print("hello, John!")
else:
 print("Hello Stranger")

if age > 18:
 print("You are an adult")
else:
 print("You are a minor")

if score > 90 :
 print("You got an A")
else:
 print("you got a B or Lower")

if temp > 30 :
 print("it is hot outside")
else:
 print("it is not hot outside")

if city == "Harare":
 print("You are in the capital city of Zimbabwe")
else:
 print("You are not in Harare")

if country == "Zimbabwe" :
 print("You are in Zimbabwe")
else:
 print("You are not in Zimbabwe")

lang = input("What is your language")

if lang == "Shona":
 print("You speak Shona")
else:
 print("You do not speak Shona")

#If Elif Else Statements

#Elif works if there is another way than else to meet a condition

#Elif is short for else-if

if x> 5 :
 print("x is greater than 5")
elif x==5:
 print("x is equal to 5")
else:
 print("x is less than 5")

if y < 10:
 print("y is less than 10")
elif y == 10:
 print("Y is equal to 10")
else:
 print("Y is greater than 10")

if z == 0 :
 print("Z is equal to 0")
elif z < 0:
 print("Z is less than 0")
else: 
 print("Z is greater than 0")

if name =="John":
 print("Hello, John!")
elif name =="Jane":
 print("Hello Jane!")
else:
 print("Hello Stranger!")

if age > 18:
 print("You are an adult")
elif age == 18:
 print("You are 18")
else:
 print("You are a minor")

if score>90 :
 print("you got an A")
elif score > 80:
 print("you got a B")
else:
 print("you got a C or Lower")

if temp > 30:
 print("it is hot outside")
elif temp > 20:
 print("it's warm outside")
else:
 print("it's cold outside")

if city == "Harare":
 print("you are in Harare")
elif city == "Chitungwiza":
 print("You are in Chitungwiza")
else:
 print("you are in another city")

if country =="Zimbabwe":
 print("You are in Zimbabwe")
elif country =="Zambia":
 print("You are in Zambia")
else:
 print("You are in another country Bro!")

if lang == "Shona":
 print("You speak Shona!")
elif lang == "ndebele":
 print("You speak Ndebele")
else:
 print("You speak another language")
 
# nested If Statements

if x > 5:
 if y> 10:
  print("x is greater than 5 and y is greater than 10")

if z == 0 :
 if x!= 0 :
  print("z is equal to 0 and w is not equal to 0")  

if name == "John":
 if age > 18:
  print("hello John you are an adult")

grade = input("What is your grade?")
if score > 90:
 if grade == "A":
  print("You got an A")
  print("You are an A student")

humidity = int(input("how humid is it?"))
if temp >30 :
    if humidity > 80:
        print("It is hot and humid outside")

if city == "Harare":
  if country== "Zimbabwe":
   print("You are in Zimbabwe and its capital city")
if x> 5:
  if y<10:
    print("x is greater than 5 and y is less than 10")

if z !=0 :
  if x > 0:
    print("z is not equal to 0 and x is greater than 0")

if name!= "John":
  if age < 18:
    print("hello stranger,you are a minor")

if x > 5:
  if y < 10:
    print("x is greater than 5 and y is less than 10")

if z != 0:
  if x > 0:
    print("z is not equal to 0 and x is greater than 0")

#nested if else statements

if x > 5:
    if y > 10:
        print("x is greater than 5 and y is greater than 10")
    else:
        print("x is greater than 5 but y is not greater than 10")
else:
    print("x is not greater than 5")


if z == 0:
    if x != 0:
        print("z is equal to 0 and x is not equal to 0")
    else:
        print("z is equal to 0 and x is equal to 0")
else:
    print("z is not equal to 0")


if name == "John":
    if age > 18:
        print("Hello John, you are an adult")
    else:
        print("Hello John, you are a minor")
else:
    print("Hello, stranger")


grade = input("What is your grade?")
score = int(input("What is your score?"))
if score > 90:
    if grade == "A":
        print("You got an A")
        print("You are an A student")
    else:
        print("You have a high score but did not get an A")
else:
    print("Your score is not greater than 90")


humidity = int(input("How humid is it?"))
temp = int(input("What is the temperature?"))
if temp > 30:
    if humidity > 80:
        print("It is hot and humid outside")
    else:
        print("It is hot but not very humid outside")
else:
    print("It is not hot outside")

city = input("Which city are you in?")
country = input("Which country are you in?")
if city == "Harare":
    if country == "Zimbabwe":
        print("You are in Zimbabwe and its capital city")
    else:
        print("You are in Harare, but not in Zimbabwe")
else:
    print("You are not in Harare")

# Example 7: Nested if-else with x and y
if x > 5:
    if y < 10:
        print("x is greater than 5 and y is less than 10")
    else:
        print("x is greater than 5 but y is not less than 10")
else:
    print("x is not greater than 5")

# Example 8: Nested if-else with z and x
if z != 0:
    if x > 0:
        print("z is not equal to 0 and x is greater than 0")
    else:
        print("z is not equal to 0 but x is not greater than 0")
else:
    print("z is equal to 0")

# Example 9: Nested if-else with name and age
if name != "John":
    if age < 18:
        print("Hello stranger, you are a minor")
    else:
        print("Hello stranger, you are an adult")
else:
    print("Hello John")



#loops are repetition of a statement until the condition is met

#For loops
# loop can be repetition or iteration

#For loops

#A for loop is used to iterate over a sequence (like lists, tuples, dictionaries, strings, or ranges).

#
#iterable = 0
#
#for variable in iterable:
#    #code to execute

#Looping through a list

fruits =    ["apple","banana","cherry"]
for i in fruits:
    print(fruits)

#Looping through a String
for letter in "Wessy" :
    print(letter)

#using range() with a for loop()
for i in range(5) :
    print(i) #prints from 0 to 4

print(" ")

for j in range(2,10,2):#loops from 2 to 8 with a step of 2
    print(j)

#looping through a dictionary

student = {
           "name":"John",
           "age" : 25,
           "grade":"A"
           }

for key, value in student.items():
    print(key,":",value)

    #while loops
    i = 0
    while i <10:
        print(i)
        i = i + 1

##for variable in sequnce:
    #code block to execute
# The loop iterates over each element in sequence, assigning it to variable and executing the code block

#Example looping through a list
#fruits = ["apple","banana","cherry"]
#for fruit in fruits:
#    print(fruit)

for n in range(5):
   print(n)

#using range(start,stop,step)

#for i in range(1,10,2): #start from i to go to 10
#    print(i)

#for iterating over a string
for letter in "python":
    print(letter)
#Iterating over a dictionary
person = {"name":"Alice","age":25,"city":"Harare"}
for key, value in person.items():
   print(key,":", value)

#using break in a for loop
#the break statement stops the loop when a condition is met.

for num in range(10):
    if num == 5:
        break
    print(num)

#Using continue in a For loopp
#The continue statement skips the current iteration and moves to the next.

for num in range(5):
    if num == 2:
        continue
    print(num)

#while loops

#simple loopcounting from 1 to 5:

count = 1
while count <= 5: # will continue to iterate until is equal to 5
    print(count)
    count = count +1

number = 1
while number <= 10: # will continue to iterate until is equal to 10
    print(number)
    number = number + 1 

total = 0
num = 1
while num <= 10:
    total = total +num
    num +=1#faster way of adding 
    print(total)

count = 10
while count > 0:
    print(count)
    count -=1

count = 10 
while count > 0:
    print(count) #will print all numbers from 10 to 1    excluding 5
    
    count -=1
    if count == 5:
        break

#while True:
#    print("Hello") # will print Hello forever until you press ctrl+c

user = input("YES/NO")
while user == "Yes".lower :
    user =input("Do you want to continue? (yes/no)")
    if user =="yes":
        print("continuing")
    else:
        print("your lose my nigga") 

#LISTS


fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]  
last_fruit = fruits[-1]  # Accessing the last element
print("First fruit:", first_fruit)  # Output: apple
print("Last fruit:", last_fruit)  # Output: cherry

#slicing the listexamples:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
slice_a = numbers[2:5]  # Elements from index 2 to index 4
print( slice_a)  # Output: [3, 4, 5]


slice_b= numbers[4:]  # Elements from index 4 to the end
print( slice_b)  # Output: [5, 6, 7, 8, 9]

#  Changing an element in a list :
numbers[0] = 10  # Changing the first element to 10
print( numbers)  # Output: [10, 2, 3, 4, 5, 6, 7, 8, 9]

#Using `append()` to add an element at the end
fruits.append("orange")  # Adds "orange" to the end of the fruits list
print( fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Using `insert()` to add an element at a specific position
numbers.insert(0, 5)  # Insert 5 at the beginning (index 0)
print( numbers)  # Output: [5, 10, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 7: Adding a list to another list using `+`
new_numbers = [8] + numbers  # Add 8 at the start of the list
print(new_numbers)

#Using `remove()` to remove a specific element
numbers.remove(3)  # Removes the first occurrence of 3
print(numbers)  # Output: [5, 10, 2, 4, 5, 6, 7, 8, 9]

#Using `pop()` to remove an element by index
popped_element = numbers.pop(0)  # Removes the element at index 0 and returns it
print("Popped element:", popped_element)  # Output: 5
print( numbers)  # Output: [10, 2, 4, 5, 6, 7, 8, 9]

#Using `clear()` to remove all elements in a list
numbers.clear()  # Empties the list
print(numbers)# even if you where to print the output it will show the list,since nothing will be there









 

