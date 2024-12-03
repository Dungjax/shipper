from pygame import sprite, MOUSEBUTTONUP
from pymunk import Body, Poly, Vec2d, Transform
from common import WIDTH, HEIGHT, WINDOW, space, drawText
from bike import Bike
from sprite_importer import backgroundSprite
from paralax_sprite import ParalaxSprite
from obstacle import Obstacle
from enums import ShapeType
from random import randint

class GamePlay:
    def __init__(self) -> None:
        #physics
        self.translation = Transform()
        self.translated = self.translation.translated(0, 0)
        #sprite
        self.backGroudSprite = backgroundSprite
        self.paralaxSpries = sprite.LayeredUpdates()
        self.obstacleSprites = sprite.LayeredUpdates()
        
        #platform
        self.groundBody = Body(mass=1, moment=1, body_type=Body.STATIC)
        self.groundBody.position = Vec2d(WIDTH // 2, HEIGHT // 1.5)

        self.groundShape = Poly.create_box(self.groundBody, size=(WIDTH * 200, 1))
        self.groundShape.elasticity = 0.25
        self.groundShape.friction = 1
        self.groundShape.collision_type = ShapeType.GROUND.value

        space.add(self.groundBody, self.groundShape)
        #bike
        self.bikes = sprite.LayeredUpdates()
        self.bike = Bike(self.bikes, Vec2d(400, 400), space)
        self.collision = {}
        pass

        ParalaxSprite(self.paralaxSpries, (self.bike.body.position.x + WIDTH, self.groundBody.position.y))
        Obstacle(self.obstacleSprites, Vec2d(WIDTH, 400), space)

    def handleEvent(self, events):
        for ev in events:
            if ev.type == MOUSEBUTTONUP:
                self.bike.jump()
        pass

        if len(self.collision) > 0:
            return "main menu"
        
        return False

    def update(self):
        self.bikes.update(self.translated)
        self.paralaxSpries.update(self.translated)
        self.obstacleSprites.update(self.translated)

        if self.paralaxSpries.get_sprite(0).rect.left < self.bike.rect.left + WIDTH // 1.5:
            ParalaxSprite(self.paralaxSpries, (self.bike.body.position.x + WIDTH, self.groundBody.position.y))

        if self.obstacleSprites.get_sprite(len(self.obstacleSprites) - 1).rect.left < self.bike.rect.left:
            [Obstacle(self.obstacleSprites, Vec2d(self.bike.body.position.x + WIDTH, 0), space) for i in range(randint(1, 3))]
                
            #pass

        self.translated = self.translation.translated(self.bike.body.position.x - self.bike.fixedPosition.x, self.bike.body.position.y - self.bike.fixedPosition.y)

        self.collision = sprite.groupcollide(self.bikes, self.obstacleSprites, False, False)

        
        
        pass
    def draw(self):
        WINDOW.blit(self.backGroudSprite, (-self.translated.tx % WIDTH, 0))
        WINDOW.blit(self.backGroudSprite, (-self.translated.tx % WIDTH - WIDTH, 0))
        
        self.paralaxSpries.draw(WINDOW)
        self.obstacleSprites.draw(WINDOW)
        self.bikes.draw(WINDOW)

        drawText(str((self.bike.body.position.x - self.bike.fixedPosition.x) // 50) + "m", (0, 0))
        pass