import tweepy
from PIL import Image, ImageDraw
from random import randint, choice
from tokens import *
from time import sleep


class Piet:
    def __init__(self):
        self.colors = [(255, 5, 78), (160,89,135), (255, 31, 176), (30,20,43)]

    def createImageInPietStyle(self):
        def split(self, fatherFrame, vertical):
            if vertical:
                lineToPaste = Image.new('RGB', (20, fatherFrame['height']), color = (0, 0, 0))
                imageToPasteWidth = randint(100, fatherFrame['width'] - 100)
                imageToPasteHeight = fatherFrame['height']
                imageToPaste = Image.new('RGB', (imageToPasteWidth, imageToPasteHeight), color = choice(self.colors))
                image.paste(imageToPaste, fatherFrame['position'])
                image.paste(lineToPaste, (fatherFrame['position'][0] + imageToPasteWidth - 10, fatherFrame['position'][1]))
                descendent1 = {'position': fatherFrame['position'], 'width': imageToPasteWidth - 10, 'height': imageToPasteHeight}
                descendent2 = {'position': (fatherFrame['position'][0] + imageToPasteWidth, fatherFrame['position'][1]), 'width': fatherFrame['width'] - imageToPasteWidth, 'height': imageToPasteHeight}
            else:
                lineToPaste = Image.new('RGB', (fatherFrame['width'], 20), color = (0, 0, 0))
                imageToPasteWidth = fatherFrame['width']
                imageToPasteHeight = randint(100, fatherFrame['height'] - 100)
                imageToPaste = Image.new('RGB', (imageToPasteWidth, imageToPasteHeight), color = choice(self.colors))
                image.paste(imageToPaste, fatherFrame['position'])
                image.paste(lineToPaste, (fatherFrame['position'][0], fatherFrame['position'][1] + imageToPasteHeight - 10))
                descendent1 = {'position': fatherFrame['position'], 'width': imageToPasteWidth, 'height': imageToPasteHeight - 10}
                descendent2 = {'position': (fatherFrame['position'][0], fatherFrame['position'][1] + imageToPasteHeight), 'width': imageToPasteWidth, 'height': fatherFrame['height'] - imageToPasteHeight}

            frames.append(descendent1)
            frames.append(descendent2)
            frames.remove(fatherFrame)

        def verifyFrames(self, frames, minimalSize):
            validFrames = list()

            for frame in frames:
                if frame['width'] >= minimalSize and frame['height'] >= minimalSize: validFrames.append(frame)

            return validFrames

        image = Image.new('RGB', (1500, 1500), color = choice(self.colors))
        frames = [{'position': (0, 0), 'width': 1500, 'height': 1500}]

        while True:
            try:
                vertical = choice((True, False))
                frames = verifyFrames(self, frames, 300)
                activeFrame = choice(frames)

                if activeFrame['width'] == activeFrame['height']:
                    if vertical and activeFrame['width'] > 300: split(self, activeFrame, vertical)
                    else: split(self, activeFrame, vertical)
                elif activeFrame['width'] > activeFrame['height']: split(self, activeFrame, vertical=True)
                else: split(self, activeFrame, vertical=False)
            except IndexError: break

        image.save('image.jpg')
        print('Piet Style Art Created')

    def createSimpleArt(self):
        def verifyFrames(frames):
            validFrames = list()

            for frame in frames:
                if not frame['width'] < 70: validFrames.append(frame)

            return validFrames

        def splitVertical(fatherFrame):
            imageToPasteWidth = randint(0, fatherFrame['width'])
            imageToPasteHeight = fatherFrame['height']
            imageToPaste = Image.new('RGB', (imageToPasteWidth, imageToPasteHeight), color = choice(self.colors))
            image.paste(imageToPaste, fatherFrame['position'])
            descendent1 = {'position': fatherFrame['position'], 'width': imageToPasteWidth, 'height': imageToPasteHeight}
            descendent2 = {'position': (fatherFrame['position'][0] + imageToPasteWidth, fatherFrame['position'][1]), 'width': fatherFrame['width'] - imageToPasteWidth, 'height': imageToPasteHeight}
            imageToPasteWidth = descendent2['width']
            imageToPasteHeight = descendent2['height']
            image.paste(imageToPaste, descendent2['position'])
            frames.append(descendent1)
            frames.append(descendent2)
            frames.remove(fatherFrame)

        print('Simple Art Created')
        image = Image.new('RGB', (2000, 1500), color = (0, 0, 0))
        frames = [{'position': (0, 0), 'width': 2000, 'height': 1500}]

        while True:
            try:
                frames = verifyFrames(frames)
                activeFrame = choice(frames)
                splitVertical(activeFrame)
            except IndexError: break

        image.save(f'image.jpg')

    def createTiled(self):
        def tiledLines(self):
            diagonalOrVertical = choice(('diagonal', 'vertical'))
            blockSize = choice((50, 60))
            color1 = choice(self.colors[0:2])
            color2 = choice(self.colors[0:2])
            print('Tiled Lines Created')

            if diagonalOrVertical == 'diagonal':
                for x in range(0, 1500 + blockSize, blockSize):
                    for y in range(0, 1500 + blockSize, blockSize):
                        diagonal = choice((True, False))
                        teste = (x, y) + (x + blockSize, y + blockSize)

                        if diagonal: ImageDraw.Draw(image).line(teste, width = 5, fill=color1)
                        else: ImageDraw.Draw(image).line((x, y + blockSize) + (x + blockSize, y), width = 5, fill=color2)

            else:
                for x in range(0, 1500 + blockSize, blockSize):
                    for y in range(0, 1500 + blockSize, blockSize):
                        vertical = choice((True, False))
                        teste = (x + (blockSize / 2), y) + (x + (blockSize / 2), y + blockSize)

                        if vertical: ImageDraw.Draw(image).line(teste, width = 5, fill=color1)
                        else: ImageDraw.Draw(image).line((x, y + blockSize / 2) + (x + blockSize, y + blockSize / 2), width = 5, fill=color2)


        def tiledEdgesCurves(self):
            from math import ceil
            color1 = choice(self.colors[0:2])
            color2 = choice(self.colors[0:2])
            blockSize = choice((50, 60))
            width = blockSize
            height = blockSize
            lineSize = ceil(blockSize * 0.2)
            filled = choice((True, False))
            print('Tiled Curves Created')


            for x in range(0, 1500 + blockSize, blockSize):
                for y in range(0, 1500 + blockSize, blockSize):
                    option = choice((True, False))

                    if option:
                        x1 = x + width - (width + width / 2) - (lineSize / 2)
                        y1 = y + height / 2 - (lineSize / 2)
                        x2 = x + width / 2 + (lineSize / 2)
                        y2 = y + height + height / 2 + (lineSize / 2)
                        x3 = x + width / 2 - (lineSize / 2)
                        y3 = y + height / 2 * -1 - (lineSize / 2)
                        x4 = x + width + (width / 2) + (lineSize / 2)
                        y4 = y + height / 2 + (lineSize / 2)
                        varStart1 = 270
                        varEnd1 = 360
                        varStart2 = 90
                        varEnd2 = 180
                    else:
                        x1 = x + width / 2 * -1 - (lineSize / 2)
                        y1 = y + height / 2 * -1 - (lineSize / 2)
                        x2 = x + width / 2 + (lineSize / 2)
                        y2 = y + height / 2 + (lineSize / 2)
                        x3 = x + width / 2 - (lineSize / 2)
                        y3 = y + height / 2 - (lineSize / 2)
                        x4 = x + width + (width / 2) + (lineSize / 2)
                        y4 = y + height + (height / 2) + (lineSize / 2)
                        varStart1 = 0
                        varEnd1 = 90
                        varStart2 = 180
                        varEnd2 = 270

                    coordinates1 = (x1, y1, x2, y2)
                    coordinates2 = (x3, y3, x4, y4)

                    if filled:
                        ImageDraw.Draw(image).chord(coordinates1, start=varStart1, end=varEnd1, width=lineSize, fill=color1)
                        ImageDraw.Draw(image).chord(coordinates2, start=varStart2, end=varEnd2, width=lineSize, fill=color2)
                    else:
                        ImageDraw.Draw(image).arc(coordinates1, start=varStart1, end=varEnd1, width=lineSize, fill=color1)
                        ImageDraw.Draw(image).arc(coordinates2, start=varStart2, end=varEnd2, width=lineSize, fill=color2)

        style = choice((1, 2))

        if style == 1:
            backgroundColor = choice(((0, 0, 0), (13, 6, 18)))
            image = Image.new('RGB', (1500, 1500), color = backgroundColor)
            tiledLines(self)
        elif style == 2:
            backgroundColor = choice(((0, 0, 0), (13, 6, 18)))
            image = Image.new('RGB', (1500, 1500), color = backgroundColor)
            tiledEdgesCurves(self)

        image.save('image.jpg')

def runScript():
    piet = Piet()
    artStyle = choice((1, 2, 3))
    if artStyle == 1: piet.createImageInPietStyle()
    elif artStyle == 2: piet.createSimpleArt()
    else: piet.createTiled()

if __name__ == '__main__':
    while True:
        runScript()
        sleep(1)
