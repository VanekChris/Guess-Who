import pygame
import random

Adam_traits = ["white", "male", "blond hair", "short hair", "blue eyes", "glasses"] 
Alicia_traits = ["white", "woman", "blond hair", "long hair", "blue eyes"]
Chris_traits = ["white", "male", "black hair", "short hair", "brown eyes", "hat"]
David_traits = ["white", "male", "black hair", "short hair", "green eyes", "hat"]
Derek_traits = ["white", "male", "black hair", "short hair", "glasses", "beard"]
Eric_traits = ["white", "male", "blond hair", "short hair", "brown eyes"]
Georgia_traits = ["black", "woman", "brown hair", "short hair", "brown eyes"]
Jack_traits = ["white", "male", "brown hair", "short hair", "blue eyes"]
Justin_traits = ["black", "male", "black hair", "short hiar", "brown eyes", "hat"]
Kira_traits = ["white", "woman", "black hair", "long hair", "brown eyes"]
Kurt_traits = ["white", "male", "brown hair", "short hair", "blue eyes"]
Lynda_traits = ["white", "woman", "red hair", "long hair", "green eyes", "earrings"]
Mercedes_traits = ["black", "woman", "black hair", "long hair", "brown eyes", "earrings"]
Mike_traits = ["white", "male", "black hair", "short hair", "brown eyes"]
Nursery_traits = ["white", "male", "brown hair", "short hair", "green eyes", "curly hair", "beard"]
Racheal_traits = ["white", "woman", "brown hair", "long hair", "brown eyes"]
Scott_traits = ["white", "man", "black hair", "short hair", "brown eyes"]
Styles_traits = ["white", "male", "brown hair", "short hair", "brown eyes"]
Suzanne_traits = ["white", "woman", "blond hair", "long hair", "brown eyes"]
Tina_traits = ["white", "woman", "black hair", "long hair", "brown eyes", "hat"] 

character_pictures = ["Adam.jpg", "Alicia.jpg", "Chris.jpg", "David.jpg", "Derek.jpg", "Eric.jpg", "Georgia.jpg", "Jack.jpg", "Justin.jpg", "Kira.jpg", "Kurt.jpg", "Lynda.jpg", "Mercedes.jpg", "Mike.jpg", "Nursery.jpg", "Racheal.jpg", "Scott.jpg", "Styles.jpg", "Suzan.jpg", "Tina.jpg"]
character_traits = [Adam_traits, Alicia_traits, Chris_traits, David_traits, Derek_traits, Eric_traits, Georgia_traits, Jack_traits, Justin_traits, Kira_traits, Kurt_traits, Lynda_traits, Mercedes_traits, Mike_traits, Nursery_traits, Racheal_traits, Scott_traits, Styles_traits, Suzanne_traits, Tina_traits]
random_index = random.randint(0, len(character_traits) - 1)
random_trait = character_traits[random_index]
random_character = character_pictures[random_index]

class MysteryFace:

    def __init__(self, x, y, iamge, trait):
        super().__init__()
        self.x = x
        self.y = y
        self.trait = trait
        self.image = pygame.image.load("mystery-person.jpg")
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def reveal(self, image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (125, 125))

    