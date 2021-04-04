import tweepy
import schedule
from PIL import Image
from random import randint, choice
from tokens import *
from time import sleep
from math import floor
from config import *

class Piet:
    def createImage(self):
        def split(self, edge, width, height):
            splitOnVertical = choice((True, False))

            if splitOnVertical:
                whereToSplit = randint(0, width-50)
                newWidth = width - whereToSplit
                newWidth2 = width - newWidth
                whereToDraw = edge[:]
                whereToDraw2 = (newWidth, edge[-1])
                print(f'figura 1: Vertical = Sim, Comprimento = {newWidth}x{height}, Posição = {whereToDraw}')
                print(f'figura 2: Vertical = Sim, Comprimento = {newWidth2}x{height}, Posição = {whereToDraw2}')
                draw(self, whereToDraw, newWidth, height)
                draw(self, whereToDraw2, newWidth2, height)
                if not whereToDraw in edgers: edgers.append(whereToDraw)
                if not whereToDraw2 in edgers: edgers.append(whereToDraw2)
            else:
                whereToSplit = randint(0, height-50)
                newHeight = height - whereToSplit
                newHeight2 = height - newHeight
                whereToDraw = edge[:]
                whereToDraw2 = (edge[0], newHeight)
                print(f'figura 1: Vertical = Não, Comprimento = {width}x{newHeight}, Posição = {whereToDraw}')
                print(f'figura 2: Vertical = Não, Comprimento = {width}x{newHeight2}, Posição = {whereToDraw2}')
                draw(self, whereToDraw, width, newHeight)
                draw(self, whereToDraw2, width, newHeight2)
                if not whereToDraw in edgers: edgers.append(whereToDraw)
                if not whereToDraw2 in edgers: edgers.append(whereToDraw2)

        def draw(self, whereToDraw, width, height):
            colorToPaint = (randint(0, 255), randint(0, 255), randint(0, 255))
            imageToPaste = Image.new('RGB', (width, height), color = colorToPaint)
            image.paste(imageToPaste, whereToDraw)
            image.save('image.jpg')

        width = 1500
        height = 1500
        edgers = [(0, 0)]
        image = Image.new('RGB', (width, height), color = (1, 1, 1))

        for index in range(randint(5, 8)):
            split(self, choice(edgers), width, height)
            print(edgers)
            input()

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
    piet.createImage()
    # twitterApi = Twitter()
    # twitterApi.postTweet()

if __name__ == '__main__':
    # schedule.every(2).hours.do(runScript)
    #
    # while True:
    #     schedule.run_pending()
    #     sleep(2)

    runScript()
