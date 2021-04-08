import RPi.GPIO as GPIO
from time import sleep #imports time and sleep from a python library
GPIO.setwarnings(False)


GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #Turns the power on for pin 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)


#Below, I set all my functions before the game starts, so when they get recalled, they're there.
def correct():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5,GPIO.OUT) #turns on pin 5 on the cobbler
    print ('Correct!')
    GPIO.output((5), True)
    sleep(1)
    GPIO.output((5), False)
    yes = str(input('Play again? (y/n) '))
    if yes == 'y' or yes == 'yes' or yes == 'YES' or yes == 'Y':
        startgame()
def incorrect():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6,GPIO.OUT)
    print ('Wrong!')
    GPIO.output((6), True)
    sleep(1)
    GPIO.output((6), False)
    yes = str(input('Try again? (y/n) '))
    if yes == 'y' or yes == 'yes' or yes == 'YES' or yes == 'Y':
        startgame()
def red():
    GPIO.output((16), False) #Makes the tricolor LED red
    sleep(0.6)
    GPIO.output((16), True)
    sleep(0)

def green():
    GPIO.output((21), False) #makes it green 
    sleep(0.6)
    GPIO.output((21), True) 
    sleep(0)
    
def blue():
    GPIO.output((12), False) 
    sleep(0.6)
    GPIO.output((12), True) 
    sleep(0)
    
def purple():    
    GPIO.output((12,16), False) #Mixes red and blue to make purple
    sleep(0.6)
    GPIO.output((12,16), True) 
    sleep(0)
    
def yellow():
    GPIO.output((21,16,), False) #Mixes red and green to make yellow
    sleep(0.6)
    GPIO.output((21,16), True) 
    sleep(0)

def ques11(): #provides the first question for difficulty 1
    print ('Remember the sequence of colors. The flashes are 1, 2, 3, 4 respectively.') #displays instructions for the game  
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    red()
    green()
    purple()
    blue()
    answer = input(str('What color was the 3rd flash? ')) #allows the user to input an answer
    if answer == 'purple' or answer == 'Purple' or answer == 'PURPLE' or answer == 'p' or answer == 'P': #provides multiple acceptable answers
        correct() #if the answer is correct, an LED will light up green
    else:
        incorrect() #if not, it will light up red
        
def ques12():
    print ('Remember the sequence of colors. The flashes are 1, 2, 3, 4 respectively.')   
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    green()
    blue()
    red()
    yellow()
    answer = input(str('What color was the 4th flash? '))
    if answer == 'yellow' or answer == 'Yellow' or answer == 'YELLOW' or answer == 'y' or answer == 'Y':
        correct()
    else:
        incorrect()

def ques13():
    print ('Remember the sequence of colors. The flashes are 1, 2, 3, 4 respectively.')   
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    yellow()
    purple()
    green()
    red()
    answer = input(str('What color was the 1st flash? '))
    if answer == 'Yellow' or answer == 'yellow' or answer == 'YELLOW' or answer == 'y' or answer == 'Y':
        correct()
    else:
        incorrect()

def ques14():
    print ('Remember the sequence of colors. The flashes are 1, 2, 3, 4 respectively.')   
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    red()
    green()
    blue()
    red()
    answer = input(str('What color was the 3rd flash? '))
    if answer == 'blue' or answer == 'Blue' or answer == 'BLUE' or answer == 'b' or answer == 'B':
        correct()
    else:
        incorrect()

def ques15():
    print ('Remember the sequence of colors. The flashes are 1, 2, 3, 4 respectively.')   
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    yellow()
    red()
    red()
    purple()
    answer = input(str('What color was the 4th flash? '))
    if answer == 'red' or answer == 'Red' or answer == 'RED' or answer == 'r' or answer == 'R':
        correct()
    else:
        incorrect()

def diff1(): #defines a function, which this one sets a difficulty.
    for x in range(0, 1): #Creates a loop over an interval of 0 to the entered number which gives you 5 blinks
        from random import randrange
        qs1 = randrange(1, 6) #Creates a random value between 1-5
        if qs1 == 1:
            ques11() #Plays question 1 if the randomly generated value is 1
        if qs1 == 2:
            ques12()
        if qs1 == 3:
            ques13()
        if qs1 == 4:
            ques14()
        if qs1 == 5:
            ques15()
       
def ques21(): #question function
    print ('Remember the sequence of colors. The flashes are 1, 2, 3, 4, 5 respectively.')
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    purple()
    red()
    blue()
    yellow()
    red()
    green()
    green()
    answer = input(str('What color do you get if you mix the colors of 2 and 3? '))
    if answer == 'purple' or answer == 'Purple' or answer == 'PURPLE' or answer == 'P' or answer == 'p':
        correct()
    else:
        incorrect()

def ques22():
    print ('Remember the sequence of colors. The flashes are 1, 2, 3, 4, 5 respectively.')
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    purple()
    red()
    blue()
    yellow()
    red()
    answer = input(str('What color do you get if you mix the colors of 4 and 5? '))
    if answer == 'orange' or answer == 'Orange' or answer == 'ORANGE' or answer == 'o' or answer == 'O':
        correct()
    else:
        incorrect()

