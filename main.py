#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RAISED, RIGHT
from ttk import Frame, Label, Entry, Button


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
        
        lbl1 = Label(frame1, text="Title", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)           
       
        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)
        
        ### Frame 2
        frame2 = Frame(self)
        frame2.pack(fill=X)
        
        lbl2 = Label(frame2, text="Author", width=6)
        lbl2.pack(side=LEFT, padx=5, pady=5)        

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)
        
        ### Frame 4
        frame4 = Frame(self)
        frame4.pack(fill=BOTH, expand=True)
        
        # Close button -> close on click
        closeButton = Button(self, text="Close", command=self.master.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)

        # Save button -> save a new line in the file and continues the exec
        okButton = Button(self, text="Salva", command=lambda: valueGET(entry1.get(), entry2.get()))
        okButton.pack(side=RIGHT)

    # Function for the ok button
    def salva(self):
        print("Sto salvando...")

def valueGET(val1, val2):
    print val1 + "  " + val2

def main():
  
    root = Tk()
    root.geometry("800x600+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  