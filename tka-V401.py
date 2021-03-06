"""
TK Assistant V4.1 April 2nd 2021

Freeware, but (c) By Steve Shambles.
https://stevepython.wordpress.com/

Written in Python V3.76 64bit AMD Windows version.

pip3 install pyperclip
pip3 install tkcalendar
pip3 install Pillow
pip3 install tk_tools
pip3 install wget

Needed to run examples:
-----------------------
Smart option menu: pip3 install tk_tools
display image: pip3 install pillow
tooltips: ttips.py in same directory script is run from (included).
date picker: pip3 install tkcalendar
toolbar with icons, needs icons folder and ttips.py (included)

-----Update log-----
V4.01: Removed file checks, caused all sorts of problems with Pyinstaller

V4.0:
Updated all code squirts to my latest knowledge.
Updated all squirts to be 100% PEP8 compliant.
Improved many squirts in look feel and substance.
Replaced some squirts with better examples.
Added recommended yt tkinter video channels menu.
Added status bar, but not in use properly yet.
Added new squirt: After
Added new squirt: Canvas
Added new squirt: Scrollbar
Added new squirt: Toplevel
Added new squirt: Treeview
Updated main tk assistant code to PEP8 as close as I could.
"""
import os
import sys
from threading import Timer
import time
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Combobox
import webbrowser as web

from PIL import Image, ImageTk
import pyperclip
import wget

import ttips

root = tk.Tk()
root.title('TK Assistant V4.1 - By Steve Shambles. 55 squirts.')
root.resizable(False, False)
root.eval('tk::PlaceWindow . Center')

# Need to do this after the file checks, not before.
root.iconbitmap('first_aid.ico')


def help_page():
    """Visit on-line help page from file menu."""
    web.open('https://stevepython.wordpress.com/2021/04/01/tk-assistant-v4-01/')


def tk_docs():
    """Visit Python Tkinter documentation webpage."""
    web.open('https://docs.python.org/3.7/library/tk.html')


def visit_blog():
    """Visit my blog from file menu."""
    web.open('https://stevepython.wordpress.com/')


def about_menu():
    """Disply about message box from file menu."""
    messagebox.showinfo('About Tk Assistant',
                        'TK Assistant V4.01\nIncludes 55 squirts.\n'
                        '\nFreeware.\nBy Steve Shambles,\nApril 2021.\n')


def exit_app():
    """Yes-no requestor to exit program."""
    ask_yn = messagebox.askyesno('Question',
                                 'Are you sure you want to exit Tk Assistant?')
    if not ask_yn:
        return
    root.destroy()
    sys.exit()


def open_folder():
    """Open squirts folder in default file viewer."""
    cwd = os.getcwd()
    web.open(cwd+'/squirts')


def contact_me():
    """Use my blog contact page."""
    web.open('https://stevepython.wordpress.com/contact')


def ytube_tuts():
    """Go to Youtube and list tkinter tutorial videos."""
    web.open('https://www.youtube.com/results?search_query=python+tkinter+tutorial&sp=EgIIBQ%253D%253D')


def go_reddit():
    """Go to Reddit learn python forum for help."""
    web.open('https://www.reddit.com/r/learnpython/')


def python_forum():
    """Visit Python GUI forum for help."""
    web.open('https://python-forum.io/Forum-GUI')


def quick_help():
    """Quick start help pop up."""
    web.open('tka-help.txt')


def git_hub():
    """Look at main TKAssistant source code on GitHub."""
    web.open('https://github.com/steveshambles/Tk-Assistant')


def donate_me():
    """Want more goodness? Please donate."""
    web.open("https:\\paypal.me/photocolourizer")


# Create the icon toolbar.
toolbar = tk.Frame(root,
                   borderwidth=2,
                   bg='slategray4',
                   relief='raised')
toolbar.grid(row=0, column=1, padx=20)

# Load all the images first as PNGs and use ImageTk to convert
# them to usable Tkinter images for icon menu.
img = Image.open(r'icons/qstart32v2.png')
qs_icon = ImageTk.PhotoImage(img)

img = Image.open(r'icons/help.png')
online_help_icon = ImageTk.PhotoImage(img)

img = Image.open(r'icons/folder.png')
squirts_folder_icon = ImageTk.PhotoImage(img)

img = Image.open(r'icons/readdoc.png')
read_docs_icon = ImageTk.PhotoImage(img)

