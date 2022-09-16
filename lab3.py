print('Welcome to the Flarsheim Guesser!')

print('Please think of a number between and including 1 and 100.')

game = True
while game:
    print('\n Please think of a number between and including 1 and 100.')
    remainder3 = 0
    remainder5 = 0
    remainder7 = 0
    remainder3 = int(input('What is the remainder when your number is divided by 3 ?'))
    while remainder3 < 0 or remainder3 >= 3:
        if remainder3 < 0:
            print('The value entered must be 0 or greater')
        
        elif remainder3 >= 3:
            print('The value you entered must be less thsn 3')
        
        remainder3 = int(input('What is the remainder when your number is divided by 3 ?'))
        break

    remainder5 = int(input('What is the remainder when your number is divided by 5 ?'))
    while remainder5 < 0 or remainder5 >= 5:
        if remainder5 < 0:
            print('The value entered must be 0 or greater')
        elif remainder5 >= 5:
            print('The value you entered must be less thsn 5')
        remainder5 = int(input('What is the remainder when your number is divided by 5 ?'))
        break

    remainder7 = int(input('What is the remainder when your number is divided by 7 ?'))
    while remainder7 < 0 or remainder7 >= 7:
        if remainder7 < 0:
            print('The value entered must be 0 or greater')
        elif remainder7 >= 7:
            print('The value you entered must be less thsn 7')
        remainder7 = int(input('What is the remainder when your number is divided by 7 ?'))
        break
    
    print('How amazing is that?')
    

    for i in range(1,101):
        if (i%3 == remainder3 and i%5 == remainder5 and i%7 == remainder7):
            print('Your number was' , i)
            print('How amazing is that? \n')

    
    while True:
        exit_con = input('Do you want to play again? Y to continue, N to quit  ==> ')
        if (exit_con == 'n'):
            game = False
            break
        elif (exit_con == 'y'):
            break
    
