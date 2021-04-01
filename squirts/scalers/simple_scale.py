"""Simple scale.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('Simple scale demo')


def final_setting():
    """Display scale value setting if OK button clicked."""
    scale_setting = scale_meter.get()
    print('Scale reads:', scale_setting)


scale_meter = tk.Scale(root,
                       fg='green',
                       from_=0, to=100,
                       orient=tk.HORIZONTAL)
scale_meter.grid(padx=65, pady=10)

ok_btn = tk.Button(root,
                   bg='indianred',
                   text='OK',
                   command=final_setting)
ok_btn.grid(pady=5, padx=5, sticky='WE')


root.mainloop()
