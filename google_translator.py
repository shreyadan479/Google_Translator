from tkinter import *
from tkinter import ttk  # adds combo box
from googletrans import LANGUAGES
from deep_translator import GoogleTranslator


def change(text="type", src="english", dest="hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = GoogleTranslator(source=src1, target=dest1)
    trans1 = trans.translate(text)
    return trans1


def data():
    print("Data is being processed")
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    print("Source Language: ", s)
    print("Destination Language: ", d)
    print("Source Text: ", msg)
    textget = change(text=msg, src=s, dest=d)
    print("Destination Text: ", textget)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


root = Tk()

root.title("Translator")
root.geometry("500x700")
root.config(bg="red")

lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"))
# It places the Label according to the specified x-axis , y-axis,height and width
lab_txt.place(x=100, y=40, height=50, width=300)


frame = Frame(root).pack(side=BOTTOM)


lab_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"))
lab_txt.place(x=100, y=100, height=20, width=300)


Sor_txt = Text(frame, font=("Times New Roman", 40, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)


list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=10, y=300, height=40, width=100)
comb_sor.set("english")

# RAISED gives the 3D-ness in button
button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=100)


comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=330, y=300, height=40, width=100)
comb_dest.set("english")


lab_txt = Label(root, text="Dest Text", font=("Times New Roman", 20, "bold"))
lab_txt.place(x=100, y=360, height=20, width=300)


dest_txt = Text(frame, font=("Times New Roman", 40, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
