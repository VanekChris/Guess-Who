import pygame

class CharacterFaces:

    def __init__(self, x, y, face, traits):
        self.x = x
        self.y = y
        self.face = face
        self.traits = traits
        self.image = pygame.image.load(face)
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.flip = False

    def turn_over(self):
        self.flip = True
        self.image = pygame.image.load("flipped_card.jpg")
        
    #def stay(self):
     #   self.image = pygame.image.load(self.face)
      #  self.image = pygame.transform.scale(self.image, (125, 125))