from tkinter import *
from random import *

myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background="black")
s.pack()

x1 = 0
y1 = 0
w = 100

for i in range(0, 64):
    for j in range(0, 80):
        x2 = randint(x1+3, x1+w-3)
        y2 = randint(y1+3, y1+w-3)
        w2 = randint(0, 10)
        if y1 % 200 == 0:
            if x1 % 200 == 0:
                s.create_rectangle(x2, y2, x2+w2, y2+w2, fill="blue")
            else:
                s.create_rectangle(x2, y2, x2+w2, y2+w2, fill="green")
        else:
            if x1 % 200 == 0:
                s.create_rectangle(x2, y2, x2+w2, y2+w2, fill="green")
            else:
                s.create_rectangle(x2, y2, x2+w2, y2+w2, fill="blue")
    if x1+w >= 800:
        x1 = 0
        y1 += 100
    else:
        x1 += 100
    s.update()
    s.mainloop()
