


import tkinter as tk


CELL = 44       
MARGIN = 18     
INSET = 13      

GRID_COLOR = "#333333"
PEG_COLOR = "#1f2933"
CANVAS_BG = "#f7f7f5"


BOARD_LAYOUTS = {
    "English": [
        "  ooo  ",
        "  ooo  ",
        "ooooooo",
        "ooo.ooo",
        "ooooooo",
        "  ooo  ",
        "  ooo  ",
    ],
    "Hexagon": [
        "  ooo  ",
        " ooooo ",
        "ooooooo",
        "ooo.ooo",
        "ooooooo",
        " ooooo ",
        "  ooo  ",
    ],
    "Diamond": [
        "   o   ",
        "  ooo  ",
        " ooooo ",
        "ooo.ooo",
        " ooooo ",
        "  ooo  ",
        "   o   ",
    ],
}


class Sprint0Window(tk.Frame):
    """The main window."""

    def __init__(self, master):
        super().__init__(master, padx=14, pady=14)
        master.title("Peg Solitaire - CS 449 Sprint 0")
        master.resizable(False, False)
        self.pack()

        
        self.board_type = tk.StringVar(value="English")
        self.record_game = tk.BooleanVar(value=True)
        self.status = tk.StringVar()

        # Three horizontal strips, built top to bottom.
        self.build_top()
        self.build_middle()
        self.build_bottom()

        # Draw the starting board.
        self.refresh()

    
    def build_top(self):
        """The title bar strip."""
        top = tk.Frame(self)
        top.pack(fill=tk.X)

        
        tk.Label(
            top,
            text="Sample GUI of Solitaire",
            font=("TkDefaultFont", 14, "bold"),
        ).pack(side=tk.LEFT)

        
        tk.Label(top, text="7", relief=tk.SUNKEN, width=4).pack(side=tk.RIGHT)
        tk.Label(top, text="Board size").pack(side=tk.RIGHT, padx=(0, 6))

    
    def build_middle(self):
        """Radio buttons on the left, the board on the right."""
        middle = tk.Frame(self)
        middle.pack(pady=12)

        left = tk.Frame(middle)
        left.pack(side=tk.LEFT, anchor=tk.N, padx=(0, 16))

        tk.Label(left, text="Board Type").pack(anchor=tk.W)

        
        for name in BOARD_LAYOUTS:
            tk.Radiobutton(
                left,
                text=name,
                value=name,
                variable=self.board_type,
                command=self.refresh,
            ).pack(anchor=tk.W)

        
        self.canvas = tk.Canvas(
            middle,
            width=7 * CELL + 2 * MARGIN,
            height=7 * CELL + 2 * MARGIN,
            background=CANVAS_BG,
            highlightthickness=0,
        )
        self.canvas.pack(side=tk.LEFT)

   
    def build_bottom(self):
        """Check box on the left, status text on the right."""
        bottom = tk.Frame(self)
        bottom.pack(fill=tk.X)

        tk.Checkbutton(
            bottom,
            text="Record game",
            variable=self.record_game,
            command=self.refresh,
        ).pack(side=tk.LEFT)

       
        tk.Label(bottom, textvariable=self.status, foreground="#555555").pack(
            side=tk.RIGHT
        )

    
    def refresh(self):
        """Clear the canvas and redraw whichever board is selected."""
        layout = BOARD_LAYOUTS[self.board_type.get()]
        self.canvas.delete("all")

        pegs = 0
        for row, line in enumerate(layout):
            for col, symbol in enumerate(line):
                if symbol == " ":
                    continue           
                self.draw_square(row, col)
                if symbol == "o":
                    self.draw_peg(row, col)
                    pegs += 1

        recording = "on" if self.record_game.get() else "off"
        self.status.set(
            f"{self.board_type.get()} board - {pegs} pegs - recording {recording}"
        )

    def draw_square(self, row, col):
        """Draw the four lines outlining one position on the board."""
        
        x0 = MARGIN + col * CELL
        y0 = MARGIN + row * CELL
        x1 = x0 + CELL
        y1 = y0 + CELL

        # Four lines, each starting where the previous one ended.
        self.canvas.create_line(x0, y0, x1, y0, fill=GRID_COLOR)   # top
        self.canvas.create_line(x1, y0, x1, y1, fill=GRID_COLOR)   # right
        self.canvas.create_line(x1, y1, x0, y1, fill=GRID_COLOR)   # bottom
        self.canvas.create_line(x0, y1, x0, y0, fill=GRID_COLOR)   # left

    def draw_peg(self, row, col):
        """Draw a filled circle inside one square."""
        
        x0 = MARGIN + col * CELL + INSET
        y0 = MARGIN + row * CELL + INSET
        x1 = MARGIN + (col + 1) * CELL - INSET
        y1 = MARGIN + (row + 1) * CELL - INSET
        self.canvas.create_oval(x0, y0, x1, y1, fill=PEG_COLOR, outline=PEG_COLOR)


def main():
    """Build the window and hand control to Tkinter."""
    root = tk.Tk()
    Sprint0Window(root)
    root.mainloop()


if __name__ == "__main__":
    main()