import pygame
pygame.init()
#class gameFrame:
#initializing the pygame interface
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Pong The Greatest")

#Creating the pattles
pColor = (100,100,100)
bColor = (250,250,250)

#height and width of the screen
width = screen.get_width()
height = screen.get_height()

#run variable so the game can start
run = True

#Creating the score and the player labels
score = 0

#Making the font for the title
fontPath = r"C:\Users\morys_txn4i9v\.vscode\projects\PongTheGreatest\PongTheGreatest\bit5x5.ttf"
textFont = pygame.font.Font(fontPath,70)

#function to make text
def drawText(text,font,textColor,x,y):
    img = font.render(text,True,textColor)
    screen.blit(img,(x,y))

#making the button


nonHoverColor = (170,170,170)
hoverColor = (100,100,100)

text = textFont.render('quit',True, nonHoverColor)

    
#Drawing the title and score
drawText("PONG THE GREATEST",textFont,(250,250,250),width - (width - width / 11),20)
pygame.display.update()
    
#Code for the game screen
#screen.fill("black")
    #Drawing the title and score
    #drawText("PONG THE GREATEST",textFont,(250,250,250),220,20)
    #The player paddle
padOne = pygame.draw.rect(screen,bColor,pygame.Rect(20,height/2.5,20,150),30)

    #The Ai paddle
padTwo = pygame.draw.rect(screen,bColor,pygame.Rect(width - 45,height/2.5,20,150),30)

    #The ball
ball = pygame.draw.rect(screen,bColor,pygame.Rect(width/2.1,height/2,30,30),20)
pygame.display.flip()



#Running the screen for the game

while run:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False
            pygame.display.flip()
pygame.quit()
