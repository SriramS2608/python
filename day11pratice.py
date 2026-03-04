##############################################################################################################
#                                  floor division
#----------------------------------------------------------------------------------------------------------------

a = 98
b = 43
print (a/b)

a = 6
b = 3
print(a/b)

# floor division

a = 98
b = 43
print(a//b)

a = 98.45
b = 42.54
print(a//b)
 
a = 789654
print(a // 10)

a = 78349232
print(a//100)

a = 7896213
print(a//1000)

#modules
a = 11
b = 2
print(a%b)

a = 10
b = 2
print(a%b)

a = 789453
print(a%10)

a = 789453
print(a%100)

a = 789453
print(a%1000)

#relational operatior

a = 98
b = 45
print(a == b)

a = 98
b = 98
print(a == b)

s1 = 'jspiders'
s2 = 'Jspiders'
print(s1 == s2)

list1 = [10,20,30]
list2 = [10,20,30]
print(list1 == list2)

a = 98
b = 100
print(a != b)

a = 'java'
b = 'python'
print(a != b)

s1 = 'python'
s2 = 'java'
print(s1 > s2)

print(ord('A'))
print(ord('a'))

s1 = 'A'
result = ord(s1)+32
print(chr(result))

s1 = 'a'
result = ord(s1)-32
print(chr(result))

#swap 2 number without using 3rd variable

a = 45
b = 90
print(f'before the values a :{a} and value of b :{b}' )
a , b = b , a
print(f'after the value a :{a} and value of b :{b}')

# swap the values with using third variable
a = 45
b = 90
print(f'before the values a :{a} and value of b :{b}' )
temp = a
a = b
b = temp
print(f'after the value a :{a} and value of b :{b}')