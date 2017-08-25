from Tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()  # it will create the frame widget and pack it

        self.button = Button(frame, text="Quit", fg='red', command=frame.quit)
        self.button.pack(side=LEFT)

        self.hello = Button(frame, text="Say hello", command=self.say_hello)
        self.hello.pack()

        # frame1 = Frame(width=268, height=276, bg="", colormap="new")
        # frame1.pack()

        Label(text="one").pack()

        separator = Frame(height=2, bd=10, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

    def say_hello(self):
        print "Hello to everyOne This is my first code for tkinter"


root = Tk()

w = Label(text="Hello bro", fg='green')
w.pack()

app = App(root)

root.mainloop()
root.destroy()
