string='smith'
i=0
while i<len(string):
    print(ord(string[i]))
    i=i+1


#to uppercase


string='smith'
i=0
result= ' '
while i<len(string):
    if 'a'<=string[i]<='z':
        result=result+ chr(ord(string[i])-32)
    i=i+1
print(result)


# to lowercase

st='GJOKGMGLGDV'
result=' '
i=0
while i<len(st):
    if 'A'<=st[i]<='Z':
        result=result+ chr(ord(st[i])+32)
    else:
        result=result+st[i]
    i+=1
print(result)




#total accurence of a char
s='python'
i=0
count=0
while i<len(s):
    count=count+1
    i+=1
print(count)

#accurence of char s
s='qsipders'
i=0
ch='s'
count=0
while i<len(s):
    if s[i]==ch:
        count=count+1
    i+=1
print(count)

s='kfjconihffcwrfgtbkniugfvdc'
count=0
i=0
while i<len(s):
    if s[i] in 'aeiouAEIOU':
        count+=1
    i+=1
print(count)

#number of vowels and consonents
s='rtcgwqrygun9yv8tihcw'
i=0
vowle=0
conso=0
while i< len(s):
    if s[i] in 'aeiouAEIOU':
        vowle+=1
    else:
        conso+=1
    i+=1
print(f'vowles={vowle}, con={conso}')




#toggle characters
s='pYtHoN'
i=0
result=' '
while i<len(s):
    if 'A'<=s[i]<='Z':
        result=result+chr(ord(s[i])+32)
    elif 'a'<=s[i]<='z':
        result=result+chr(ord(s[i])-32)
    i+=1
print(result) 



#ATM pin atuntication

pin='1235'
balance=12000
attempts=0
#pin 
while attempts<3:
    entered=input('enter the pin:')
    if entered==pin:
        break
    else:
        print('wrong pin')
        attempts+=1
else:
    print('accountlocked')
    exit()
while True:
    print('\n 1.balance \n2.deposit \n3.withdraw')
    choice=input('enter chooce:')
    if choice=='1':
        print(f'balance ;{balance}')
    elif choice=='2':
        deposit=input('enter the ammount:')
        balance=balance+deposit
        print(balance)
    elif choice=='3':
        withdraw=int(input('enter the amount u want to withdraw:'))
        if withdraw<=balance:
            balance-=withdraw
            print(f'updated balance{balance}')
        else:
            print('insuffient balance')
    elif choice=='4':
        print('good bye')
else:
    print('invalid option')






