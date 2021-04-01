"""Colour Sliders code.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com

Originally from the book Adventures In Python.
Edited and updated by Steve Shambles
"""
import tkinter as tk
root = tk.Tk()
root.title('Colour sliders')


def slider_update(source):
    """Update sliders values."""
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()

    colour = '#%02x%02x%02x' % (red, green, blue)
    can_vas.config(bg=colour)
    hex_text.delete(0, tk.END)
    hex_text.insert(0, colour)


can_vas = tk.Canvas(root,
                    width=200,
                    height=200)
can_vas.grid(row=2, column=1, columnspan=3)

red_slider = tk.Scale(root,
                      from_=0,
                      to=255,
                      command=slider_update)
red_slider.grid(row=1, column=1)

green_slider = tk.Scale(root,
                        from_=0,
                        to=255,
                        command=slider_update)
green_slider.grid(row=1, column=2)

blue_slider = tk.Scale(root,
                       from_=0,
                       to=255,
                       command=slider_update)
blue_slider.grid(row=1, column=3)

hex_text = tk.Entry(root)
hex_text.grid(row=3, column=1, columnspan=3)

can_vas.config(bg='steelblue')


root.mainloop()
