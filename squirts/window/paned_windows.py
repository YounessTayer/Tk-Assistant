"""Paned Windows.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   Unknown source, Edited by Shambles.
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('PanedWindow Example')

m1 = tk.PanedWindow(showhandle=True)
m1.pack(fill=tk.BOTH, expand=1)
left_pane = tk.Label(m1,
                     bg='skyblue',
                     text='Left PanedWindow',
                     relief='sunken',
                     bd=4)
m1.add(left_pane)


m2 = tk.PanedWindow(m1, orient=tk.VERTICAL, showhandle=True)
m1.add(m2)

top_pane = tk.Label(m2,
                    bg='red',
                    text='Top PanedWindow',
                    relief='sunken',
                    bd=4)
m2.add(top_pane)

btm_pane = tk.Label(m2,
                    bg='gold',
                    text='Bottom PanedWindow',
                    relief='sunken',
                    bd=4)
m2.add(btm_pane)


root.mainloop()
