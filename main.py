#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we use the pack manager
to create a more complex layout.

Author: Jan Bodnar
Last modified: December 2015
Website: www.zetcode.com
"""

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
        
        ### Frame 3
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)
        
        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)        

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)           
        
        ### Frame 4

        frame4 = Frame(self)
        frame4.pack(fill=BOTH, expand=True)
        
        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)


def main():
  
    root = Tk()
    root.geometry("300x300+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  