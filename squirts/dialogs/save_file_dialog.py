"""Save file dialog.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()

save_file = filedialog.asksaveasfilename(title='Save file')
print('The file name you saved is:\n', save_file)
# Note this demo does not actually save a file,
# it is just for user to select path and name via dialog.

root.mainloop()
