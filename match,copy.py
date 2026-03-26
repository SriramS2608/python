#days
day=eval(input('enter the day:'))
match day:
    case 1:
        print('monday')
    case 2:
        print('tue')
    case 3:
        print('wed')
    case 4:
        print('thr')
    case 5:
        print('fri')
    case 6:
        print('sat')
    case 7:
        print('sun')

#simple calculater
operation=eval(input('enter the number:'))
a=45
b=43
match operation:
    case 1:
        print('add',a+b)
    case 2:
        print('sub',a-b)
    case 3:
        print('mul',a*b)
    case 4:
        print('floordiv',a//b)
    case 5:
        print('truediv',a/b)



#bank 1balance 2)deposit 3)withdraw 4)exit

balance=10000000
while True:
    print('\n________ATM menu___________')
    print('1)balance')
    print('2) deposit')
    print('3) withdraw')
    print('4) exit')
    choice=eval(input('enter your choice:'))
    match choice:
        case 1:
            print(f'your bank balance is {balance}')
        case 2:
            deposit=float(input('enter the amount u want to deposit:'))
            balance=balance+deposit
            print(f'your balanceis{balance}')
        case 3:
            withdraw=float(input('howmuch u want:'))
            balance=balance-withdraw
            print(f'nin balance{balance}')
        case 4:
            print('thank you for deal')
            break
        case _:
            print('enter in range of 1-4')