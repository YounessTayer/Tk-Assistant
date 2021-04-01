""" Date and ticking clock.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com

Note:
You may need to install the 'Digital-7 Mono' font I have use here,
I have supplied this font in the same dir as this code.
or get it, or a different digital clock font, from here:
https://www.1001fonts.com/digital+clock-fonts.html
"""
from threading import Timer
import time
import tkinter as tk
import tkinter.font as TkFont

root = tk.Tk()
root.title('Date and Time Example')
root.config(padx=30, pady=30)

# To see your installed fonts, unrem next line.
# print(TkFont.families())

my_font = TkFont.Font(family='Digital-7 Mono',
                      size=40,
                      weight='bold',
                      # slant='italic',
                      # underline=1,
                      # overstrike=1,
                      )


# Create label for clock.
date_clock = tk.Label(root,
                      fg='blue',
                      font=my_font)
date_clock.grid(row=2, column=1, padx=20)


def start_clock():
    """Threading timer prints date and time every second.
       Note; If you dont want seconds on show remove the ':%S'"""
    curr_time = (time.strftime('%a, %d %b %Y \n %H:%M:%S'))
    date_clock.config(text=curr_time, font=my_font)
    tmr = Timer(1.0, start_clock)
    tmr.start()


# Starts the timer.
start_clock()


root.mainloop()
