from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import*

background="#008B8B"
framebg="EDEDED"
framefg="06283D"

a= CurrencyConverter()
root = tk.Tk()
root.geometry("700x380")
root.title("CurrencyConverter")
root.resizable(False,False)

#background image 
frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="bg1.PNG")
Label(frame,image=backgroundimage).pack()


def clicked():
    amount=(e1.get())
    cur1=e2.get()
    cur2=e3.get()
    data = a.convert(amount,cur1,cur2)
    l5=tk.Label(root,text=data,font= "Times 15 bold",bg="#00264d",fg="#57a1f8").place(x=420,y=340)


#icon image 
image_icon=PhotoImage(file="icon1.png")
root.iconphoto(False,image_icon)


l1=tk.Label(root,text="Currency  Converter",font= "Times 25 bold",bg="white",fg="#57a1f8").place(x=215,y=20)
l2=tk.Label(root,text="Enter amount",font= "Times 18 bold",bg="white").place(x=208,y=110)
e1=tk.Entry(root)
l3=tk.Label(root,text="Enter currency",font= "Times 18 bold",bg="white").place(x=202,y=160)
e2=tk.Entry(root)
l4=tk.Label(root,text="Required currency",font= "Times 16 bold",bg="white").place(x=198,y=256)
e3=tk.Entry(root)
e4=tk.Entry(root,bg="#00264d",width=30,border=0)
e5=tk.Entry(root,bg="#00264d",width=30,border=0)


button= tk.Button(root,width=10,text="Convert",border=0,bg="#00264d",cursor='hand2',fg="#57a1f8",font= "Times 14 bold",command=clicked)
button.place(x=130,y=340)
e1.place(x=380,y=120)
e2.place(x=380,y=170)
e3.place(x=375,y=258)
e4.place(x=420,y=340)
e5.place(x=420,y=352)

root.mainloop()
