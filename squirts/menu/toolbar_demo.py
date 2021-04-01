"""Toolbar example
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com

This is an upgrade of snippet 111.
revision 3

pip3 install pillow
also requires ttips.py in current dir
and icons in a folder named icons.

free icons sourced from:
https://all-free-download.com/free-icon/download/
free_icons_for_developers_icons_pack_120612_download.html
"""
import tkinter as tk
import ttips
from PIL import Image, ImageTk


root = tk.Tk()
root.title('Tkinter Toolbar example')


def callback(icon_msg):
    """Print in textbox which icon has been clicked on"""
    txt_box.insert(tk.INSERT, icon_msg+'\n')


# Create the toolbar as a frame.
toolbar = tk.Frame(root,
                   borderwidth=2,
                   bg='gold',
                   relief='raised')

# Load all the images first as PNGs and use ImageTk to convert
# them to usable Tkinter images.
img1 = Image.open(r'icons/about.png')
about_img = ImageTk.PhotoImage(img1)
img2 = Image.open(r'icons/help.png')
help_img = ImageTk.PhotoImage(img2)
img3 = Image.open(r'icons/website.png')
web_img = ImageTk.PhotoImage(img3)
img4 = Image.open(r'icons/search.png')
search_img = ImageTk.PhotoImage(img4)
img5 = Image.open(r'icons/music.png')
music_img = ImageTk.PhotoImage(img5)
img6 = Image.open(r'icons/exit.png')
exit_img = ImageTk.PhotoImage(img6)

# Set up all the buttons for use on the toolbars.
about_btn = tk.Button(toolbar,
                      image=about_img,
                      command=lambda: callback("clicked about icon"))
about_btn.pack(side=tk.LEFT, fill=tk.X)
ttips.Create(about_btn, 'About')

help_btn = tk.Button(toolbar,
                     image=help_img,
                     command=lambda: callback("clicked help icon"))
help_btn.pack(side=tk.LEFT, fill=tk.X)
ttips.Create(help_btn, 'Help')

website_btn = tk.Button(toolbar,
                        image=web_img,
                        command=lambda: callback("clicked visit blog icon"))
website_btn.pack(side=tk.LEFT, fill=tk.X)
ttips.Create(website_btn, 'Visit blog')

search_btn = tk.Button(toolbar,
                       image=search_img,
                       command=lambda: callback("clicked search icon"))
search_btn.pack(side=tk.LEFT, fill=tk.X)
ttips.Create(search_btn, 'Search')

music_btn = tk.Button(toolbar,
                      image=music_img,
                      command=lambda: callback("clicked music icon"))
music_btn.pack(side=tk.LEFT, fill=tk.X)
ttips.Create(music_btn, 'Play Music')

exit_btn = tk.Button(toolbar,
                     image=exit_img,
                     command=root.destroy)
exit_btn.pack(side=tk.LEFT, fill=tk.X)
ttips.Create(exit_btn, 'Exit')

# Add the toolbar.
toolbar.pack(side=tk.TOP, fill=tk.X)

# Set up a Text box and scroll bar.
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

txt_box = tk.Text(root,
                  bg='khaki',
                  width=50,
                  height=10)
txt_box.pack()

txt_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt_box.yview)


root.mainloop()
