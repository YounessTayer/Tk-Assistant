"""askyn msg box.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import messagebox, Tk

root = Tk()
root.withdraw()  # Remove annoying window.

ask_yn = messagebox.askyesno('Question',
                             'This is a Ask Yes No message box.')

if ask_yn:
    print('You clicked on Yes')
else:
    print('You clicked No')


root.mainloop()
