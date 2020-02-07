from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
#root = Tk()
"""topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text= "Button 1", fg="blue")
button2 = Button(topFrame, text= "Button 2", fg="yellow")
button3 = Button(topFrame, text= "Button 3", fg="red")
button4 = Button(bottomFrame, text= "Button 4", fg="green")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack() 
thelabel2 = Label( root, text="Texto expandido X",  bg="black", fg="white")
thelabel2.pack(fill=X)

thelabel3 = Label( root, text="Texto expandido Y",  bg="black", fg="white")
thelabel3.pack(fill=Y, side= BOTTOM)
"""
#Entradas y Grid
"""
user = Label(root, text="Usuario")
password = Label(root, text="Password")
entrada1 = Entry(root)
entrada2 = Entry(root)

user.grid(row=0, sticky=E)
password.grid(row=1, sticky=E)
entrada1.grid(row=0, column=1)
entrada2.grid(row=1, column=1,columnspan=2)

    #Checkbutton

check= Checkbutton(root, text="Keep me logged in")
check.grid(columnspan=2)
"""
#Click Button y evento
"""
def printName(event):
    print("Mi nombre es Juan")

#botonPrint = Button(root, text="¿Como te llamas?", command=printName)
botonPrint = Button(root, text="¿Como te llamas?")
#Eventos
botonPrint.bind("<Button-1>", printName)
botonPrint.pack()
"""
# Eventos en distintos clicks en frames
"""
def leftClick(event):
    print("Izquierda")

def rigthClick(event):
    print("Derecha")

def middleClick(event):
    print("Medio")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-3>",rigthClick)
frame.bind("<Button-2>",middleClick)
frame.pack()
"""

# Classes
"""
class ButtonsClass:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame, text="Print", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quickButton = Button(frame, text="Exit", command=frame.quit)
        self.quickButton.pack(side=LEFT)
    
    def printMessage(self):
        print("Lesson 8")

root= Tk()
b = ButtonsClass(root)
"""
#  Menu
"""
def doNothing():
    print("Has pinchado en el Menú")

root= Tk()    
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu= editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# Toolbar

toolbar = Frame(root)
insertButton = Button(toolbar, text="Insert", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)
saveButton = Button(toolbar, text="Save", command= doNothing)
saveButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

# Status Bar

status = Label(root, text="Waiting", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
"""

root = Tk()

#Messages Box
"""
tkinter.messagebox.showinfo('Titulo de la Ventana', 'Mensaje emergente')
answer = tkinter.messagebox.askquestion('Question 1','¿Do you like animals?')
if answer == 'yes':
    print(":)")
else:
    print(":(")
"""

#Shapes and Graphics
"""
canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0,0,200,100)
redLine = canvas.create_line(0,100,200,0, fill="red")
greenBox = canvas.create_rectangle(25,25,100,50, fill="green")
canvas.delete(redLine)
#DELETE ALL
canvas.delete(ALL)
"""

#Insert Photo
"""
img = ImageTk.PhotoImage(Image.open(file = "C:/Users/usuario/Desktop/frames/frame_00001.jpg"))  
label = Label(root,image=img)
label.pack()
"""

#Abrir otra ventana y minimizar la padre
"""
    otra_ventana = Tkinter.Toplevel(root)   
    root.iconify()

"""
root.mainloop()