from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob


root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

#icon
image_icon = PhotoImage(file="googletrans.png")
root.iconphoto(False, image_icon)

language = googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()


combo1=ttk.Combobox(root,values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("English")

root.configure(bg="white")
root.mainloop()

