"""Display image.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com

   Requires:
   pip3 install pillow
   ducks.jpg in current dir (supplied)
   Note:
   ducks.jpg is (c) Steve Shambles on behalf
   of my sister Karen who took it and owns it.
"""
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Display image example')

# Create frame for the image.
img_frame = tk.LabelFrame(root, relief=tk.RIDGE)
img_frame.grid(padx=18, pady=18)

# Insert image, note:image file needs to be in same dir as this script
# runs from or you will need to give a file location of the image.
# Rename ducks.jpg to your image below.
img = Image.open('ducks.jpg')
PHOTO = ImageTk.PhotoImage(img)

img_lab = tk.Label(img_frame, image=PHOTO)
img_lab.img = PHOTO
img_lab.grid()


root.mainloop()