img = Image.open(r'icons/ytube.png')
you_tube_icon = ImageTk.PhotoImage(img)

img = Image.open(r'icons/reddit.png')
reddit_icon = ImageTk.PhotoImage(img)

img = Image.open(r'icons/pythonv2.png')
forum_icon = ImageTk.PhotoImage(img)

img = Image.open(r'icons/exit.png')
exit_icon = ImageTk.PhotoImage(img)

# Set up the buttons for use on the icon toolbar.
qstart_btn = tk.Button(toolbar,
                       image=qs_icon,
                       text=' START ',
                       compound=tk.TOP,
                       command=quick_help)
qstart_btn.grid(row=0, column=0)
ttips.Create(qstart_btn,
             'Quick start help',
             fontname='helvetica',
             fontsize=12)

help_btn = tk.Button(toolbar,
                     image=online_help_icon,
                     text='   HELP   ',
                     compound=tk.TOP,
                     command=help_page)
help_btn.grid(row=0, column=1)
ttips.Create(help_btn,
             'On-line help page',
             fontname='helvetica',
             fontsize=12)

folder_btn = tk.Button(toolbar,
                       image=squirts_folder_icon,
                       text='SQUIRTS',
                       compound=tk.TOP,
                       command=open_folder)
folder_btn.grid(row=0, column=2)
ttips.Create(folder_btn,
             'View squirts folder',
             fontname='helvetica',
             fontsize=12)

tkdocs_btn = tk.Button(toolbar,
                       image=read_docs_icon,
                       text='   DOCS   ',
                       compound=tk.TOP,
                       command=tk_docs)
tkdocs_btn.grid(row=0, column=3)
ttips.Create(tkdocs_btn,
             'Read Tkinter documentation',
             fontname='helvetica',
             fontsize=12)

ytube_btn = tk.Button(toolbar,
                      image=you_tube_icon,
                      text='YouTube',
                      compound=tk.TOP,
                      command=ytube_tuts)
ytube_btn.grid(row=0, column=4)
ttips.Create(ytube_btn,
             'Tkinter YouTube Video Tutorials',
             fontname='helvetica',
             fontsize=12)

reddit_btn = tk.Button(toolbar,
                       image=reddit_icon,
                       text='REDDIT',
                       compound=tk.TOP,
                       command=go_reddit)
reddit_btn.grid(row=0, column=5)
ttips.Create(reddit_btn,
             'Get Tkinter help on Reddit',
             fontname='helvetica',
             fontsize=12)

py_forum_btn = tk.Button(toolbar,
                         image=forum_icon,
                         text='FORUM',
                         compound=tk.TOP,
                         command=python_forum)
py_forum_btn.grid(row=0, column=6)
ttips.Create(py_forum_btn,
             'Visit Python GUI forum',
             fontname='helvetica',
             fontsize=12)

exit_btn = tk.Button(toolbar,
                     image=exit_icon,
                     text='  EXIT  ',
                     compound=tk.TOP,
                     command=exit_app)
exit_btn.grid(row=0, column=7)
ttips.Create(exit_btn,
             'Exit Tk Assistant',
             fontname='helvetica',
             fontsize=12)

# Add the toolbar.
toolbar.grid()

# Create frame for the digital date and clock.
date_clock = tk.Label(root,
                      bg='steelblue',
                      fg='white',
                      font='helvetica 12',
                      relief=tk.SUNKEN,
                      border=4)
date_clock.grid(row=2, column=1, padx=20, pady=10, sticky='WE')


def date_time():
    """Threading timer prints date and time every second."""
    curr_time = (time.strftime('%a, %d %b %Y. %H:%M:%S'))
    date_clock.config(text=curr_time)  # Print updated clock.
    t = Timer(1.0, date_time)
    t.start()


# Starts the timer.
date_time()

# Add a status bar.
st_bar = tk.Label(root,
                  bg='khaki',
                  text='Status: Welcome to TK Assistant V4.01. April 2021',
                  bd=1,
                  relief=tk.SUNKEN,
                  anchor=tk.W)
st_bar.grid(row=3, column=1, padx=20, pady=10, sticky='WE')


