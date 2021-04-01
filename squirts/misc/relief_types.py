"""Relief types.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('Relief types')

flat_btn = tk.Button(root,
                     text="FLAT",
                     font='helvetica',
                     bg='orange',
                     width=25,
                     border=4,
                     relief=tk.FLAT)
flat_btn.grid(pady=10, padx=15, sticky=tk.W+tk.E)

groove_btn = tk.Button(root,
                       text="GROOVE",
                       bg='yellow',
                       font='helvetica',
                       border=4,
                       relief=tk.GROOVE)
groove_btn.grid(pady=10, padx=15, sticky=tk.W+tk.E)

raised_btn = tk.Button(root,
                       text="RAISED",
                       font='helvetica',
                       bg='powderblue',
                       border=4,
                       relief=tk.RAISED)
raised_btn.grid(pady=10, padx=15, sticky=tk.W+tk.E)

ridge_btn = tk.Button(root,
                      text="RIDGE",
                      bg='springgreen',
                      font='helvetica',
                      border=4,
                      relief=tk.RIDGE)
ridge_btn.grid(pady=10, padx=15, sticky=tk.W+tk.E)

sunken_btn = tk.Button(root,
                       text="SUNKEN",
                       font='helvetica',
                       bg='indianred',
                       border=4,
                       relief=tk.SUNKEN)
sunken_btn.grid(pady=10, padx=15, sticky=tk.W+tk.E)


root.mainloop()
