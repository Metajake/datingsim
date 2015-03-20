import pygame
from pygame.locals import *
import PyDark.engine, PyDark.ui

class Graphics(object):
    def __init__(self, engine):
        self.engine = engine
        self.DARKGREEN = (16, 88, 4)
        self.GREEN = (0, 255, 0)        
        
        self.day_overlay = PyDark.ui.Overlay(
            name="day_overlay",
            parent=self.engine.day_scene,
            size=self.engine.window_size,
            color=self.GREEN,
            endcolor=self.DARKGREEN,
            position=(0, 0))
        
        self.text_entry = PyDark.ui.TextBox(
            name="text_entry",
            position=(0, 250),
            default_image="assets/input.png")
        
        self.submit = PyDark.ui.Button(
            name="submit",
            position=(0, 225),
            on_press=self.submit_pressed,
            center=True,
            default_image="assets/button.png",
            image_hover="assets/button_hover.png",
            image_selected="assets/button_hover.png")

    def submit_pressed(self, event):
        print self.text_entry.text
        #self.engine.current_scene = 'idle_engine'
        
    def initialize(self):
        self.day_overlay.add_object(self.text_entry)
        self.day_overlay.add_object(self.submit)
        self.engine.day_scene.add_object(self.day_overlay)