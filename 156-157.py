from tkinter import*
from PIL import ImageTk,Image
import random
root=Tk()
root.title("Dice Game")
root.geometry("600x400")
root.configure(background="yellow")
img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))
label1=Label(root,text="player1",bg="royal blue",fg="white")
label1.place(relx=0.1,rely=0.3,anchor=CENTER)
label2=Label(root,text="player2",bg="royal blue",fg="white")
label2.place(relx=0.9,rely=0.3,anchor=CENTER)
label3=Label(root,bg="royal blue",fg="white")
label3.place(relx=0.1,rely=0.4,anchor=CENTER)
label4=Label(root,bg="royal blue",fg="white")
label4.place(relx=0.9,rely=0.4,anchor=CENTER)
label5=Label(root,bg="royal blue",fg="white")
label5.place(relx=0.5,rely=0.5,anchor=CENTER)

player1score=0
def player1():
    global player1score
    random_no=random.randint(1,6)
    label5["text"]="player1 dice random number: "+str(random_no)
    player1score=player1score+random_no
    label3["text"]=str(player1score)
btn1=Button(root,image=img,command=player1)
btn1.place(relx=0.1,rely=0.6,anchor=CENTER)
player2score=0
def player2():
    global player2score
    random_no=random.randint(1,6)
    label5["text"]="player2 dice random number: "+str(random_no)
    player2score=player2score+random_no
    label4["text"]=str(player2score)
btn2=Button(root,image=img,command=player2)
btn2.place(relx=0.9,rely=0.6,anchor=CENTER)
root.mainloop()
