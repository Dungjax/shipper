from pygame import sprite, transform
from sprite_importer import importImage
from pymunk import Body, Circle, Space, Vec2d
from math import degrees

tireSprite = importImage("assets/tire.png").convert_alpha()

class Tire(sprite.Sprite):
    def __init__(self, _group: sprite.LayeredUpdates, _position: Vec2d, _space: Space) -> None:
        super().__init__()
        #game
        self.isColliding = False
        #physics
        mass = 1
        self.body = Body(mass=mass, moment=200*mass, body_type=Body.DYNAMIC)
        self.body.position = _position

        self.shape = Circle(self.body, radius=tireSprite.get_width() // 2)
        self.shape.elasticity = 0.25
        self.shape.friction = 10

        _space.add(self.body, self.shape)

        self.collisionHandle = _space.add_collision_handler(0, 0)
        self.collisionHandle.begin = self.collsionBegin
        self.collisionHandle.pre_solve = self.collisionPreSolve
        self.collisionHandle.post_solve = self.collisionPostSovle
        self.collisionHandle.separate = self.collisionSeparate
        #sprite
        self.image = tireSprite
        self.rect = self.image.get_rect()
        self.rect.center = self.body.position

        _group.add(self)
        _group.move_to_back(self)
    
    def update(self, translated):
        self.image = transform.rotate(tireSprite, -degrees(self.body.angle))
        self.rect = self.image.get_rect()
        self.rect.center = self.body.position - Vec2d(translated.tx, 0)

        self.body.angular_velocity = 20
        pass

    def collsionBegin(self, arbiter, space, data):
        
        return True

    def collisionPreSolve(self, arbiter, space, data):
        self.isColliding = True
        return True

    def collisionPostSovle(self, arbiter, space, data):
        
        return True

    def collisionSeparate(self, arbiter, space, data):
        self.isColliding = False
        return True