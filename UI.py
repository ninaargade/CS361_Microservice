from tkinter import *

root = Tk()

def click():

        randNum = e.get()
        numFile = open('randNum.txt', 'w')
        numFile.write(randNum)
        numFile.close()

e = Entry(root, bg='grey')
e.pack()

myButton = Button(root, text='Enter', padx=0, pady=0, command=click, bg='blue')
myButton.pack()

root.mainloop()
