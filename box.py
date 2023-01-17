import tkinter as tk
import json

class Draggable():
    def make_draggable(self, widget):
        widget.bind("<Button-1>", self.on_drag_start)
        widget.bind("<B1-Motion>", self.on_drag_motion)
        widget.bind("<Double-Button-1>", self.make_con)

    def make_con(self):
        print("let's join!")
        f = open('cache.json', 'r')
        data = json.load(f)
        f.close()

        if data["open_con"] == "":
            data["open_con"] = self.title.cget("text")
            data["open_vals"] = self.notes.get("1.0", "end-1c")
            print(data["open_vals"], data["open_con"])
        else:
            data["closed_cons"].append([data["open_con"], self.title.cget("text")])
            data["con_vals"].append([data["open_vals"], self.notes.get("1.0", "end-1c")])
            data["open_con"] = ""
            data["open_vals"] = ""
            print(data["closed_cons"])
        
        json_object = json.dumps(data, indent=4)

        with open("cache.json", "w") as outfile:
            outfile.write(json_object)

    def on_drag_start(self, event):
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

    def on_drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        widget.place(x=x, y=y)

    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.make_draggable(self)

        # Resize the frame to fit the widgets
        self.pack_propagate(True)

        # Create a frame to hold the widgets
        self.frame = tk.Frame(self, bd=2, height=100, width=200)
        self.frame.pack(fill="both", expand=True)

        # Split frame into header, body and results
        self.header = tk.Frame(self.frame, bd=2, height=50, width=200)
        self.header.pack(side="top", fill="both", expand=True)

        self.body = tk.Frame(self.frame, bd=2, height=50, width=200)
        self.body.pack(side="bottom", fill="both", expand=True)

        # Add widgets to the header
        self.title = tk.Label(self.header, text=title)
        self.title.pack(side="top", padx=5)

        self.con = tk.Button(self.header, text="Con", command=self.make_con)
        self.con.pack(side="left", padx=5)

        self.remove = tk.Button(self.header, text="Remove", command=self.destroy)
        self.remove.pack(side="right", padx=5)

        # Add widgets to the body
        self.notes = tk.Text(self.body, height=5, width=10)
        self.notes.pack(side="left", padx=5)


class Box(Draggable, tk.Frame):
    pass
