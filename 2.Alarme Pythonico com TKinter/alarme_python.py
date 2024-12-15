import tkinter as tk
import datetime
import time
import os
#import pygame

def alarm():
    while True:
        set_alarm_time = f'{hour.get()}:{minute.get()}:{second.get()}'
        time.sleep(1)
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(current_time, set_alarm_time)

        if(set_alarm_time == current_time):
            #afplay
            #playsound('Alarm07.wav')
            #pygame.mixer.init()
            #pygame.mixer.music.load("Alarm07.wav")
            #pygame.mixer.music.play()
            print('TOCAR O ALARME')

root = tk.Tk()
root.geometry("400x200")
root.title('Alarme Pythonico | Programador Aventureiro')

tk.Label(root, text='Alarme Pythonico | Programador Aventureiro', font=('Helvetica 20 bold')).pack(pady=10)
tk.Label(root, text='Definir alarme').pack(pady=5)

frame = tk.Frame(root)
frame.pack()

def option(value):
    opt = tk.StringVar(root)
    options = [str(i).zfill(2) for i in range(value)]
    opt.set(options[0])
    tk.OptionMenu(frame, opt, *options).pack(side=tk.LEFT)
    return opt

hour = option(24)
minute = option(60)
second = option(60)

tk.Button(root, text='Definir', font=('Helvetica 15'), command=alarm).pack(pady=20)

root.mainloop()