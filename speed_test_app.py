# Internet Speed Test made with tkinter 🪶
import tkinter
from tkinter import PhotoImage, Label
from PIL import Image, ImageTk
import speedtest

# 1- Define root window and configure its properties
root = tkinter.Tk()
root.title("Internet Speed Test")
root.geometry('360x600+500+100')
root.resizable(False,False)
root.config(bg='#1a212d')

# 2- Set application icon
image_icon = PhotoImage(file='logo.png')
root.iconphoto(False, image_icon)

# 3 - Set the images in the application
top_image = PhotoImage(file='top.png')
main_image = PhotoImage(file='main.png')
button_image = PhotoImage(file='button.png')

# 4- Make the widgets
speed_test_top_label = tkinter.Label(root, image=top_image, bg='#1a212d')
speed_test_main_label = tkinter.Label(root, image=main_image, bg='#1a212d')
start_button = tkinter.Button(root,
                              text="Start",
                              font=('Arial', 30, 'bold'),
                              bg='#1a212d',
                              highlightbackground='#1a212d',
                              bd=0,
                              activebackground='#1a212d',
                              cursor='hand2')

# pack the widgets into root window
speed_test_top_label.pack()
speed_test_main_label.pack(pady=(40,0))
start_button.pack()

# 🔁 run the mainloop() method of root
root.mainloop()