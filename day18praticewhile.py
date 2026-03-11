#date = 11/march/2026


#sum of items in a list

list=[23,456,89,341,435]
sum=0
i=0
while i<len(list):
    sum=sum+list[i]
    i=i+1
print(f'total sum of values in list is {sum}')


# pratice 
list=[1,2,3,4,5,6,7,8,9]
sum=0
i=0
while i<len(list):
    sum=sum+list[i]
    i=i+1
print(f'total is {sum}')



#sum of even digit from given list
list=[1,2,3,4,5,6,7,8,9]
sum=0
i=0
while i<len(list):
    if list[i]%2==0:
        sum=sum+list[i]
    i=i+1
print(f'total even is {sum}')





#####################################################################
#           factor of a number
###################################################################

num=10
i=1
while i<=num:
    if num%i==0:
        print(i)
    i=i+1

#2nd time
num=3458439876
i=1
while i<=num:
    if num%i==0:
        print(i)
    i=i+1

#sum of factor of a number 
num=234
i=1
sum=0
while i<=num:
    if num%i==0:
        sum=sum+i
    i=i+1
print(sum)




# factorial number 
num=5
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(fact)

#2nd time
num=3
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(fact)



#############################################################
#                      strong numbers                       #
#############################################################
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
    print('strong')
else:
    print('not strong ')
    