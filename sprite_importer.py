from pygame import image, transform
from os import walk

def importImage(_path):
    return image.load(_path)

def importSprite(_path):
    origin = image.load(_path).convert_alpha()
    
    width = origin.get_width()
    height = origin.get_height()
    collums = width // height
    
    return [origin.subsurface((i * height, 0, width // collums, height)).convert_alpha() for i in range(collums)]

def importSpriteFromFolder(_path):
    for _, __, imagePaths in walk(_path):
        return [image.load(_path + "/" + imagePath).convert_alpha() for imagePath in imagePaths]
