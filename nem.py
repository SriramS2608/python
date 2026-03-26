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