#prime numbers
num=4
count=0
i=1
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')


#armstrong number 

num=153
temp=num
sum=0
length=(len(str(num)))
while num>0:
    digit= num%10
    sum=sum+digit**length
    num=num//10
if sum==temp:
    print('armstrong no')
else:
    print('not armstrong no')


#fibonacii number
num=5
a,b=0,1
count=0
while count<num:
    print(a ,end=' ')
    a,b=b,a+b
    count=count+1




num=10
a,b=0,1
count=0
while count<num:
    print(a ,end=' ')
    a,b=b,a+b
    count=count+1


#neon number
num=9
square=num**2
sum_digit=0
temp=square
while temp>0:
    digit=temp%10
    sum_digit+= digit
    temp=temp//10
if sum_digit==num:
    print('neon')
else:
    print('not neon')
