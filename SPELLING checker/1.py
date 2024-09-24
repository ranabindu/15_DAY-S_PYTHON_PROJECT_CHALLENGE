import tkinter as tk       #creating graphical user interfaces (GUIs). The module is imported with the alias tk
from tkinter import *       
from textblob import TextBlob   #used to check and correct spelling.

# Initialize the main window
root = Tk()                           # Creates the main window of the GUI application
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

# Function to check spelling
def check_spelling(): 
    word = enter_text.get()  #Retrieves the text entered by the user in the input field (enter_text) and stores it in the variable word
    a = TextBlob(word)       # Creates a TextBlob object with the text stored in word.The TextBlob class has methods for performing, including spelling check
    right = str(a.correct()) #Uses the correct() method of TextBlob to find the correct spelling of the text in word. The corrected text is then converted to a string and stored in the variable right

    # Display the corrected text
    cs = Label(root, text="Correct text is:", font=("Poppins", 20), bg="#dae6f6", fg="#364971")
    cs.place(x=100, y=250)
    
    spell = Label(root, text=right, font=("Poppins", 20), bg="#dae6f6", fg="#364971")
    spell.place(x=300, y=250)

# Heading label
heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

# Entry widget for user input
enter_text = Entry(root, justify="center", width=30, font=("Poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

# Button to trigger spell check
button = Button(root, text="Check", font=("Arial", 20, "bold"), bg="red", fg="white", command=check_spelling)
button.pack()

# Run the Tkinter event loop
root.mainloop()   #Starts the Tkinter event loop, which keeps the window open and responsive to user interactions
