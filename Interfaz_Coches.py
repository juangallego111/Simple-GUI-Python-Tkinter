from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import tkinter
import cv2
import numpy as np
import pytesseract
#Para window
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"




CONF_THRESH, NMS_THRESH = 0.2, 0.2

CONFIG = "C:/Users/usuario/Desktop/darknet/yolov3.cfg" #'darknet/yolov31.cfg'
WEIGHTS = "C:/Users/usuario/Desktop/darknet/backup/yolov3_2000.weights" #'darknet/backup/yolov3_2000.weights'
NAMES = "C:/Users/usuario/Desktop/darknet/obj.names" #'darknet/obj.names'

def canvasInterfaceframe(frame):
    canvasCoches = tkinter.Canvas(frame, width=800, height=400, bg="black")
    canvasCoches.grid(row=0, column=0)
    label1 = tkinter.Label(frame, text = "Elige la Matrícula")
    label1.grid(row=0, column=1, padx=10)
    lista = tkinter.Listbox(frame)
    lista.grid(row=0, column=2, padx=10)
    values= ("Python", "C", "C++", "Java")
    lista.insert(0,*values)
    #Llama a la funcion cuando cambian de selección
    #combo.bind("<<ComboboxSelected>>", self.selection_changed)
    insertButton = tkinter.Button(frame, text = "Insertar", command = lambda : abrirArchivo(canvasCoches))
    insertButton.grid(row=1, column=0, pady=10)
    runButton = tkinter.Button(frame, text = "Ejecutar", command = lambda : ejecutar_red(ruta_ima, canvasCoches, lista))
    runButton.grid(row=1, column=1, pady=10)
    #insertButton.bind("<Button-1>", abrirArchivo)
    

def iniciarVentanas(ventana):
    #ventanaPrincipal.title("Detection License Plates")
    #ventanaPrincipal.iconbitmap("form.ico")
    #ventanaPrincipal.geometry('{}x{}'.format(460, 350))
    ventana.geometry("1280x600+50+50")
    ventana.minsize(1280, 600)


def abrirArchivo(canvasCoches):
        global ruta_ima
        archivo = filedialog.askopenfile()
        ruta_ima = archivo.name
        #archivoCoches=PhotoImage(file=archivo.name)
        global rImg
        im= Image.open(archivo.name)
        o_size = im.size
        f_size= (800,400)
        factor = min(float(f_size[1])/o_size[1], float(f_size[0])/o_size[0])
        width = int(o_size[0] * factor)
        height = int(o_size[1] * factor)

        rImg= im.resize((width, height), Image.ANTIALIAS)
        rImg = ImageTk.PhotoImage(rImg)

        #ima_prueba = ImageTk.PhotoImage(im)

        canvasCoches.create_image(f_size[0]/2, f_size[1]/2, image=rImg, anchor=tkinter.CENTER)

def mostrar_imagen(canvasCoches):
    global rImg
    im= Image.open("resultado"+str(nombre_img)+".jpg")
    o_size = im.size
    f_size= (800,400)
    factor = min(float(f_size[1])/o_size[1], float(f_size[0])/o_size[0])
    width = int(o_size[0] * factor)
    height = int(o_size[1] * factor)

    rImg= im.resize((width, height), Image.ANTIALIAS)
    rImg = ImageTk.PhotoImage(rImg)
    canvasCoches.create_image(f_size[0]/2, f_size[1]/2, image=rImg, anchor=tkinter.CENTER)

def inicalizacion():
    frameInicio = tkinter.Frame(ventanaPrincipal)
    frameInicio.pack(fill='both', expand=1, padx=400)
    buttonFoto = tkinter.Button(frameInicio, text="Fotos", command=pulsaFotos)
    buttonFoto.pack(ipadx=10, ipady=10, side=LEFT, padx=100)
    buttonVideo = tkinter.Button(frameInicio, text="Video")
    buttonVideo.pack(side=LEFT,ipadx=10, ipady=10)
    #buttonExit = tkinter.Button(frameInicio, text="Salir", fg="red")

def pulsaFotos():
    ventanaVideos.deiconify()
    ventanaPrincipal.withdraw()
    frameCanvas = tkinter.Frame(ventanaVideos)
    frameCanvas.columnconfigure(0, weight=1)
    frameCanvas.rowconfigure(0, weight=1)
    frameCanvas.grid(sticky="nsew")
    #frameCanvas.pack(fill='both', expand=1)
    canvasInterfaceframe(frameCanvas)


def cerrar_app():
    ventanaPrincipal.destroy()

def ejecutar_red(imagen_red, canvasCoches,lista):
    # Load the network
    lista.delete(0, END)
    net = cv2.dnn.readNetFromDarknet(CONFIG, WEIGHTS)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    # Get the output layer from YOLO
    layers = net.getLayerNames()
    output_layers = [layers[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Read and convert the image to blob and perform forward pass to get the bounding boxes with their confidence scores
    img = cv2.imread(imagen_red)
    img_bn = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    height, width = img_bn.shape[:2]
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_outputs = net.forward(output_layers)

    class_ids, confidences, b_boxes = [], [], []
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > CONF_THRESH:
                center_x, center_y, w, h = (detection[0:4] * np.array([width, height, width, height])).astype('int')

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                b_boxes.append([x, y, int(w), int(h)])
                confidences.append(float(confidence))
                class_ids.append(int(class_id))

    # Perform non maximum suppression for the bounding boxes to filter overlapping and low confident bounding boxes
    indices = cv2.dnn.NMSBoxes(b_boxes, confidences, CONF_THRESH, NMS_THRESH).flatten().tolist()

    # Draw the filtered bounding boxes with their class to the image
    with open(NAMES, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    color = (255, 0, 0) 
    for index in indices:
        x, y, w, h = b_boxes[index]
        print(x,y,w,h)
        crop_img = img_bn[y:y+h, x:x+w]

        ret,thresh = cv2.threshold(crop_img,0,255,cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
        #ret,thresh2 = cv2.threshold(crop_img,127,255,cv2.THRESH_BINARY)
        #contornos, jerarquia = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.imwrite("1_1"+".jpg",thresh)
        blurred = cv2.GaussianBlur(thresh, (3, 3), 0)
        #wide = cv2.Canny(crop_img, 10, 200)
        #edged = cv2.Canny(crop_img, lower, upper)
        texto = pytesseract.image_to_string(blurred, config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 7') #config='--psm 7'
        #texto1 = pytesseract.image_to_string(crop_img, config='--psm 7')
        #texto1 = pytesseract.image_to_string(blurred, lang='eng', config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        #cv2.imwrite("recortada"+".jpg",crop_img)

        print(texto)
        lista.insert(lista.size(), texto)
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    
    global nombre_img
    nombre_img = nombre_img + 1
    cv2.imwrite("resultado"+str(nombre_img)+".jpg",img)
    mostrar_imagen(canvasCoches)
    #leer_matricula(x,y,w,h,imagen_red)

#MAIN
nombre_img = 0
ventanaPrincipal = tkinter.Tk()
ventanaVideos = tkinter.Toplevel(ventanaPrincipal)
ventanaVideos.protocol("WM_DELETE_WINDOW", cerrar_app)
iniciarVentanas(ventanaPrincipal)
iniciarVentanas(ventanaVideos)
ventanaVideos.withdraw()


inicalizacion()


ventanaPrincipal.mainloop()
