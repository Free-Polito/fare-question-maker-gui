#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
from ttk import Frame, Label, Entry, Button
import tkMessageBox


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()

    def initUI(self):
      
        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)
        
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
        
        risposta3 = Label(frame4, text="Risposta 3 - ERRATA", width=20)
        risposta3.pack(side=LEFT, padx=5, pady=5)        

        entry4 = Entry(frame4)
        entry4.pack(fill=X, padx=5, expand=True)

        ### Frame 5
        frame5 = Frame(self)
        frame5.pack(fill=X)
        
        risposta_giusta = Label(frame5, text="Risposta CORRETTA", width=20)
        risposta_giusta.pack(side=LEFT, padx=5, pady=5)        

        entry5 = Entry(frame5)
        entry5.pack(fill=X, padx=5, expand=True)

        ### Frame 6
        frame6 = Frame(self)
        frame6.pack(fill=BOTH, expand=True)
        
        # Close button -> close on click
        closeButton = Button(self, text="Close", command=self.master.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)

        # Save button -> save a new line in the file and continues the exec
        okButton = Button(self, text="Salva", command=lambda: self.valueGET(entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get()))
        okButton.pack(side=RIGHT)

    def valueGET(self, domanda, r1, r2, r3, rcorrect):
        # check
        if not domanda:
          # non definita
          tkMessageBox.showinfo("Attenzione!", "Non è stato inserito correttamente il testo della domanda! Reinserire grazie")
          return
        if not r1:
          # non definita
          tkMessageBox.showinfo("Attenzione!", "Non è stato inserito correttamente il testo della risposta 1! Reinserire grazie")
          return
        if not r2:
          # non definita
          tkMessageBox.showinfo("Attenzione!", "Non è stato inserito correttamente il testo della risposta 2! Reinserire grazie")
          return
        if not r3:
          # non definita
          tkMessageBox.showinfo("Attenzione!", "Non è stato inserito correttamente il testo della risposta 3! Reinserire grazie")
          return
        if not rcorrect:
          # non definita
          tkMessageBox.showinfo("Attenzione!", "Non è stato inserito correttamente il testo della risposta corretta! Reinserire grazie")
          return
        
        da_appendere = domanda + ";" + r1 + ";" + r2 + ";" + r3 + ";" + rcorrect
        da_appendere_completo = da_appendere + "2;1;0\n"
        with open("data.jj", "a") as myfile:
          myfile.write(da_appendere)
        tkMessageBox.showinfo("Stampato", da_appendere_completo)


def main():
  
    root = Tk()
    root.geometry("600x300+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  