def ask_execute(py_file):
    """Pop up asks if user wants to execute code example."""
    # Check tk_tools installed on system before running
    # smart option menu example.
    if py_file == (r'squirts\menu\smart_option_menu.py'):
        try:
            import tk_tools
        except ImportError:
            pyperclip.copy('pip3 install tk_tools')
            messagebox.showwarning('Cannot run example:',
                                   'You need to pip install tk_tools\n'
                                   'for this example to work.\n\n'
                                   'Copied install command to clipboard')
            return

    # Check pillow installed.
    if py_file == (r'squirts\misc\display_image.py') or  \
                  py_file == (r'squirts\menu\toolbar_demo.py'):
        try:
            import PIL
        except ImportError:
            pyperclip.copy('pip3 install pillow')
            messagebox.showwarning('Cannot run example:',
                                   'You need to pip install pillow\n'
                                   'for this example to work.\n\n'
                                   'Copied install command to clipboard')
            return

    # Check tkcalendar installed.
    if py_file == (r'squirts\dialogs\date_picker_dialog.py'):
        try:
            from tkcalendar import Calendar
        except ImportError:
            pyperclip.copy('pip3 install tk_calendar')
            messagebox.showwarning('Cannot run example:',
                                   'You need to pip install tkcalendar\n'
                                   'for this example to work.\n\n'
                                   'Copied install command to clipboard')
            return

    ask_yn = messagebox.askyesno('Question', 'Run example?')
    if ask_yn:
        web.open(py_file)


def pasted_info():
    """Pop up explains example code has been copied to clipboard."""
    messagebox.showinfo('Code copied',
                        'The code for your selection\n'
                        'has been copied to the clipboard.\n\n'
                        'You can paste this straight into\n'
                        'your code editor and it should work.')


def get_source_code(source_file):
    """Copy simple button example code to clipboard."""
    pyperclip.copy('')  # Clear clipboard.
    # Open py file,(passed into this function) as text.
    with open(source_file, 'r') as contents:
        squirt_code = contents.read()

        pyperclip.copy(squirt_code)  # Copy code to clipboard.
        pasted_info()  # Pop up message.
        ask_execute(source_file)  # Execute code example?


def combo_boxes():
    """Main gui, comboboxes."""
    sel_item = boxes_combo.get()
    if sel_item == 'BOXES':
        return

    if sel_item == 'Combo Box':
        get_source_code(r'squirts\boxes\combo_box.py')

    if sel_item == 'Entry Box':
        get_source_code(r'squirts\boxes\entry_box.py')

    if sel_item == 'List Box':
        get_source_code(r'squirts\boxes\list_box.py')

    if sel_item == 'Scr Txt Box':
        get_source_code(r'squirts\boxes\scrolled_text_box.py')

    if sel_item == 'Spin Box':
        get_source_code(r'squirts\boxes\spin_box.py')


def combo_buttons():
    """Main gui, combo buttons."""
    sel_item = btns_combo.get()
    if sel_item == 'BUTTONS':
        return

    if sel_item == 'Check Buttons':
        get_source_code(r'squirts\buttons\check_button.py')

    if sel_item == 'Image Button':
        get_source_code(r'squirts\buttons\image_button.py')

    if sel_item == 'Image Button + Text':
        get_source_code(r'squirts\buttons\image_btn_with_text.py')

    if sel_item == 'Menu Button':
        get_source_code(r'squirts\buttons\menu_button.py')

    if sel_item == 'Radio Buttons':
        get_source_code(r'squirts\buttons\radio_buttons.py')

    if sel_item == 'Simple Button':
        get_source_code(r'squirts\buttons\simple_button.py')


def dialogs():
    """Main gui file dialogs."""
    sel_item = dialogs_combo.get()
    if sel_item == 'DIALOGS':
        return

    if sel_item == 'Ask Directory':
        get_source_code(r'squirts\dialogs\ask_directory_dialog.py')

    if sel_item == 'Color Picker':
        get_source_code(r'squirts\dialogs\color_picker_dialog.py')

    if sel_item == 'Date Picker':
        get_source_code(r'squirts\dialogs\date_picker_dialog.py')

    if sel_item == 'Open File':
        get_source_code(r'squirts\dialogs\open_file_dialog.py')

    if sel_item == 'Open Many Files':
        get_source_code(r'squirts\dialogs\open_many_files_dialog.py')

    if sel_item == 'Save File':
        get_source_code(r'squirts\dialogs\save_file_dialog.py')

    if sel_item == 'User Input':
        get_source_code(r'squirts\dialogs\user_input_dialog.py')


