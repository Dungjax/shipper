from pygame import sprite, MOUSEBUTTONUP


class Button(sprite.Sprite):
    def __init__(self, group: sprite.LayeredUpdates, position, image, work) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position

        group.add(self)

        self.work = work

    def handleEvent(self, events, mousePosition):
        for ev in events:
            if ev.type == MOUSEBUTTONUP:
                if self.rect.collidepoint(mousePosition):
                    self.work()
                    return True
                    pass

    def update(self):
        pass

    def draw(self):
        pass

