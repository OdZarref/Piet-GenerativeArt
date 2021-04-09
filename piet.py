import tweepy
import schedule
from PIL import Image, ImageDraw
from random import randint, choice
from tokens import *
from time import sleep


class Piet:
    def createImageInPietStyle(self):
        def split(self, fatherFrame, vertical):
            if vertical:
                lineToPaste = Image.new('RGB', (20, fatherFrame['height']), color = (0, 0, 0))
                imageToPasteWidth = randint(100, fatherFrame['width'] - 100)
                imageToPasteHeight = fatherFrame['height']
                imageToPaste = Image.new('RGB', (imageToPasteWidth, imageToPasteHeight), color = choice(colors))
                image.paste(imageToPaste, fatherFrame['position'])
                image.paste(lineToPaste, (fatherFrame['position'][0] + imageToPasteWidth - 10, fatherFrame['position'][1]))
                descendent1 = {'position': fatherFrame['position'], 'width': imageToPasteWidth - 10, 'height': imageToPasteHeight}
                descendent2 = {'position': (fatherFrame['position'][0] + imageToPasteWidth, fatherFrame['position'][1]), 'width': fatherFrame['width'] - imageToPasteWidth, 'height': imageToPasteHeight}
            else:
                lineToPaste = Image.new('RGB', (fatherFrame['width'], 20), color = (0, 0, 0))
                imageToPasteWidth = fatherFrame['width']
                imageToPasteHeight = randint(100, fatherFrame['height'] - 100)
                imageToPaste = Image.new('RGB', (imageToPasteWidth, imageToPasteHeight), color = choice(colors))
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

        image = Image.new('RGB', (1500, 1500), color = choice(colors))
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

        global pietStyleCounter
        global status
        pietStyleCounter += 1
        image.save('image.jpg')
        status = f'Piet Style Art N. {pietStyleCounter}'

    def createSimpleArt(self):
        def verifyFrames(frames):
            validFrames = list()

            for frame in frames:
                if not frame['width'] < 70: validFrames.append(frame)

            return validFrames

        def splitVertical(fatherFrame):
            imageToPasteWidth = randint(0, fatherFrame['width'])
            imageToPasteHeight = fatherFrame['height']
            imageToPaste = Image.new('RGB', (imageToPasteWidth, imageToPasteHeight), color = choice(colors))
            image.paste(imageToPaste, fatherFrame['position'])
            descendent1 = {'position': fatherFrame['position'], 'width': imageToPasteWidth, 'height': imageToPasteHeight}
            descendent2 = {'position': (fatherFrame['position'][0] + imageToPasteWidth, fatherFrame['position'][1]), 'width': fatherFrame['width'] - imageToPasteWidth, 'height': imageToPasteHeight}
            imageToPasteWidth = descendent2['width']
            imageToPasteHeight = descendent2['height']
            image.paste(imageToPaste, descendent2['position'])
            frames.append(descendent1)
            frames.append(descendent2)
            frames.remove(fatherFrame)

        image = Image.new('RGB', (2000, 1500), color = (0, 0, 0))
        frames = [{'position': (0, 0), 'width': 2000, 'height': 1500}]

        while True:
            try:
                frames = verifyFrames(frames)
                activeFrame = choice(frames)
                splitVertical(activeFrame)
            except IndexError: break

        global simpleArtCounter
        global status
        simpleArtCounter += 1
        status = f'Simple Art N. {simpleArtCounter}'
        image.save(f'image.jpg')

    def createTiled(self):
        def diagonalLines(self):
            for x in range(0, 1500 + blockSize, blockSize):
                for y in range(0, 1500 + blockSize, blockSize):
                    diagonal = choice((True, False))

                    if diagonal: ImageDraw.Draw(image).line((x, y) + (x + blockSize, y + blockSize), width = 5, fill=color1)
                    else: ImageDraw.Draw(image).line((x, y + blockSize) + (x + blockSize, y), width = 5, fill=color2)

        def horizontalLines(self):
            for x in range(0, 1500 + blockSize, blockSize):
                for y in range(0, 1500 + blockSize, blockSize):
                    vertical = choice((True, False))

                    if vertical: ImageDraw.Draw(image).line((x + (blockSize / 2), y) + (x + (blockSize / 2), y + blockSize), width = 5, fill=color1)
                    else: ImageDraw.Draw(image).line((x, y + blockSize / 2) + (x + blockSize, y + blockSize / 2), width = 5, fill=color2)

        backgroundColor = choice(((0, 0, 0), (59,31,82)))
        blockSize = choice((20, 30, 50, 60))
        color1 = choice(colors[0:2])
        color2 = choice(colors[0:2])
        image = Image.new('RGB', (1500, 1500), color = backgroundColor)
        style = choice((1, 2))

        if style == 1: diagonalLines(self)
        elif style == 2: horizontalLines(self)

        global tiledSStyleCounter
        global status
        tiledSStyleCounter += 1
        status = f'Tiled Art N. {tiledSStyleCounter}'

        image.save('image.jpg')


class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
        self.auth.set_access_token(accessToken, accessTokenSecret)
        self.api = tweepy.API(self.auth)

    def postTweet(self):
        global status
        imagePath = 'image.jpg'
        self.api.update_with_media(imagePath, status)


def runScript():
    piet = Piet()
    artStyle = choice((1, 2, 3))
    if artStyle == 1: piet.createImageInPietStyle()
    elif artStyle == 2: piet.createSimpleArt()
    else: piet.createTiled()
    twitterApi = Twitter()
    twitterApi.postTweet()
    print(f'Post: {status}')

def postOnTerminal():
    print(f'Running again in the next {hours} hours.')

if __name__ == '__main__':
    colors = [(221,129,156), (160,89,135), (59,31,82), (30,20,43)]
    hours = int(input('How many hours to wait? '))
    pietStyleCounter = int(input('Piet Counter: '))
    simpleArtCounter = int(input('Simple Art Counter: '))
    tiledSStyleCounter = int(input('Tiled Style Counter: '))
    status = ''
    schedule.every(hours).hours.do(runScript)
    schedule.every(1).hours.do(postOnTerminal)

    while True:
        schedule.run_pending()
        sleep(1)
