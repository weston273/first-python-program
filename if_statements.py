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