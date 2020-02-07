from tkinter import *
import tkinter

def iniciarVentanas(ventana):
    #ventanaPrincipal.title("Detection License Plates")
    #ventanaPrincipal.iconbitmap("form.ico")
    #ventanaPrincipal.geometry('{}x{}'.format(460, 350))
    ventana.geometry("1280x600+50+50")
    ventana.minsize(1280, 600)

def inicalizacion():
    
    frameInicio = Frame(ventanaPrincipal)
    frameInicio.pack(fill='both', expand=1, padx=400)
    buttonFoto = Button(frameInicio, text="Fotos")
    buttonFoto.pack(ipadx=10, ipady=10, side=LEFT, padx=100)
    buttonVideo = Button(frameInicio, text="Videos", command=pulsaVideos)
    buttonVideo.pack(side=LEFT,ipadx=10, ipady=10)
    buttonExit = Button(frameInicio, text="Salir", fg="red")

def pulsaVideos():
    ventanaVideos.deiconify()
    ventanaPrincipal.withdraw()
    frameVideo = Frame (ventanaPrincipal)
    frameVideo.pack(fill='both', expand=1)

    buttonPrueba = Button(frameVideo, text = "adsf")
    buttonPrueba.pack()

def cerrar_app():
    ventanaPrincipal.destroy()

ventanaPrincipal = Tk()
ventanaVideos = tkinter.Toplevel(ventanaPrincipal)
ventanaVideos.protocol("WM_DELETE_WINDOW", cerrar_app)
iniciarVentanas(ventanaPrincipal)
iniciarVentanas(ventanaVideos)
ventanaVideos.withdraw()


inicalizacion()


ventanaPrincipal.mainloop()
