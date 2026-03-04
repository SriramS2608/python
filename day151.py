#looping statements
#while loop

#sequence from 1 to 5 
i=0
while i<=5:
    print(i,end=' ')
    i=i+1
else:
    print('program ended')

#hello 3times

i=0
while i<3:
    print('hello python' ,end=' ')
    i=i+1

#sequence from 6 to 1
i=6
while i>0:
    print(i , end=' ')
    i=i-1

#even number from 1 to 10
i=0
while i<10:
    if i%2==0:
        print(i)
    i=i+1

#even without if
i=0
while i<10:
    print(i)
    i+=2

#odd number
i=0
while i<10:
    if i%2!=0:
        print(i ,end=' ') 
    i+=1

#odd with out if
i=1
while i<10:
    print(i)
    i=i+2

#table
num = 3
i=1
while i<=10:
    print(f'{num} * {i} = {num*i}')
    i=i+1

#sum of first 5 natural num
i=1
sum=0
while i<=5:
    sum=sum+i
    i=i+1
print(sum)

#sum of even number from 1 to 10
i=1
total=0
while i<=10:
    if i%2==0:
        total=total+i
    i=i+1
print(total)

#sum of odd number from 1 to 10
i=1
total=0
while i<=10:
    if i%2!=0:
        total=total+i
    i=i+1
print(total)



#even and odd sum from 0 to 10
i=1
total_even=0
total_odd=0
while i<=10:
    if i%2==0:
        total_even=total_even+i
    else:
        total_odd=total_odd+i
    i+=1
print(f'even:{total_even},odd:{total_odd}')


#product and sum of even and odd to 10
i=1
total_even=0
total_odd=0
product_odd=0
product_even=0
while i<=10:
    if i%2==0:
        total_even=total_even+i
        product_even=product_even*i
    else:
        product_even=product_even+i
        product_odd=product_odd+i
    i=i+1
print(f'total_even:{total_even} ,total_odd:{total_odd} ,product_odd:{product_odd} , product_even{product_even}')



i=1
product=1
while i<=20:
    if i%2==0:
        product=product*i
    i=i+1
print(product)


#odd
i=1
product=1
while i<=20:
    if i%2!=0:
        product=product*i
    i=i+1
print(product)


#####
#number of digit present
num =1234
count = 0
while num>0:
    count=count+1
    num=num//10
print(count)

#repeat
num=9452042405234323
count=0
while num>0:
    count=count+1
    num=num//10
print(count)