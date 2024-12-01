from pygame import display, time, font
from pymunk import Space, pygame_util

font.init()

WIDTH = 1200
HEIGHT = 800

WINDOW = display.set_mode((WIDTH, HEIGHT))
options = pygame_util.DrawOptions(WINDOW)

space = Space()
space.gravity = (0, 800)

clock = time.Clock()

defaultFont = font.Font(None, 50)

def drawText(_text, position):
    text = defaultFont.render(str(_text), True, (0, 0, 0))
    WINDOW.blit(text, position)
