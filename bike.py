from pygame import sprite, transform
from sprite_importer import importImage
from pymunk import Body, Poly, Space, Vec2d, Transform
from pymunk.constraints import DampedSpring, GrooveJoint
from tire import Tire
from math import degrees

bikeSrpite = importImage("assets/bike_full.png").convert_alpha()

class Bike(sprite.Sprite):
    def __init__(self, _group: sprite.LayeredUpdates, _position: Vec2d, _space: Space) -> None:
        super().__init__()

        #sprite
        self.image = bikeSrpite
        self.rect = self.image.get_rect()
        self.fixedPosition = _position
        self.rect.center = _position

        _group.add(self)
        #physics
        mass = 5
        self.body = Body(mass=mass, moment=450*mass, body_type=Body.DYNAMIC)
        self.body.position = _position

        self.shape = Poly.create_box(self.body, size=(self.image.get_width(), self.image.get_height() // 4))
        #tire
        length = self.image.get_width() // 2
        frontOffset = self.image.get_width() // 2.2
        backOffset = self.image.get_width() // 3

        frontTirePosition = self.body.position + Vec2d(self.image.get_width() // 2.3, self.image.get_height() // 2.2)
        self.frontTire = Tire(_group, frontTirePosition, _space)
        self.frontTireDampedSpring = DampedSpring(self.body, self.frontTire.body, anchor_a=(frontOffset, 0), anchor_b=(0, 0), rest_length=length, stiffness=200, damping=10)
        self.frontTireDampedSpring._set_max_force(10000)
        self.frontTireGroveJoint = GrooveJoint(self.body, self.frontTire.body, groove_a=(frontOffset, 0), groove_b=(frontOffset, length), anchor_b=(0, 0))

        backTirePosition = self.body.position + Vec2d(-self.image.get_width() // 2.6, self.image.get_height() // 2.2)
        self.backTire = Tire(_group, backTirePosition, _space)
        self.backTireDampedSpring = DampedSpring(self.body, self.backTire.body, anchor_a=(-backOffset, 0), anchor_b=(0, 0), rest_length=length, stiffness=200, damping=10)
        self.backTireDampedSpring._set_max_force(10000)
        self.backTireGroveJoint = GrooveJoint(self.body, self.backTire.body, groove_a=(-backOffset, 0), groove_b=(-backOffset, length), anchor_b=(0, 0))

        _space.add(self.body, self.shape, self.frontTireDampedSpring, self.frontTireGroveJoint, self.backTireDampedSpring, self.backTireGroveJoint)

    def input(self, isPressed: bool):
        if isPressed:
            if self.backTire.isColliding:
                self.body.apply_impulse_at_local_point((-self.body.mass * 30, -self.body.mass * 600))

    def update(self, translated):
        self.image = transform.rotate(bikeSrpite, -degrees(self.body.angle))
        self.rect = self.image.get_rect()
        self.rect.center = self.body.position - Vec2d(translated.tx, 0)

        pass

    def draw(self):
        pass