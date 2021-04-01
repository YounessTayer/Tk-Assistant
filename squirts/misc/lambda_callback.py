"""Lambda callback.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk

root = tk.Tk()
root.title('Lambda callback example')
root.config(padx=70, pady=20, bg='green')


def clkd_btn(btn_num):
    """A button was clicked, print which one."""
    print(btn_num)


main_frame = tk.Frame(root)
main_frame.grid(padx=30)

btn_one = tk.Button(main_frame,
                    bg='skyblue',
                    text='Click Me 1',
                    command=lambda: clkd_btn("clicked button 1"))
btn_one.grid()

btn_two = tk.Button(main_frame,
                    bg='orange',
                    text='Click Me 2',
                    command=lambda: clkd_btn("clicked button 2"))
btn_two.grid()


root.mainloop()