def menu():
    """Main gui menu calls."""
    sel_item = menu_combo.get()
    if sel_item == 'MENU':
        return

    if sel_item == 'Drop-down Menu':
        get_source_code(r'squirts\menu\drop_down_menu.py')

    if sel_item == 'Menu Check-marks':
        get_source_code(r'squirts\menu\menu_check_marks.py')

    if sel_item == 'Right-click Context Menu':
        get_source_code(r'squirts\menu\right_click_menu.py')

    if sel_item == 'Smart Option Menu':
        get_source_code(r'squirts\menu\smart_option_menu.py')

    if sel_item == 'Toolbar with Icons':
        get_source_code(r'squirts\menu\toolbar_demo.py')


def misc():
    """Main gui, misc combo."""
    sel_item = misc_combo.get()
    if sel_item == 'MISC':
        return

    if sel_item == 'After demo':
        get_source_code(r'squirts\misc\after_demo.py')

    if sel_item == 'Bitmaps and cursors':
        get_source_code(r'squirts\misc\Bitmaps_and_cursors.py')

    if sel_item == 'Canvas demo':
        get_source_code(r'squirts\misc\canvas_demo.py')

    if sel_item == 'Colours Chart':
        get_source_code(r'squirts\misc\colours_chart.py')

    if sel_item == 'Digital Clock':
        get_source_code(r'squirts\misc\date_clock.py')

    if sel_item == 'Display Image':
        get_source_code(r'squirts\misc\display_image.py')

    if sel_item == 'Key Bind Reporter':
        get_source_code(r'squirts\misc\key_bind_reporter.py')

    if sel_item == 'Lambda Callback':
        get_source_code(r'squirts\misc\lambda_callback.py')

    if sel_item == 'Relief Types':
        get_source_code(r'squirts\misc\relief_types.py')

    if sel_item == 'Scrollbar demo':
        get_source_code(r'squirts\misc\scrollbar_demo.py')

    if sel_item == 'Simple Label':
        get_source_code(r'squirts\misc\simple_label.py')

    if sel_item == 'Tool-Tips':
        get_source_code(r'squirts\misc\tool_tips.py')

    if sel_item == 'Treeview demo':
        get_source_code(r'squirts\misc\treeview_demo.py')


def msg_boxes():
    """Main gui, ask msgbox combo."""
    sel_item = msg_boxes_combo .get()
    if sel_item == 'ASK MSG BOXES':
        return

    if sel_item == 'AskOkCancel':
        get_source_code(r'squirts\msg-boxes\askokcancel_msg_box.py')

    if sel_item == 'AskRetryCancel':
        get_source_code(r'squirts\msg-boxes\askretrycancel_msg_box.py')

    if sel_item == 'AskYN':
        get_source_code(r'squirts\msg-boxes\askyn_msg_box.py')

    if sel_item == 'AskYNCancel':
        get_source_code(r'squirts\msg-boxes\askyncancel_msg_box.py')

    if sel_item == 'Custom msg box':
        get_source_code(r'squirts\msg-boxes\custom_msg_box.py')

    if sel_item == 'Info MsgBox':
        get_source_code(r'squirts\msg-boxes\info_msg_box.py')

    if sel_item == 'Error MsgBox':
        get_source_code(r'squirts\msg-boxes\error_msg_box.py')

    if sel_item == 'Warning MsgBox':
        get_source_code(r'squirts\msg-boxes\warning_msg_box.py')


def scalers():
    """Main gui, info scalers combo."""
    sel_item = scalers.combo.get()
    if sel_item == 'SCALERS':
        return

    if sel_item == 'Colour sliders':
        get_source_code(r'squirts\scalers\colour_sliders.py')

    if sel_item == 'Simple scale':
        get_source_code(r'squirts\scalers\simple_scale.py')

    if sel_item == 'Progress Bar':
        get_source_code(r'squirts\scalers\progress_bar.py')

    if sel_item == 'Vertical Scale':
        get_source_code(r'squirts\scalers\vertical_scale.py')


