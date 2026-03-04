##########################################################
# assignment operators
##############################################################


#  +=
a = 34
a += 6
print(a)

a = 6
a += 24
print(a)

# -=
a = 6
a -= 2
print(a)

a = 1000
a -= 424
print(a)

# *=
a = 45
a *= 5
print(a)

# /=
a = 1000
a /= 2
print(a)

a = 1000
a //=2
print(a)


# %=

a = 1000
a %= 2
print(a)

#**=
a=1000
a **= 2
print(a)

#logical operators
a = 98
b = 34
print(a>b and b<a)

a =97
b=11
print(a>b or b>a)

a=11
b=95
print(a>b or a==b)

a=94
b=34
print(not(a>b))

a = 100
b=100
print(not(a==b))


a= 100
b=90
c=60
print(a>b and b>c and c<a)

a = 100
b = 50
c = 35
print(a<b or b>c or c>a)


#membership operators

# in and not in

s1 = 'python'
print('p' in s1)

s2 = 'education'
print('t' in s2)

s3 = 'education'
print('j' in s3)

s4 = 'python is a programming language'
print('python' in s4)

s5='python python'
print('python' in s5)

list1 = [10,20,30]
print(10 in list1)

list2 = [10,20,30,98]
print(98 not in list2)


# identity operator

# is ,is not

a=98
b=98
print(id(a))
print(id(b)) # to find the address of the variable stored
print(a is b)

a = 98
b = '98'
print(id(a))
print(id(b))

a=98
b=98
print(a is b)
print(a is not b)

s1 = 'python'
s2 = 'java'
print(s1 is s2)
print(s1 is not s2)

s1 = 'python'
s2 = 'python'
print(s1 is s2)
print(s1 is not s2)


list = [10,20,30,40]
list2 = [10,20,30,40]
print(id(list))
print(id(list2))
print(list is list2)
print(list is not list2)