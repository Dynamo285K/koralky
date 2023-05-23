import tkinter as tk
import random
import PIL
root = tk.Tk()



w = 500
h = 500
colors = ["pink" ,"yellow", "blue", "green"]
count = 40
size = 20
image = tk.PhotoImage("koralik_nit.png")
moveable = []
processed = []
counter = 0

canvas = tk.Canvas(width=w, height=h, bg = 'white')
canvas.pack()
# for i in range(4):
#     for r in range(10):
#         x = random.randrange(0,450)
#         y = random.randrange(0,400)
#         canvas.create_oval(x,y,x+20,y+20, fill = colors[i])

def setup():
   global moveable
   for i in range(40):
       x = random.randrange(0,480)
       y = random.randrange(0,400)
       moveable.append(canvas.create_oval(x,y,x+size,y+size, fill = colors[i//10],outline = colors[i//10]))
       canvas.create_oval(50,460,70,480, fill = "black")
       canvas.create_line(70,470,480,470)
   # canvas.create_image(0,h-40, image = image,anchor = tk.NW)
setup()

def checkit(e):
    global processed, moveable
    zoz = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz) != 0 and zoz[0] in moveable:
        if len(processed) == 0:
            processed.append(zoz[0])
            moveable.remove(zoz[0])
            print("stalo sa")
            print(zoz)
            moveit()



def moveit():
    global processed, counter, zoz
    if len(processed) != 0:
        print(canvas.coords(processed[0]))
        coor = canvas.coords(processed[0])
        finalpos = (w-size,h-size)
        print(finalpos)
        dx = w-coor[2]
        dy = finalpos[1]-coor[3]
        # if coor[0] == finalpos[0]:
        if coor[0] > 479 and coor[0] < 481:
            coor1 = canvas.coords(processed[0])
            while coor1[0]> 70+counter*size:
                coor1 = canvas.coords(processed[0])
                canvas.move(processed[0],-1,0)
                canvas.update()
            else:
                processed.clear()
                counter += 1
                print("finish", counter)
                return processed

        elif dx > dy:
            dx = dx/dy
            dy = 1
        elif dx < dy:
            dy = dy/dx
            dx = 1
        # else:
            # if coor[0] == finalpos[0]:
            #     coor1 = canvas.coords(processed[0])
            #     while coor1[0]> 70+counter*size:
            #         coor1 = canvas.coords(processed[0])
            #         canvas.move(processed[0],-1,0)
            # else:
            #     processed.pop()[0]
            #     print("finish")
            #     return processed
        # if coor[1]>finalpos[1]:
        #     dy = coor[1]/finalpos[1]
        # elif coor[1]<finalpos[1]:
        #     dy = finalpos[1]/coor[1]
        canvas.move(processed[0],dx,dy)
    # print("ja budem hybat")
    canvas.after(5, moveit)
        




def move_on_line():
    lx = canvas.coords(processed[0])
    if lx >70 + 20*counter:
        canvas.move(processed[0],-1,0)
    canvas.after(5,move_on_line())



canvas.bind("<Button-1>", checkit)
# canvas.pack()
# moveit()

root.mainloop()
