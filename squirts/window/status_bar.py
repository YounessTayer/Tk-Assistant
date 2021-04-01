"""Status bar.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
   """
import tkinter as tk

root = tk.Tk()
root.title('Status bar example')
root.geometry('300x150')
root.config(bg='slategray')


def sb_upd(event):
    """Call here when mouse click detected in main window."""
    st_bar.config(text='Status: You clicked da mouse')
    root.update()
    root.after(3000)
    st_bar.config(text='Status: Ready')


st_bar = tk.Label(root,
                  text='Try clicking in the window and watch here.',
                  bd=1,
                  relief=tk.SUNKEN,
                  anchor=tk.W)
st_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.bind('<Button-1>', sb_upd)


root.mainloop()
