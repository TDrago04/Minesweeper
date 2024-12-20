from piece import Piece
from random import random
import pygame
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Board():

    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
        self.lost = False
        self.won = False
        self.numClicked = 0
        self.numNonBombs = 0
        self.setBoard()
        
        

    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                hasBomb = random() < self.prob
                if (not hasBomb):
                    self.numNonBombs += 1
                piece = Piece(hasBomb)
                row.append(piece)
            self.board.append(row)
        self.setNeighbors()


    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)

    def getListOfNeighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if (same or outOfBounds):
                    continue
                neighbors.append(self.getPiece((row, col)))
        return neighbors


    def getSize(self):
        return self.size
    
    def getPiece(self, index):
        return self.board[index[0]][index[1]]


    def handleClick(self, piece, flag, canPlaySFX, multiSFX):
        
        if (piece.getClicked() or (not flag and piece.getFlagged())):
            return
        if (flag):
            piece.toggleFlag()
            return
        piece.click()
        
        if (piece.getHasBomb()):
            pygame.mixer.Sound(resource_path("sfx/explode.mp3")).play()
            self.lost = True
            return
        self.numClicked += 1
        if (not piece.getHasBomb()):
            if (canPlaySFX == True):
                pygame.mixer.Sound(resource_path("sfx/click.mp3")).play()
        if (piece.getNumAround() != 0):
            return

        if (multiSFX == True):
            pygame.mixer.Sound(resource_path("sfx/multi.mp3")).play()
        
        cnt = 0
        for neighbor in piece.getNeighbors():
            if (not neighbor.getHasBomb() and not neighbor.getClicked()):
                if cnt == 0:
                    cnt+=1
                    self.handleClick(neighbor, False, False, False)
                    
                else:
                    self.handleClick(neighbor, False, False, False)

    def getLost(self):
        return self.lost
    
    def getWon(self):
        return self.numNonBombs == self.numClicked