"""Canvas Example
   Stand-alone example from Tk Assistant.
   Updated March 2021
   source: https://coderslegacy.com/python/list-of-tkinter-widgets/
   Edited by Shambles.
"""
import tkinter as tk

root = tk.Tk()
root.title('Canvas example')

frame = tk.Frame(root)
frame.grid()

canvas = tk.Canvas(frame, bg='slategray')
canvas.grid()

coordinates = 20, 50, 210, 230
arc = canvas.create_arc(coordinates, start=0, extent=250, fill="blue")
arc = canvas.create_arc(coordinates, start=250, extent=50, fill="red")
arc = canvas.create_arc(coordinates, start=300, extent=60, fill="yellow")


root.mainloop()
