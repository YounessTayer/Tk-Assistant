"""Scrollbar Example
   Stand-alone example from Tk Assistant.
   Updated March 2021
   source:https://coderslegacy.com/python/list-of-tkinter-widgets/
   Edited by Steve Shambles.
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('Scrollbar demo')
root.config(padx=20)

myscroll = tk.Scrollbar(root)
myscroll.pack(side=tk.RIGHT, fill=tk.Y)

mylist = tk.Listbox(root, yscrollcommand=myscroll.set)

for line in range(1, 100):
    mylist.insert(tk.END, "Number " + str(line))

mylist.pack(side=tk.LEFT, fill=tk.BOTH)

myscroll.config(command=mylist.yview)


root.mainloop()
