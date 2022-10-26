import dearpygui.dearpygui as gui
import glob
import game

def saveGameProperties():
    game.gameName = gui.get_value("GameName")
    game.WindowWidth = gui.get_value("WINDOWWIDTH")
    game.WindowHeight = gui.get_value("WINDOWHEIGHT")
    game.runGame()

def createGPE():
    with gui.window(label=" ", width=300, height=10, pos=(850, 0)):
        gui.add_button(label="Save", callback=saveGameProperties)
        gui.add_input_text(tag="GameName", label="Game Name", source="string_value")
        gui.add_input_text(tag="WINDOWWIDTH", label="Window Width", source="int_value")
        gui.add_input_text(tag="WINDOWHEIGHT", label="Window Height", source="int_value")

    gui.set_value("GameName", "Game")
    gui.set_value("WINDOWWIDTH", 800)
    gui.set_value("WINDOWHEIGHT", 600)