def window():
    """Main gui window calls."""
    sel_item = wndw_combo.get()
    if sel_item == 'WINDOW':
        return

    if sel_item == 'Bind Keys':
        get_source_code(r'squirts\window\bind_and_detect_key_presses.py')

    if sel_item == 'Centre Window':
        get_source_code(r'squirts\window\centre_window.py')

    if sel_item == 'Message Window':
        get_source_code(r'squirts\window\message_window.py')

    if sel_item == 'Paned Windows':
        get_source_code(r'squirts\window\paned_windows.py')

    if sel_item == 'Status Bar':
        get_source_code(r'squirts\window\status_bar.py')

    if sel_item == 'Tabbed Windows':
        get_source_code(r'squirts\window\tabbed_window.py')

    if sel_item == 'Toplevel demo':
        get_source_code(r'squirts\window\toplevel_demo.py')

    if sel_item == 'Window Icon':
        get_source_code(r'squirts\window\window_icon.py')


def widget_imgs(image):
    """Display widget demo image select from widget-imgs menu."""
    w_img_frame = tk.Toplevel(root)
    img = Image.open(image)
    PHOTO = ImageTk.PhotoImage(img)
    img_lab = tk.Label(w_img_frame, image=PHOTO)
    img_lab.img = PHOTO
    img_lab.grid()


# 1st Drop-down menu.
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Menu', menu=file_menu)
file_menu.add_command(label='Quick start help', command=quick_help)
file_menu.add_command(label='On-line Help Page', command=help_page)
file_menu.add_separator()
file_menu.add_command(label='About program', command=about_menu)
file_menu.add_command(label='Visit my Python blog', command=visit_blog)
file_menu.add_command(label='Contact me', command=contact_me)
file_menu.add_command(label='Source code on GitHub', command=git_hub)
file_menu.add_command(label='Make small donation', command=donate_me)
file_menu.add_separator()
file_menu.add_command(label='View squirts Folder', command=open_folder)
file_menu.add_separator()
file_menu.add_command(label='Tkinter Documentation', command=tk_docs)
file_menu.add_command(label='YouTube Tkinter Tutorials', command=ytube_tuts)
file_menu.add_command(label='Reddit ask for help', command=go_reddit)
file_menu.add_command(label='Python GUI Forum', command=python_forum)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit_app)
root.config(menu=menu_bar)

# Tools drop-down menu.
tools_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Tools', menu=tools_menu)

tools_menu.add_command(label='Color Chart',
                       command=lambda: web.open(r'squirts\misc\colours_chart.py'))
tools_menu.add_command(label='Color Picker',
                       command=lambda: web.open(r'squirts\dialogs\color_picker_dialog.py'))
tools_menu.add_command(label='Key Bind Reporter',
                       command=lambda: web.open(r'squirts\misc\key_bind_reporter.py'))
root.config(menu=menu_bar)

# Widget images drop-down menu and submenus.
imgs_menu = tk.Menu(menu_bar, tearoff=0)

# Boxes.
menu_bar.add_cascade(label='Widget Imgs', menu=imgs_menu)

boxes_submenu = tk.Menu(imgs_menu, tearoff=0)
imgs_menu.add_cascade(label='Boxes', menu=boxes_submenu)

boxes_submenu.add_command(label='Combobox',
                          command=lambda: widget_imgs(r'w-imgs\combobox.png'))
boxes_submenu.add_command(label='Entrybox',
                          command=lambda: widget_imgs(r'w-imgs\entrybox.png'))
boxes_submenu.add_command(label='Listbox',
                          command=lambda: widget_imgs(r'w-imgs\listbox.png'))
boxes_submenu.add_command(label='Scr txt box',
                          command=lambda: widget_imgs(r'w-imgs\scr-text-box.png'))
boxes_submenu.add_command(label='Spinbox',
                          command=lambda: widget_imgs(r'w-imgs\spinbox.png'))
# Btns.
btns_submenu = tk.Menu(imgs_menu, tearoff=0)
imgs_menu.add_cascade(label='Buttons', menu=btns_submenu)

btns_submenu.add_command(label='Check btns',
                         command=lambda: widget_imgs(r'w-imgs\checkbuttons.png'))
btns_submenu.add_command(label='Image btn',
                         command=lambda: widget_imgs(r'w-imgs\imgbutton.png'))
btns_submenu.add_command(label='Img btn + txt',
                         command=lambda: widget_imgs(r'w-imgs\img-btn-txt.png'))
btns_submenu.add_command(label='Menu btn',
                         command=lambda: widget_imgs(r'w-imgs\menubtn.png'))
btns_submenu.add_command(label='Radio btn',
                         command=lambda: widget_imgs(r'w-imgs\radiobtn.png'))
