import tkinter as tk
from box import Box
from connectionmanager import compute
import json

cons = []
convals = {}

main = tk.Tk()
main.geometry("700x350")

button_container=tk.Frame(main, relief="sunken", borderwidth=2)
button_container.pack(side="top", fill="both")

attribute_container=tk.Frame(main, relief="sunken", borderwidth=2)
attribute_container.pack(side="bottom", fill="both")

side_container=tk.Frame(main, relief="sunken", borderwidth=2)
side_container.pack(side="left", fill= "both")


box_name=tk.Text(button_container, height=1, width=10)

# Create new widget with button
def new_box():
    title = box_name.get("1.0", "end-1c")
    if title == "":
        title = "Untitled"
    # pass in string from box_name
    frame = Box(title, side_container, bd=5, bg="black")
    frame.place(x=10, y=10)

def clean_cons():
    with open("cachebackup.json", "r") as outfile:
        data = json.load(outfile)
    
    with open("cache.json", "w") as outfile:
        json_object = json.dumps(data, indent=4)
        outfile.write(json_object)
    

# Add widgets in frames
new_box=tk.Button(button_container, text="New Box", command=new_box)
new_con=tk.Button(button_container, text="Clean", command=clean_cons)
save_btn=tk.Button(button_container, text="Run", command=compute)

new_box.pack(side="left", padx= 10)
new_con.pack(side="left", padx= 10)
save_btn.pack(side="left", padx=10)
box_name.pack(side="left", padx=10)

def draw_line(event):
   global click_num
   global x1,y1
   if click_num==0:
      x1=event.x
      y1=event.y
      click_num=1
   else:
      x2=event.x
      y2=event.y
      click_num=0
   # Draw the line in the given co-ordinates
   canvas.create_line(x1,y1,x2,y2, fill="black", width=5)

canvas=tk.Canvas(side_container, width=700, height=350, bg="white")
canvas.pack(side= "bottom", fill="both", expand=True)
canvas.bind('<Button-1>', draw_line)
click_num=0

txt_label=tk.Label(side_container, text=" "*1000)
txt_label.pack(side= "bottom", padx=10)


txt_label=tk.Label(attribute_container, text=" "*1000)
txt_label.pack(side= "bottom", padx=10)

tk.mainloop()