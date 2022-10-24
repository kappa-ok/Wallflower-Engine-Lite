import sys
import dearpygui.dearpygui as gui
import glob
import PyGuiInit
import game
import menu
import GameObjectsEditor as GOE

GOE.createGOE()

def runGame():
    name = gui.get_value("GameName")
    print(game.gameObjects)
    print(name)

with gui.window(label=" ", width=50, height=10, pos=(1100, 0)):
    gui.add_button(label="Run Game", callback=runGame)
    gui.add_input_text(tag="GameName", label="Game Name", source="string_value")

gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()

def stop():
    sys.exit()