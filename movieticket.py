print('welcome to book my show!')
theatername=input('enter the theater name (PVR/INOX):')
if theatername=='PVR'or theatername=='INOX':
    if theatername=='PVR':
        print('\n movies available are')
        movie1='avatar  850'
        movie2='mission imposible 800'
        ticket1=850
        ticket2=800
    else:
        print('\n movie available in INOX')
        movie1='batman   600'
        movie2='avenger 500'
        ticket1=600
        ticket2=500

    print(f'1.{movie1}')
    print(f'2.{movie2}')
    movie_choice=input('enter the number to select movie(1/2):')
    if movie_choice=='1' or movie_choice=='2':
         if movie_choice=='1':
            selected_movie= movie1
            ticket_price=ticket1
         else:
            selected_movie=movie2
            ticket_price=ticket2
    print(f'\n you have select : {selected_movie}')
    print(f'\n ticket price:{ticket_price}')
    confromation=input('\n do you want to conform the booking:(yes/no):')
    if confromation=='yes':
                 print(f"\n your ticket for {selected_movie} has been booked successfully!")
    else:
                 print('\n ticket cancelled')
else:
         print('invalid movie choice please try again')
         
        

