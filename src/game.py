import sys
import os
import pygame
import editor
#import dearpygui.dearpygui as gui

gameName = "Game"
WindowWidth = 800
WindowHeight = 600

gameObjects = []

def runGame():

    print("Game ran successfully \n")

    print(gameName)
    print(gameObjects)
    pygame.init()
    pygame.display.init()
    pygame.display.set_mode(size=(WindowWidth, WindowHeight))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
print("Game exited successfully")