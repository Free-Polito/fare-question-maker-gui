#!/usr/bin/python
# -*- coding: utf-8 -*-
#  FARE Question Maker GUI - Write and save JJ game DB
#  Copyright (C) 2018 libremente <surf@libremente.eu>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.

# Imports
from Tkinter import Tk, BOTH, X, LEFT, RIGHT
from ttk import Frame, Label, Entry, Button
from random import randint
import tkMessageBox


class Question(object):
    """ Class for storing the question/answers """
    def __init__(self, question, ans_1, ans_2, ans_correct):        
        self.empty = False
         # Check values
        if not question:
            # not defined 
            tkMessageBox.showinfo("Attenzione!", "Non è stato inserito " \
                    "correttamente il testo della domanda! Reinserire grazie")
            self.empty = True 
            return
        if not ans_1:
          # not defined 
            tkMessageBox.showinfo("Attenzione!", "Non è stato inserita " \
                    "correttamente la risposta 1! Reinserire grazie")
            self.empty = True 
            return
        if not ans_2:
          # not defined 
            tkMessageBox.showinfo("Attenzione!", "Non è stato inserita " \
                    "correttamente la risposta 2! Reinserire grazie")
            self.empty = True 
            return
        if not ans_correct:
          # not defined 
            tkMessageBox.showinfo("Attenzione!", "Non è stato inserito " \
                    "correttamente la risposta corretta! Reinserire grazie")
            self.empty = True 
            return

        self.question = question
        self.ans_1 = ans_1
        self.ans_2 = ans_2
        self.ans_correct = ans_correct


# QuestionMaker main class
class QuestionMaker(Frame):
    """ Main class for the GUI creation """
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.init_ui(self)

    @classmethod
    def init_ui(cls, self):
        """ Init the UI, creating all the frames """
      
        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)
       
        ## Frame 0 - Description Only 
        frame0 = Frame(self)
        frame0.pack(fill=X)
        
        descrizione = Label(frame0, text="Compilare tutti i campi e poi " \
        "salvare per inserire una nuova riga nel file", width=100)
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
                        command=lambda: self.value_get(self, \
                                Question(entry1.get(), entry2.get(), \
                                entry3.get(), entry4.get())))
        ok_button.pack(side=RIGHT)

    @classmethod
    def value_get(cls, self, question):
        """ Get the value from the frames """

        if(question.empty):
            return
       
        # Mixing answers 
        # Extracting casual number between 1 and 3 
        casual = randint(1, 3)
        # Building the final string to be printed 
        if(casual == 1):
            da_appendere = question.question + ";" \
                    + question.ans_correct + ";" \
                    + question.ans_1 + ";" + question.ans_2 + ";1;1;0\n"
        elif(casual == 2):
            da_appendere = question.question + ";" \
                    + question.ans_1 + ";" \
                    + question.ans_correct + ";" \
                    + question.ans_2 + ";2;1;0\n"
        else:
            da_appendere = question.question + ";" \
                    + question.ans_2 + ";" \
                    + question.ans_1 + ";" + question.ans_correct + ";3;1;0\n"

        # Name of output file
        filename = "data.jj"
       
        self.open_file(filename, question, da_appendere)

    @classmethod
    def open_file(cls, filename, question, da_appendere):
        """ Check, open file and write inside """
        # Try to open file 
        try:
            myfile = open(filename, "r")
            try:
                # Check if line exists
                for line in myfile:
                    if( (question.ans_1 in line) 
                        and (question.ans_2 in line) 
                        and (question.ans_correct in line)):
                        tkMessageBox.showinfo("Attenzione!", 
                        "La riga inserita esiste già nel database." \
                                "Evita i duplicati!")
                        return
            finally:
                myfile.close()
        except IOError :
            print "Il file " + filename + " non esiste!"
            # Create line 
            try:
                myfile = open(filename, "w")
                try:
                    riga_iniziale = "Domanda;risposta 1;risposta 2;risposta 3;"\
                    "risposta esatta;punti risposta esatta;" \
                    "punti riposta sbagliata\n"
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
            tkMessageBox.showinfo("Salvato!", "Ho salvato la riga:\n" \
                    + da_appendere + "\nnel file chiamato: " + filename)


# main function with main loop
def main():
    """ Main function """
  
    root = Tk()
    root.geometry("600x300+300+300")
    QuestionMaker(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  
