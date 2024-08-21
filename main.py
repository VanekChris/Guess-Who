import pygame
import random
import sys
from character import CharacterFaces
from mysteryface import MysteryFace
pygame.init()

WIDTH = 800
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess Who")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

rows = 4
cols = 5
space_x = WIDTH // (cols + 1)
space_y = HEIGHT // (rows * 2.75 + 1)

Adam_traits = ["white", "male", "blond hair", "short hair", "blue eyes", "glasses", "no hat", "no earrings", "no beard"] 
Alicia_traits = ["white", "woman", "blond hair", "long hair", "blue eyes", "no glasses", "no hat", "no earrings", "no beard"]
Chris_traits = ["white", "male", "black hair", "short hair", "brown eyes", "no glasses", "hat", "no earrings", "no beard"]
David_traits = ["white", "male", "black hair", "short hair", "green eyes", "hat", "no glasses", "no earrings", "no beard"]
Derek_traits = ["white", "male", "black hair", "short hair", "glasses", "beard", "no hat", "no earrings"]
Eric_traits = ["white", "male", "blond hair", "short hair", "brown eyes", "no beard", "no hat", "no earrings", "no glasses"]
Georgia_traits = ["black", "woman", "brown hair", "short hair", "brown eyes", "no beard", "no hat", "no earrings", "no glasses"]
Jack_traits = ["white", "male", "brown hair", "short hair", "blue eyes", "no beard", "no hat", "no earrings", "no glasses"]
Justin_traits = ["black", "male", "black hair", "short hiar", "brown eyes", "hat", "no beard", "no earrings", "no glasses"]
Kira_traits = ["white", "woman", "black hair", "long hair", "brown eyes", "no beard", "no hat", "no earrings", "no glasses"]
Kurt_traits = ["white", "male", "brown hair", "short hair", "blue eyes", "no beard", "no hat", "no earrings", "no glasses"]
Lynda_traits = ["white", "woman", "red hair", "long hair", "green eyes", "earrings", "no beard", "no hat", "no glasses"]
Mercedes_traits = ["black", "woman", "black hair", "long hair", "brown eyes", "earrings", "no beard", "no hat", "no glasses"]
Mike_traits = ["white", "male", "black hair", "short hair", "brown eyes", "no beard", "no hat", "no earrings", "no glasses"]
Nursery_traits = ["white", "male", "brown hair", "short hair", "green eyes", "curly hair", "beard", "no hat", "no earrings", "no glasses"]
Racheal_traits = ["white", "woman", "brown hair", "long hair", "brown eyes", "no beard", "no hat", "no earrings", "no glasses"]
Scott_traits = ["white", "man", "black hair", "short hair", "brown eyes", "no beard", "no hat", "no earrings", "no glasses"]
Styles_traits = ["white", "male", "brown hair", "short hair", "brown eyes", "no beard", "no hat", "no earrings", "no glasses"]
Suzanne_traits = ["white", "woman", "blond hair", "long hair", "brown eyes", "no beard", "no hat", "no earrings", "no glasses"]
Tina_traits = ["white", "woman", "black hair", "long hair", "brown eyes", "hat", "no beard", "no earrings", "no glasses"] 

character_pictures = ["Adam.jpg", "Alicia.jpg", "Chris.jpg", "David.jpg", "Derek.jpg", "Eric.jpg", "Georgia.jpg", "Jack.jpg", "Justin.jpg", "Kira.jpg", "Kurt.jpg", "Lynda.jpg", "Mercedes.jpg", "Mike.jpg", "Nursery.jpg", "Racheal.jpg", "Scott.jpg", "Styles.jpg", "Suzan.jpg", "Tina.jpg"]
character_traits = [Adam_traits, Alicia_traits, Chris_traits, David_traits, Derek_traits, Eric_traits, Georgia_traits, Jack_traits, Justin_traits, Kira_traits, Kurt_traits, Lynda_traits, Mercedes_traits, Mike_traits, Nursery_traits, Racheal_traits, Scott_traits, Styles_traits, Suzanne_traits, Tina_traits]

character_list = []

