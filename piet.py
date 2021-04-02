from PIL import Image
from random import randint, choice

class Piet:
    def createImageSquared(self):
        from config import colors

        image = Image.new('RGB', (1580, 1580), color = (1, 1, 1))
        placeHorizontal = 0
        placeVertical = 0
        shapeSize = (300, 300)

        for _ in range(5):
            for _ in range(5):
                shapeToPaste = Image.new('RGB', (shapeSize[0], shapeSize[1]), color = (choice(colors)))
                image.paste(shapeToPaste, (placeHorizontal, placeVertical))
                placeVertical = placeVertical + 300 + 20
                image.save('image.jpg')

            placeHorizontal = placeHorizontal + 300 + 20
            placeVertical = 0

if __name__ == '__main__':
    piet = Piet()
    piet.createImage())
