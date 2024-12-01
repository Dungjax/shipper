from pygame import display, event, QUIT, MOUSEBUTTONUP
from common import WINDOW, options, space, clock
from world import World

display.init()


class Game:
    def __init__(self) -> None:
        self.isRunning = True
        self.fps = 60
        self.deltaTime = 1/ self.fps

        self.isPressed = False

        self.world = World()
        
        pass
    
    def input(self):
        for ev in event.get():
            if ev.type == QUIT:
                self.isRunning = False
            elif ev.type == MOUSEBUTTONUP:
                self.isPressed = True
            else:
                self.isPressed = False

            self.world.input(self.isPressed)
    
    def update(self):
        clock.tick(self.fps)

        self.world.update()

        space.step(self.deltaTime)

        pass

    def draw(self):
        WINDOW.fill((0, 0, 0))
        self.world.draw()

        #space.debug_draw(options)

        display.update()
        pass

    def run(self):
        while self.isRunning:
            self.input()
            self.update()
            self.draw()
            pass


if __name__ == "__main__":
    game = Game()
    game.run()