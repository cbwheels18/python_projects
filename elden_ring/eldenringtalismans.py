import requests
import PIL.Image
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from io import BytesIO

def make_api_call():
    r = requests.get(url=URL) 
    data = r.json()

    for item in data['data']:
        Name = item['name']
        Image = item['image']
        Description = item['description']
        Effect = item['effect']
        Id = item['id']

        # Insert the information into the text widget
        result_text.insert(tk.END, f"Name: {Name}\nImage: {Image}\nDescription: {Description}\nEffect: {Effect}\nId: {Id}\n\n")

greeting = tk.Label(text="Ahoy Elden Lord Lets Ascend The Elden Throne!")
greeting.grid(row=0, column=0, columnspan=10)

# Create a text widget to display the results
result_text = tk.Text(height=20, width=50)
result_text.grid(row=3, column=8, rowspan=10, columnspan=10)

URL = "https://eldenring.fanapis.com/api/talismans"

