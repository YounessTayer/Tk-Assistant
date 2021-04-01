"""Image button with text
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('Image Btn with text example')
root.config(bg='slategray')

# Frame
btn_frame = tk.Frame(root)
btn_frame.grid(padx=110, pady=20)


# Callback.
def yt_btn():
    """Image Button was clicked."""
    print('Button clicked')


# Load img.
PHOTO = tk.PhotoImage(file=r'ytube.png')
# Note the "compound=tk.TOP" for img for text placement.
yt_img_btn = tk.Button(btn_frame,
                       text='YouTube',
                       compound=tk.TOP,
                       relief='solid',
                       command=yt_btn)

# Use width and height to adjust size button.
yt_img_btn.config(image=PHOTO, width='80', height='45')
yt_img_btn.grid()


root.mainloop()
