import pygame
import random
from twister.twister import generate_number
from twister.twister import generate_randomness
pygame.init()

#dictionary
choices = {
    "rock": {"rock":"draw", "scissors":"win", "paper":"lose"},
    "paper": {"paper":"draw", "scissors":"lose", "rock":"win"},
    "scissors": {"scissors":"draw", "paper":"win", "rock":"lose"}
}
aiDict = {
    1:"rock",
    2:"scissors",
    3:"paper"
}

# Screen setup
screenWidth = 900
screenHeight = int(screenWidth * 0.5625)
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Main Menu")

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
button_col = (255, 0, 0)
hover_col = (75, 225, 255)
click_col = (50, 150, 255)
text_col = (0, 0, 0)

# ranNum = random.randint(1,3)
# if ranNum == 1:
#     aiSelection = "rock"
# if ranNum == 2:
#     aiSelection = "scissors"
# if ranNum == 3:
#     aiSelection = "paper"

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


# buttons
rock = Button(screenWidth/7, screenHeight/2, 200, 150, "Rock")
scissors = Button(screenWidth/2.5, screenHeight/2, 200, 150, "Scissors")
paper = Button(screenWidth/1.5, screenHeight/2, 200, 150, "Paper")
playAgain = Button(screenWidth/3, screenHeight/1.3, 200, 150, "Player Again")

# main loop
main = True
game = False
clicked = False

#ai
aiSelecting = True
scope = True
thingy = True
while thingy:
    while main:
        global playerSelection
        global aiSelection
        screen.fill(white)

        if aiSelecting:
            random_numbers = generate_number()
            aiSelecting = False
        
        if scope:
            randomness = generate_randomness()
            randomness = int(randomness[0])
            scope = False
        
        if aiSelecting is False and scope is False:
            aiChoice = random_numbers[randomness]
            aiSelection = aiDict[aiChoice]
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False

        if rock.draw_button():
            playerSelection = "rock"
            game = True
            main = False
        if scissors.draw_button():
            playerSelection = "scissors"
            game = True
            main = False
        if paper.draw_button():
            playerSelection = "paper"
            game = True
            main = False

        pygame.display.flip()

    while game:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        #Better dictionary win handler
        win = choices[playerSelection][aiSelection]

        # OBSELETE WIN HANDLER
        # if playerSelection == "rock":
        #     if aiSelection == "rock":
        #         win = "draw"
        #     elif aiSelection == "scissors":
        #         win = "win"
        #     elif aiSelection == "paper":
        #         win = "lose"
        # elif playerSelection == "paper":
        #     if aiSelection == "paper":
        #         win = "draw"
        #     elif aiSelection == "rock":
        #         win = "win"
        #     elif aiSelection == "scissors":
        #         win = "lose"
        # elif playerSelection == "scissors":
        #     if aiSelection == "scissors":
        #         win = "draw"
        #     elif aiSelection == "paper":
        #         win = "win"
        #     elif aiSelection == "rock":
        #         win = "lose"

        if win == "draw":
            endText = ("You Selected ", playerSelection, "Your Opponent Selected", aiSelection, "The Game Is A Draw.")
        elif win == "lose":
            endText = ("You Selected ", playerSelection, "Your Opponent Selected", aiSelection, "The Game Is A Loss.")
        elif win == "win":
            endText = ("You Selected ", playerSelection, "Your Opponent Selected", aiSelection, "The Game Is A Win.")
        else:
            print('error')
        

    
        finalText = font.render(str(endText), True, black)
        textRect = finalText.get_rect()
        textRect.center = (screenHeight/2, screenWidth/3)
        screen.blit(finalText, textRect)

        if playAgain.draw_button():
            # reset game variables
            playerSelection = None
            aiSelection = None
            main = True
            game = False 
            aiSelecting = True
            scope = True

        pygame.display.flip()
    
        
pygame.quit()