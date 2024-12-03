from main_menu import MainMenu
from game_play import GamePlay
from common import space


class SceneManager:
    def __init__(self) -> None:
        self.scenes = {}
        self.currentScene = None
        pass

    def addScene(self, name, scene):
        self.scenes[name] = scene

    def setScene(self, name):
        if name in self.scenes:
            self.currentScene = self.scenes[name]

    def handleEvent(self, events):
        if self.currentScene:
            result = self.currentScene.handleEvent(events)
            
            if result:
                self.setScene(result)
                if result == "main menu":
                    return True
                    pass
                
            pass

    def update(self):
        if self.currentScene:
            self.currentScene.update()
        pass

    def draw(self):
        if self.currentScene:
            self.currentScene.draw()
        pass
