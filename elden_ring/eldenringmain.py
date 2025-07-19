import requests
import PIL.Image
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from io import BytesIO
import eldenringtalismans

greeting = tk.Label(text="Ahoy Elden Lord Lets Ascend The Elden Throne!")
greeting.grid(row=3, column=0, columnspan=10)
choose = tk.Label(text="Choose A Category")
choose.grid(row=0, column=0, columnspan=10)

categories = ["ammos", "armors", "ashes"]

# Create a grid of buttons
ammos_button = tk.Button(text="ammos", width=10, height=5, command=eldenringtalismans)
ammos_button.grid(row=(1), column=(1))
button = tk.Button(text="armors", width=10, height=5)
button.grid(row=(1), column=(2))
button = tk.Button(text="ashes", width=10, height=5)
button.grid(row=(1), column=(3))
button = tk.Button(text="bosses", width=10, height=5)
button.grid(row=(1), column=(4))
button = tk.Button(text="classes", width=10, height=5)
button.grid(row=(1), column=(5))
button = tk.Button(text="incantations", width=10, height=5)
button.grid(row=(1), column=(6))
button = tk.Button(text="items", width=10, height=5)
button.grid(row=(1), column=(7))
button = tk.Button(text="locations", width=10, height=5)
button.grid(row=(2), column=(1))
button = tk.Button(text="npcs", width=10, height=5)
button.grid(row=(2), column=(2))
button = tk.Button(text="shields", width=10, height=5)
button.grid(row=(2), column=(3))
button = tk.Button(text="sorceries", width=10, height=5)
button.grid(row=(2), column=(4))
button = tk.Button(text="spirits", width=10, height=5)
button.grid(row=(2), column=(5))
button = tk.Button(text="talismans", width=10, height=5, command=eldenringtalismans.make_api_call)
button.grid(row=(2), column=(6))
button = tk.Button(text="weapons", width=10, height=5)
button.grid(row=(2), column=(7))

tk.mainloop()