def ques23():
    print ('Remember the sequence of colors. The flashes are 1, 2, 3, 4, 5 respectively.')
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    purple()
    red()
    blue()
    yellow()
    red()
    answer = input(str('What color do you get if you mix the colors of 2 and 5? '))
    if answer == 'red' or answer == 'Red' or answer == 'RED' or answer == 'r' or answer == 'R':
        correct()
    else:
        incorrect()

def ques24():
    print ('Remember the sequence of colors. The flashes are 1, 2, 3, 4, 5 respectively.')
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    red()
    blue()
    green()
    yellow()
    red()
    answer = input(str('What color do you get if you mix the colors of 2 and 5? '))
    if answer == 'purple' or answer == 'Purple' or answer == 'PURPLE' or answer == 'p' or answer == 'P':
        correct()
    else:
        incorrect()

def ques25():
    print ('Remember the sequence of colors. The flashes are 1, 2, 3, 4, 5 respectively.')
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    green()
    blue()
    blue()
    red()
    green()
    answer = input(str('What color do you get if you mix the colors of 2 and 3? '))
    if answer == 'blue' or answer == 'Blue' or answer == 'BLUE' or answer == 'b' or answer == 'B':
        correct()
    else:
        incorrect()

def diff3():
    for x in range(0, 1): #Creates a loop over an interval of 0 to the entered number which gives you 5 blinks
        from random import randrange #see diff1 for more comments
        qs2 = randrange(1, 6)
        if qs2 == 1:
            ques21()
        if qs2 == 2:
            ques22()
        if qs2 == 3:
            ques23()
        if qs2 == 4:
            ques24()
        if qs2 == 5:
            ques25()
        
def ques31():
    print ('Remember the sequence of colors. Hint: There are 6 flashes')
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    red()
    blue()
    red()
    purple()
    green()
    yellow()
    answer = input(str('What was the sequence of colors? (Enter the first letter of each color) '))
    if answer == 'rbrpgy' or answer == 'RBRPGY' or answer == 'R B R P G Y' or answer == 'r b r p g y':
        correct()
    else:
        incorrect()
        
def ques32():
    print ('Remember the sequence of colors. Hint: There are 6 flashes')
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    green()
    purple()
    yellow()
    red()
    blue()
    yellow()
    answer = input(str('What was the sequence of colors? (Enter the first letter of each color, no spaces) '))
    if answer == 'gpyrby' or answer == 'GPYRBY' or answer == 'g p y r b y' or answer == 'G P Y R B Y':
        correct()
    else:
        incorrect()
        
def ques33():
    print ('Remember the sequence of colors. Hint: There are 6 flashes')
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    purple()
    green()
    blue()
    yellow()
    green()
    red()
    answer = input(str('What was the sequence of colors? (Enter the first letter of each color, no spaces) '))
    if answer == 'pgbygr' or answer == 'PGBYGR' or answer == 'p g b y g r' or answer == 'P G B Y G R':
        correct()
    else:
        incorrect()
        
def ques34():
    print ('Remember the sequence of colors. Hint: There are 6 flashes')
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    red()
    yellow()
    blue()
    red()
    purple()
    green()
    answer = input(str('What was the sequence of colors? (Enter the first letter of each color, no spaces) '))
    if answer == 'rybrpg' or answer == 'RYBRPG' or answer == 'r y b r p g' or answer == 'R Y B R P G':
        correct()
    else:
        incorrect()
        
def ques35():
    print ('Remember the sequence of colors. Hint: There are 6 flashes')
    sleep(3)
    print ('Ready?')
    sleep(1)
    print ('Set...')
    sleep(1)
    print ('Go!')
    sleep(1)
    purple()
    green()
    blue()
    yellow()
    red()
    red()
    answer = input(str('What was the sequence of colors? (Enter the first letter of each color, no spaces) '))
    if answer == 'pgbyrr' or answer == 'PGBYRR' or answer == 'P G B Y R R' or answer == 'p g b y r r':
        correct()
    else:
        incorrect()
        
def diff2(): #see diff1 for more comments
    for x in range(0, 1): #Creates a loop over an interval of 0 to the entered number which gives you 5 blinks
        from random import randrange
        qs3 = randrange(1, 6)
        if qs3 == 1:
            ques31()
        if qs3 == 2:
            ques32()
        if qs3 == 3:
            ques33()
        if qs3 == 4:
            ques34()
        if qs3 == 5:
            ques35()
        
def startgame(): #sets the main game code as a function so it can be recalled later to restart the game
    print ('This is a brain game! You will be asked a question based off of the sequence of lights.' )
    difficulty = int(input('How difficult do you want the game to be? (Enter a Number between 1 and 3): '))
    if difficulty == 1: #so if the entered difficulty is 1, it will run the respective difficulty function
        diff1()
    elif difficulty == 2:
        diff2()
    elif difficulty == 3:
        diff3()
    else:
        print('That wasnt a choice, silly!')
        yes = str(input('Try again? (y/n) '))
        if yes == 'y' or yes == 'yes' or yes == 'YES':
            startgame()
        if yes == 'n' or yes == 'no' or yes == 'No' or yes == 'NO':
            
            if difficulty != [1,2,3]:
                print ('That was not a choice!')
                startgame()
startgame() #starts the game!

