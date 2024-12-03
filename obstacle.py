from pygame import sprite, transform
from pymunk import Body, Circle, Space
from sprite_importer import importImage
from enums import ShapeType
from math import degrees
from random import randint

tireSprite = importImage("assets/tire.png").convert_alpha()

class Obstacle(sprite.Sprite):
    def __init__(self, group: sprite.LayeredUpdates, position, space: Space) -> None:
        super().__init__()
        #sprite
        size = randint(30, 90)
        self.fixedImage = transform.scale(tireSprite, (size, size))
        self.image = self.fixedImage
        self.rect = self.image.get_rect()
        self.fixedPosition = position
        self.rect.center = position

        group.add(self)
        #physics
        self.space = space
        mass = 5
        self.body = Body(mass=mass, moment=450*mass, body_type=Body.DYNAMIC)
        self.body.position = position
        self.shape = Circle(self.body, self.image.get_width() // 2)
        self.shape.elasticity = 0.5
        self.shape.friction = 1
        self.shape.collision_type = ShapeType.OBSTACLE.value

        space.add(self.body, self.shape)
    
    def update(self, translated):
        self.image = transform.rotate(self.fixedImage, -degrees(self.body.angle))
        self.rect = self.image.get_rect()
        self.rect.center = (self.body.position[0] - translated.tx, self.body.position[1])

        if self.rect.right < 0:
            self.kill()
            self.space.remove(self.body, self.shape)
        
        self.body._set_angular_velocity(-10)

        pass