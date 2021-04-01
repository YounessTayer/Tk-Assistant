"""Tabbed GUI.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles.
   stevepython.wordpress.com
"""
import time
import tkinter as tk
from tkinter import ttk

import pyperclip


root = tk.Tk()
root.title('Tabbed GUI example')

tab_ctrl = ttk.Notebook(root)
tab_one = ttk.Frame(tab_ctrl)
tab_ctrl.add(tab_one, text='Tab 1')

tab_two = ttk.Frame(tab_ctrl)
tab_ctrl.add(tab_two, text='Tab 2')
tab_ctrl.pack(expand=1, fill='both')

tab_lab1 = ttk.Label(tab_one, text='This is Tab 1')
tab_lab1.grid()

tab_lab2 = ttk.Label(tab_two, text='This is Tab 2')
tab_lab2.grid()

txt = tk.Text(tab_one)
txt.grid()

txt2 = tk.Text(tab_two)
txt2.grid()
txt2.insert(tk.INSERT,'Try typing some text here.')

txt.config(bg='steelblue', fg='white')
tab_lab1.config(background='gold')
tab_lab2.config(background='skyblue')


def view_cb():
    """Get current clipboard contents and display."""
    cb_get = pyperclip.paste()

    tit_bar = '-' * 5
    txt.config(wrap=tk.WORD)
    curr_time = time.asctime()

    # Insert clipboard text into text box with time and date stamp.
    txt.insert(tk.INSERT,
               '\n' + tit_bar + 'Clipboard contents at: '
               + curr_time + ' ' + tit_bar + '\n\n')

    if not cb_get:
        cb_get = 'No text currently found on clipboard'

    txt.insert(tk.INSERT, cb_get + '\n')


view_cb()


root.mainloop()
