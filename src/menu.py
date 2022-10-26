import dearpygui.dearpygui as gui
import GameObjectsEditor as GOE
import GamePropertyEditor as GPE
import glob

def print_me(sender):
    print(f"Menu Item: {sender}")

def GOEShow():
    GOE.createGOE()

def GPEShow():
    GPE.createGPE()

with gui.viewport_menu_bar():
    with gui.menu(label="File"):
        gui.add_menu_item(label="New", callback=print_me)
        gui.add_menu_item(label="Save", callback=print_me)
        gui.add_menu_item(label="Save As", callback=print_me)

        with gui.menu(label="Settings"):
            gui.add_menu_item(label="Setting 1", callback=print_me, check=True)
            gui.add_menu_item(label="Setting 2", callback=print_me)

    with gui.menu(label="Show"):
        gui.add_menu_item(label="Game Object Editor", callback=GOEShow)
        gui.add_menu_item(label="Game Property Editor", callback=GPEShow)

    gui.add_menu_item(label="Help", callback=print_me)