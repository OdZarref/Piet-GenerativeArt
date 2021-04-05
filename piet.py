import tweepy
import schedule
from PIL import Image
from random import randint, choice
from tokens import *
from time import sleep
from math import floor
from config import *

class Piet:
    def draw(self, pos, width, height, image):
        colorToPaint = (randint(0, 255), randint(0, 255), randint(0, 255))
        imageToPaste = Image.new('RGB', (width, height), color = colorToPaint)
        image.paste(imageToPaste, pos)
        image.save(f'image.jpg')

    def createImage(self):
        def split(self, activeFrame):
            splitOnVertical = choice((True, False))
            position = activeFrame['pos']
            width = activeFrame['width']
            height = activeFrame['height']

            if splitOnVertical:
                whereToSplit = randint(200 , width)
                widthObject1 = width - whereToSplit
                widthObject2 = width - widthObject1
                object1 = {'pos': position[:], 'width': widthObject1, 'height': height, 'ignore': False}
                object2 = {'pos': (widthObject1, position[-1]), 'width': widthObject2, 'height': height, 'ignore': False}
                print(f'figura 1: Vertical = Sim, Comprimento = {widthObject1}x{height}, Posição = {object1["pos"]}')
                print(f'figura 2: Vertical = Sim, Comprimento = {widthObject2}x{height}, Posição = {object2["pos"]}')
                draw(self, object1['pos'], widthObject1, height)
            else:
                whereToSplit = randint(200, height)
                heightObject1 = height - whereToSplit
                heightObject2 = height - heightObject1
                object1 = {'pos': position[:], 'width': width, 'height': heightObject1, 'ignore': False}
                object2 = {'pos': (position[0], heightObject1), 'width': width, 'height': heightObject2, 'ignore': False}
                print(f'figura 1: Vertical = Não, Comprimento = {width}x{heightObject1}, Posição = {object1["pos"]}')
                print(f'figura 2: Vertical = Não, Comprimento = {width}x{heightObject2}, Posição = {object2["pos"]}')
                draw(self, object1['pos'], width, heightObject1)

            if not object1 in frames:
                if object1['width'] < 300 or object1['height'] < 300: object1['ignore'] = True
                frames.append(object1)

            if not object2 in frames:
                if object1['width'] < 300 or object1['height'] < 300: object1['ignore'] = True
                frames.append(object2)

            activeFrame['ignore'] = True

        frames = [{'pos': (0, 0), 'width': 1500, 'height': 1500, 'ignore': False}]
        image = Image.new('RGB', (frames[0]['width'], frames[0]['height']), color = (randint(0, 255), randint(0, 255), randint(0, 255)))

        for counter in range(5):
            possibleFrames = list()

            for frame in frames:
                if not frame['ignore']: activeFrame = frame

            # activeFrame = choice(possibleFrames)

            for frame in frames: print(frame)
            print(f'Objeto Ativo: {activeFrame}')
            split(self, activeFrame)
            input()

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

        image.save(f'image.jpg')

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
    piet.createSimpleArt()
    twitterApi = Twitter()
    twitterApi.postTweet()

if __name__ == '__main__':
    schedule.every(24).hours.do(runScript)

    while True:
        schedule.run_pending()
        sleep(2)