btns_submenu.add_command(label='Simple btn',
                         command=lambda: widget_imgs(r'w-imgs\button.png'))
# Dialogs.
dialogs_submenu = tk.Menu(imgs_menu, tearoff=0)
imgs_menu.add_cascade(label='Dialogs', menu=dialogs_submenu)

dialogs_submenu.add_command(label='Ask directory',
                            command=lambda: widget_imgs(r'w-imgs\askdir.png'))
dialogs_submenu.add_command(label='Color picker',
                            command=lambda: widget_imgs(r'w-imgs\colorpicker.png'))
dialogs_submenu.add_command(label='Date picker',
                            command=lambda: widget_imgs(r'w-imgs\datepicker.png'))
dialogs_submenu.add_command(label='Open file',
                            command=lambda: widget_imgs(r'w-imgs\openfile.png'))
dialogs_submenu.add_command(label='Open many files',
                            command=lambda: widget_imgs(r'w-imgs\openmanyfiles.png'))
dialogs_submenu.add_command(label='Save file',
                            command=lambda: widget_imgs(r'w-imgs\savefile.png'))
dialogs_submenu.add_command(label='User input',
                            command=lambda: widget_imgs(r'w-imgs\userinput.png'))
# Menus.
menus_submenu = tk.Menu(imgs_menu, tearoff=0)
imgs_menu.add_cascade(label='Menus', menu=menus_submenu)

menus_submenu.add_command(label='Drop down menu',
                          command=lambda: widget_imgs(r'w-imgs\dropdownmenu.png'))
menus_submenu.add_command(label='Menu check-marks',
                          command=lambda: widget_imgs(r'w-imgs\menucheckmarks.png'))
menus_submenu.add_command(label='Right click context menu',
                          command=lambda: widget_imgs(r'w-imgs\rightclickcontextmenu.png'))
menus_submenu.add_command(label='Smart option menu',
                          command=lambda: widget_imgs(r'w-imgs\smartoptionmenu.png'))
menus_submenu.add_command(label='Toolbar with icons',
                          command=lambda: widget_imgs(r'w-imgs\toolbar.png'))
# Misc.
misc_submenu = tk.Menu(imgs_menu, tearoff=0)
imgs_menu.add_cascade(label='Misc', menu=misc_submenu)

misc_submenu.add_command(label='After example',
                         command=lambda: widget_imgs(r'w-imgs\after.png'))
misc_submenu.add_command(label='Bitmaps and cursors',
                         command=lambda: widget_imgs(r'w-imgs\bitmaps-cursors.png'))
misc_submenu.add_command(label='Canvas example',
                         command=lambda: widget_imgs(r'w-imgs\canvas.png'))
misc_submenu.add_command(label='Color chart',
                         command=lambda: widget_imgs(r'w-imgs\colorschart.png'))
misc_submenu.add_command(label='Digital clock',
                         command=lambda: widget_imgs(r'w-imgs\digitalclock.png'))
misc_submenu.add_command(label='Display image',
                         command=lambda: widget_imgs(r'w-imgs\displayimage.png'))
misc_submenu.add_command(label='Key bind reporter',
                         command=lambda: widget_imgs(r'w-imgs\keybindreporter.png'))
misc_submenu.add_command(label='Lambda callback',
                         command=lambda: widget_imgs(r'w-imgs\lambdacallback.png'))
misc_submenu.add_command(label='Relif types',
                         command=lambda: widget_imgs(r'w-imgs\relieftypes.png'))
misc_submenu.add_command(label='Scrollbar example',
                         command=lambda: widget_imgs(r'w-imgs\scrollbar.png'))
misc_submenu.add_command(label='Simple label',
                         command=lambda: widget_imgs(r'w-imgs\simplelabel.png'))
misc_submenu.add_command(label='Tooltips',
                         command=lambda: widget_imgs(r'w-imgs\tooltips.png'))
misc_submenu.add_command(label='Treeview example',
                         command=lambda: widget_imgs(r'w-imgs\treeview.png'))

# Msg boxes.
msgboxes_submenu = tk.Menu(imgs_menu, tearoff=0)
imgs_menu.add_cascade(label='Msg boxes', menu=msgboxes_submenu)

msgboxes_submenu.add_command(label='AskOkCancel',
                             command=lambda: widget_imgs(r'w-imgs\askokcancel.png'))
