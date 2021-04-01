"""Radio buttons example.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Radio Buttons example')
root.config(padx=55)


# Callback.
def radio_sel():
    """Display radio button selected by user."""
    radio = VRB.get()
    messagebox.showinfo('You picked:',
                        'Radio button ' + str(radio))


# Create a frame for the radio buttons.
radio_frame = tk.LabelFrame(root,
                            fg='green',
                            text='Select a Radio button')
radio_frame.grid(padx=10, pady=13)

VRB = tk.IntVar()

# Radio btn one.
rd_btn_one = tk.Radiobutton(radio_frame,
                            text='One',
                            variable=VRB,
                            command=radio_sel,
                            value=1)
rd_btn_one.grid(sticky=tk.W)

# Radio btn two.
rd_btn_two = tk.Radiobutton(radio_frame,
                            text='Two',
                            variable=VRB,
                            command=radio_sel,
                            value=2)
rd_btn_two.grid(sticky=tk.W)

# Radio btn three.
rd_btn_three = tk.Radiobutton(radio_frame,
                              text='Three',
                              variable=VRB,
                              command=radio_sel,
                              value=3)
rd_btn_three.grid(sticky=tk.W)


root.mainloop()
