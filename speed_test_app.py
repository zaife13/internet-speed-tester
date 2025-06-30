# Internet Speed Test made with tkinter 🪶
import tkinter
from tkinter import PhotoImage, Label, ttk
import speedtest
from PIL import ImageTk, Image

# 1- Define root window and configure its properties
root = tkinter.Tk()
root.title("Internet Speed Test")
root.geometry('360x600+500+100')
root.resizable(False,False)
root.config(bg='#1a212d')

# ✅ Define functions here
def check_speed():
    test = speedtest.Speedtest()
    upload_speed = round(test.upload()/(1024 * 1024), 3)
    upload_speed_label.config(text=upload_speed)
    print(f"upload speed: {upload_speed}")

    download_speed = round(test.download()/(1024 * 1024),3)
    download_speed_label.config(text=download_speed)
    Download.config(text=download_speed, foreground='#26cc00')
    print(f"download speed : {download_speed}")

    ping_speed_label.config(text=test.results.ping)
    print(f"ping: {test.results.ping}")

# 2- Set application icon
image_icon = PhotoImage(file='logo.png')
root.iconphoto(False, image_icon)

# 3 - Set the images in the application
top_image = PhotoImage(file='top.png')
main_image = PhotoImage(file='main.png')
#button_image = PhotoImage(file='button.png')

# 4- Make the widgets
# using ttk.Style() method to create button style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton",
                font=("Arial", 20, "bold"),
                foreground="white",
                background="#2c3442",
                padding=10)
style.map("TButton", background=[("active", "#3a4452")])

speed_test_top_label = tkinter.Label(root, image=top_image, bg='#1a212d')
speed_test_main_label = tkinter.Label(root, image=main_image, bg='#1a212d')
start_button = ttk.Button(root, text="START", style="TButton", command=check_speed)

# 5- Make the Labels
ping_label = tkinter.Label(root, text='Ping', font=('arial',10,'bold'), bg='#384056', fg='white')
ping_speed_label = tkinter.Label(root, text='00', font=('arial',10,'bold'), bg='#384056', fg='white')
ping_ms_label = tkinter.Label(root, text='MS', font= ('arial',7,'bold'), bg='#384056', fg='white')

download_label = tkinter.Label(root, text='Download', font= ('arial',10,'bold'), bg='#384056', fg='white')
download_speed_label = tkinter.Label(root, text='00', font=('arial',10,'bold'), bg='#384056', fg='white')
download_mbps_label = tkinter.Label(root, text='MBPS', font= ('arial',7,'bold'), bg='#384056', fg='white')

upload_label = tkinter.Label(root, text='Upload', font= ('arial',10,'bold'), bg='#384056', fg='white')
upload_speed_label = tkinter.Label(root, text='00', font=('arial',10,'bold'), bg='#384056', fg='white')
upload_mbps_label = tkinter.Label(root, text='MBPS', font= ('arial',7,'bold'), bg='#384056', fg='white')


download_main = tkinter.Label(root, text='Download', font= ('arial',15,'bold'), bg='#384056', fg='white')
mbps_main = tkinter.Label(root, text='MBPS', font= ('arial',15,'bold'), bg='#384056', fg='white')

Download = tkinter.Label(root, text='00', font= ('arial',40,'bold'), bg='#384056', fg='white')

# 6- pack the widgets and labels into root window
speed_test_top_label.pack()
speed_test_main_label.pack(pady=(40,0))
start_button.pack(pady=(30,0))

# place the labels according to the layout using x-axis and y-axis
ping_label.place(x=55, y=3)
ping_speed_label.place(x=70, y=60, anchor='center')
ping_ms_label.place(x=62, y=80)

download_label.place(x=150, y=3)
download_speed_label.place(x=180, y=60, anchor='center')
download_mbps_label.place(x=168, y=80)

upload_label.place(x=270, y=3)
upload_speed_label.place(x=293, y=60, anchor='center')
upload_mbps_label.place(x=280, y=80)

download_main.place(x=148, y=280)
mbps_main.place(x=160, y=380)

Download.place(x=185, y=350, anchor='center')

# 🔁 run the mainloop() method of root
root.mainloop()