msgboxes_submenu.add_command(label='AskRetrykCancel',
                             command=lambda: widget_imgs(r'w-imgs\askretrycancel.png'))
msgboxes_submenu.add_command(label='AskYesNo',
                             command=lambda: widget_imgs(r'w-imgs\askyn.png'))
msgboxes_submenu.add_command(label='AskYesNoCancel',
                             command=lambda: widget_imgs(r'w-imgs\askyncancel.png'))
msgboxes_submenu.add_command(label='Custom Msg Box',
                             command=lambda: widget_imgs(r'w-imgs\custommsgbox.png'))
msgboxes_submenu.add_command(label='Error Msg Box',
                             command=lambda: widget_imgs(r'w-imgs\errormsgbox.png'))
msgboxes_submenu.add_command(label='Info Msg Box',
                             command=lambda: widget_imgs(r'w-imgs\infomsgbox.png'))
msgboxes_submenu.add_command(label='Warning Msg Box',
                             command=lambda: widget_imgs(r'w-imgs\warningmsgbox.png'))
# Scalers.
scalers_submenu = tk.Menu(imgs_menu, tearoff=0)
imgs_menu.add_cascade(label='Scalers', menu=scalers_submenu)

scalers_submenu.add_command(label='Color sliders',
                            command=lambda: widget_imgs(r'w-imgs\colorsliders.png'))
scalers_submenu.add_command(label='Progress bar',
                            command=lambda: widget_imgs(r'w-imgs\progressbar.png'))
scalers_submenu.add_command(label='Simple scale',
                            command=lambda: widget_imgs(r'w-imgs\simplescale.png'))
scalers_submenu.add_command(label='Vertical scale',
                            command=lambda: widget_imgs(r'w-imgs\verticalscale.png'))
# Window.
window_submenu = tk.Menu(imgs_menu, tearoff=0)
imgs_menu.add_cascade(label='Window', menu=window_submenu)

window_submenu.add_command(label='Bind keys',
                           command=lambda: widget_imgs(r'w-imgs\bindkeys.png'))
window_submenu.add_command(label='Centre window',
                           command=lambda: widget_imgs(r'w-imgs\centrewindow.png'))
window_submenu.add_command(label='Message window',
                           command=lambda: widget_imgs(r'w-imgs\msgwindow.png'))
window_submenu.add_command(label='Paned window',
                           command=lambda: widget_imgs(r'w-imgs\paned.png'))
window_submenu.add_command(label='Status bar',
                           command=lambda: widget_imgs(r'w-imgs\statusbar.png'))
window_submenu.add_command(label='Tabbed windows',
                           command=lambda: widget_imgs(r'w-imgs\tabbed.png'))
window_submenu.add_command(label='Toplevel example',
                           command=lambda: widget_imgs(r'w-imgs\toplevel.png'))
window_submenu.add_command(label='Window icon',
                           command=lambda: widget_imgs(r'w-imgs\changedicon.png'))
root.config(menu=menu_bar)


# Recomended YouTube Tk videos.
vid_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Best YT Chans', menu=vid_menu)

vid_menu.add_command(label='Alan D Moore Codes',
                     command=lambda: web.open('https://www.youtube.com/channel/UCj7i-mmOjLV17YTPIrCPkog'))
vid_menu.add_command(label='Codemy',
                     command=lambda: web.open('https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw'))
vid_menu.add_command(label='Python Simplified',
                     command=lambda: web.open('https://www.youtube.com/watch?v=itRLRfuL_PQ&list=PLqXS1b2lRpYRVrpyN19e3vzLZfFoPLTRL&index=2'))
root.config(menu=menu_bar)


# Create inner labelframe.
combo_frame = tk.LabelFrame(root,
                            relief=tk.RIDGE,
                            fg='blue',
                            text='Please Select an item from the '
                            'drop-down boxes below')
combo_frame.grid(padx=20, pady=15, column=1, row=1)

# Combo boxes for main gui.
boxes_combo = Combobox(combo_frame)
boxes_combo['values'] = ('BOXES', 'Combo Box', 'Entry Box', 'List Box',
                         'Scr Txt Box', 'Spin Box')
boxes_combo.current(0)
boxes_combo.grid(row=0, column=0, padx=5, pady=5)
boxes_btn = tk.Button(combo_frame,
                      bg='plum',
                      text='Get',
                      command=combo_boxes)
