from tkinter import *

window = Tk()
window.title("Top Results!")
window.geometry('1000x1000')
window.configure(background="black")

Label (window, text="Google's Top Photo Results for {word}:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)

# "File" will be changed depending on how the microservice passes scraped data to the text file.
photo1 = PhotoImage(file="flower.png")
photo2 = PhotoImage(file="flower.png")
photo3 = PhotoImage(file="flower.png")
Label (window, image=photo1, bg="black") .grid(row=2, column=0, sticky=W)
Label (window, image=photo2, bg="black") .grid(row=2, column=1, sticky=W)
Label (window, image=photo3, bg="black") .grid(row=2, column=2, sticky=W)


Label (window, text="Bing's Top Photo Results for {word}:", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)

# "File" will be changed depending on how the microservice passes scraped data to the text file.
photo4 = PhotoImage(file="flower.png")
photo5 = PhotoImage(file="flower.png")
photo6 = PhotoImage(file="flower.png")
Label (window, image=photo4, bg="black") .grid(row=5, column=0, sticky=W)
Label (window, image=photo5, bg="black") .grid(row=5, column=1, sticky=W)
Label (window, image=photo6, bg="black") .grid(row=5, column=2, sticky=W)

Label (window, text="Yahoo's Top Photo Results for {word}:", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)

# "File" will be changed depending on how the microservice passes scraped data to the text file.
photo7 = PhotoImage(file="flower.png")
photo8 = PhotoImage(file="flower.png")
photo9 = PhotoImage(file="flower.png")
Label (window, image=photo7, bg="black") .grid(row=7, column=0, sticky=W)
Label (window, image=photo8, bg="black") .grid(row=7, column=1, sticky=W)
Label (window, image=photo9, bg="black") .grid(row=7, column=2, sticky=W)

def close_window():
    window.destroy()
    exit()

Button(window, text="Exit", width=14, command=close_window) .grid(row=0, column=5, sticky=E)

window.mainloop()

#window = Tk()
#window.title("Photo Results!")
#window.geometry('600x350')
#window.configure(background="black")

#photo1 = PhotoImage(file="flower.png")

#Label (window, text="Pick a keyword, any keyword: ", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)
#Label (window, image=photo1, bg="black") .grid(row=0, column=2, sticky=W)