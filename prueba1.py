from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1200, height=600)
canvas.pack()
x=900
y=200
imagej=PhotoImage(file="balon.png")
canvas.create_image(900,200,anchor=NW,image=imagej)
imagel=PhotoImage(file="Porte.png")
canvas.create_image(0,80,anchor=NW,image=imagel)

def movetriangle(event):
    global x
    global y
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
        y=y-3
        print(y)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
        y=y+3
        print(y)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
        x=x-3
        print(x)
        if(x<700):
            print("gol")
    else:
        canvas.move(1, 3, 0)
        x=x+3
        print(x)
       
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()



