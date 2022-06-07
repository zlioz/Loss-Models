from tkinter import *               # Importa la libreria Tkinter con el asterisco implica que es con todas las clases dentro del paquete
import tkinter as tk
from PIL import Image, ImageTk
from math import *
from tkinter import ttk,Text,Label,Button,Entry,Frame,Tk,messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox
from turtle import end_fill, textinput
from urllib import request
import webbrowser
from tkinter.font import Font, nametofont
#from tkintermapview import TkinterMapView
import urllib


#======== Inicio del codigo ======================================================================================================

root = Tk()                                     # Crea la instancia de la clase Tk la cual iniciativa Tk y crea el interprete asociado a Tcl y Crea la ventana principal
root.title("Cálculo de Parametros en enlace")   # titulo de la ventana
root.geometry("900x600")                        # tamaño de la ventana
root.iconbitmap('Itm.ico')                      # pone icono en la ventana principal
#root.iconphoto(False, tk.PhotoImage(file='Itm.png'))   # pone icono en la ventana principal, soporta mas formatos

#======== Menu ======================================================================================================

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Botón no tiene acciones")
   button.pack()

def creditos():
   filewin = Toplevel(root)
   button = Button(filewin, text="Programado por Andrés Molina, Sebastian Ortiz y Julian Mosquera \n" + 
                                "\nCon la asesoria del Profesor del ITM: Germán David Goez Sánchez \n" + 
                                "\nPara la materia Radiocomunicaciones. ")
   button.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=donothing)
filemenu.add_command(label="Abrir", command=donothing)
filemenu.add_command(label="Save", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="Créditos", command= creditos)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


#======== Pestañas ======================================================================================================


def Zonafres():
    resultado= (17.32) * (sqrt(d.get()/(4*f.get())))
    
    lblResultados= ttk.Label(p1, text=" La zona de Fresnel es =  " + str(resultado) + " Mts").place(x=50, y=170)
    
    
def ZonafresN():
    C=3*10**8 
    
    Fn= sqrt((n.get()*(C/(f.get()*10**6))*d1.get()*d2.get())/(d1.get()+d2.get()))
    
    lblResultados= ttk.Label(p1, text=" La zona n de Fresnel es =   "  + str(Fn)+ " Mts").place(x=50, y=390)

def Okuha():
    
    ahm=((1.1*log10(f3.get())-0.7)*hm.get()) - (1.56*log10(f3.get())-0.8)
    Lb=69.55+(26.16*log10(f3.get()))-(13.82*(log10(hb.get())))-ahm+(44.9-6.55*log(hb.get()))*log10(dm.get())
    lblResultados= ttk.Label(p3, text=" La pérdida básica de propagación en ciudad media-pequeña es =   " + str(Lb)).place(x=50, y=390)
    

f = DoubleVar()
f2 = DoubleVar()
d = DoubleVar()
n = IntVar()
L = DoubleVar()
d1 = DoubleVar()
d2 = DoubleVar()
f3 = DoubleVar()
hb = DoubleVar()
hm = DoubleVar()
dm = DoubleVar()



#INCLUIMOS PANEL PARA LAS PESTAÑAS.
nb = ttk.Notebook(root)
nb.pack(fill='both',expand='yes')

#CREAMOS PESTAÑAS
p1 = ttk.Frame(nb)

fondo= PhotoImage(file='ITM.png')              # Establece la imagen gif o png
root= ttk.Label(p1, image=fondo, anchor="se")
root.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)

etiqueta13= ttk.Label(p1, text="Ingrese los datos para calcular la primera zona de Fresnel ").place(x=20,y=20)
etiqueta14= ttk.Label(p1, text="Ingrese la frecuencia (Ghz):").place(x=20,y=50)
etiqueta15= ttk.Label(p1, text="Ingrese la distancia entre enlaces (d en Km):").place(x=20,y=80)

etiqueta16= ttk.Label(p1, text="Ingrese los datos para calcular cualquier zona de Fresnel ").place(x=20,y=220)
etiqueta17= ttk.Label(p1, text="Ingrese la zona a calcular (n): ").place(x=20,y=250)
etiqueta18= ttk.Label(p1, text="Ingrese la frecuencia (Ghz): ").place(x=20,y=270)
etiqueta19= ttk.Label(p1, text="Ingrese la distancia 1 entre enlaces (d1 en Km): ").place(x=20,y=290)
etiqueta20= ttk.Label(p1, text="Ingrese la distancia 2 entre enlaces (d2 en Km): ").place(x=20,y=310)

