import os
import tkinter as tk
from tkinter import PhotoImage

class LegendPanel(tk.Frame):
    def __init__(self, height):
        super().__init__()

        self.animalNames = [
            "Human", "Chad", "Antelope", "Fox", "Sheep", "Turtle", "Wolf",
            "Belladonna", "Grass", "Guarana", "Sosnowsky", "Sow_thistle", "Meadow"
        ]
        self.blackBorder = 2

        self.create_legend(height)

    def create_legend(self, height):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        for animalName in self.animalNames:
            photoFilePath = os.path.join(current_dir, f"{animalName}.png")
            photoIcon = PhotoImage(file=photoFilePath)
            scaledImage = photoIcon.subsample(1, 1)
            scaledPhotoIcon = scaledImage

            photoLabel = tk.Label(self, image=scaledPhotoIcon)
            descriptionLabel = tk.Label(self, text=animalName)

            legendPanel = tk.Frame(self, bd=self.blackBorder)
            legendPanel.pack(pady=5)
            photoLabel.pack(side=tk.LEFT)
            descriptionLabel.pack(side=tk.LEFT)