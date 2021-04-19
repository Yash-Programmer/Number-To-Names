from tkinter import *
from tkinter import ttk
from num2words import num2words
import clipboard as cb

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
languages = [
    'en (English)',
    'ar (Arabic)',
    'cz (Czech)',
    'de (German)',
    'dk (Danish)',
    'es (Spanish)',
    'eu (EURO)',
    'fi (Finnish)',
    'fr (French)',
    'fr_CH (French - Switzerland)',
    'fr_BE (French - Belgium)',
    'fr_DZ (French - Algeria)',
    'he (Hebrew)',
    'id (Indonesian)',
    'it (Italian)',
    'ja (Japanese)',
    'kn (Kannada)',
    'ko (Korean)',
    'lt (Lithuanian)',
    'lv (Latvian)',
    'no (Norwegian)',
    'pl (Polish)',
    'pt (Portuguese)',
    'pt_BR (Portuguese - Brazilian)',
    'sl (Slovene)',
    'sr (Serbian)',
    'ro (Romanian)',
    'ru (Russian)',
    'sl (Slovene)',
    'tr (Turkish)',
    'th (Thai)',
    'vi (Vietnamese)',
    'nl (Dutch)',
    'uk (Ukrainian)',
]

root = Tk()
root.geometry('500x495')
root.title('Number Names GUI__By Yash Varshney')
root.resizable(height=False, width=False)


Frame1 = LabelFrame(root, text='Number_Details', padx=10, pady=5)
Frame1.pack()

Frame2 = LabelFrame(root, text='Output', padx=10, pady=10)
Frame2.pack()


def ans():
    t.delete(1.0, END)
    ll.config(text='')
    try:
        num = int(e.get())
        try:
            Lang_Choice = languages_dropDown.get().split()
            Ans = num2words(num, lang=Lang_Choice[0])
            t.insert(1.0, Ans + '\n\n============(Copied to Clipboard Also)=============')
            cb.copy(Ans)
        except IndexError:
            ll.config(text='Please Select Language', fg='red')

    except ValueError:
        ll.config(text='This is not a Number', fg='red')


ll1 = Label(Frame1, text='Enter Number', font='Arial 20', fg='dark blue')
ll1.pack()
e = Entry(Frame1, width=50, borderwidth=2, font='Calabri 12')
e.pack()
ll2 = Label(Frame1, text='Select Language', font='Arial 20', fg='dark blue')
ll2.pack()
languages_dropDown = ttk.Combobox(Frame1, values=languages)
languages_dropDown.pack()
ll3 = Label(Frame1, text='')
ll3.pack()
b = Button(Frame1, text='Submit',bg='light blue', pady=10, padx=10, command=ans)
b.pack()
ll = Label(Frame2, text='Output', font='Arial 20', fg='dark blue')
ll.pack()
t = Text(Frame2, height=10, width=50, font='Calabri 13', borderwidth=2)
t.pack()

root.mainloop()