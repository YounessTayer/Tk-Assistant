"""Custom message box.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('Main window')
root.config(bg='slategray', padx=90)

custom_mbox = tk.Toplevel(root)
custom_mbox.resizable(False, False)
# custom_mbox.wm_overrideredirect(True)  # Use this line for no window bar.
custom_mbox.title('Custom messagebox')
custom_mbox.attributes('-topmost', 1)  # Bring custom window to front.


def btn_clk():
    """Button was clicked in custom messagebox."""
    print('Clicked Button')
    custom_mbox.destroy()


cust_mb_lbl = tk.Label(custom_mbox,
                       bg='khaki',
                       text='This is an example of a custom pop up box.\n'
                       'You can add almost any feature you can think of\n'
                       'inside this window.\n\nThe main benefit of using\n'
                       ' your own pop up is that it is non-code-blocking,\n'
                       ' unlike the built in pop up boxes which stop the\n '
                       ' code execution until a button is clicked.')
cust_mb_lbl.grid()

cmb_btn = tk.Button(custom_mbox,
                    bg="skyblue",
                    text='OK',
                    command=btn_clk)
cmb_btn.grid(sticky='WE')


root.mainloop()
