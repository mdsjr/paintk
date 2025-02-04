from tkinter import *

class Paintk:

    def __init__(self):

        self.window = Tk()
        self.window.title("Paintk")
        self.window.minsize (width=1280, height=720)
        self.window.resizable(0,0)

        self.img_line = PhotoImage(file="icons/line.png")
        self.img_erase = PhotoImage(file="icons/eraser.png")
        self.img_new = PhotoImage(file="icons/new.png")
        self.img_oval = PhotoImage(file="icons/oval.png")
        self.img_save = PhotoImage(file="icons/save.png")
        self.img_square = PhotoImage(file="icons/square.png")

        self.colors = ("black", "#3b3b3b", "gray", "white", "red", "green", "blue", "purple", "orange", "yellow", "brown", "cyan", "pink")

        self.pick_colors = "black"

        self.bar_menu = Frame(self.window, bg="#3b3b3b", height=50)
        self.bar_menu.pack(fill=X)

        self.text_color = Label(self.bar_menu, text="  Color:  ",  fg="white", bg="#3b3b3b")
        self.text_color.pack(side=LEFT)

        for i in self.colors:
            self.button_color = Button(self.bar_menu, bg=i, width=3, height=2,
                                       command=lambda col=i :self.select_colors(col)).pack(side=LEFT)

        self.text_pen_size = Label(self.bar_menu, text="  Size:  ",  fg="white", bg="#3b3b3b").pack(side=LEFT)

        self.pen_size = Spinbox(self.bar_menu, from_=1, to=50)
        self.pen_size.pack(side=LEFT)


        self.text_brushs = Label(self.bar_menu, text="  Brushs:  ",  fg="white", bg="#3b3b3b").pack(side=LEFT)

        self.button_line = Button(self.bar_menu, image=self.img_line, command=None).pack(side=LEFT)
        self.button_line = Button(self.bar_menu, image=self.img_oval, command=None).pack(side=LEFT)
        self.button_line = Button(self.bar_menu, image=self.img_erase, command=None).pack(side=LEFT)

        self.text_options = Label(self.bar_menu, text="  Options:  ", fg="white", bg="#3b3b3b").pack(side=LEFT)

        self.button_save = Button(self.bar_menu, image=self.img_save, command=None).pack(side=LEFT)
        self.button_new = Button(self.bar_menu, image=self.img_new, command=None).pack(side=LEFT)



        self.area_draw = Canvas(self.window,  height=720)
        self.area_draw.pack(fill="both")
        self.area_draw.bind("<B1-Motion>", self.draw)


        self.window.mainloop()

    def draw(self, event):
        x1, y1 = (event.x), (event.y)
        x2, y2 = (event.x), (event.y)

        self.area_draw.create_oval(x1, y1, x2, y2, fill=self.pick_colors,
                                   outline=self.pick_colors, width=self.pen_size.get())

    def select_colors(self, col):
        self.pick_colors = col

Paintk()

