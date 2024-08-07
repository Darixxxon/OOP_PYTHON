import tkinter as tk
from tkinter import messagebox
import Constants
import Antelope
import Belladonna
import Cyber_Sheep
import Fox
import Grass
import Guarana
import Sheep
import Sosnowsky
import Sow_thistle
import Turtle
import Wolf

class BoardButtons(tk.Frame):
    def __init__(self, world, x_tiles, y_tiles, height):
        super().__init__()
        self.world = world
        self.x_tiles = x_tiles
        self.y_tiles = y_tiles
        self.height = height
        self.tileSize = self.height // self.x_tiles
        self.board = [[None] * self.y_tiles for _ in range(self.x_tiles)]
        self.legendPanel = None
        self.create_board()

    def create_board(self):
        self.x_tiles = self.world.getTilesX()
        self.y_tiles = self.world.getTilesY()
        self.tileSize = self.height // self.x_tiles

        boardContainer = tk.Frame(self)
        boardContainer.pack(side=tk.LEFT)

        self.legendPanel = tk.Frame(self, width=56, height=self.height)
        self.legendPanel.pack(side=tk.RIGHT)

        for row in range(self.x_tiles):
            for column in range(self.y_tiles):
                button = tk.Button(boardContainer, width=self.tileSize, height=self.tileSize)
                button.grid(row=row, column=column)
                button.bind("<Button-3>", lambda event, r=row, c=column: self.show_popup(event, r, c))
                self.board[row][column] = button

    def draw(self):
        self.x_tiles = self.world.getTilesX()
        self.y_tiles = self.world.getTilesY()
        self.board = [[None] * self.y_tiles for _ in range(self.x_tiles)]
        self.create_board()

        for column in range(self.y_tiles):
            for row in range(self.x_tiles):
                organism = self.world.getOrganism(row, column)
                icon_path = ""

                if organism is not None:
                    if organism.getName() == Constants.NAME_HUMAN and organism.getDUR() > 0:
                        icon_path = "chad.png"
                    else:
                        icon_path = organism.getName() + ".png"
                else:
                    icon_path = "meadow.png"

                icon = self.create_icon(icon_path)
                self.board[row][column].config(image=icon)
                self.board[row][column].bind("<Button-3>", lambda event, r=row, c=column: self.show_popup(event, r, c))

    def create_icon(self, icon_path):
        image = tk.PhotoImage(file=icon_path)
        resized_image = image.subsample(self.tileSize, self.tileSize)
        return resized_image

    def show_popup(self, event, row, column):
        popup_menu = tk.Menu(self, tearoff=0)

        menu_items = ["Antelope", "Fox", "Sheep", "Turtle", "Wolf", "Belladonna", "Grass", "Guarana", "Sosnowsky", "Sow_thistle"]

        for item in menu_items:
            popup_menu.add_command(label=item, command=lambda r=row, c=column, name=item: self.add_organism(r, c, name))

        popup_menu.tk_popup(event.x_root, event.y_root)

    def add_organism(self, row, column, name):
        if name == "Antelope":
            organism = Antelope(self.world, row, column)
        elif name == "Fox":
            organism = Fox(self.world, row, column)
        elif name == "Sheep":
            organism = Sheep(self.world, row, column)
        elif name == "Turtle":
            organism = Turtle(self.world, row, column)
        elif name == "Wolf":
            organism = Wolf(self.world, row, column)
        elif name == "Belladonna":
            organism = Belladonna(self.world, row, column)
        elif name == "Grass":
            organism = Grass(self.world, row, column)
        elif name == "Guarana":
            organism = Guarana(self.world, row, column)
        elif name == "Sosnowsky":
            organism = Sosnowsky(self.world, row, column)
        elif name == "Sow_thistle":
            organism = Sow_thistle(self.world, row, column)
        else:
            return

        self.world.addOrganism(organism)