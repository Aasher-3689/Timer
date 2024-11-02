#Developed by Muhammad_Aasher

import threading
from tkinter import *
from time import sleep
import pygame

#---------------------------

running = False
pause = False
current_value = ""
remaining_seconds = 0

#----------------------------
pygame.mixer.init()

def play_audio():
    pygame.mixer.music.load("times-up.wav")
    pygame.mixer.music.play(loops=0)

def stop_audio():
    pygame.mixer.music.stop()

def start_time():
    global running, pause, remaining_seconds
    running = True
    pause = False
    if remaining_seconds == 0:
        in_hours = int(hour_scale.get())
        in_minutes = int(minute_scale.get())
        in_seconds = int(second_scale.get())
        remaining_seconds = in_hours * 3600 + in_minutes * 60 + in_seconds
        if remaining_seconds > 0:
            start_button.config(state=DISABLED)
        threading.Thread(target=update_timer, daemon=True).start()

def stop_time():
    global running, pause
    stop_button.config(text="Stop")
    stop_audio()
    if remaining_seconds  > 1:
        if running and not pause:
            pause = True
            stop_button.config(text="Resume")
        elif running and pause:
            pause = False
            stop_button.config(text="Stop")
        threading.Thread(target=update_timer, daemon=True).start()
    else:
        pass

def reset_time():
    global running, pause, remaining_seconds
    running = False
    pause = False
    remaining_seconds = 0
    label_time.config(text="00 : 00 : 00")
    start_button.config(state=ACTIVE)
    stop_button.config(text="Stop")
    stop_audio()


def update_timer():
    global current_value, remaining_seconds
    for time_left in range(remaining_seconds, -1, -1):
        if running and not pause:
            remaining_seconds = time_left

            if remaining_seconds ==1 and running:
                play_audio()

            seconds = int(time_left % 60)
            minutes = int((time_left / 60) % 60)
            hours = int(time_left / 3600)

            current_value = f'{hours:02} : {minutes:02} : {seconds:02}'
            label_time.config(text=current_value)
            sleep(1)

            if time_left == 0:
                while pygame.mixer.music.get_busy():
                    if not running:
                        break
                    sleep(0.1)
                start_button.config(state=ACTIVE)
        else:
            break

#-------------------------------
window = Tk()

window.geometry("420x485")
window.title("Timer-Aasher_Elahi")
window.resizable(False, False)
window.config(background="#161e70")
window.iconbitmap("Aasher.ico")

#-------------------------------
heading = Label(window,
                text="Quick-timing Timer",
                font=("Arial Rounded MT Bold", 26, "bold"),
                fg="white", bg="#292c75",
                relief=RAISED, bd=1,
                padx=70, pady=10)
heading.pack()
#-------------------------------
footer = Label(window,
               text="       ",
               font=("Arial Rounded MT Bold", 26, "bold"),
               fg="white", bg="#292c75",
               relief=RAISED, bd=1,
               padx=200)
footer.place(y=455)

#-------------------------------
photo_timer = PhotoImage(file="timer.png")
ph_timer = Label(image=photo_timer,
                 bg="#161e70")
ph_timer.place(x=180, y=67)

#-------------------------------
hour_scale = Scale(window,
                   from_=0, to=23,
                   orient='horizontal', label="Hours",
                   font=("Arial 16 bold", 11, "bold"),
                   fg="White", bg="#292c75",
                   activebackground="#292c75")
hour_scale.place(h=70, w=130,
                 x=10, y=220)
#-------------------------------
minute_scale = Scale(window,
                     from_=0, to=59,
                     orient='horizontal', label="Minutes",
                     font=("Arial 16 bold", 11, "bold"), border=0,
                     fg="White", bg="#292c75",
                     activebackground="#292c75")
minute_scale.place(h=70, w=130,
                   x=145, y=220)
#-------------------------------
second_scale = Scale(window,
                     from_=0, to=59,
                     orient='horizontal', label="Seconds",
                     font=("Arial 16 bold", 11, "bold"), border=0,
                     fg="White", bg="#292c75",
                     activebackground="#292c75")
second_scale.set(10)
second_scale.place(h=70, w=130,
                   x=280, y=220)

#-------------------------------
start_button = Button(window,
                      text="Start",
                      font=("Arial Rounded MT Bold", 17),
                      fg="white", bg="#292c75",
                      activeforeground="white",
                      activebackground="#292c75",
                      command=start_time)
start_button.place(h=35, w=180,
                   x=120, y=315)

#-------------------------------
stop_button = Button(window,
                     text="Stop",
                     font=("Arial Rounded MT Bold", 17),
                     fg="white", bg="#292c75",
                     activeforeground="white",
                     activebackground="#292c75",
                     command=stop_time)
stop_button.place(h=35, w=180,
                  x=120, y=358)

#-------------------------------
reset_button = Button(window,
                      text="Reset",
                      font=("Arial Rounded MT Bold", 17),
                      fg="white", bg="#292c75",
                      activeforeground="white",
                      activebackground="#292c75",
                      command=reset_time)
reset_button.place(h=35, w=180,
                   x=120, y=400)

#-------------------------------
label_time = Label(window,
                   text="00 : 00 : 00", font=('Arial Rounded MT Bold', 50),
                   fg='#cdd1d1', bg='#161e70')
label_time.place(x=37, y=128)
#-------------------------------
window.mainloop()

# © All right reserved - Owned by Tabassat and Aasher's team!
