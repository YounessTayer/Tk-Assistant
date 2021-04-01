"""Open file dialog.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()

file_slctd = filedialog.askopenfilename(title='Select a file')
print('The file you selected is:\n' + file_slctd)


root.mainloop()
