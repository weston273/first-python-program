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