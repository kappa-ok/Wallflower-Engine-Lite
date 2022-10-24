import dearpygui.dearpygui as gui
import glob

gui.create_context()
gui.create_viewport(title="Wallflower Engine", width=1200, height=700)

gui.set_viewport_small_icon("resources/wallflowerIcon.ico")
gui.set_viewport_large_icon("resources/wallflowerIcon.ico")

gui.setup_dearpygui()
