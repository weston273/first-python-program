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




