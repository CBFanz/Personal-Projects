import random
import subprocess



while True:
    inp = input('''
               RACING GAME
Type:
Start - Start the game
Help - Tutorial
Quit - Quit the game
Real - Try it :)
    ''').upper()
    
    
    
    if inp == 'HELP':
        print('''
The game will give you two options,
to input 'w' to accelerate,
and to input 's' to decelerate.
Sometimes the game will tell you to slow down, to which you can either decelerate or 
continue accelerating and take the risk of either crashing
or dodging the obstacle.

Winning the game may be difficult, but is not impossible.
There is a chance of losing if you're too slow and crashing if you're too fast as said.
Enjoy!
        ''')
    
    
    elif inp == 'QUIT':
        break
    
    
    elif inp == 'START':
        win = False
        crash = False
        n = random.randint(10, 20)
        for play in range(n):
            obs = random.choice(['slow', 'dodge'])
            x = input('>').lower()
            if obs == 'slow':
                print('Slow down!')
            if obs == 'slow' and x =='w':
                if random.choice(['crash','dodge']) == 'crash':
                    win = False
                    crash = True
                    print('CRASHED!')
                    break
            if x == 's':
                win = random.choice([True,False])
        if win == True:
            print('YOU WON!')
        elif win == False and crash == False:
            print('You were too slow')
            
    elif inp == 'REAL':
        subprocess.call('D://Games//Forza Horizon 4')
    else:
        print('Invalid input.')
    print('''    
    
    










    
    ''')