boxes_btn.grid(row=0, column=1, sticky='W', padx=5, pady=5)
# ---------------
btns_combo = Combobox(combo_frame)
btns_combo['values'] = ('BUTTONS',
                        'Check Buttons', 'Image Button',
                        'Image Button + Text',
                        'Menu Button', 'Radio Buttons',
                        'Simple Button')
btns_combo.current(0)
btns_combo.grid(row=1, column=0, padx=5, pady=5)
btns_btn = tk.Button(combo_frame,
                     bg='skyblue',
                     text='Get',
                     command=combo_buttons)
btns_btn.grid(row=1, column=1, sticky='W', padx=5, pady=5)

# ---------------
dialogs_combo = Combobox(combo_frame)
dialogs_combo['values'] = ('DIALOGS', 'Ask Directory', 'Color Picker',
                           'Date Picker', 'Open File', 'Open Many Files',
                           'Save File', 'User Input')
dialogs_combo.current(0)
dialogs_combo.grid(row=2, column=0, padx=5, pady=5)
dialogs_btn = tk.Button(combo_frame,
                        bg='red',
                        text='Get',
                        command=dialogs)
dialogs_btn.grid(row=2, column=1, sticky='WE', padx=5, pady=5)
# ---------------
menu_combo = Combobox(combo_frame)
menu_combo['values'] = ('MENU', 'Drop-down Menu', 'Menu Check-marks',
                        'Right-click Context Menu', 'Smart Option Menu',
                        'Toolbar with Icons')
menu_combo.current(0)
menu_combo.grid(row=3, column=0, padx=5, pady=5)
menu_btn = tk.Button(combo_frame,
                     bg='yellow',
                     text='Get',
                     command=menu)
menu_btn.grid(row=3, column=1, sticky='WE', padx=5, pady=5)

# ---------------
msg_boxes_combo = Combobox(combo_frame)
msg_boxes_combo['values'] = ('MSG BOXES', 'AskOkCancel',
                             'AskRetryCancel', 'AskYN', 'AskYNCancel',
                             'Custom msg box', 'Error MsgBox',
                             'Info MsgBox', 'Warning MsgBox')
# ---------------
misc_combo = Combobox(combo_frame)
misc_combo['values'] = ('MISC', 'After demo', 'Bitmaps and cursors',
                        'Canvas demo', 'Colours Chart',
                        'Digital Clock', 'Display Image',
                        'Key Bind Reporter', 'Lambda Callback',
                        'Relief Types', 'Scrollbar demo',
                        'Simple Label', 'Tool-Tips', 'Treeview demo')
misc_combo.current(0)
misc_combo.grid(row=0, column=2, padx=5, pady=5)
misc_btn = tk.Button(combo_frame,
                     bg='orange',
                     text='Get',
                     command=misc)
misc_btn.grid(row=0, column=3, sticky='WE', padx=5, pady=5)
# ---------------
msg_boxes_combo .current(0)
msg_boxes_combo .grid(row=1, column=2, padx=5, pady=5)
askmsg_btn = tk.Button(combo_frame,
                       bg='springgreen',
                       text='Get',
                       command=msg_boxes)
askmsg_btn.grid(row=1, column=3, sticky='W', padx=5, pady=5)
# ---------------
scalers.combo = Combobox(combo_frame)
scalers.combo['values'] = ('SCALERS', 'Colour sliders', 'Progress Bar',
                           'Simple scale', 'Vertical Scale', )
scalers.combo.current(0)
scalers.combo.grid(row=2, column=2, padx=5, pady=5)
info_btn = tk.Button(combo_frame,
                     bg='steelblue',
                     text='Get',
                     command=scalers)
info_btn.grid(row=2, column=3, sticky='WE', padx=5, pady=5)

# ---------------
wndw_combo = Combobox(combo_frame)
wndw_combo['values'] = ('WINDOW', 'Bind Keys', 'Centre Window',
                        'Message Window', 'Paned Windows',
                        'Status Bar', 'Tabbed Windows',
                        'Toplevel demo', 'Window Icon')
wndw_combo.current(0)
wndw_combo.grid(row=3, column=2, padx=5, pady=5)
wndw_btn = tk.Button(combo_frame,
                     bg='salmon',
                     text='Get',
                     command=window)
wndw_btn.grid(row=3, column=3, sticky='WE', padx=5, pady=5)
# ---------------

root.protocol("WM_DELETE_WINDOW", exit_app)


root.mainloop()
