for i in range(5,0,-1):
    print(i)

names=['rama','beema','sooma','kantha']
for name in names:
    print(name)


#char in string
subject='python'
for ch in subject:
    print(ch)

#print 10,20,30,40,50 using for
for i in range(10,51,10):
    print(i)


# even odd from numbers from 1 to 10

for i in range(1,11):
    if i%2==0:
        print(f'even:{i}')
    else:
        print(f'odd:{i}')



# even numbers till 20

for i in range(0,21):
    if i%2==0:
        print(i)


#sum of starting 10 natural numbers
total=0
for i in range(1,11):
    total+=i
print(total)

#factorial of number
num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

#print tables
num=3
for i in range(1,11):
    print(f'{num}x{i}={num*i}')


#number of digit in given number
num=32534
count=0
for i in str(num):
    count+=1
print(count)

#sum of digits
num=39423
sum=0
for i in str(num):
    sum=sum+int(i)
print(sum)

#product of numbers
num=34
product=1
for i in str(num):
    product=product*int(i)
print(product)




#reverse the string
num=12345
rev=0
for i in str(num):
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

#num is prime or not
num=11
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print('prime')
else:
    print('not prime')


#number of vowels

st='python'
vowels=0
for i in st:
    if i in 'AEIOUaeiou':
        vowels+=1
print(vowels)


#palindrome or not
num=121
temp=num
rev=0
for i in str(num):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print('palindrome')
else:
    print('not')

#armstrong number or not


num=153
temp=num
total=0
for i in str(num):
    if num>0:
        digit=num%10
        total=total+digit**len(str(temp))
        num=num//10
if temp==total:
    print('armstrong')
else:
    print('not')


#                  (or)

num=153
powers=0
digits=len(str(num))
for digit in str(num):
    powers=powers+int(digit)**digits
if powers==num:
    print('arm')
else:
    print('not')




#highest element in the list
nums=[10,20,30,40,50]
highest=nums[0]
for i in nums:
    if i>highest:
        highest=i
print(highest)

#lowest numbers in list
nums=[12,435,647,74]
lowest=nums[0]
for i in nums:
    if i<lowest:
        lowest=i
print(lowest)



#secound largest number
nums=[10,20,45,98,35]
highest=secound=float('-inf')
for i in nums:
    if i>highest:
        secound=highest
        highest=i
    elif i>secound and i!=highest:
        secound=i
print(secound)



# palindrome
text='erijfjie'
rev=''
for i in text:
    rev=i+rev
if rev==text:
    print('palindrome')
else:
    print('not')
        
#store char from one collection to another
text='weujgorw'
result=' '
for i in text:
    result=result+i
print(result)


#store only alpha frm str
input='sdfger452t4gw'
result=''
for ch in input:
    if ('a'<=ch<='z') or ('A'<=ch<='Z'):
        result=result+ch
print(result)



#print alpha digit in string
input='jcn82uy34ncurewj9847852735823wdfs'
alpha=''
digit=''
for ch in input:
    if ('a'<=ch<='z') or ('A'<=ch<='Z'):
        alpha+=ch
    elif ('0'<=ch<='9'):
        digit+=ch
print(alpha)
print(digit)



#upper to lower
input='PyThOn'
upper=''
for i in input:
    if 'A'<=i<='Z':
        upper+= chr(ord(i)+32)
    else:
        upper+=i
print(upper)


# only special char
input='hxneu2@# ehfnuh$34#%$%^&'
spe=''
for ch in input:
    if not (('a'<=ch<='z') or ('A'<=ch<='Z') or ('0'<=ch<='9')):
        spe+=ch
print(spe)


#replace space with _
string='hello welcome to python'
out=''
for i in string:
    if i==' ':
        out=out+'_'
    else:
        out+=i
print(out)

#perfect number

num=6
temp=num
sum=0
for i in range(1,num):  # note: dont start range with 0
    if num%i==0:
        sum=sum+i
if temp==sum:
    print('perfect')
else:
    print('not')



#spy number

num=1124
temp=num
sum=0
product=1
for i in str(num):
    sum=sum+int(i)
    product=product*int(i)
if sum==product:
    print('spy')
else:
    print('not')



#fid
num=10
a=0
b=1
for i in range(0,num):
    print(a)
    a,b=b,a+b


#neon
a=9
n=a*a
sum=0
for i in str(n):
    sum+=int(i)
if sum==a:
    print('neon')
else:
    print('no neon')

    




