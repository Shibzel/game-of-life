import tkinter as tk
from time import perf_counter

from .plate import Board
from .statehandler import BaseStateHandler, ConwaysStateHandler

MS_BEFORE_UPDATE = 150

class Frame(tk.Tk):
    def __init__(self, name: str = "Game Of Life by Shibzel", icon_fp: str = "icon.ico", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title(name)
        self.iconbitmap(icon_fp)

class GUI(tk.Canvas):
    def __init__(self, state_handler: BaseStateHandler = ConwaysStateHandler(Board(randomized=True)),
                 frame: tk.Tk = Frame(), height: int = 600, width: int = 600) -> None:
        super().__init__(master=frame, height=height, width=width)
        self.pack()
        self.state_handler = state_handler
        self.state = None
        
        lines, columns = self.state_handler.board.lines, self.state_handler.board.columns
        case_height, case_width = height // lines, width // columns
        self.cases = [
            [self.create_rectangle(i*case_height, j*case_width, (i+1)*case_height, (j+1)*case_width, fill="#CCCCCC")
                for i in range(lines)]
            for j in range(columns)
            ]
        
        button1 = tk.Button(self.master, text="Start", command=self.next)
        button1.pack()

        button2 = tk.Button(self.master, text="Stop", command=self.stop)
        button2.pack()
    
    def update(self) -> None:
        handler = self.state_handler
        board = handler.board
        for l in range(board.lines):
            for c in range(board.columns):
                color = '#000000' if board.array[l][c] else '#FFFFFC'
                self.itemconfigure(self.cases[l][c], fill=color)
    
    def next(self) -> None:
        start_time = perf_counter()
        self.state_handler.next_iteration()
        self.update()
        time = MS_BEFORE_UPDATE - (perf_counter() - start_time)*1000
        self.state = self.master.after(int(time) if time > 0 else 1, self.next)
    
    def stop(self) -> None:
        if self.state:
            self.master.after_cancel(self.state)
        self.master.destroy()
        
    def start(self) -> None:
        self.mainloop()