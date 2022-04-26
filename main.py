import tkinter as tk
from tkinter import *

#import click as click

def click():
    entered_text=textentry.get()
    googleFlag=var1.get()
    bingFlag=var2.get()
    yahooFlag=var3.get()
    try:
        write_File(entered_text, googleFlag, bingFlag, yahooFlag)
    except:
        print('write_File failure')



def write_File(entered_text, googleFlag, bingFlag, yahooFlag):
    with open('data.txt', 'a') as file:
        file.seek(0)
        file.truncate()
        file.write('{0}\n{1}\n{2}\n{3}'.format(entered_text, googleFlag, bingFlag, yahooFlag))


window = Tk()
window.title("Top Photo Finder!")
window.geometry('650x375')
window.configure(background="black")

photo1 = PhotoImage(file="flower.png")

Label (window, image=photo1, bg="black") .grid(row=0, column=2, sticky=W)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Google', bg="black", fg="white", font="none 12 bold", variable=var1, onvalue=1, offvalue=0, selectcolor="black") .grid(row=1, column=0, sticky=W)
#c1.pack()
c2 = tk.Checkbutton(window, text='Bing', bg="black", fg="white", font="none 12 bold", variable=var2, onvalue=1, offvalue=0, selectcolor="black") .grid(row=1, column=2, sticky=W)
#c2.pack()
c3 = tk.Checkbutton(window, text='Yahoo', bg="black", fg="white", font="none 12 bold", variable=var3, onvalue=1, offvalue=0, selectcolor="black") .grid(row=1, column=3, sticky=W)

Label (window, text="Pick a keyword, any keyword: ", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)

textentry = Entry(window, width=20, bg="white")
textentry.grid(row=5, column=0, sticky=W)

Button(window, text="SUBMIT", width=6, command=click) .grid(row=6, column=0, sticky=W)

def close_window():
    window.destroy()
    exit()

Button(window, text="Exit", width=14, command=close_window) .grid(row=7, column=10, sticky=E)

window.mainloop()


