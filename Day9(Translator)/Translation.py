from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from textblob import TextBlob

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

translator = Translator()

def label_change():
    c = combol.get()
    c1 = combo2.get()
    labell.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        c2 = combol.get()
        c3 = combo2.get()

        if text_:
            # Detect the language of the text
            detected_language = translator.detect(text_).lang

            # Find the corresponding language code
            target_language_code = None
            for lang_code, lang_name in LANGUAGES.items():
                if lang_name.lower() == c3.lower():
                    target_language_code = lang_code
                    break

            if target_language_code:
                # Translate the text
                translated_text = translator.translate(text_, src=detected_language, dest=target_language_code).text
                text2.delete(1.0, END)
                text2.insert(END, translated_text)
            else:
                messagebox.showerror("Translation Error", "Selected language not found!")
    except Exception as e:
        messagebox.showerror("Translation Error", f"Error: {str(e)}. Please try again.")

# Icon
image_icon = PhotoImage(file="E:/sadow/python projects/TRNSLATOR/6fdd4190-681d-4f36-a542-5a4a173161f6.png")
root.iconphoto(False, image_icon)

# Arrow
arrow_image = PhotoImage(file="E:/sadow/python projects/TRNSLATOR/resize-17254330211873476530stockvectorexchangeiconsymbolofexchangeandconvertconverticonvectorsymbolofbidirectionalarrows12267464171 (1).png")
image_label = Label(root, image=arrow_image, width=100)
image_label.place(x=485, y=200)

languageV = list(LANGUAGES.values())

combol = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combol.place(x=110, y=20)
combol.set("ENGLISH")

labell = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
labell.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic",
                   activebackground="purple", cursor="hand2", bd=5, bg='red',
                   fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.configure(bg="white")
root.mainloop()