p2 = ttk.Frame(nb)
#======== Variables y calculos ======================================================================================================

def Calculo ():
        VFr= Fr.get()
        Vbw= bw.get()
        VD= D.get()
        VGtx= Gtx.get()
        VA= A.get()
        Vgdbi= gdbi.get()
        Vcmin= cmin.get()
        VB= B.get()
        Vlf= lf.get()
        Vlb= lb.get()
        Vconfi= confi.get()
        Vsn= sn.get()
        

        C=3*10**8               #velocidad de la luz
        K = 1.38*10**-23        #Constante de boltzman
        T=290                   #KELVINS
        
        Porc=Vconfi/100
                
        FHz = VFr*10**9
                
        lfs=92.44+20*log10(VFr)+20*log10(VD)
                
        FM=30*log10(VD)+10*log10(6*VA*VB*VFr)-10*log10(1-(Porc))-70
        
        gi = 10**(Vgdbi/10) 
        
        Gs= FM + lfs + Vlf + Vlb - VGtx - Vgdbi
        
        ptx= Gs + Vcmin
        
        Ndbm=10*log10((K*T)/0.001)+10*log10(Vbw*10**6)
        
        cminn= Ndbm+Vsn
                
        pot= Gs+cminn
        
        PIRE = ptx-(Vlf/2)-(Vlb/2)+VGtx
        
        fr = PIRE+VGtx-lfs-FM
       
        lblResultados= ttk.Label(p2, text=" Los Calculos del enlace son: \n"
                                            + "\n Las Pérdidas por dispersión en espacio libre son = " + str(lfs)+" dB"
                                            + "\n La Confiabilidad del sistema es = " + str(Porc)+" ~ "+ str(Vconfi)+" % de confiabilidad"
                                            + "\n El Margen de desvanecimiento es =  " + str(FM)+" dB"
                                            + "\n La Ganancia del sistema es = " + str(Gs)+" dB"
                                            + "\n La Potencia ideal del radio Tx es =  " + str(ptx)+" dBm"
                                            + "\n La Potencia de Ruido es =  " + str(Ndbm)+" dBm"
                                            + "\n La nueva confiabilidad que se requiere para el sistema es =  " + str(cminn)+" dBm"
                                            + "\n La Potencia que cumple con el requerimiento de S/N es =  " + str(pot)+" dBm"
                                            + "\n La Potencia efectiva radiada (PIRE) es = " + str(PIRE)+" dB"
                                            + "\n La Potencia recibida (Friis) es =   " + str(fr)+" dBm").place(x=50, y=320)   # Muestra los resultados como etiquetas en un lugar de la pantalla


#========= FRAMES ==============================================================================================================

frm = ttk.Frame(p2, padding=50)   # Crea el marco del widget, el cual en este caso contendrá la etiqueta y el botón que crearemos después. El marco encaja dentro de la ventana raíz.
frm.grid()    

#======== Etiquetas e ingreso de valores en Frame1 ======================================================================================================

etiqueta1= ttk.Label(frm, text="Ingrese la frecuencia (GHz):").grid(column=0, row=0)
Fr=DoubleVar()
Frecuencia= Entry(frm, textvariable=Fr).grid(column=1, row=0)

etiqueta2= ttk.Label(frm, text="Ingrese el ancho de banda (MHz):").grid(column=0, row=1)
bw=DoubleVar()
Bw= Entry(frm, textvariable=bw).grid(column=1, row=1)

etiqueta3= ttk.Label(frm,justify=tk.RIGHT, text="Ingrese la distancia (Km):" ).grid(column=0, row=2)
D=DoubleVar()
Distancia= Entry(frm, textvariable=D).grid(column=1, row=2)

etiqueta4= ttk.Label(frm, text="Ingrese la ganancia de la antena Tx (dbi):", anchor="w").grid(column=0, row=3)   # Etiqueta para el widget que contiene una cadena de texto estática. El método grid() es usado para especificar la posición del diseño de la etiqueta que está dentro del marco del widget, similar a como trabajan las tablas en HTML.
Gtx=DoubleVar()
Gananciatx= Entry(frm, textvariable=Gtx).grid(column=1, row=3)

