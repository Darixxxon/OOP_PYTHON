import tkinter as tk
from tkinter import filedialog, messagebox

class FramePanel(tk.Tk):
    def __init__(self, world):
        super().__init__()
        self.x_tiles = 0
        self.y_tiles = 0
        self.bNextTurn = None
        self.mOpen = None
        self.mSave = None
        self.world = world
        self.board = None
        self.screenSize = self.winfo_screenwidth(), self.winfo_screenheight()

        self.setup_frame()

        self.title("Dariusz Morzuch 193074 meadow")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.world.makeTurn()
        self.board.draw()

    def setup_frame(self):
        self.geometry(f"{int(self.screenSize[0] * 0.9)}x{int(self.screenSize[1] * 0.9)}")
        mainPanel = tk.Frame(self)
        mainPanel.pack(fill=tk.BOTH, expand=True)
        self.board = BoardButtons(mainPanel, self.world, self.x_tiles, self.y_tiles, int(self.screenSize[1] * 0.9))

        buttonPanel = tk.Frame(mainPanel)
        self.bNextTurn = tk.Button(buttonPanel, text="Next turn", command=self.on_next_turn)
        self.bNextTurn.pack(side=tk.BOTTOM)
        buttonPanel.pack(side=tk.BOTTOM)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self)

        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="Open", accelerator="Ctrl+O", command=self.on_open)
        menu_file.add_command(label="Save", accelerator="Ctrl+S", command=self.on_save)

        menubar.add_cascade(label="Game", menu=menu_file)

        self.config(menu=menubar)

    def on_open(self):
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
        filepath = filedialog.askopenfilename(filetypes=filetypes)
        if filepath:
            try:
                self.world.open(filepath)
                messagebox.showinfo("Success", f"Opened file {filepath}")
            except Exception as e:
                messagebox.showerror("Error", f"Error while opening file:\n{e}")

    def on_save(self):
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
        filepath = filedialog.asksaveasfilename(filetypes=filetypes)
        if filepath:
            try:
                self.world.save(filepath)
                messagebox.showinfo("Success", f"Saved game at {filepath}")
            except Exception as e:
                messagebox.showerror("Error", f"Error while saving file:\n{e}")

    def on_next_turn(self):
        if self.world.isHumanLive_ == 0:
            try:
                self.world.makeTurn()
                self.board.draw()
            except Exception as e:
                messagebox.showerror("Error", f"Error while making the next turn:\n{e}")

    def on_close(self):
        self.destroy()


class BoardButtons(tk.Canvas):
    def __init__(self, parent, world, x_tiles, y_tiles, height):
        super().__init__(parent, width=x_tiles, height=y_tiles)
        self.world = world
        self.x_tiles = x_tiles
        self.y_tiles = y_tiles
        self.height = height

    def draw(self):
        # Implement the drawing logic here based on your requirements
        pass