from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter


def canvasInterfaceframe(frame):
    canvasCoches = Canvas(frame, width=800, height=400)
    canvasCoches.grid(row=0, column=0)
    
    insertButton = Button(frame, text = "Insertar", command = lambda : abrirArchivo(canvasCoches))
    insertButton.grid(row=1, column=0, pady=10)
    #insertButton.bind("<Button-1>", abrirArchivo)
    

    

def iniciarVentanas(ventana):
    #ventanaPrincipal.title("Detection License Plates")
    #ventanaPrincipal.iconbitmap("form.ico")
    #ventanaPrincipal.geometry('{}x{}'.format(460, 350))
    ventana.geometry("1280x600+50+50")
    ventana.minsize(1280, 600)


def abrirArchivo(canvasCoches):
        archivo = filedialog.askopenfile()
        #archivoCoches=PhotoImage(file=archivo.name)
        global im
        global ima_prueba
        im= Image.open(archivo.name)
        ima_prueba = ImageTk.PhotoImage(im)
        canvasCoches.create_image(0,0, image=ima_prueba, anchor=NW)

def inicalizacion():
    frameInicio = Frame(ventanaPrincipal)
    frameInicio.pack(fill='both', expand=1, padx=400)
    buttonFoto = Button(frameInicio, text="Fotos")
    buttonFoto.pack(ipadx=10, ipady=10, side=LEFT, padx=100)
    buttonVideo = Button(frameInicio, text="Video", command=pulsaVideos)
    buttonVideo.pack(side=LEFT,ipadx=10, ipady=10)
    buttonExit = Button(frameInicio, text="Salir", fg="red")

def pulsaVideos():
    ventanaVideos.deiconify()
    ventanaPrincipal.withdraw()
    frameCanvas = Frame(ventanaVideos)
    frameCanvas.columnconfigure(0, weight=1)
    frameCanvas.rowconfigure(0, weight=1)
    frameCanvas.grid(sticky="nsew")
    #frameCanvas.pack(fill='both', expand=1)
    canvasInterfaceframe(frameCanvas)


def cerrar_app():
    ventanaPrincipal.destroy()

#MAIN

ventanaPrincipal = Tk()
ventanaVideos = tkinter.Toplevel(ventanaPrincipal)
ventanaVideos.protocol("WM_DELETE_WINDOW", cerrar_app)
iniciarVentanas(ventanaPrincipal)
iniciarVentanas(ventanaVideos)
ventanaVideos.withdraw()


inicalizacion()


ventanaPrincipal.mainloop()
