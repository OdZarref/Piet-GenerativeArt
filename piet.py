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
                imageToPaste = Image.new('RGB', (shapeSize[0], shapeSize[1]), color = (choice(colors)))
                image.paste(imageToPaste, (placeHorizontal, placeVertical))
                placeVertical = placeVertical + 300 + 20
                image.save('image.jpg')

            placeHorizontal = placeHorizontal + 300 + 20
            placeVertical = 0

    def createImage(self):
        def paint(color, edge):
            imageToPaste = Image.new('RGB', (100, 100), color = (imageToPasteColor))
            image.paste(imageToPaste, (edge))

        def multFifteenFunction(index):
            result = 0

            while True:
                if result % 15 == 0 and result > index:
                    return result
                else:
                    result += 5

        def howMuchToTheBottomFunction(index):
            multFifteen = multFifteenFunction(index)
            howMuch = randint(0, (multFifteen - (index)))
            print(howMuch)

            if howMuch > 8:
                howMuch = 0

            return howMuch

        def paintToTheBottom(howMuchToTheBottom, color, index):
            for c in range(howMuchToTheBottom):
                if not edgers[index] == edgers[-1]:
                    paint(color, edgers[index + c])
                    mustBeIgnored.append(index + c)

        from config import edgers, colors

        image = Image.new('RGB', (1500, 1500), color = (1, 1, 1))
        mustBeIgnored = list()

        for edge in edgers:
            index = edgers.index(edge)

            if index not in mustBeIgnored:
                howMuchToTheBottom = howMuchToTheBottomFunction(index)
                imageToPasteColor = choice(colors)
                paint(imageToPasteColor, edge)

                if not index == 224:
                    paintToTheBottom(howMuchToTheBottom, imageToPasteColor, index)

        image.save('image.jpg')

if __name__ == '__main__':
    piet = Piet()
    piet.createImage()
