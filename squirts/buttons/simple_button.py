"""Simple button.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk

# Set up the root window.
root = tk.Tk()
root.title('Simple button example')
root.config(bg='plum', padx=100, pady=20)


# Callback.
def clkd_btn():
    """Button was clicked."""
    print('Button was clicked')


# Create and display button.
btn_one = tk.Button(root,
                    bg='powderblue',
                    relief='solid',
                    text='Click Me',
                    command=clkd_btn)
btn_one.grid()


root.mainloop()
