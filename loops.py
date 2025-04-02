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

#for n in range(5):
 #   print(n)

#using range(start,stop,step)

##for i in range(1,10,2): #start from i to go to 10
##    print(i)

#for iterating over a string

##for letter in "python":
##    print(letter)

#Iterating over a dictionary
#person = {"name":"Alice","age":25,"city":"Harare"}
#for key, value in person.items():
#    print(key,":", value)

#using break in a for loop
#the break statement stops the loop when a condition is met.

##for num in range(10):
##    if num == 5:
##        break
##    print(num)

#Using continue in a For loopp
#The continue statement skips the current iteration and moves to the next.

##for num in range(5):
##    if num == 2:
##        continue
##    print(num)



 
#While loops
