#================================================================================================
#                                      range datatype
#============================================================================================

r1 = range(11)
print(list(r1))
print(tuple(r1))

r2 = range (4,10)
print(list(r2))
print(tuple(r2))

r3 = range(24,30,1)
print(list(r3))
print(tuple(r3))


#reversing
r4 = range(10,1,-1)
print(list(r4))

r5 = range(100,50,-2)
print(list(r5))


# indexing

r1 = range(10,101,10)
updated = list(r1)
print(updated)
print(updated[4])
print(updated[-1])
print(updated[9])
print(updated[2])
print(updated[6])
print(updated[5])
print(updated[-6])
print(updated[-5])
print(updated[-3])

#            slicing positive
r1 = range(10,101,10)
updated = list(r1)
print(updated)
print(updated[2:5:1])
print(updated[2:6:1])
print(updated[2:8:])
print(updated[:4:1])
print(updated[3:6:2])
print(updated[1:3:1])
print(updated[2:7:5])
print(updated[3:2:4])
print(updated[1::3])
print(updated[3::2])

# negative slicing
r1 = range(10,101,10)
updated = list(r1)
print(updated)
print(updated[-9:-2:1]) 

#reverse slicing
r1 = range(10,101,10)
updated = list(r1)
print(updated)
print(updated[10::-1]) 


#=========================================================================================
#                          input and print statement
#=========================================================================================

a =input('enter the value:')
print(a)
print(type(a))

c=input('enter the values;')
print(c)

a = input("enter the values:")
print(a)