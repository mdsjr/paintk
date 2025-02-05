from tkinter import *

from tkinter import colorchooser

import pyscreenshot

class Paintk:

    def __init__(self):

        self.window = Tk()
        self.window.title("Paintk")
        self.window.minsize (width=1280, height=720)
        self.window.resizable(0,0)

        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False


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

        self.label_colors_choose = Label(self.bar_menu, text="  Color Choose:  ",  fg="white", bg="#3b3b3b")
        self.label_colors_choose.pack(side=LEFT)

        self.color_choose = Button(self.bar_menu, image=self.img_square, command=self.selected_color)
        self.color_choose.pack(side=LEFT)

        self.text_pen_size = Label(self.bar_menu, text="  Size:  ",  fg="white", bg="#3b3b3b").pack(side=LEFT)

        self.pen_size = Spinbox(self.bar_menu, from_=1, to=50)
        self.pen_size.pack(side=LEFT)


        self.text_brushs = Label(self.bar_menu, text="  Brushs:  ",  fg="white", bg="#3b3b3b").pack(side=LEFT)

        self.button_line = Button(self.bar_menu, image=self.img_line, command=self.brush_line).pack(side=LEFT)
        self.button_oval = Button(self.bar_menu, image=self.img_oval, command=self.brush_oval).pack(side=LEFT)
        self.button_eraser = Button(self.bar_menu, image=self.img_erase, command=self.brush_eraser).pack(side=LEFT)

        self.text_options = Label(self.bar_menu, text="  Options:  ", fg="white", bg="#3b3b3b").pack(side=LEFT)

        self.button_save = Button(self.bar_menu, image=self.img_save, command=self.save).pack(side=LEFT)
        self.button_new = Button(self.bar_menu, image=self.img_new, command=self.clean).pack(side=LEFT)



        self.area_draw = Canvas(self.window,  height=720, bg="gainsboro")
        self.area_draw.pack(fill="both")
        self.area_draw.bind("<B1-Motion>", self.draw)

        self.window.bind("<F1>", self.clean)
        self.window.bind("<F2>", self.save)


        self.window.mainloop()

    def draw(self, event):
        x1, y1 = (event.x), (event.y)
        x2, y2 = (event.x), (event.y)

        if self.oval_brush:
            self.area_draw.create_oval(x1, y1, x2, y2, fill=self.pick_colors, outline=self.pick_colors, width=self.pen_size.get())

        elif self.line_brush:
            self.area_draw.create_line(x1 -10, y1 -10, x2, y2, fill=self.pick_colors, width=self.pen_size.get())

        else:
            self.area_draw.create_oval(x1, y1, x2, y2, fill="gainsboro", outline="gainsboro", width=self.pen_size.get())


    def select_colors(self, col):
        self.pick_colors = col


    def brush_oval(self):
        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False

    def brush_line(self):
        self.oval_brush = False
        self.line_brush = True
        self.eraser_brush = False

    def brush_eraser(self):
        self.oval_brush = False
        self.line_brush = False
        self.eraser_brush = True

    def clean(self, event):
        self.area_draw.delete("all")

    from PIL import ImageGrab

    def save(self, event):
        from PIL import ImageGrab  # Importação dentro da função
        x = self.window.winfo_rootx() + self.area_draw.winfo_x()
        y = self.window.winfo_rooty() + self.area_draw.winfo_y()
        x1 = x + self.area_draw.winfo_width()
        y1 = y + self.area_draw.winfo_height()

        img = ImageGrab.grab().crop((x, y, x1, y1))
        img.save("image.png", "PNG")

    def selected_color(self):
        color = colorchooser.askcolor()
        print(color)
        self.pick_colors = color[1]

     #   x = self.window.winfo_rootx() + self.area_draw.winfo_x()
     #   y = self.window.winfo_rooty() + self.area_draw.winfo_y()
     #   x1 = self.window.winfo_rootx() + self.area_draw.winfo_width()
     #   y1 = self.window.winfo_rooty() + self.area_draw.winfo_height()

     #   img = pyscreenshot.grab(bbox=(x,y, x1, y1))
     #   img.save("image.jpeg", "jpeg")

     # No Windows, o pyscreenshot não funciona perfeitamente, ele acaba salvando além da área de desenho, então utilizamos o ImageGrab.



Paintk()

#Também podemos utilizar o ImageGrab no lugar do pyscreenshot.

#def save_canvas(self):

 #       from PIL import ImageGrab

 #      x=self.window.winfo_rootx()+self.drawing_area.winfo_x()

 #       y=self.window.winfo_rooty()+self.drawing_area.winfo_y()

 #       x1=x+self.drawing_area.winfo_width()

 #       y1=y+self.drawing_area.winfo_height()

 #       ImageGrab.grab().crop((x,y,x1,y1)).save("teste.png")