from PIL import Image
from random import randint, choice

class Piet:
    def __init__(self):
        self.image = Image.new('RGB', (1580, 1580), color = (1, 1, 1))
        self.colors = [(0, 0, 0,), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255,0,255), (75,0,130), (255,127,80), (0,255,255), (47,79,79), (128,128,0)]

    def createImage(self):
        placeHorizontal = 0
        placeVertical = 0 
        shapeSize = (300, 300)

        for _ in range(5):
            for _ in range(5):
                shapeToPaste = Image.new('RGB', (shapeSize[0], shapeSize[1]), color = (choice(self.colors)))
                self.image.paste(shapeToPaste, (placeHorizontal, placeVertical))
                placeVertical = placeVertical + 300 + 20
                self.image.save('image.jpg')
            
            placeHorizontal = placeHorizontal + 300 + 20
            placeVertical = 0

if __name__ == '__main__':
    piet = Piet()
    piet.createImage()

