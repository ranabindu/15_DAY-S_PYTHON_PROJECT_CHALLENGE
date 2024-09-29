from datetime import datetime
import pytz
import tkinter as tk

root = tk.Tk()  # Initialization of Tk window
root.geometry("500x300")  # Adjusted window size for better layout
root.title("World Clock")
root.configure(bg="#2c3e50")  # Set background color

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

# Define a function to create a clock frame
def create_clock_frame(parent, x, y):
    frame = tk.Frame(parent, bg="#34495e", bd=2, relief="solid")
    frame.place(x=x, y=y, width=220, height=120)

    name = tk.Label(frame, font=("Helvetica", 15, "bold"), bg="#34495e", fg="#ecf0f1")
    name.pack(pady=5)

    clock = tk.Label(frame, font=("Helvetica", 20, "bold"), bg="#34495e", fg="#ecf0f1")
    clock.pack()

    nota = tk.Label(frame, text="Hours minutes seconds", font=("Helvetica", 10, "bold"), bg="#34495e", fg="#bdc3c7")
    nota.pack(pady=5)

    return name, clock

# Create clock frames for each timezone
name, clock = create_clock_frame(root, 30, 30)
name1, clock1 = create_clock_frame(root, 250, 30)
name2, clock2 = create_clock_frame(root, 30, 150)
name3, clock3 = create_clock_frame(root, 250, 150)

# Start updating the clocks
times()

root.mainloop()