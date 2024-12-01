from pygame import sprite, transform
from sprite_importer import importSpriteFromFolder
from random import randint

paralaxSprites = importSpriteFromFolder("assets/paralax")

class ParalaxSprite(sprite.Sprite):
    def __init__(self, _group: sprite.LayeredUpdates, _position) -> None:
        super().__init__()
        self.image = paralaxSprites[randint(0, len(paralaxSprites) - 1)]
        self.rect = self.image.get_rect()
        self.fixedPosition = _position
        self.rect.bottomleft = _position

        _group.add(self)
        _group.move_to_back(self)
    
    def update(self, translated):
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.fixedPosition[0]-translated.tx, self.fixedPosition[1])

        if self.rect.right < 0:
            self.kill()

        pass