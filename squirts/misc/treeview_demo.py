"""Treeview Example
   Stand-alone example from Tk Assistant.
   Updated March 2021
   source:https://pythonguides.com/python-tkinter-treeview/
   Bijay Kumar. Edited by Steve Shambles.Ssee link its good.
   stevepython.wordpress.com
"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Treeview Demo')

tv = ttk.Treeview(root)
tv['columns'] = ('Rank', 'Name', 'Badge')
tv.column('#0', width=0, stretch=tk.NO)
tv.column('Rank', anchor=tk.CENTER, width=80)
tv.column('Name', anchor=tk.CENTER, width=80)
tv.column('Badge', anchor=tk.CENTER, width=80)

tv.heading('#0', text='', anchor=tk.CENTER)
tv.heading('Rank', text='Id', anchor=tk.CENTER)
tv.heading('Name', text='rank', anchor=tk.CENTER)
tv.heading('Badge', text='Badge', anchor=tk.CENTER)

tv.insert(parent='', index=0, iid=0, text='',
          values=('1', 'Vineet', 'Alpha'))
tv.insert(parent='', index=1, iid=1, text='',
          values=('2', 'Anil', 'Bravo'))
tv.insert(parent='', index=2, iid=2, text='',
          values=('3', 'Vinod', 'Charlie'))
tv.insert(parent='', index=3, iid=3, text='',
          values=('4', 'Vimal', 'Delta'))
tv.insert(parent='', index=4, iid=4, text='',
          values=('5', 'Manjeet', 'Echo'))
tv.pack()


root.mainloop()
