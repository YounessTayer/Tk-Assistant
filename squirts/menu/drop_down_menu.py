"""Drop-down menu.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import Menu, messagebox, Tk
import webbrowser as web

root = Tk()
root.title('Menu demo')


def about_menu():
    """About program pop up box."""
    messagebox.showinfo('About',
                        'Menu created by Tk Assistant.')


def visit_blog():
    """Visit my Python blog website."""
    web.open('https://stevepython.wordpress.com/')


menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label='Menu', menu=file_menu)
file_menu.add_command(label='Visit Blog', command=visit_blog)
file_menu.add_separator()
file_menu.add_command(label='About', command=about_menu)
file_menu.add_command(label='Exit', command=root.destroy)

root.config(menu=menu_bar)


root.mainloop()
