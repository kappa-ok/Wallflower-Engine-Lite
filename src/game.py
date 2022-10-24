#import sys
import dearpygui.dearpygui as gui

#print("Game Ran Successfully!")

gameObjects = []

def runGame():

    print(gameObjects)

    gui.create_context()
    gui.create_viewport(title="Game Title", width=1200, height=700)
    gui.setup_dearpygui()

    with gui.window(label="Game", width=500, height=200, pos=(10, 10)):
        gui.add_text("Game")

    gui.show_viewport()
    gui.start_dearpygui()
    gui.destroy_context()