from tkinter import *
import winsound
import time
root = Tk()
root.geometry('600x400')
root.resizable(0, 0)
root.title('T I M E R'.center(180))
color = True
i = 60


def colour():
    global color, i, time_label
    time_label.config(state='disabled', disabledforeground='red', relief='sunken')
    if i >= 0:
        if color:
            can_obj['bg'] = 'deepskyblue3'
            winsound.PlaySound('tick.wav',winsound.SND_FILENAME | winsound.SND_ASYNC)
            color = False
        else:
            can_obj['bg'] = 'royalblue1'
            winsound.PlaySound('tick.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            color = True
        time_label['text'] = i
        i -= 1
        root.after(1000, colour)
    else:
        winsound.PlaySound('horn.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        time.sleep(5)
        time_label.config(state='normal', text='START', font=('Rockwell', 20, 'bold'), bg='chartreuse3', relief='raised', borderwidth=3)
        i = 60


can_obj = Canvas(root, height=600, width=600, bg='royalblue1')
can_obj.pack()

can_obj.create_rectangle(100, 100, 500, 300, fill='steelblue1')      # big rectangle centre
can_obj.create_rectangle(200, 150, 400, 250, fill='cyan')      # small rectangle centre

can_obj.create_line(0, 0, 100, 100, width=5, fill='green2')
can_obj.create_line(600, 0, 500, 100, width=5, fill='green2')
can_obj.create_line(0, 400, 100, 300, width=5, fill='green2')
can_obj.create_line(600, 400, 500, 300, width=5, fill='green2')

time_label = Button(root, text="START", width='8', font=('Rockwell', 20, 'bold'), bg='chartreuse3', command=lambda: colour(), relief='raised', borderwidth=3)
time_label.place(relx=0.38, rely=0.43)

root.mainloop()
