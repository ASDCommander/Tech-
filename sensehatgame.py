from sense_hat import SenseHat #imports sense_hat from python library
from time import sleep
sense = SenseHat()
sense.clear()


r = (255,0,0)
w = (255,255,255)
b = (0,0,0)
bl = (0,0,255)
g = (0,255,0)

myscore=0
begin=False

def begingame(): #allows the game to be restarted later
    global myscore
    myscore=0
    print ('Welcome to the game! Use the joystick to jump over the obstacles!') #just some intro to the game
    print ('Press up to jump and hold to jump over doubles!')
    sense.show_message ('3', text_colour = b, back_colour = w)
    sense.show_message ('2', text_colour = w, back_colour = bl)
    sense.show_message ('1', text_colour = bl, back_colour = r)
    sense.show_message ('Go!', text_colour = r, back_colour = g)
    sleep(0.5)
    for x in range (0,1): #creates a loop for the range of 0-1
        from random import randrange #imports the random functions and stuff
        scene = randrange(1, 3) #Creates a random value between 1-2
        if scene == 1: #if the random number is 1, then play scene 1
            scene1()
        if scene == 2: #if the random number is 2, then play scene 2
            scene2()
    
def tryagain():
    print('Game Over') #prints 'game over' then shows it on the sensehat
    sense.show_message('Game Over', text_colour = r, back_colour = b, scroll_speed = 0.05)
    score=str(myscore) #turns the myscore variable into a string so it can be displayed on the sensehat
    print('Score:' + score) #prints the word Score: with the actual score
    sense.show_message('Score:' + score, text_colour = b, back_colour = w, scroll_speed = 0.05) #displays the score on the sensehat
    sleep(0.5)
    print('Press Up to Try Again!')
    #sense.show_message('Press Up to Try Again!', text_colour = b, back_colour = w, scroll_speed = 0.05)
    gameover = False #starts gameover as false
    sleep(2) #then it waits 2 second for a user input
    #i need something here to clear the "event" of pressing up for the second iteration try again
    for event in sense.stick.get_events(): #prepares the sensehat to look for an event
        if event.action == "pressed" and event.direction == "up": #if the event is press up
            gameover = True #then it plays again
            begingame()
        elif gameover == False:
            kill() #otherwise it should stop
    
def jump1(): #the first jump scene over the single
    sense.load_image("frame7.png") #You get this scene by meeting the criteria in the
    sleep(0.3)                  #  "scene1" variable, then it will play these frames
    sense.load_image("frame8.png")
    sleep(0.3)
    sense.load_image("frame9.png")
    sleep(0.3)
    sense.load_image("frame10.png")
    sleep(0.3)
    sense.load_image("frame11.png")
    sleep(0.3)
    game()
    
def fail1(): #failure scene where you collide with the obstacle and fall
    sense.load_image("frame12.png") #basically this scene is if you don't jump (press up),
    sleep(0.3) #                     then you fail and this scene plays
    sense.load_image("frame13.png")
    sleep(0.3)
    sense.load_image("frame14.png")
    sleep(0.3)
    sense.load_image("frame15.png")
    sleep(0.3)
    tryagain() #then, this function is used to ask the player if they want to try again
    
def fail2(): #failure scene where you collide with the obstacle and fall
    sense.load_image("frame213.png") #basically this scene is if you don't jump (press up),
    sleep(0.3) #                     then you fail and this scene plays
    sense.load_image("frame214.png")
    sleep(0.3)
    sense.load_image("frame215.png")
    sleep(0.3)
    sense.load_image("frame216.png")
    sleep(0.3)
    sense.load_image("frame217.png")
    sleep(0.3)
    tryagain() #then, this function is used to ask the player if they want to try again

def scene1():
    global myscore #sets myscore as a global variable
    sense.load_image("frame1.png") #displays the matrix image
    sleep(0.3)
    sense.load_image("frame2.png")
    sleep(0.3)
    sense.load_image("frame3.png")
    sleep(0.3)
    sense.load_image("frame4.png")
    sleep(0.3)
    sense.load_image("frame5.png")
    sleep(0.5)
    jumped = False #starts with jumped as false
    for event in sense.stick.get_events(): #tells the sense hat to look for an "event"
        if event.action == "pressed" and event.direction == "up": #if the event is the joystick being pressed up, then ...
            jumped = True #jumped becomes true which allows the scene for jump1 to play
            myscore+=1 #so if jumped=true, then it raises your score by 1 and plays jump1()
            jump1()
    if jumped == False: #otherwise, if the criteria isn't hit, then you get the failure scene
        fail1()

def jump2(): #the second jump scene over the double
    sense.load_image("frame27.png")
    sleep(0.3)
    sense.load_image("frame28.png")
    sleep(0.3)
    sense.load_image("frame29.png")
    sleep(0.3)
    #sense.load_image("frame210.png")
    #sleep(0.3)
    sense.load_image("frame211.png")
    sleep(0.3)
    sense.load_image("frame212.png")
    sleep(0.3)
    game()

def scene2(): #the second scene with the double jump
    global myscore
    sense.load_image("frame21.png") #displays the matrix image
    sleep(0.3)
    sense.load_image("frame22.png")
    sleep(0.3)
    sense.load_image("frame23.png")
    sleep(0.3)
    sense.load_image("frame24.png")
    sleep(0.3)
    sense.load_image("frame25.png")
    sleep(0.5)
    jumped2 = False #starts with jumped2 as false
    for event in sense.stick.get_events(): #tells the sense hat to look for an "event"
        if event.action == "held" and event.direction == "up": #if the event is the joystick being held up, then ...
            jumped2 = True #jumped2 becomes true which allows the scene for jump2 to play
            myscore+=1 #see scene1
            jump2()
    if jumped2 == False: #otherwise, if the criteria isn't hit, then you get the failure scene
        fail2()
                
    
def game(): #creates a function to use after the jump variable to continue looping infinitely
    for x in range (0,1):
        from random import randrange
        scene = randrange(1, 3) #Creates a random value between 1-2
        if scene == 1:
            scene1()
        if scene == 2:
            scene2()

def kill(): #this function is used to end the game if they don't want to play again
    quit() #quits the function

begingame()
kill()











