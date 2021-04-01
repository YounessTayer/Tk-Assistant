"""Progress bar.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   This replaces the truly awful old version of progress bar.
   Based on code from:
   https://python-commandments.org/tkinter-progressbar/
   stevepython.wordpress.com
"""
import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title('Progress Bar demo')
root.config(bg='steelblue')


def increment():
    """Inc progress bar indicator."""
    for i in range(100):
        p1["value"] = i+1
        root.update()
        time.sleep(0.1)


p1 = ttk.Progressbar(root,
                     length=200,
                     cursor='spider',
                     mode="determinate",
                     orient=tk.HORIZONTAL)
p1.grid(row=1, column=1, padx=5, pady=10)

btn = tk.Button(root,
                bg='gold',
                text="Start",
                command=increment)
btn.grid(row=1, column=0, padx=5, pady=10)


root.mainloop()
