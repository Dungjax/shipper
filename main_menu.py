from pygame import sprite, MOUSEBUTTONDOWN, mouse
from sprite_importer import backgroundSprite, playButtonSprite
from button import Button
from common import WINDOW, WIDTH, HEIGHT


class MainMenu:
    def __init__(self) -> None:
        self.buttons = sprite.LayeredUpdates()
        self.startButton = Button(self.buttons, (WIDTH // 2, HEIGHT // 2), playButtonSprite, lambda: None)
        pass

    def handleEvent(self, events):
        for ev in events:
            if ev.type == MOUSEBUTTONDOWN:
                pass
            
        result = self.startButton.handleEvent(events, mouse.get_pos())
        if result:
            return "game play"

            pass
        return False
    def update(self):
        self.buttons.update()
        pass

    def draw(self):
        WINDOW.blit(backgroundSprite,(0, 0))
        self.buttons.draw(WINDOW)
        pass