"""Menu button example
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('Menu button example')
root.config(bg='indianred', padx=40, pady=40)


# Callback.
def menu_sel():
    """Check and report on menu selection."""
    if VAR1.get():
        print('V2 ticked')
    if VAR2.get():
        print('V3 ticked')


# Menubutton widget.
menu_btn = tk.Menubutton(root,
                         font='50',
                         text='Choose your Python Version',
                         bg='skyblue',
                         relief=tk.SUNKEN)
menu_btn.grid(padx=20, pady=20)

menu_btn.menu = tk.Menu(menu_btn, tearoff=0)
menu_btn['menu'] = menu_btn.menu

VAR1 = tk.IntVar()
VAR2 = tk.IntVar()

menu_btn.menu.add_checkbutton(label='Python V2',
                              variable=VAR1,
                              command=menu_sel)

menu_btn.menu.add_checkbutton(label='Python V3',
                              variable=VAR2,
                              command=menu_sel)
menu_btn.grid()


root.mainloop()
