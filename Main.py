
from final import fullNote
#import cv2
#import numpy as np
#import imutils
import math
import os
import pygame
pygame.init()

##########################################################

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (200,200,0)

light_green = (0,150,0)


#update game kolaha
#pygame.display.flip()

#update el 7ta el 3yzhaa bs lw edenaalo parameter
#pygame.display.update()

A0 = pygame.mixer.Sound('Piano.ff.A4.wav')
B0 = pygame.mixer.Sound('Piano.ff.B4.wav')
C0 = pygame.mixer.Sound('Piano.ff.C4.wav')
D0 = pygame.mixer.Sound('Piano.ff.D4.wav')
E0 = pygame.mixer.Sound('Piano.ff.E4.wav')
F0 = pygame.mixer.Sound('Piano.ff.F4.wav')
G0 = pygame.mixer.Sound('Piano.ff.G4.wav')
A1 = pygame.mixer.Sound('Piano.ff.A5.wav')
B1 = pygame.mixer.Sound('Piano.ff.B5.wav')
C1 = pygame.mixer.Sound('Piano.ff.C5.wav')
D1 = pygame.mixer.Sound('Piano.ff.D5.wav')
E1 = pygame.mixer.Sound('Piano.ff.E5.wav')
F1 = pygame.mixer.Sound('Piano.ff.F5.wav')
G1 = pygame.mixer.Sound('Piano.ff.G5.wav')


display_width = 800
display_height  = 600

game = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Music App")

gameExit = False
intro = True

lead_x = 300
lead_y = 300

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

img = pygame.image.load('kb.jpeg')

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()
    
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    game.blit(textSurf, textRect)

def text_to_button(msg , color , x , y , w , h , size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = ( (x+(w/2) ) , (y+ (h/2) ) )
    game.blit(textSurf, textRect)
	
def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(game, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                #gameExit = True
                pass
				
            if action == "play":
                #intro = False
                pass
    else:
        pygame.draw.rect(game, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

font = pygame.font.Font(None, 32) 
input_box = pygame.Rect(100, 100, 140, 32)
input_box.center = (display_width / 2)+ 50 , (display_height / 2)+ 50
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
	
	
l = [ "qG0" , "qG0" , "qG0" , "qD0" , "qE0" , "qE0" , "hD0" , "qB1" , "qB1" , "qA0" , "qA0" ]
	
while not gameExit:

    for event in pygame.event.get():
	
        if event.type==pygame.QUIT:
            gameExit = True 
            
        if event.type == pygame.MOUSEBUTTONDOWN:
			# If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
				# Toggle the active variable.
                active = not active
            else:
                active = False
			# Change the current color of the input box.
            color = color_active if active else color_inactive
		
        if event.type == pygame.KEYDOWN:
            keyname = pygame.key.name(event.key)
            #print (keyname)
			
            if event.key==pygame.K_ESCAPE:
                print ("bye")
                gameExit = True
                

            if intro : 
                if event.key == pygame.K_UP:
                    intro = False

                
                if event.key == pygame.K_DOWN:
                    gameExit = True

                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        path = text
                        os.system("detection.py")
                        print("here")
                        print(fullNote)
                        l = []
                        l = fullNote
			
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                     			
                    else:
                        text += event.unicode
			
            if not intro : 
			
                if event.key == pygame.K_LEFT:
                    print("left")
                    lead_x = lead_x - 10
                
                if event.key == pygame.K_RIGHT:
                    print("right")
                    lead_x = lead_x + 10     
                
                if event.key == pygame.K_UP:
                    print("up")
                    lead_y = lead_y - 10
                
                if event.key == pygame.K_DOWN:
                    print("down")
                    lead_y = lead_y + 10
			
                if event.key == pygame.K_a:
                    print("Hey, you pressed 'Do'!")
                    ch = C0.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_s:
                    print("Hey, you pressed 'Re'!")
                    ch = D0.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_d:
                    print("Hey, you pressed , 'Me'!")
                    ch = E0.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_f:
                    print("Hey, you pressed , 'Fa'!")
                    ch = F0.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_g:
                    print("Hey, you pressed , 'Sol'!")
                    ch = G0.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_h:
                    print("Hey, you pressed , 'La'!")
                    ch = A0.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
						
                if event.key == pygame.K_j:
                    print("Hey, you pressed , 'Si'!")
                    ch = B0.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
						
                if event.key == pygame.K_w:
                    print("Hey, you pressed , 'Do'!")
                    ch = C1.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_e:
                    print("Hey, you pressed , 'Re'!")
                    ch = D1.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_r:
                    print("Hey, you pressed , 'Me'!")
                    ch = E1.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_t:
                    print("Hey, you pressed , 'Fa'!")
                    ch = F1.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_y:
                    print("Hey, you pressed , 'Sol'!")
                    ch = G1.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_u:
                    print("Hey, you pressed , 'La'!")
                    ch = A1.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
						
                if event.key == pygame.K_i:
                    print("Hey, you pressed , 'Si'!")
                    ch = B1.play(loops=0, maxtime=2000, fade_ms=0)
                    while ch.get_busy():
                        pygame.time.delay(10)
					
                if event.key == pygame.K_z:
                    message_to_screen("Hi there , press C to play again or Q to quit", red)
                    pygame.display.update()
                    pygame.time.delay(1000)
						   
                if event.key == pygame.K_x:
                    print("Hey, you pressed 'x'")
                    for i in l :
                        if i.startswith('q'):
                            note = i.replace('q','')
                            ch = eval(note).play(loops=0, maxtime=1000, fade_ms=0)
                            while ch.get_busy():
                                pygame.time.delay(5)
								
                        elif i.startswith('h'):
                            note = i.replace('h','')
                            ch = eval(note).play(loops=0, maxtime=2000, fade_ms=0)
                            while ch.get_busy():
                                pygame.time.delay(5)
						
                        elif i.startswith('f'):
                            note = i.replace('f','')
                            ch = eval(note).play(loops=0, maxtime=4000, fade_ms=0)
                            while ch.get_busy():
                                pygame.time.delay(5)
                    print ("Done")	
				

    if intro :
        game.fill(white)
        message_to_screen("Welcome to Music App", green, -200, "medium")
        message_to_screen("The objective of the App is to read musical sheet", black, -140)
        message_to_screen("You can also play piano on your keyboard", black,  -100)
        message_to_screen("     Up arrow to play              Down arrow to quit.",  black, 220)
        message_to_screen("first write the picture name with its path ",  black, 0)
        message_to_screen("write here -->                                  ",  black, 50)
        message_to_screen("press enter , and here we go to play !",  black, 100)
		
        button("Hey !"  , 200 , 450 , 100 , 50 ,green , light_green , "play" )
        button("bye ? " , 500  , 450 , 100 , 50 , green , light_green , "quit" )
		
		
		# Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max( 200, txt_surface.get_width()+10 )
        input_box.w = width
        # Blit the text.
        game.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(game, color, input_box, 2)
		
        pygame.display.update()
        
    else :
	
	
        game.fill(white)
        #our graphic
        #pygame.draw.rect(game , black , [lead_x,lead_y,10,10])
	
	
        message_to_screen("Welcome to Music App", green, -200, "medium")
        message_to_screen("press to play piano", black, 0)
        message_to_screen("press x to hear your picture music ", black, -100)
        message_to_screen("", black, -50 )
        
		
		
        rest = img.get_rect()
        rest.center = (display_width / 2 ), (display_height / 2 + 150 )
        game.blit(img, rest)
	
        pygame.display.update()    



pygame.quit()
quit()
