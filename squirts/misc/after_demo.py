"""After demo
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles.
   stevepython.wordpress.com
"""
import tkinter as tk


root = tk.Tk()
root.title('After demo')
root.config(bg='steelblue')
btn = tk.Button(root,
                bg='gold',
                text='Click me',
                command=lambda: print('clicked'))
btn.grid(padx=70, pady=50)

print('Running for 8 seconds, try clicking the button.')

# After 8 seconds the root window will be destroyed,
# but during that time you can still click the button.
# If using sleep instead of after the button
# would freeze until the 8 seconds was up.

root.after(8000, root.destroy)


root.mainloop()

print('Demo over')
