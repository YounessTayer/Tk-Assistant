"""Tkinters internal bitmaps and cursors
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('Bitmaps and cursors')


def clkd_btn(txt):
    """A button was clicked. Report which in console."""
    print('Clicked on ' + txt)


main_frame = tk.LabelFrame(root,
                           fg='blue',
                           text='Tk internal bitmaps and cursors\n'
                           'Move mouse over a button')
main_frame.grid(padx=30, pady=10)


info_btn = tk.Button(main_frame,
                     bg='plum',
                     bitmap='info',
                     cursor='exchange',
                     command=lambda: clkd_btn('Info btn'))
info_btn.grid(pady=5, padx=5)

hrglss_btn = tk.Button(main_frame,
                       bg='gold',
                       bitmap='hourglass',
                       cursor='pirate',
                       command=lambda: clkd_btn('Hour-glass btn'))
hrglss_btn.grid(pady=5, padx=5, row=0, column=1)

qst_btn = tk.Button(main_frame,
                    bg='lightgreen',
                    bitmap='question',
                    cursor='crosshair',
                    command=lambda: clkd_btn('Question mark btn'))
qst_btn.grid(pady=5, padx=5, row=0, column=2)

err_btn = tk.Button(main_frame,
                    bg='skyblue',
                    bitmap='error',
                    cursor='heart',
                    command=lambda: clkd_btn('Error btn'))
err_btn.grid(pady=5, padx=5, row=0, column=3)

wrn_btn = tk.Button(main_frame,
                    bg='orange',
                    bitmap='warning',
                    cursor='hand1',
                    command=lambda: clkd_btn('Warning btn'))
wrn_btn.grid(pady=5, padx=5, row=0, column=4)

qhd_btn = tk.Button(main_frame,
                    bg='bisque',
                    bitmap='questhead',
                    cursor='watch',
                    command=lambda: clkd_btn('Question head btn'))
qhd_btn.grid(pady=5, padx=5, row=1, column=0)

gry75_btn = tk.Button(main_frame,
                      bitmap='gray75',
                      cursor='sailboat',
                      command=lambda: clkd_btn('Grey 75 btn'))
gry75_btn.grid(pady=5, padx=5, row=1, column=1)

gry50_btn = tk.Button(main_frame,
                      bitmap='gray50',
                      cursor='shuttle',
                      command=lambda: clkd_btn('Grey 50 btn'))
gry50_btn.grid(pady=5, padx=5, row=1, column=2)

gry25_btn = tk.Button(main_frame,
                      bitmap='gray25',
                      cursor='spraycan',
                      command=lambda: clkd_btn('Grey 25 btn'))
gry25_btn.grid(pady=5, padx=5, row=1, column=3)

gry12_btn = tk.Button(main_frame,
                      bitmap='gray12',
                      cursor='watch',
                      command=lambda: clkd_btn('Grey 12 btn'))
gry12_btn.grid(pady=5, padx=5, row=1, column=4)


root.mainloop()
