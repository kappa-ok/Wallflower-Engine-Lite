import dearpygui.dearpygui as gui
import glob
import game

def addGameObject():
    ObjectName = gui.get_value("ObjName")
    ObjectX = int(gui.get_value("ObjX"))
    ObjectY = int(gui.get_value("ObjY"))

    game.gameObjects.append(f"NAME:{ObjectName}, X:{ObjectX}, Y:{ObjectY}")

def createGOE():
    with gui.window(label="Game Object Editor", width=450, height=150, pos=(10, 10)):
        gui.add_text("Game Object")
        gui.add_input_text(tag="ObjName", label="Object Name", source="string_value")
        gui.add_input_text(tag="ObjX", label="X", source="float_value")
        gui.add_input_text(tag="ObjY", label="Y", source="float_value")
        gui.add_button(label="add", callback=addGameObject)

