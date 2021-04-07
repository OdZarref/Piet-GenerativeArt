import tweepy
import schedule
from PIL import Image
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

        colors = [(255, 0, 0), (255, 255, 255), (0, 0, 255), (244,203,2)]
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
        status = f'Piet Style n. {pietStyleCounter}'

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

        colors = [(105, 60, 114), (193, 80, 80), (217, 118, 66), (212, 157, 66)]
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
        status = f'Simple Art n. {simpleArtCounter}'
        image.save(f'image.jpg')

class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
        self.auth.set_access_token(accessToken, accessTokenSecret)
        self.api = tweepy.API(self.auth)

    def postTweet(self):
        global status
        imagePath = 'image.jpg'
        self.api.update_with_media(imagePath, status)
        print(f'Post: {status}')

def runScript():
    piet = Piet()
    pietStyle = choice((True, False))
    if pietStyle: piet.createImageInPietStyle()
    else: piet.createSimpleArt()
    # twitterApi = Twitter()
    # twitterApi.postTweet()

if __name__ == '__main__':
    pietStyleCounter = 0#int(input('Piet Counter: '))
    simpleArtCounter = 0#int(input('Simple Art Counter: '))
    status = ''
    schedule.every(8).hours.do(runScript)

    while True:
        # schedule.run_pending()
        runScript()
        sleep(1)
