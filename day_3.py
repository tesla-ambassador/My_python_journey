name = input('Mandem, welcome to my game! Please state your name?\n')
if name.lower() == 'mebz':
    print(f'Welcome Agent {name}!')
    body_count = input('How many times have you kissed someone?\n')
    girlfriends = input('How many girlfriends have you had?\n')
    continents = input('How many continents exist on planet earth?\n')
    if int(body_count or int(girlfriends)) > 0:
        print('Stop the cap sir')
    else:
        print('You are the Jame Bond of losers.')
        print('''
    ,a8888a,       ,a8888a,  888888888888  
 ,8P"'  `"Y8,   ,8P"'  `"Y8,        ,8P'  
,8P        Y8, ,8P        Y8,      d8"    
88          88 88          88    ,8P'     
88          88 88          88   d8"       
`8b        d8' `8b        d8' ,8P'        
 `8ba,  ,ad8'   `8ba,  ,ad8' d8"          
   "Y8888P"       "Y8888P"  8P'     
      ''')
else:
    print(f'Welcome {name} this is a treasure hunt')
    left = input('Do you want to go left or right? ')
    if left.lower() == 'left':
        fly = input('You are able to defy the laws of physics! Will you fly or swim? ')
        if fly.lower() == 'fly':
            sun = input('You have reached the sun, will you enter it or not? ')
            if sun.lower() == 'yes':
                print('Congragulations, you have reached the core of the sun and you have discovered nuclear fusion')
            else:
                print('This game is not for loosers and cowards...Game Over')
        else:
            print('You are dumb, swimming doesn\'t defy the laws of physics')
    else:
        print('Game over freak!')
    