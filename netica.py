import tkinter as tk
from box import Box 


main = tk.Tk()
main.geometry("1280x720")

frame = Box(main, bd=5, bg="black")
frame.place(x=10, y=10)


tk.mainloop()

