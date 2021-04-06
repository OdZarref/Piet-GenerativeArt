import tweepy
import schedule
from PIL import Image
from random import randint, choice
from tokens import *
from time import sleep
from math import floor

class Piet:
    def createImageInPietStyle(self):
        def splitVertical(self, fatherFrame):
            lineToPaste = Image.new('RGB', (20, fatherFrame['height']), color = (0, 0, 0))
            imageToPasteWidth = randint(100, fatherFrame['width'] - 100)
            imageToPasteHeight = fatherFrame['height']
            imageToPaste = Image.new('RGB', (imageToPasteWidth, imageToPasteHeight), color = choice(colors))
            image.paste(imageToPaste, fatherFrame['position'])
            image.paste(lineToPaste, (fatherFrame['position'][0] + imageToPasteWidth - 10, fatherFrame['position'][1]))
            descendent1 = {'position': fatherFrame['position'], 'width': imageToPasteWidth - 10, 'height': imageToPasteHeight}
            descendent2 = {'position': (fatherFrame['position'][0] + imageToPasteWidth, fatherFrame['position'][1]), 'width': fatherFrame['width'] - imageToPasteWidth, 'height': imageToPasteHeight}
            frames.append(descendent1)
            frames.append(descendent2)
            frames.remove(fatherFrame)

        def splitHorizontal(self, fatherFrame):
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

        def verifyFrames(self, frames):
            validFrames = list()

            for frame in frames:
                if frame['width'] >= 300 and frame['height'] >= 300:
                    validFrames.append(frame)

            return validFrames

        colors = [(255, 0, 0), (255, 255, 255), (0, 0, 255), (244,203,2)]
        image = Image.new('RGB', (1500, 1500), color = choice(colors))
        frames = [{'position': (0, 0), 'width': 1500, 'height': 1500}]

        while True:
            try:
                frames = verifyFrames(self, frames)

                activeFrame = choice(frames)

                if activeFrame['width'] == activeFrame['height']:
                    vertical = choice((True, False))
                    if vertical and activeFrame['width'] > 300:
                        splitVertical(self, activeFrame)
                    else:
                        splitHorizontal(self, activeFrame)
                elif activeFrame['width'] > activeFrame['height']:
                    splitVertical(self, activeFrame)
                else:
                    splitHorizontal(self, activeFrame)

            except IndexError:
                break

        global pietStyleCounter
        global status
        pietStyleCounter += 1
        image.save('image.jpg')
        status = f'Piet Style n. {pietStyleCounter}'
        print(status)

    def createSimpleArt(self):
        from math import ceil
        def drawSimpleArt(self, pos, width, height, image):
            colors = [(105, 60, 114), (193, 80, 80), (217, 118, 66), (212, 157, 66)]
            colorToPaint = choice(colors)
            imageToPaste = Image.new('RGB', (width, height), color = colorToPaint)
            image.paste(imageToPaste, pos)

        width = 2000
        height = 1500
        horizontalPosition = 0
        imageColor = (randint(0, 255), randint(0, 255), randint(0, 255))
        image = Image.new('RGB', (width, height), color = imageColor)
        drawSimpleArt(self, (horizontalPosition, 0), width, height, image)

        while True:
            if width < 50:
                drawSimpleArt(self, (2000 - width, 0), width, height, image)
                break
            split = randint(0, ceil(width / randint(2, 4)))
            width -= split
            horizontalPosition += split
            drawSimpleArt(self, (horizontalPosition, 0), width, height, image)

        global simpleArtCounter
        global status
        simpleArtCounter += 1
        status = f'Simple Art n. {simpleArtCounter}'
        image.save(f'image.jpg')
        print(status)

class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
        self.auth.set_access_token(accessToken, accessTokenSecret)
        self.api = tweepy.API(self.auth)

    def postTweet(self):
        imagePath = 'image.jpg'
        status = ''
        self.api.update_with_media(imagePath, status)

def runScript():
    piet = Piet()
    pietStyle = choice((True, False))
    if pietStyle: piet.createImageInPietStyle()
    else: piet.createSimpleArt()
    twitterApi = Twitter()
    twitterApi.postTweet()

if __name__ == '__main__':
    pietStyleCounter = int(input('Piet Counter'))
    simpleArtCounter = int(input('Simple Art Counter'))
    status = ''
    schedule.every(3).hours.do(runScript)
