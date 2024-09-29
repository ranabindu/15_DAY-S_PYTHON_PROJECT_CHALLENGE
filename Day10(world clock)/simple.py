from datetime import datetime
import pytz
import tkinter

root = tkinter.Tk()  # Initialization of Tk window
root.geometry("400x300")  # Adjusted window size for better layout


def times():
    # India Time
    home = pytz.timezone('Asia/Kolkata')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    name.config(text="India")

    # Australia Time
    home = pytz.timezone('Australia/Victoria')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock1.config(text=current_time)
    name1.config(text="Australia")

    # Africa Time
    home = pytz.timezone('Africa/Timbuktu')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock2.config(text=current_time)
    name2.config(text="Africa")

    # America Time
    home = pytz.timezone('America/New_York')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock3.config(text=current_time)
    name3.config(text="America")

    root.after(1000, times)  # Update every second

# Define the first set of labels for India (Top Left)
name = tkinter.Label(root, font=("times", 15, "bold"))
name.place(x=30, y=5)

clock = tkinter.Label(root, text="Clock 1", font=("times", 20, "bold"))
clock.place(x=30, y=40)

nota = tkinter.Label(root, text="Hours minutes seconds", font=("times", 10, "bold"))
nota.place(x=30, y=80)

# Define the second set of labels for Australia (Top Right)
name1 = tkinter.Label(root, font=("times", 15, "bold"))
name1.place(x=230, y=5)

clock1 = tkinter.Label(root, font=("times", 20, "bold"))
clock1.place(x=230, y=40)

nota1 = tkinter.Label(root, text="Hours minutes seconds", font=("times", 10, "bold"))
nota1.place(x=230, y=80)

# Define the third set of labels for Africa (Bottom Left)
name2 = tkinter.Label(root, font=("times", 15, "bold"))
name2.place(x=30, y=130)

clock2 = tkinter.Label(root, font=("times", 20, "bold"))
clock2.place(x=30, y=160)

nota2 = tkinter.Label(root, text="Hours minutes seconds", font=("times", 10, "bold"))
nota2.place(x=30, y=200)

# Define the fourth set of labels for America (Bottom Right)
name3 = tkinter.Label(root, font=("times", 15, "bold"))
name3.place(x=230, y=130)

clock3 = tkinter.Label(root, font=("times", 20, "bold"))
clock3.place(x=230, y=160)

nota3 = tkinter.Label(root, text="Hours minutes seconds", font=("times", 10, "bold"))
nota3.place(x=230, y=200)

# Start updating the clocks
times()

root.mainloop()
