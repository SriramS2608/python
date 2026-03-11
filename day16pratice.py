#  reverse the number using while
num=123456789
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)



#reverse palindrome numbers
num=12345678987654321
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num==rev:
    print(f'{num} is palinddrome')
else:
    print(f'{num} is not in palindrome')



#2nd highest number
num=897348235
first=-1
secound=-1
while num>0:
    digit=num%10
    if digit>first:
        secound=first
        first=digit
    elif digit >secound and digit != first:
        secound=digit
    num=num//10
print('secound num' , secound)