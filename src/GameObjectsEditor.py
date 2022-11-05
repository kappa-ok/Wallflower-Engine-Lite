import dearpygui.dearpygui as gui
import glob
import game

def addGameObject():
    Name = gui.get_value("ObjName") 
    ObjectX = int(gui.get_value("ObjX"))
    ObjectY = int(gui.get_value("ObjY"))
    ObjectSprite = gui.get_value("Sprite")

    [Name] = GameObject(Name, ObjectX, ObjectY, ObjectSprite)

    #game.gameObjects.append([Name])



def saveSprite():
    print("Sprite set successfully!")

def createGOE():
    with gui.window(label="Game Object Editor", width=450, height=150, pos=(10, 10)):
        gui.add_text("Game Object")
        gui.add_input_text(tag="ObjName", label="Object Name", source="string_value")
        gui.add_input_text(tag="ObjX", label="X", source="float_value")
        gui.add_input_text(tag="ObjY", label="Y", source="float_value")
        gui.add_input_text(tag="Width", label="W", source="float_value")
        gui.add_input_text(tag="Height", label="H", source="float_value")
        gui.add_button(label="sprite", callback=lambda: gui.show_item("Sprite"))
        gui.add_button(label="add", callback=addGameObject)

with gui.file_dialog(directory_selector=False, show=False, callback=saveSprite, tag="Sprite", width=600, height=600):
    gui.add_file_extension(".png")
    gui.add_file_extension(".jpg")
    gui.add_file_extension(".jpeg")
    gui.add_file_extension(".tiff")

ObjectName = gui.get_value("ObjName")
    

class GameObject:
    def __init__(self, Name, x, y, Sprite):
        self.name = Name
        self.x = x
        self.y = y
        self.sprite = Sprite