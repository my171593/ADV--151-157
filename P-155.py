from tkinter import *
import random

root = Tk()
root.title("Dictionary")
root.geometry("600x400")

dictionary = {"Color" : ["AntiqueWhite1", "AntiqueWhite2", "AntiqueWhite3", "AntiqueWhite4", 
                         "CadetBlue1", "CadetBlue2", "CadetBlue3", "CadetBlue4", 
                         "DarkGoldenrod1", "DarkGoldenrod2", "DarkGoldenrod3", "DarkGoldenrod4", 
                         "DarkOliveGreen1", "DarkOliveGreen2", "DarkOliveGreen3", "DarkOliveGreen4", 
                         "DarkOrange1", "DarkOrange2", "DarkOrange3", "DarkOrange4", 
                         "DarkOrchid1", "DarkOrchid2", "DarkOrchid3", "DarkOrchid4", 
                         "DarkSeaGreen1", "DarkSeaGreen2", "DarkSeaGreen3", "DarkSeaGreen4", 
                         "DarkSlateGray1", "DarkSlateGray2", "DarkSlateGray3", "DarkSlateGray4", 
                         "DeepPink2", "DeepPink3", "DeepPink4", 
                         "DeepSkyBlue2", "DeepSkyBlue3", "DeepSkyBlue4", 
                         "DodgerBlue2", "DodgerBlue3", "DodgerBlue4", 
                         "HotPink1", "HotPink2", "HotPink3", "HotPink4", 
                         "IndianRed1"]}

def bg_color_change():
    random_color = random.randint(0, 478)
    print(dictionary["Color"][random_color])
    root.configure(background = dictionary["Color"][random_color])

btn = Button(root, text = "Click Me To Change The BG Color", command = bg_color_change)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()