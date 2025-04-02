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








