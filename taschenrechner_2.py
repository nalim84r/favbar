#Einfacher Taschenrechner
#Benutzeroberfläche
#Vier Grundrechenarten
#Manuelle Werte Eingabe
#Ausgabe

import tkinter

def addieren():
    try:
        zahl1 = int(etEingabe1.get())
        zahl2 = int(etEingabe2.get())
        lbAusgabe["text"] = zahl1 + zahl2
    except:
        lbAusgabe["text"] = "Keine Zahlen"

def subtrahieren():
    try:
        zahl1 = int(etEingabe1.get())
        zahl2 = int(etEingabe2.get())
        lbAusgabe["text"] = zahl1 - zahl2
    except:
        lbAusgabe["text"] = "Keine Zahlen"

def multiplizieren():
    try:
        zahl1 = int(etEingabe1.get())
        zahl2 = int(etEingabe2.get())
        lbAusgabe["text"] = zahl1 * zahl2
    except:
        lbAusgabe["text"] = "Keine Zahlen"

def dividieren():
    try:
        zahl1 = int(etEingabe1.get())
        zahl2 = int(etEingabe2.get())
        lbAusgabe["text"] = zahl1 / zahl2
    except:
        lbAusgabe["text"] = "Keine Zahlen"  

def ende():
    fenster.destroy()



fenster = tkinter.Tk()
fenster.title("+-*/")
fenster.resizable(0,0)

lbEingabe = tkinter.Label(fenster, text="Ihre Eingabe:")
lbEingabe.grid(row=0, column=0, padx=5, pady=5)

etEingabe1 = tkinter.Entry(fenster, width=13)
etEingabe1.grid(row=0, column=1, padx=5, pady=5)

etEingabe2 = tkinter.Entry(fenster, width=13)
etEingabe2.grid(row=0, column=2, padx=5, pady=5)

buAdd = tkinter.Button(fenster, text="addieren", command=addieren,width=10)
buAdd.grid(row=1,column=1,sticky="w", padx=5, pady=5)

buSub = tkinter.Button(fenster, text="subtrahieren", command=subtrahieren,width=10)
buSub.grid(row=1, column=2, sticky="w",padx=5, pady=5)

buMulti = tkinter.Button(fenster, text="multiplizieren", command=multiplizieren,width=10)
buMulti.grid(row=2, column=1, sticky="w", padx=5, pady=5)

buDiv = tkinter.Button(fenster, text="dividieren", command=dividieren,width=10)
buDiv.grid(row=2, column=2, sticky="w", padx=5, pady=5)



lbAusgabe = tkinter.Label(fenster,text="rechnen wir!")
lbAusgabe.grid(row=4, column=0,sticky="w",padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende,width=10)
buEnde.grid(row=5, column=1,sticky="e",padx=5, pady=5)

fenster.mainloop()

