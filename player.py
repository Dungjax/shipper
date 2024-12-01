from pygame import sprite, Vector2, transform
from sprite_importer import importImage
from pymunk import Body, Poly, Space, constraints
from bike import Bike

shipperSrpite = importImage("assets/shipper.png").convert_alpha()

class Player(sprite.Sprite):
    def __init__(self, _group: sprite.Group, _position: Vector2, _space: Space) -> None:
        super().__init__()

        #sprite
        self.image = shipperSrpite
        self.rect = self.image.get_rect()
        self.rect.center = _position

        #physics
        


    def update(self):
        self.rect.center = self.body.position
        pass

    def draw(self):
        pass