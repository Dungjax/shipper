from pygame import display, event
from pygame.locals import QUIT
from common import WINDOW, options, space, clock
from scene_manager import SceneManager
from game_play import GamePlay
from main_menu import MainMenu

display.init()

class Game:
    def __init__(self) -> None:
        self.isRunning = True
        self.fps = 60
        self.deltaTime = 1 / self.fps

        self.isPressed = False

        self.sceneManager = SceneManager()
        self.sceneManager.addScene("game play", GamePlay())
        self.sceneManager.addScene("main menu", MainMenu())
        self.sceneManager.setScene("main menu")
        
        pass
    
    def handleEvent(self):
        events = event.get()
        for ev in events:
            if ev.type == QUIT:
                self.isRunning = False
            
        result = self.sceneManager.handleEvent(events)
        if result:
            self.isRunning = False

    
    def update(self):
        clock.tick(self.fps)

        self.sceneManager.update()

        space.step(self.deltaTime)

        pass

    def draw(self):
        self.sceneManager.draw()
        #space.debug_draw(options)

        display.update()
        pass

    def run(self):
        while self.isRunning:
            self.handleEvent()
            self.update()
            self.draw()
            pass


if __name__ == "__main__":
    game = Game()
    game.run()