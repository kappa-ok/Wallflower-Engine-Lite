import sys
import dearpygui.dearpygui as gui
import glob
import PyGuiInit
import game
import menu
import GameObjectsEditor as GOE
import GamePropertyEditor as GPE

GOE.createGOE()
GPE.createGPE()

gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()

def stop():
    sys.exit()