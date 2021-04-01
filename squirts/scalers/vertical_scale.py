"""Vertical scale.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('Vertical scale demo')


def set_height(can_vas, height_str):
    """Set scale height."""
    height = 21
    height = height + 21
    height_y2 = height - 30
    print(height_str)  # Holds current scale pointer.
    if height_y2 < 21:
        height_y2 = 21


can_vas = tk.Canvas(root,
                    width=65,
                    height=50,
                    bd=0,
                    highlightthickness=0)

scale = tk.Scale(root,
                 orient=tk.VERTICAL,
                 length=284,
                 from_=0,
                 to=250,
                 tickinterval=25,
                 command=lambda h, c=can_vas: set_height(c, h))
scale.grid(padx=80, sticky='NE')

# Starting point on scale.
scale.set(125)


root.mainloop()
