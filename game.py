import pygame
import os
from time import sleep
from board import Board
from random import random
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Game():
    def __init__(self, board, size, prob , screenSize):
        self.board = board
        self.size = size
        self.prob = prob
        self.screenSize = screenSize
        
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()


    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        themeSong = pygame.mixer.Sound(resource_path("sfx/theme.mp3"))
        themeSong.play(-1)
        pygame.display.set_caption("Minesweeper")
        pygame.display.set_icon(pygame.image.load(resource_path("images/flag.ico")))
        while running == True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
                if (event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_7:
                        for row in range(self.board.getSize()[0]):
                            for col in range(self.board.getSize()[1]):
                                piece = self.board.getPiece((row, col))
                                if (piece.getHasBomb() == True):
                                    self.board.handleClick(piece, True, False, False)
                                else:
                                    continue
                    
                    
                    if event.key == pygame.K_1:
                        sleep(.1)
                        pygame.mixer.Sound(resource_path("sfx/revive.mp3")).play()
                        self.__init__(Board(self.size, self.prob), self.size, self.prob, self.screenSize)



            self.draw()
            pygame.display.flip()
            if (self.board.getWon()):
                #sound = pygame.mixer.Sound("win.wav")
                #sound.play()
                sleep(.5)
                pygame.mixer.Sound(resource_path("sfx/won.mp3")).play()
                sleep(2)
                pygame.mixer.Sound(resource_path("sfx/revive.mp3")).play()
                self.__init__(Board(self.size, self.prob), self.size, self.prob, self.screenSize)
            if (self.board.getLost()):
                print(self.size)
                print(self.prob)
                pygame.mixer.Sound(resource_path("sfx/lost.wav")).play()
                sleep(2)
                pygame.mixer.Sound(resource_path("sfx/revive.mp3")).play()
                self.__init__(Board(self.size, self.prob), self.size, self.prob, self.screenSize)

        pygame.quit()

    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]



    def loadImages(self):
        self.images = {}
        for fileName in os.listdir(resource_path("images")):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image


    def getImage(self, piece):
        string = None
        if (piece.getClicked()):
            string = "boom" if piece.getHasBomb() else str(piece.getNumAround())
        else:
            string = "flag" if piece.getFlagged() else  "default"
        return self.images[string]
    
    def handleClick(self, position, rightClick):
        if (self.board.getLost()):
            return 
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick, True, False)