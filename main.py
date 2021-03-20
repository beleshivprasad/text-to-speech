
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
import datetime



################### Initialized window####################

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.config(bg = '#0059b3')
root.title('Text to Speech')


##heading
Label(root, text = 'TEXT TO SPEECH' , font='arial 18 bold' , bg ='white smoke').pack()



#label
Label(root, text ='Enter Text', font ='arial 17 bold' , bg ='white smoke').place(x=170,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg,width=75)
entry_field.place(x=20,y=120)


###################define function##############################

def tts():
    x = datetime.datetime.now()
    message = entry_field.get()
    speech = gTTS(text = message)
    name = x.strftime("audio-"+"%b-%d-%H-%M-%S"+".mp3")
    speech.save(name)
    playsound(name)
    # os.remove(name)

def exit():
    root.destroy()

def reset():
    Msg.set("")


#Button
font_style = 'arial 15 bold'
Button(root, text = "PLAY" , font = f"{font_style}", command = tts, width =4).place(x=50, y=200)
Button(root, text = 'RESET', font = f"{font_style}", command = reset).place(x= 190 , y =200)
Button(root,text = 'EXIT',font = f"{font_style}" , command = exit).place(x=360,y=200)


#infinite loop to run program
root.mainloop()
