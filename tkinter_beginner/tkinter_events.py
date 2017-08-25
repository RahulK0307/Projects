from Tkinter import *

root = Tk()


def caller(event):
    print "my value called : ", event.x, event.y

frame = Frame(root, height=300, width=300)
frame.bind("<Button-1>", caller)
frame.pack()

root.mainloop()
