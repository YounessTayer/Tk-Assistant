"""Date picker dialog.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com

requirements:
pip3 install tkcalendar
"""
import tkinter as tk
from tkcalendar import Calendar

root = tk.Tk()
root.withdraw()  # Hide naff extra window.
root.title('Please choose a date')


def pick_date_dialog():
    """Display date picker dialog, print date selected when OK clicked."""
    def print_sel():
        """Print date selected."""
        selected_date = (cal.get_date())
        print(selected_date)

    top_win = tk.Toplevel(root)
    cal = Calendar(top_win,
                   font='Arial 10',
                   background='darkblue',
                   foreground='white',
                   selectmode='day')

    cal.grid()

    ok_btn = tk.Button(top_win,
                       text='OK',
                       command=print_sel)
    ok_btn.grid()


pick_date_dialog()


root.mainloop()
