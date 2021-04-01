"""Message Widow.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import Message, Tk

root = Tk()
root.title('Message window demo')

MSG_TXT = 'What you think of me is none of my business.'

msg = Message(root,
              text=MSG_TXT,
              bg='steelblue',
              fg='gold',
              font=('verdant', 60)
              )
msg.grid()


root.mainloop()
