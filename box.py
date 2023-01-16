import tkinter as tk

class Draggable:
    def make_draggable(self, widget):
        widget.bind("<Button-1>", self.on_drag_start)
        widget.bind("<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

    def on_drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        widget.place(x=x, y=y)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.make_draggable(self)
        self.notes = tk.Text(self, height=5, width=20)
        self.notes.pack()




class Box(Draggable, tk.Frame):
    pass
