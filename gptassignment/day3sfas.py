a=34
print(float(a))
print(str(a))
print(bool(a))


a=34.56
print(int(a))

a=23
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 987654321
print(a // 10)
print(a%10)

a =10
b=10
print(a==b)
print(a>b)

a = range(1,20)
print(list(a))
print(a[5])
print(a[-1])
print(list(a[3:8:1]))

a = 987
print(a%10)
print(a%100)

d1 = a%10
d2 = (a//10)%10
d3 = a//100
print(d1+d2+d3)

a =45
b =50
a,b = b,a
print(a)
print(b)

a =45
b =50
temp=a
a=b
b=temp
print(a)
print(b)

stri = 'python is a programming language '
print('python' in stri)
print('p' in stri)

a = range(10,100)
print(list(a[::-10]))
print(list(a[::]))
print(list(a[::2]))

a=input('enter the values:')
result=eval(a)
print(result)
print(type(result))


a ='python'
b ='java'
print(a == b)


a ='z'
print(ord(a))
result = ord(a)- 32
print(result)
print(chr(result))


a = input('enter the value:')
b = a/15
c = b==0
print(c)