etiqueta5= ttk.Label(frm, text="Ingrese factor de aspereza del terreno:").grid(column=0, row=4)
A=DoubleVar()
Aspereza= Entry(frm, textvariable=A).grid(column=1, row=4)

etiqueta6= ttk.Label(frm, text="Ingrese la ganancia de la antena Rx (dbi):").grid(column=0, row=5)
gdbi=DoubleVar()
Gananciarx= Entry(frm, textvariable=gdbi).grid(column=1, row=5)

etiqueta7= ttk.Label(frm, text="Ingrese la sensibilidad minima del Rx (dbm):").grid(column=0, row=6)
cmin=DoubleVar()
cminbilidad= Entry(frm, textvariable=cmin).grid(column=1, row=6)

etiqueta8= ttk.Label(frm, text="Ingrese factor de condicion de clima:").grid(column=0, row=7)
B=DoubleVar()
Clima= Entry(frm, textvariable=B).grid(column=1, row=7)

etiqueta9= ttk.Label(frm, text="Ingrese perdida en alimentador de guia de onda(db):").grid(column=0, row=8)
lf=DoubleVar()
Perdidaguia= Entry(frm, textvariable=lf).grid(column=1, row=8)

etiqueta10= ttk.Label(frm, text="Ingrese perdida por acoplamiento (db):").grid(column=0, row=9)
lb=DoubleVar()
Perdidaaco= Entry(frm, textvariable=lb).grid(column=1, row=9)

etiqueta11= ttk.Label(frm, text="Ingrese confiabilidad del sistema (%):").grid(column=0, row=10)
confi=DoubleVar()
Confiablidad= Entry(frm, textvariable=confi).grid(column=1, row=10)

etiqueta12= ttk.Label(frm, text="Ingrese relacion señal a ruido (db):").grid(column=0, row=11)
sn=DoubleVar()
Sn= Entry(frm, textvariable=sn).grid(column=1, row=11)

botoncalculo= ttk.Button(frm, text="Calcular Enlace", command= Calculo).grid(column=1, row=13)


p3 = ttk.Frame(nb)
etiqueta21= ttk.Label(p3, text="El modelo de Okumura es utilizado para predecir la potencia en un receptor ubicado"
                                + "\nen un área urbana para comunicaciones móviles. Este modelo es aplicable para el"
                                + "\nrango de frecuencias entre 150 a 1920 MHz es decir comprende la banda de VHF Y UHF." 
                                + "\nSegún este modelo, la distancia máxima de separación que puede existir entre el " 
                                + "\ntransmisor y el receptor es de hasta 100 km. Puede ser usado para alturas de la " 
                                + "\nantena de la estación base en el rango de 30 m a 1000 m. ").place(x=20,y=30)
etiqueta22= ttk.Label(p3, text="Ingrese los datos para calcular ").place(x=20,y=150)

etiqueta23= ttk.Label(p3, text="Ingrese la frecuencia (Mhz): ").place(x=20,y=180)
etiqueta24= ttk.Label(p3, text="Ingrese la distancia entre enlaces (d en Km): ").place(x=20,y=200)
etiqueta25= ttk.Label(p3, text="Ingrese la altura de Tx: ").place(x=20,y=220)
etiqueta26= ttk.Label(p3, text="Ingrese la altura de Rx: ").place(x=20,y=240)

p4 = ttk.Frame(nb)

f3=DoubleVar()
d3=DoubleVar()

etiqueta27= ttk.Label(p4, text="El modelo COST 231 es un modelo semi-empírico de predicción de las pérdidas en un trayecto,"
                                + "\nresultado de la combinación de los modelos Walfisch-Bertoni e Ikegami."
                                + "\nEs recomendado para macro-células en escenarios urbanos y suburbanos, con buenos resultados de" 
                                + "\nlas pérdidas en el trayecto para antenas transmisoras situadas por encima de la altura media de" 
                                + "\nlos tejados. Sin embargo, el error en las predicciones aumenta considerablemente a medida que la " 
                                + "\naltura del transmisor se acerca a la altura de los tejados, llegando a tener un rendimiento muy"
                                + "\npobre para transmisores situados por debajo de ese nivel.\n"
                                + "\nRespecto a modelos precedentes como Okumura-Hata, el modelo COST 231 incluye"
                                + "\nuna serie de parámetros adicionales al proceso de cálculo, además de ampliar"
                                + "\nel rango de frecuencias en el cual puede usarse (800 - 2000 MHz)." ).place(x=20,y=30)


