"""Open askdirectory dialog.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Hide horrid window.

# Open the file requestor.
folder_slctd = filedialog.askdirectory()
print('The folder you selected is:\n' + folder_slctd)


root.mainloop()
