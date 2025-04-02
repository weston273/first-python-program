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