def COST ():
    lost= 42.6+(26*log10(d3.get()))+(20*log10(f3.get()))
    lblResultados= ttk.Label(p4, text=" La pérdida básica de propagación con el modelo Cost 231 es: " + str(lost)+" dB").place(x=20,y=370)

etiqueta28= ttk.Label(p4, text="Ingrese los datos para calcular ").place(x=20,y=230)
etiqueta29= ttk.Label(p4, text="Ingrese la frecuencia (Mhz): ").place(x=20,y=250)
etiqueta30= ttk.Label(p4, text="Ingrese la distancia entre enlaces (d en Km): ").place(x=20,y=270)

Entry(p4, textvariable= f3).place(x=300,y=250)
Entry(p4, textvariable= d3).place(x=300,y=270)

botoncost= ttk.Button(p4, text="Calcular COST", command= COST).place(x=320,y=300)

p5 = ttk.Frame(nb)

etiqueta31= ttk.Label(p5, text="El modelo Longley-Rice predice la posible propagación a larga-media distancia"
                                + "\nsobre terreno irregular. Fue diseñado para frecuencias entre los 20MHz y"
                                + "\n20GHz, para longitudes de trayecto de entre 1 y 2000 Km.").place(x=20,y=30)


etiqueta32= ttk.Label(p5, text="Dirijase a la página de Xirio-online para reliazar los cálculos de este modelo ").place(x=20,y=100)

def hipervinculo ():                                # Crea un botón que abre una pagina web
        webbrowser.open("https://www.xirio-online.com/web/")
Button(p5, text='Xirio Online',bg='light blue',command=hipervinculo,cursor="hand2").place(x=180,y=130)


p6 = ttk.Frame(nb)
## API de google maps
## pip install -U googlemaps
## pip install --upgrade pip

#import googlemaps
#from datetime import datetime

#gmaps = googlemaps.Client(key='Add Your Key here')

## Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

## Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))


#=========Solo mostrar mapa de colombia con un marcador en medellin========================================================
# create map widget
map_widget = TkinterMapView(p6, width=600, height=400, corner_radius=0)
map_widget.pack(fill="both", expand=True)

# google normal tile server
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

map_widget.set_address("Colombia ITM Medellin", marker=True)
map_widget.set_address("Colombia Volador Medellin", marker=True)
#==========================================================================================================================


#ELEMENTOS PESTAÑA 3

Button(p3, text='Calcular O-H',bg='light blue',command= Okuha).place(x=320,y=260)
Entry(p3, textvariable= f3).place(x=300,y=180)
Entry(p3, textvariable= hb).place(x=300,y=200)
Entry(p3, textvariable= hm).place(x=300,y=220)
Entry(p3, textvariable= dm).place(x=300,y=240)

#ELEMENTOS PESTAÑA fresnel.1

Button(p1, text='Calcular r1',bg='light blue',command= Zonafres).place(x=330,y=110)
Entry(p1, textvariable= f).place(x=300,y=50)
Entry(p1, textvariable= d).place(x=300,y=80)

Button(p1, text='Calcular rn',bg='light blue',command= ZonafresN).place(x=330,y=340)
Entry(p1, textvariable= n).place(x=300,y=250)
Entry(p1, textvariable= f2).place(x=300,y=270)
Entry(p1, textvariable= d1).place(x=300,y=290)
Entry(p1, textvariable= d2).place(x=300,y=310)


#AGREGAMOS PESTAÑAS CREADAS
nb.add(p1,text='Zonas de Fresnel')
nb.add(p2,text='Path Loos')
nb.add(p3,text='Okumura-Hata')
nb.add(p4,text='Cost 231')
nb.add(p5,text='Longley-Rice')
nb.add(p6,text='API Google Maps')



#======== Botones ======================================================================================================



#botoncerrar= ttk.Button(root, text="Salir", command= root.quit).place(x=500,y=110)


#======== Fin del codigo ======================================================================================================

root.mainloop()             # El método mainloop() muestra todo en pantalla y responde a la entrada del usuario hasta que el programa termina.

