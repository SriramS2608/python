#factor of a number
num=6
sum=0
i=1
while i<num:
    if num%2==0:
        sum=sum+i
    i=i+1
print(sum)



#factorial
num=6
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(fact)


#armstrong no    153=1**3+5**3+3**3 ==153

num=153
temp=num
length=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**length
    temp=temp//10
if num==sum:
    print('armstrong')
else:
    print('not')



#fibinacii
num=5
i=1
a,b=0,1
while i<num:
    print(a)
    a,b=b,a+b
    i=i+1



#neon number  9**2= 81=8+1=9
num=9
square=num**2
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit
    temp=temp//10
if sum==num:
    print('neon')
else:
    print('not')


#sum of num in list

lst=[10,20,30,40,50]
sum=0
length=0
while length<len(lst):
    sum=sum+lst[length]
    length=length+1
print(sum)

#sum of enen digit in lst
lst=[10,20,34,50]
sum=0
i=0
while i<len(lst):
    if lst[i]%2==0:
        sum=sum+lst[i]
    i=i+1
print(sum)



#factor of a num
num=6
i=1
while i<num:
    if num%i==0:
        print(i)
    i=i+1



num=6
i=1
sum=0
while i<=num:
    if num%i==0:
        sum=sum+i
    i=i+1
    print(sum)




#factorial

num=5
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(fact)

num=9
i=1
while num>0:
    i=i*num
    num=num-1
print(i)


#strong number =145= 1!+4!+5!=145

num=145
temp=num
sum=0
while num>0:
    digit=num%10
    fact=1
    i=1
    while i<=digit:
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10
if sum==temp:
    print('neon')
else:
    print('not')



#perfect number  6=1,2,3= 1+2+3=6
num=6
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print('perfect')
else:
    print('not')



#spy number  1124=1+1+2+4=8 and 1*1*2*4=8


num=1124
sum=0
product=1
temp=num
while num>0:
    digit=num%10
    sum=sum+digit
    product=product*digit
    num=num//10
if sum==product:
    print('spy')
else:
    print('not')


