import pygame
import sys
from twister.twister import generate_number, generate_randomness

pygame.init()

aiSelecting = True
scope = True
clicked = False

# dictionaries
choices = {
    "rock": {"rock": "draw", "scissors": "win", "paper": "lose"},
    "paper": {"paper": "draw", "scissors": "lose", "rock": "win"},
    "scissors": {"scissors": "draw", "paper": "win", "rock": "lose"},
}
aiDict = {1: "rock", 2: "scissors", 3: "paper"}

# screen
screenWidth = 1280
screenHeight = int(screenWidth * 0.5625)
screen = pygame.display.set_mode((screenWidth, screenHeight))

# colours
white = (255, 255, 255)
black = (0, 0, 0)
button_col = (255, 0, 0)
hover_col = (75, 225, 255)
click_col = (50, 150, 255)
text_col = (0, 0, 0)

# font
font = pygame.font.Font(None, 40)

# global variables
playerSelection = None
aiSelection = None

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

        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(screen, click_col, button_rect)
                clicked = True
            else:
                pygame.draw.rect(screen, hover_col, button_rect)
                if clicked:
                    clicked = False
                    action = True
        else:
            pygame.draw.rect(screen, button_col, button_rect)

        text_img = font.render(self.text, True, text_col)
        text_len = text_img.get_width()
        screen.blit(
            text_img,
            (self.x + self.width // 2 - text_len // 2, self.y + self.height // 4),
        )
        return action


# buttons
rock = Button(screenWidth / 7, screenHeight / 2, 200, 150, "Rock")
scissors = Button(screenWidth / 2.5, screenHeight / 2, 200, 150, "Scissors")
paper = Button(screenWidth / 1.5, screenHeight / 2, 200, 150, "Paper")
playAgain = Button(screenWidth / 2.5, screenHeight / 2, 200, 150, "Play Again")


class Main:
    def __init__(self):
        self.stateManager = StateManager("select")
        self.select = SelectScene(screen, self.stateManager)
        self.results = ResultScene(screen, self.stateManager)
        self.states = {"select": self.select, "result": self.results}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.states[self.stateManager.get_state()].run()
            pygame.display.update()


class SelectScene:
    def __init__(self, display, stateManager):
        self.display = display
        self.stateManager = stateManager

    def run(self):
        global playerSelection, aiSelection, aiSelecting, scope
        global random_numbers, randomness
        screen.fill(white)
        aiSelecting = True
        scope = True

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

        #buttons
        if rock.draw_button():
            playerSelection = "rock"
            self.stateManager.set_state("result")
        if scissors.draw_button():
            playerSelection = "scissors"
            self.stateManager.set_state("result")
        if paper.draw_button():
            playerSelection = "paper"
            self.stateManager.set_state("result")


class ResultScene:
    def __init__(self, display, stateManager):
        self.display = display
        self.stateManager = stateManager

    def run(self):
        global playerSelection, aiSelection
        screen.fill(white)

        # determine result
        win = choices[playerSelection][aiSelection]
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
        textRect.center = (screenHeight/1.2, screenWidth/5)
        screen.blit(finalText, textRect)

        if playAgain.draw_button():
            self.stateManager.set_state("select")

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



class StateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state


if __name__ == "__main__":
    runn = Main()
    runn.run()
