from pygame import display, time
from pymunk import Space, pygame_util

WIDTH = 1200
HEIGHT = 800

WINDOW = display.set_mode((WIDTH, HEIGHT))
options = pygame_util.DrawOptions(WINDOW)

space = Space()
space.gravity = (0, 800)

clock = time.Clock()