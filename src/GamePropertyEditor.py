import dearpygui.dearpygui as gui
import glob
import game

def saveGameProperties():
    game.gameName = gui.get_value("GameName")
    game.WindowWidth = int(gui.get_value("WINDOWWIDTH"))
    game.WindowHeight = int(gui.get_value("WINDOWHEIGHT"))
    game.runGame()

def createGPE():
    with gui.window(label=" ", width=350, height=100, pos=(800, 0)):
        gui.add_button(label="Save", callback=saveGameProperties)
        gui.add_input_text(tag="GameName", label="Game Name", source="string_value")
        gui.add_input_text(tag="WINDOWWIDTH", label="Window Width", source="int_value")
        gui.add_input_text(tag="WINDOWHEIGHT", label="Window Height", source="int_value")

    gui.set_value("GameName", "Game")
    gui.set_value("WINDOWWIDTH", 800)
    gui.set_value("WINDOWHEIGHT", 600)