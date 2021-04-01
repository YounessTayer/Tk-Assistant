"""Image button example
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('Image Button example')
root.config(bg='steelblue')

btn_frame = tk.Frame(root)
btn_frame.grid(padx=90, pady=20)


# Callback.
def clkd_btn():
    """Image Button was clicked."""
    print('Button clicked')


# Button.
# The image is required in current dir.
img_btn = tk.Button(btn_frame,
                    text='BBC News',
                    relief='solid',
                    command=clkd_btn)

PHOTO = tk.PhotoImage(file='bbc-55x18.png')
# Use width and height to adjust size button.
img_btn.config(image=PHOTO, width='85', height='30')
img_btn.grid()


root.mainloop()
