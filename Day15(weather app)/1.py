from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def getWeather():
    city = textfield.get()
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # Correct API URL
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=646824f2b7b86caffec1d0b16ea77f79"
    
    # Fetching the weather data
    response = requests.get(api)
    if response.status_code == 200:
        json_data = response.json()
        
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        
        # Updating the labels
        t.config(text=(temp, "°C"))
        c.config(text=(condition, "|", "FEELS LIKE", temp, "°C"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    else:
        messagebox.showerror("Error", f"City '{city}' not found or API error.")

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# search box
Search_image = PhotoImage(file=r"E:/sadow/python projects/WEATHER APP/Copy of search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file=r"E:/sadow/python projects/WEATHER APP/resize-17256910701822206931search1.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#484848", command=getWeather)
myimage_icon.place(x=400, y=34)

# logo
Logo_image = PhotoImage(file=r"E:/sadow/python projects/WEATHER APP/resize-1725001639365303352resize1725001389593753769resize1724999440546363950logoWEATHERappremovebgpreview-removebg-preview.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file=r"E:/sadow/python projects/WEATHER APP/Copy of box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100) 
clock = Label(root, font=("Helvetica", 20)) 
clock.place(x=30, y=130)

# labels
labell = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
labell.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Weather data labels
t = Label(root, text="...", font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(root, text="...", font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
