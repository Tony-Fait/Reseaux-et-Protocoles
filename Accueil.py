# -*- coding: utf-8 -*- 
#------------------------------ 
# Author        : MASTER 1 BDGL
# Author Title  : Eudiants en Math-Informatiques
# Compagny      : Run
#-----------------------------

#from ctypes import sizeof
#from msilib.schema import SelfReg
from socket import timeout
from tkinter import *
from tkinter import ttk
import tkinter as tkinter
import os
import glob
#from typing_extensions import Self
#from typing_extensions import Self
from PIL import Image, ImageTk, ImageGrab
from pathlib import Path

from tkinter import filedialog, messagebox



def main():
    fenetre_principal = Tk()
    fenetre_principal.geometry("1055x670")
    fenetre_principal.title('Run')
    fenetre_principal.iconbitmap("Images/icon.ico")
    fenetre_principal.resizable(False, False)    
    
    app = Fenetre1(fenetre_principal)
    
    fenetre_principal.mainloop()
    
    
class Fenetre1():
    #====================================== 
    # 1 - Classe de la fenêtre pricipale 
    #======================================
    
    def __init__(self, master):            
        self.master = master
        #------------------------------
        # Definition de Tab
        #-------------------------------          
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=BOTH, expand=TRUE)
        
        
        #=============================================== ========= ========= ================== 
        # 1 - PAGE D'ACCUEIL
        #=============================================== ========= ========= ========= ========= 
        
        #------------------------------
        # Definition du frameAccueil
        #-------------------------------         
        self.frameAccueil = ttk.Frame(self.notebook)
        self.notebook.add(self.frameAccueil, text='Accueil')
        
        
        
        ################################## CANVAS ACCUEIL ###################################################
        #------------------------------
        # Je dessine un canvas pour mon imageAccueil 
        #------------------------------- 
        self.canvasAccueil = Canvas(self.frameAccueil, height = 620, width = 1055, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvasAccueil.grid(row = 0, column = 0)
        
        #------------------------------
        # Pour mon image en arrière plan Accueil 
        #-------------------------------        
        self.backgroundImageAccueil = PhotoImage(file = f"Images/backgroundAccueil.png")
        self.background = self.canvasAccueil.create_image(525, 320.0, image=self.backgroundImageAccueil)
        


        ################################## LE BOUTON CENTRAL ###################################################
        self.img0 = PhotoImage(file = f"Images/img0.png")
        """
        En réalité ce modèle de bouton ne sera pas dans le frame mais plus tot sur le frame
        c'est un bouton indépendant
        """
        
        #------------------------------
        # Un bouton qui affiche un menu
        #-------------------------------         
        self.b0 = Menubutton(self.frameAccueil, image = self.img0, bg='black', bd=2, activebackground='pink', height =170, width=170)
        
        self.l0 = Label(self.frameAccueil, text = "Cliquez ici", bg = 'black', fg = 'white')
        self.l0.place(x = 750, y = 300)
        #------------------------------
        # Le menu de mon self.b0
        #-------------------------------         
        self.b0.menu = Menu(self.b0, tearoff=0)   
        self.b0["menu"] = self.b0.menu 
        
        self.v1 = IntVar() 
        self.v2 = IntVar()
        
        #------------------------------
        # cocher les boutons si on click
        #-------------------------------         
        self.b0.menu.add_checkbutton(label = "PING", variable = self.v1, command = self.BoutonPing)   
        self.b0.menu.add_checkbutton(label = "TRACEROUTE", variable = self.v2, command = self.BoutonTraceroute)
        
        self.b0.place(x=700, y=300)#C'est pourquoi on utilise la méthode place(), command = self.BoutonPing
        
        
        
        
        ################################## MENU ###################################################
        #------------------------------
        # Création de ma barre de menu 
        #-------------------------------        
        self.menubar = Menu(self.notebook)
        
        #------------------------------
        # Les commandes du menubar
        #-------------------------------         
        self.menubar.add_command(label = "A propos", command = self.Apropos)
        
        self.menubar.add_command(label = "Quitter!", command = self.Sortir)#self.master.quit
       
        #------------------------------
        # afficher le menu
        #-------------------------------         
        self.master.config(menu=self.menubar)
        
        #-------------------------------------------------------
        self.res = StringVar()
        
        
         
    ###################################### LES FONCTIONS ################################################### ##############
    #------------------------------
    # La fonction de la commande quitter
    #-------------------------------           
    def Sortir(self):
        import tkinter as tkinter
        self.jesors = tkinter.messagebox.askyesno('Système Run', 'Confirmez votre sortie')
        if self.jesors > 0:
            self.master.destroy()
            return
    
    #------------------------------
    # La fonction de la commande quitter
    #-------------------------------   
    def Apropos(self):
        import tkinter as tkinter
        tkinter.messagebox.showinfo('Système Run', "Run est un logiciel de diagnostic réseau développé par des étudiants en master 1 BDGL de l'UFHB de cocody en Cote d'ivoire\
        Run implémente essentiellement les fonctionnalités de Ping et de Traceroute. Ecrivez-nous à l'addresse tanowenceslas@gmail.com pour vos suggestions")
    
    def BoutonPing(self):
        self.v1.get()
        if self.v1.get()==True:
            self.framePing = ttk.Frame(self.notebook)
            self.notebook.add(self.framePing, text='Ping')
            
    
            ################################## CANVAS PING ###################################################
            #------------------------------
            # Je dessine un canvas pour mon imagel Ping
            #------------------------------- 
            self.canvasPing = Canvas(self.framePing, height = 620, width = 1055, bd = 0, highlightthickness = 0, relief = "ridge")
            self.canvasPing.grid(row = 0, column = 0)
            
            #------------------------------
            # Pour mon image en arrière plan Ping
            #-------------------------------        
            self.backgroundImagePing = PhotoImage(file = f"Images/backgroundPing.png")
            self.backgroundPing = self.canvasPing.create_image(525, 320.0, image=self.backgroundImagePing) 
            
            #------------------------------
            # Pour les entries
            #------------------------------- 
            ##############################################
            self.EntryPingImage = PhotoImage(file = f"Images/AddresseIpPing.png")
            self.EntryPingBackground = self.canvasPing.create_image(690.5, 35.5, image = self.EntryPingImage)
            
            self.TargetLabel = Label(self.canvasPing, text = 'Addresse Ip', bg = 'cyan', fg = 'black')#, state=DISABLED)
            self.TargetLabel.place(x = 480.5, y = 25)#, width = 208.0, height = 20)            
            
            self.target = Entry(self.canvasPing, bd = 0, bg = "#ffffff", highlightthickness = 0)
            self.target.place(x = 590.5, y = 25, width = 208.0, height = 20)
            self.target.insert(0, "")
            
            ##############################################
            self.EntryNombreImage = PhotoImage(file = f"Images/Nombre.png")
            self.EntryNombreBackground = self.canvasPing.create_image(690.5, 90.5, image = self.EntryNombreImage)
            
            self.countLabel = Label(self.canvasPing, text = 'Nombre', bg = 'cyan', fg = 'black')#, state=DISABLED)
            self.countLabel.place(x = 480.5, y = 80)#, width = 208.0, height = 20)            
            
            self.count = Entry(self.canvasPing, bd = 0, bg = "#ffffff", highlightthickness = 0)
            self.count.place(x = 590.5, y = 80, width = 208.0, height = 20)
            self.count.insert(0, "")
            
            ##############################################
            self.EntryTailleDuPaquetImage = PhotoImage(file = f"Images/TailleDuPaquet.png")
            self.EntryTailleDuPaquetBackground = self.canvasPing.create_image(690.5, 145.5, image = self.EntryTailleDuPaquetImage)
            
            self.sizeLabel = Label(self.canvasPing, text = 'Taille Paquet', bg = 'cyan', fg = 'black')#, state=DISABLED)
            self.sizeLabel.place(x = 480.5, y = 135)#, width = 208.0, height = 20)            
            
            self.size = Entry(self.canvasPing, bd = 0, bg = "#ffffff", highlightthickness = 0)
            self.size.place(x = 590.5, y = 135, width = 208.0, height = 20)
            self.size.insert(0, "")
            
            ##############################################
            self.EntryTTLImage = PhotoImage(file = f"Images/ttlo.png")
            self.EntryTTLImage = self.canvasPing.create_image(690.5, 200.5, image = self.EntryTTLImage)
            
            self.ttlLabel = Label(self.canvasPing, text = 'TTL', bg = 'cyan', fg = 'black')#, state=DISABLED)
            self.ttlLabel.place(x = 480.5, y = 190)#, width = 208.0, height = 20)            
            
            self.ttl = Entry(self.canvasPing, bd = 0, bg = "#ffffff", highlightthickness = 0)
            self.ttl.place(x = 590.5, y = 190, width = 208.0, height = 20)
            self.ttl.insert(0, "")
            
            ##############################################
            self.EntryTempsMortImage = PhotoImage(file = f"Images/TempsMort.png")
            self.EntryTempsMortBackground = self.canvasPing.create_image(690.5, 255.5, image = self.EntryTempsMortImage)
            
            self.timeoutLabel = Label(self.canvasPing, text = 'Temps Mort', bg = 'cyan', fg = 'black')#, state=DISABLED)
            self.timeoutLabel.place(x = 480.5, y = 245)#, width = 208.0, height = 20)            
            
            self.timeout = Entry(self.canvasPing, bd = 0, bg = "#ffffff", highlightthickness = 0)
            self.timeout.place(x = 590.5, y = 245, width = 208.0, height = 20)
            self.timeout.insert(0, "")
            
            """
            self.BigText = Text(self.canvasPing)#, state=DISABLED)
            self.BigText.place(x = 420.5, y = 400, width = 600.0, height = 200)
            #-------------------------------------------------
            self.BigText.insert(1.0, str(self.ExecutePingSiTuPeux))"""
            
            #GRAND LABEL EN BAS
            self.BigLabel = Label(self.canvasPing, relief=RAISED, textvariable = self.res, fg = 'black', bg = 'cyan', text='rrrrrrrrr')#, state=DISABLED)
            self.BigLabel.place(x = 420.5, y = 330, width = 600.0, height = 270)
            
            #self.BigLabel = Scale(self.canvasPing, variable = str(self.ExecutePingSiTuPeux), fg = 'black', bg = 'cyan')#, state=DISABLED)
            #self.BigLabel.place(x = 420.5, y = 330, width = 600.0, height = 270)           
            #-------------------------------------------------
                       
            
            ################################## LE BOUTON PING ###################################################
            self.ImageBoutonPingExecution = PhotoImage(file = f"Images/ping.png")
            """
            En réalité ce modèle de bouton ne sera pas dans le frame mais pluteau sur le frame
            c'est un bouton indépendant
            """
            
            #------------------------------
            # Un bouton qui exécute ping
            #-------------------------------         
            self.BoutonPingExecution = Button(self.framePing, image = self.ImageBoutonPingExecution, bg='black', bd=2, activebackground='cyan',
                                              height =110, width=180, command = self.ExecutePingSiTuPeux)
            self.BoutonPingExecution.place(x=850, y=180)
            
            
            #------------------------------
            
            # Une fonction qui exécute ping
            #------------------------------- 
    def ExecutePingSiTuPeux(self):
        from itertools import count
        from icmplib import ping
        #from logging import root
        #from pping import*
        from socket import timeout
        from pythonping import ping
 
        self.results = ping(self.target.get(), int(self.count.get()), int(self.size.get()), int(self.ttl.get()), float(self.timeout.get()), verbose=True)
        self.res.set(self.results)
        return
        
            
        #for result in self.results:  
        #    print(f'ip={result.target} {result.ttl} Envoyer={result.sent} Reçu={result.recv} Perdu={result.lost}  temps={result.avg_rtt} ms')
        
        
    
        
        return
                
    def BoutonTraceroute(self):
        self.v2.get()
        if self.v2.get()==True:
            self.frameTraceroute = ttk.Frame(self.notebook)
            self.notebook.add(self.frameTraceroute, text='Traceroute')
            #self.b0.menu.bind('<ButtonRelease-1>')
            
            ################################## CANVAS TRACEROUTE ###################################################
            #------------------------------
            # Je dessine un canvas pour mon image Traceroute 
            #------------------------------- 
            self.canvasTraceroute = Canvas(self.frameTraceroute, height = 620, width = 1055, bd = 0, highlightthickness = 0, relief = "ridge")
            self.canvasTraceroute.grid(row = 0, column = 0)
            
            #------------------------------
            # Pour mon image en arrière plan traceroute
            #-------------------------------        
            self.backgroundImageTraceroute = PhotoImage(file = f"Images/backgroundTraceroute.png")
            self.backgroundTraceroute = self.canvasTraceroute.create_image(525, 320.0, image=self.backgroundImageTraceroute) 
            
            #------------------------------
            # Pour les entries
            #------------------------------- 
            ##############################################
            self.EntryTracerouteImage = PhotoImage(file = f"Images/AddresseIpTraceroute.png")
            self.EntryTracerouteBackground = self.canvasTraceroute.create_image(690.5, 35.5, image = self.EntryTracerouteImage)
            
            self.strLabel = Label(self.canvasTraceroute, text = 'Addresse Ip', bg = 'cyan', fg = 'black')#, state=DISABLED)
            self.strLabel.place(x = 480.5, y = 25)#, width = 208.0, height = 20)          
            
            self.str = Entry(self.canvasTraceroute, bd = 0, bg = "#ffffff", highlightthickness = 0)#, font="Asenine")
            self.str.place(x = 590.5, y = 25, width = 208.0, height = 20)
            self.str.insert(0, "")            
            
            ###############################################
            self.EntryMaximumDeHoublonImage = PhotoImage(file = f"Images/MaximumDeHoublon.png")
            self.EntryMaximumDeHoublonBackground = self.canvasTraceroute.create_image(690.5, 90.5, image = self.EntryMaximumDeHoublonImage)
            
            self.MaximumDeHoublonLabel = Label(self.canvasTraceroute, text = 'Max. Houblon', bg = 'cyan', fg = 'black')#, state=DISABLED)
            self.MaximumDeHoublonLabel.place(x = 480.5, y = 80)#, width = 208.0, height = 20)            
            
            self.max_hops = Entry(self.canvasTraceroute, bd = 0, bg = "#ffffff", highlightthickness = 0)
            self.max_hops.place(x = 590.5, y = 80, width = 208.0, height = 20)
            self.max_hops.insert(0, "")
            
            ##############################################
            self.EntryWaitTimeImage = PhotoImage(file = f"Images/WaitTime.png")
            self.EntryWaitTimeBackground = self.canvasTraceroute.create_image(690.5, 145.5, image = self.EntryWaitTimeImage)
            
            self.sizeLabel = Label(self.canvasTraceroute, text = 'Taille Paquet', bg = 'cyan', fg = 'black')#, state=DISABLED)
            self.sizeLabel.place(x = 480.5, y = 135)#, width = 208.0, height = 20)              
            
            self.timeout = Entry(self.canvasTraceroute, bd = 0, bg = "#ffffff", highlightthickness = 0)
            self.timeout.place(x = 590.5, y = 135, width = 208.0, height = 20)
            self.timeout.insert(0, "")
            
            ##############################################
            self.EntryIntervalImage = PhotoImage(file = f"Images/Interval.png")
            self.EntryIntervalBackground = self.canvasTraceroute.create_image(690.5, 200.5, image = self.EntryIntervalImage)
            
            self.IntervalLabel = Label(self.canvasTraceroute, text = 'Interval', bg = 'cyan', fg = 'black')#, state=DISABLED)
            self.IntervalLabel.place(x = 480.5, y = 190)#, width = 208.0, height = 20) 
            
            self.interval = Entry(self.canvasTraceroute, bd = 0, bg = "#ffffff", highlightthickness = 0)
            self.interval.place(x = 590.5, y = 190, width = 208.0, height = 20)
            self.interval.insert(0, "")            
            
            #GRAND LABEL EN BAS
            self.BigLabel = Label(self.canvasTraceroute, textvariable = self.res, text = 'Taille Paquet', fg = 'black', bg = 'cyan')#, state=DISABLED)
            self.BigLabel.place(x = 420.5, y = 330, width = 600.0, height = 270)
        
            ################################## LE BOUTON TRACEROUTE ###################################################
            self.ImageBoutonTracerouteExecution = PhotoImage(file = f"Images/traceroute.png")
            """
            En réalité ce modèle de bouton ne sera pas dans le frame mais pluteau sur le frame
            c'est un bouton indépendant
            """
            #------------------------------
            # Un bouton qui exécute Traceroute
            #-------------------------------         
            self.BoutonTracerouteExecution = Button(self.frameTraceroute, image = self.ImageBoutonTracerouteExecution, bg='black', bd=2, activebackground='cyan',
                                              height =110, width=180, command=self.get_traceroute)
            self.BoutonTracerouteExecution.place(x=850, y=180)  
                     
            #self.b0.menu.add_checkbutton(label = "PING", variable = self.v1, command = self.BoutonPing, state=DISABLED)
    def  get_traceroute(self):
        #from logging import root
        from socket import timeout
        from icmplib import traceroute
        #from tkinter import*


        self.hops = traceroute(self.str.get(), int(self.timeout.get()), float(self.interval.get()), first_hop=1, id=None, max_hops=30, fast=False, source=None, family=None)
        self.res.set(self.hops)
        last_distance = 0
   
        for hop in self.hops:
           if last_distance +1 != hop.distance:
               print(f'distance={hop.distance} ip={hop.address} Min={hop.min_rtt} Max={hop.max_rtt} {hop.rtts} {hop.jitter} Envoyer={hop.packets_sent} Reçu={hop.packets_received} Perdu={hop.packet_loss} {hop.is_alive} temps={hop.avg_rtt} ms')
        
               last_distance = hop.distance
               

#FIN
if __name__ == '__main__':
    main()