from tkinter import *

root = Tk()
topFrame = Frame(root)
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

thelabel = Label(root, text="Hola", bg="black", fg="white")
thelabel.pack(side=BOTTOM)

thelabel2 = Label( root, text="Texto expandido X",  bg="black", fg="white")
thelabel2.pack(fill=X)

thelabel3 = Label( root, text="Texto expandido Y",  bg="black", fg="white")
thelabel3.pack(fill=Y, side= BOTTOM)

root.mainloop()