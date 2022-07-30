from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests
from PIL import ImageTk


weather_display=""

#api
url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file="weather.key"
file_a=ConfigParser()
file_a.read(api_file)
api_key=file_a['api_key']['key']

def weather_find(city,temp):    #function to find data by json scripts
    final=requests.get(url.format(city,api_key))
    global weather_display
    if final:
        json_file=final.json()
        city=json_file['name']
        country_name=json_file['sys']['country']
        k_temp=json_file["main"]["temp"]
        c_temp=k_temp-273.15
        weather_display=json_file['weather'][0]['main']
        if weather_display=="Clear":
            bg= ImageTk.PhotoImage(file="Sunny.png")
            temp=Label(image=bg, compound='top').pack()
        result=(city,country_name,c_temp,weather_display)     #creating a list with necessary data
        return result  #returning the list to function
    else:
        return None

def printweather():
    city=search_city.get()
    weather=weather_find(city,temp_entry)
    if weather:
        location_entry['text']='{},{}'.format(weather[0],weather[1])
        temp_entry['text']='{:.2f} °C'.format(weather[2])
        weather_entry['text']=weather[3]
    else:
        messagebox.showerror('Error','No such city exists')

#window

root=Tk()
root.iconbitmap(r'icon.ico')
root.title("Weather App Trial")
root.config(background='black')
root.geometry("1920x1080")
'''variable background
music acc to weather'''

#city

search_city=StringVar()
enter_city=Entry(root,textvariable=search_city,fg="blue",font=("Times New Roman",50,"bold"),justify='center')
enter_city.pack()

#search

search_button=Button(root,text='Search Weather',width=12,fg="black",bg="red",font=("Ariel",40,"bold"),command=printweather)
search_button.pack()

#location

location_entry=Label(root,text='',font=("Ariel",45),bg="Black",fg="white")
location_entry.pack()

#temp

temp_entry=Label(root,text='',font=("Ariel",45),bg="Black",fg="white")
temp_entry.pack()

#weather

weather_entry=Label(root,text='',font=("Ariel",45),bg="Black",fg="white")
weather_entry.pack()

root.mainloop()