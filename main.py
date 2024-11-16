import pygame
import random
from twister.twister import random_numbers
pygame.init()

# Screen setup
screenWidth = 1280
screenHeight = int(screenWidth * 0.5625)
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Main Menu")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
button_col = (255, 0, 0)
hover_col = (75, 225, 255)
click_col = (50, 150, 255)
text_col = (0, 0, 0)

# Initialize variables
playerWin = -1 
aiSelection = ""  
playerSelection = "rock" 
endText = ""

# Font
font = pygame.font.Font(None, 40)

# Button Class
class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw_button(self):
        global clicked
        action = False
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Button states
        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:  # Left-click
                pygame.draw.rect(screen, click_col, button_rect)
                clicked = True
            else:
                pygame.draw.rect(screen, hover_col, button_rect)
                if clicked:  # Release after clicking
                    clicked = False
                    action = True
        else:
            pygame.draw.rect(screen, button_col, button_rect)

        # Render text
        text_img = font.render(self.text, True, text_col)
        text_len = text_img.get_width()
        screen.blit(
            text_img,
            (self.x + self.width // 2 - text_len // 2, self.y + self.height // 4),
        )
        return action


# Buttons
rock = Button(200, 200, 200, 150, "Rock")
scissors = Button(800, 200, 200, 150, "Scissors")
paper = Button(500, 400, 200, 150, "Paper")

# Main Loop
main = True
game = False
clicked = False
while main:
    screen.fill(white)  # Clear screen

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False

    # Draw buttons and handle actions
    if rock.draw_button():
        playerSelection = rock
        game = True
        main = False
    if scissors.draw_button():
        playerSelection = scissors
        game = True
        main = False
    if paper.draw_button():
        playerSelection = paper
        game = True
        main = False

    pygame.display.flip()  # Update display

while game:
    screen.fill(white)  # Clear screen

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
    
    ranNum = random.randint(1,3)
    if ranNum == 1:
        aiSelection = rock
    if ranNum == 2:
        aiSelection = scissors
    if ranNum == 1:
        aiSelection = paper

    if playerSelection is rock and aiSelection is rock or playerSelection is paper and aiSelection is paper or playerSelection is scissors and aiSelection is scissors:
        playerWin = 2
    if playerSelection is rock and aiSelection is scissors or playerSelection is paper and aiSelection is rock or playerSelection is scissors and aiSelection is paper:
        playerWin = 1
    if playerSelection is rock and aiSelection is paper or playerSelection is paper and aiSelection is scissors or playerSelection is scissors and aiSelection is rock:
        playerWin = 0

    if playerWin == 2:
        endText = ("You Selected ", playerSelection, "Your Opponent Selected", aiSelection, "The Game Is A Draw.")
    if playerWin == 1:
        endText = ("You Selected ", playerSelection, "Your Opponent Selected", aiSelection, "The Game Is A Loss.")
    if playerWin == 2:
        endText = ("You Selected ", playerSelection, "Your Opponent Selected", aiSelection, "The Game Is A Win.")
    else:
        print('error')

    finalText = font.render(endText, True, black)
    textRect = finalText.get_rect()
    textRect.center = (400 // 2, 400 // 2)
    screen.blit(finalText, textRect)

    pygame.display.flip()
    
        
pygame.quit()
