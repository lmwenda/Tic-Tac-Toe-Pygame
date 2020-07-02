space = ""
line = "________________" * 4

print(line)
print(space)

import pygame

# Name, Screen and Initializing the game
print(line)
pygame.init()

print(space)
connected = "[CONNECTED] The User has joined the game."

print(connected)

title = pygame.display.set_caption("Tic Tac Toe")
HEIGHT, WIDTH = 550, 550
screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Drawing Shapes and Mainloop
first = pygame.draw.rect(screen, (255, 255, 255), (25, 25, 150, 150))
second = pygame.draw.rect(screen, (255, 255, 255), (200, 25, 150, 150))
third = pygame.draw.rect(screen, (255, 255, 255), (375, 25, 150, 150))
    
fourth = pygame.draw.rect(screen, (255, 255, 255), (25, 200, 150 ,150))
fifth = pygame.draw.rect(screen, (255, 255, 255), (200, 200, 150, 150))
sixth = pygame.draw.rect(screen, (255, 255, 255), (375, 200, 150, 150))
    
seventh = pygame.draw.rect(screen, (255, 255, 255), (25, 375, 150, 150))
eighth = pygame.draw.rect(screen, (255, 255, 255), (200, 375, 150, 150))
ninth = pygame.draw.rect(screen, (255, 255, 255), (375, 375, 150, 150))

run = True
draw_object = 'rect'

# Grid One Shape Click System Var
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

while run:
    pygame.time.delay(100)
 
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            run = False
            disconnected = "[DISCONNECTED] The user has left the game."
            print(disconnected)
            print(line)
            screen.fill((255, 255, 255))

        # Space Bar Reset
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                first_open = True
                second_open = True
                third_open = True
                fourth_open = True
                fifth_open = True
                sixth_open = True
                seventh_open = True
                eighth_open = True
                ninth_open = True

                first = pygame.draw.rect(screen, (255, 255, 255), (25, 25, 150, 150))
                second = pygame.draw.rect(screen, (255, 255, 255), (200, 25, 150, 150))
                third = pygame.draw.rect(screen, (255, 255, 255), (375, 25, 150, 150))
                    
                fourth = pygame.draw.rect(screen, (255, 255, 255), (25, 200, 150 ,150))
                fifth = pygame.draw.rect(screen, (255, 255, 255), (200, 200, 150, 150))
                sixth = pygame.draw.rect(screen, (255, 255, 255), (375, 200, 150, 150))
                    
                seventh = pygame.draw.rect(screen, (255, 255, 255), (25, 375, 150, 150))
                eighth = pygame.draw.rect(screen, (255, 255, 255), (200, 375, 150, 150))
                ninth = pygame.draw.rect(screen, (255, 255, 255), (375, 375, 150, 150))
                               
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if first.collidepoint(pos) and first_open:
                if draw_object == 'rect':
                   pygame.draw.rect(screen, (0, 170, 200), (50, 50, 100, 100))
                   draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (225, 0, 0), (100, 100), 50)
                    draw_object = 'rect'
                first_open = False
                    
                
            if second.collidepoint(pos) and second_open:
                if draw_object == 'rect':
                   pygame.draw.rect(screen, (0, 170, 200), (225, 50, 100, 100))
                   draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (225, 0, 0), (275, 100), 50)
                    draw_object = 'rect'
                second_open = False
                
            if third.collidepoint(pos) and third_open:
                if draw_object == 'rect':
                   pygame.draw.rect(screen, (0, 170, 200), (400, 50, 100, 100))
                   draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (225, 0, 0), (450, 100), 50)
                    draw_object = 'rect'
                third_open = False
            
            if fourth.collidepoint(pos)and fourth_open :
                if draw_object == 'rect':
                   pygame.draw.rect(screen, (0, 170, 200), (50, 225, 100, 100))
                   draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (225, 0, 0), (100, 275), 50)
                    draw_object = 'rect'
                fourth_open = False
                
            if fifth.collidepoint(pos) and fifth_open:
                if draw_object == 'rect':
                   pygame.draw.rect(screen, (0, 170, 200), (225, 225, 100, 100))
                   draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (225, 0, 0), (275, 275), 50)
                    draw_object = 'rect'
                fifth_open = False
            
            if sixth.collidepoint(pos) and sixth_open:
                if draw_object == 'rect':
                   pygame.draw.rect(screen, (0, 170, 200), (400, 225, 100, 100))
                   draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (225, 0, 0), (450, 275), 50)
                    draw_object = 'rect'
                sixth_open = False

            if seventh.collidepoint(pos)and seventh_open:
                if draw_object == 'rect':
                   pygame.draw.rect(screen, (0, 170, 200), (50, 400, 100, 100))
                   draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (225, 0, 0), (100, 450), 50)
                    draw_object = 'rect'
                seventh_open = False
                
            if eighth.collidepoint(pos) and eighth_open:
                if draw_object == 'rect':
                   pygame.draw.rect(screen, (0, 170, 200), (225, 400, 100, 100))
                   draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (225, 0, 0), (275, 450), 50)
                    draw_object = 'rect'
                eighth_open = False
                
            if ninth.collidepoint(pos) and ninth_open:
                if draw_object == 'rect':
                   pygame.draw.rect(screen, (0, 170, 200), (400, 400, 100, 100))
                   draw_object = 'circle'
                else:
                    pygame.draw.circle(screen, (225, 0, 0), (450, 450), 50)
                    draw_object = 'rect'
                ninth_open = False
            
    # Display Update
    pygame.display.update()
         
pygame.quit()

