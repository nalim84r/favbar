#Einfacher Taschenrechner
#Benutzeroberfläche
#Multiplizieren
#Manuelle Werte Eingabe
#Ausgabe

import tkinter

def multiplizieren():
    try:
        zahl1 = int(etEingabe1.get())
        zahl2 = int(etEingabe2.get())
        lbAusgabe["text"] = zahl1 * zahl2
    except:
        lbAusgabe["text"] = "Keine Zahlen"  

def ende():
    fenster.destroy()



fenster = tkinter.Tk()
fenster.title("Multiplizieren")
fenster.resizable(0,0)

lbEingabe = tkinter.Label(fenster, text="Ihre Eingabe:")
lbEingabe.grid(row=0, column=0, sticky="w", padx=5, pady=5)

etEingabe1 = tkinter.Entry(fenster)
etEingabe1.grid(row=1, column=0,padx=5, pady=5)

etEingabe2 = tkinter.Entry(fenster)
etEingabe2.grid(row=2, column=0,padx=5, pady=5)

buMulti = tkinter.Button(fenster, text="", command=multiplizieren,width=10)
buMulti.grid(row=3, column=0,sticky="w",padx=5, pady=5)

lbAusgabe = tkinter.Label(fenster,text="...multiplizieren wir!")
lbAusgabe.grid(row=4, column=0,sticky="w",padx=5, pady=5)

buEnde = tkinter.Button(fenster, text="Ende", command=ende,width=10)
buEnde.grid(row=5, column=1,sticky="e",padx=5, pady=5)

fenster.mainloop()