for i, face in enumerate(character_pictures):
    x = space_x * ((i % cols) + 1)
    y = space_y * ((i // cols) * 2 + 1)
    character = CharacterFaces(x, y, character_pictures[i], character_traits[i])
    character_list.append(character)
       
random_index = random.randint(0, len(character_traits) - 1)
random_trait = character_traits[random_index]
random_character = character_pictures[random_index]

mystery_person = MysteryFace(WIDTH // 2, HEIGHT - 100, random_character, random_trait)

def highlight_border(x, y, w, h):
    pygame.draw.rect(SCREEN, "red", (x, y, w, h), 2)
    return pygame.Rect(x, y, w, h)

def draw_text(text, color, font, x, y):
    img = font.render(text, True, color)
    SCREEN.blit(img, (x, y))

def pick_trait(check_trait, character_list):
    for character in character_list:
        if check_trait not in character.traits:
            character.turn_over()
            character.flip = True
    

flipped = False
run = True
while run:

    SCREEN.fill("black")
    for character in character_list:
        SCREEN.blit(character.image, character.rect)
    SCREEN.blit(mystery_person.image, mystery_person.rect)
    draw_text("skin", "white", font, 10, 551)
    draw_text("sex", "white", font, 10, 591)
    draw_text("hair", "white", font, 10, 631)
    draw_text("length", "white", font, 10, 671)
    draw_text("eyes", "white", font, 10, 711)
    draw_text("glasses", "white", font, 10, 751)
    draw_text("hat", "white", font, 120, 551)
    draw_text("beard", "white", font, 120, 591)
    draw_text("earrings", "white", font, 120, 631)

    skin = highlight_border(9, 550, 100, 30)
    sex = highlight_border(9, 590, 100, 30)
    hair = highlight_border(9, 630, 100, 30)
    length = highlight_border(9, 670, 100, 30)
    eyes = highlight_border(9, 710, 100, 30)
    glasses = highlight_border(9, 750, 100, 30)
    hat = highlight_border(119, 550, 100, 30)
    earrings = highlight_border(119, 630, 100, 30)
    beard = highlight_border(119, 590, 100, 30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mystery_person.rect.collidepoint(event.pos):
                flipped = True
                mystery_person.reveal(random_character)    
            
            if sex.collidepoint(event.pos):
                for trait in random_trait:
                    if trait == "male":
                        pick_trait("male", character_list)
                    elif trait == "woman":
                        pick_trait("woman", character_list)

            if skin.collidepoint(event.pos):
                for trait in random_trait:        
                    if trait == "white":
                        pick_trait("white", character_list)
                    elif trait == "black":
                        pick_trait("black", character_list)
                    
            if hair.collidepoint(event.pos):
                for trait in random_trait:
                    if trait == "blond hair":
                        pick_trait("blond hair", character_list)
                    elif trait == "black hair":
                        pick_trait("black hair", character_list)
                    elif trait == "brown hair":
                        pick_trait("brown hair", character_list)
                    elif trait == "red hair":
                        pick_trait("red hair", character_list)
                    
            if length.collidepoint(event.pos):
                for trait in random_trait:
                    if trait == "short hair":
                        pick_trait("short hair", character_list)
                    elif trait == "long hair":
                        pick_trait("long hair", character_list)
                    
            if eyes.collidepoint(event.pos):
                for trait in random_trait:
                    if trait == "blue eyes":
                        pick_trait("blue eyes", character_list)
                    elif trait == "green eyes":
                        pick_trait("green eyes", character_list)
                    elif trait == "brown eyes":
                        pick_trait("brown eyes", character_list)
                    
            if glasses.collidepoint(event.pos):
                for trait in random_trait:
                    if trait == "glasses":
                        pick_trait("glasses", character_list)
                    elif trait == "no glasses":
                        pick_trait("no glasses", character_list)

            if hat.collidepoint(event.pos):
                for trait in random_trait:
                    if trait == "hat":
                        pick_trait("hat", character_list)
                    elif trait == "no hat":
                        pick_trait("no hat", character_list)

            if beard.collidepoint(event.pos):
                for trait in random_trait:
                    if trait == "beard":
                        pick_trait("beard", character_list)
                    elif trait == "no beard":
                        pick_trait("no beard", character_list)

            if earrings.collidepoint(event.pos):
                for trait in random_trait:
                    if trait == "earrings":
                        pick_trait("earrings", character_list)
                    elif trait == "no earrings":
                        pick_trait("no earrings", character_list)
            
            for face in character_list:
                if face.rect.collidepoint(event.pos):
                    face.turn_over()
                    
    if pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pressed()
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit(0)