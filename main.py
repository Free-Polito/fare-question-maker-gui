#!/usr/bin/python
# -*- coding: utf-8 -*-
# questionmakergui main py file
# Author: libremente <surf [AT] libremente [DOT] eu>

# Imports
from Tkinter import Tk, BOTH, X, LEFT, RIGHT
from ttk import Frame, Label, Entry, Button
from random import randint
import tkMessageBox

# QuestionMaker main class
class QuestionMaker(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()

    def initUI(self):
      
        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)
       
        ## Frame 0 - Description Only 
        frame0 = Frame(self)
        frame0.pack(fill=X)
        
        descrizione = Label(frame0, text="Compilare tutti i campi e poi salvare per inserire una nuova riga nel file delle domande", width=100)
        descrizione.pack(side=LEFT, padx=5, pady=5)

        ### Frame 1
        frame1 = Frame(self)
        frame1.pack(fill=X)
        
        domanda = Label(frame1, text="Domanda", width=20)
        domanda.pack(side=LEFT, padx=5, pady=5)           
       
        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)
        
        ### Frame 2
        frame2 = Frame(self)
        frame2.pack(fill=X)
        
        risposta1 = Label(frame2, text="Risposta 1 - ERRATA", width=20)
        risposta1.pack(side=LEFT, padx=5, pady=5)        

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=False)
        
        ### Frame 3
        frame3 = Frame(self)
        frame3.pack(fill=X)
        
        risposta2 = Label(frame3, text="Risposta 2 - ERRATA", width=20)
        risposta2.pack(side=LEFT, padx=5, pady=5)        

        entry3 = Entry(frame3)
        entry3.pack(fill=X, padx=5, expand=True)

        ### Frame 4
        frame4 = Frame(self)
        frame4.pack(fill=X)
        
        risposta_giusta = Label(frame4, text="Risposta CORRETTA", width=20)
        risposta_giusta.pack(side=LEFT, padx=5, pady=5)        

        entry4 = Entry(frame4)
        entry4.pack(fill=X, padx=5, expand=True)

        ### Frame 6
        frame6 = Frame(self)
        frame6.pack(fill=BOTH, expand=True)
        
        # Close button -> close on click
        close_button = Button(self, text="Chiudi", command=self.master.quit)
        close_button.pack(side=RIGHT, padx=5, pady=5)

        # Save button -> save a new line in the file and continues the exec
        ok_button = Button(self, text="Salva", 
                command=lambda: self.value_get(
                    entry1.get(), entry2.get(), entry3.get(), entry4.get()
                ))
        ok_button.pack(side=RIGHT)

    def value_get(self, domanda, r1, r2, rcorrect):
        # check
        if not domanda:
            # not defined 
            tkMessageBox.showinfo("Attenzione!", "Non è stato inserito correttamente il testo della domanda! Reinserire grazie")
            return
        if not r1:
          # not defined 
          tkMessageBox.showinfo("Attenzione!", "Non è stato inserito correttamente il testo della risposta 1! Reinserire grazie")
          return
        if not r2:
          # not defined 
          tkMessageBox.showinfo("Attenzione!", "Non è stato inserito correttamente il testo della risposta 2! Reinserire grazie")
          return
        if not rcorrect:
          # not defined 
          tkMessageBox.showinfo("Attenzione!", "Non è stato inserito correttamente il testo della risposta corretta! Reinserire grazie")
          return
        
        # da_appendere = domanda + ";" + r1 + ";" + r2 + ";" + rcorrect

        # Mixing answers 
        # Extracting casual number between 1 and 3 
        casual = randint(1,3)
        # Building the final string to be printed 
        if(casual == 1):
          da_appendere = domanda + ";" + rcorrect + ";" + r1 + ";" + r2 + ";1;1;0\n"
        elif(casual == 2):
          da_appendere = domanda + ";" + r1 + ";" + rcorrect + ";" + r2 + ";2;1;0\n"
        else:
          da_appendere = domanda + ";" + r2 + ";" + r1 + ";" + rcorrect + ";3;1;0\n"

        # Name of output file
        filename = "data.jj"
        
        # Try to open file 
        try:
          myfile = open(filename, "r")
          try:
            # Check if line exists
            for line in myfile:
              if( (r1 in line) and (r2 in line) and (rcorrect in line)):
                tkMessageBox.showinfo("Attenzione!", "La riga inserita esiste già nel database. Evita i duplicati!")
                return
          finally:
            myfile.close()
        except IOError as e:
          print "Il file " + filename + " non esiste!"
          # Create line 
          try:
            myfile = open(filename, "w")
            try:
              riga_iniziale = "Domanda;risposta 1;risposta 2;risposta 3;risposta esatta;punti risposta esatta;punti riposta sbagliata\n"
              myfile.write(riga_iniziale)
              print "Creato file: " + filename
              print "Scritta riga iniziale"
            finally:
              myfile.close()
          except IOError:
            print "Errore in scrittura"
            return

        with open(filename, "a") as myfile:
          myfile.write(da_appendere)
          tkMessageBox.showinfo("Salvato!", "Ho salvato la riga:\n" + da_appendere + "\nnel file chiamato: " + filename)


# main function with main loop
def main():
  
    root = Tk()
    root.geometry("600x300+300+300")
    app = QuestionMaker(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  
