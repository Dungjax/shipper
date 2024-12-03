from pygame import sprite, transform
from sprite_importer import bikeSrpite
from pymunk import Body, Circle, Space, Vec2d
from pymunk.constraints import DampedSpring, GrooveJoint
from tire import Tire
from math import degrees
from enums import ShapeType

class Bike(sprite.Sprite):
    def __init__(self, group: sprite.LayeredUpdates, position: Vec2d, space: Space) -> None:
        super().__init__()
        #game properies
        self.isDied = False
        
        #sprite
        self.image = bikeSrpite
        self.rect = self.image.get_rect()
        self.fixedPosition = position
        self.rect.center = position

        group.add(self)
        #physics
        mass = 4
        self.body = Body(mass=mass, moment=450*mass, body_type=Body.DYNAMIC)
        self.body.position = position

        #self.shape = Poly.create_box(self.body, size=(self.image.get_width(), self.image.get_height() // 4))
        self.shape = Circle(self.body, self.image.get_width() // 4)
        self.shape.collision_type = ShapeType.PLAYER.value

        self.collisionHandle = space.add_collision_handler(ShapeType.PLAYER.value, ShapeType.GROUND.value)
        self.collisionHandle._set_begin(self.collsionBegin)
        #tire
        length = self.image.get_width() // 2
        frontOffset = self.image.get_width() // 2.2
        backOffset = self.image.get_width() // 3
        stiffness = 500
        maxForce = 10000
        #front
        frontTirePosition = self.body.position + Vec2d(self.image.get_width() // 2.3, self.image.get_height() // 2.2)
        self.frontTire = Tire(group, frontTirePosition, space)
        self.frontTireDampedSpring = DampedSpring(self.body, self.frontTire.body, anchor_a=(frontOffset, 0), anchor_b=(0, 0), rest_length=length, stiffness=stiffness, damping=10)
        #self.frontTireDampedSpring._set_max_force(maxForce)
        self.frontTireGroveJoint = GrooveJoint(self.body, self.frontTire.body, groove_a=(frontOffset, 0), groove_b=(frontOffset, length), anchor_b=(0, 0))
        self.frontTireGroveJoint._set_max_force(maxForce)
        #back
        backTirePosition = self.body.position + Vec2d(-self.image.get_width() // 2.6, self.image.get_height() // 2.2)
        self.backTire = Tire(group, backTirePosition, space)
        self.backTireDampedSpring = DampedSpring(self.body, self.backTire.body, anchor_a=(-backOffset, 0), anchor_b=(0, 0), rest_length=length, stiffness=stiffness, damping=10)
        #self.backTireDampedSpring._set_max_force(maxForce)
        self.backTireGroveJoint = GrooveJoint(self.body, self.backTire.body, groove_a=(-backOffset, 0), groove_b=(-backOffset, length), anchor_b=(0, 0))
        self.backTireGroveJoint._set_max_force(maxForce)

        space.add(self.body, self.shape, self.frontTireDampedSpring, self.frontTireGroveJoint, self.backTireDampedSpring, self.backTireGroveJoint)

    def jump(self):
        if self.frontTire.isColliding or self.backTire.isColliding:
            self.body.apply_impulse_at_local_point((-self.body.mass * 150, -self.body.mass * 650))

            self.frontTire.isColliding = False
            self.backTire.isColliding = False
        pass      

    def update(self, translated):
        self.image = transform.rotate(bikeSrpite, -degrees(self.body.angle))
        self.rect = self.image.get_rect()
        self.rect.center = self.body.position - Vec2d(translated.tx, 0)

        # if self.isDied:
        #     self.body._set_position(self.fixedPosition)
        #     self.body._set_angle(0)
        #     self.frontTire.body._set_position(self.fixedPosition)
        #     self.backTire.body._set_position(self.fixedPosition)

        #     self.isDied = False

        pass

    def draw(self):
        pass

    def collsionBegin(self, arbiter, space, data):
        self.isDied = True
        return True