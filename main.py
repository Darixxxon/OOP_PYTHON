import tkinter as tk
from tkinter import messagebox
import World
import Frame_Panel

class Main:
    def __init__(self):
        self.run_game()

    def run_game(self):
        try:
            width = int(input("Enter width: "))
            height = int(input("Enter height: "))
            world = World(width, height)
            frame_panel = Frame_Panel(world)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid integer values.")

if __name__ == "__main__":
    main = Main()