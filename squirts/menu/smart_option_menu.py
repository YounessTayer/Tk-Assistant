"""Smart Option Menu
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com

requirement:
pip3 install tk_tools
"""
from tkinter import Label, Tk
import tk_tools

root = Tk()
root.title('Smart option menu demo')
root.config(padx=70, pady=25)


def smrt_opt_mnu(value):
    """Print selection."""
    print('You selected option:', str(value))


msg_lbl = Label(root, text='\nSelect your\nstar sign')
msg_lbl.grid(row=0, column=0, sticky='ew')


drop_down = tk_tools.SmartOptionMenu(root,
                                     ['Aries',
                                      'Aquarius',
                                      'Cancer',
                                      'Capricorn',
                                      'Gemini',
                                      'leo',
                                      'Libra',
                                      'Pisces',
                                      'Sagittarius',
                                      'Scorpio',
                                      'Taurus',
                                      'Virgo'],
                                     callback=smrt_opt_mnu)
drop_down.grid(row=0, column=1, sticky='ew')


root.mainloop()
