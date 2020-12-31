import tkinter as tk
from tkinter import *
import os

root = tk.Tk()

root.title("Fibonacci Series")
# create the fibonacci series
def click():
    fib_list =[]
    x = entry.get()
    def recursion(y):
        if y == 0:
            return 0
        elif y == 1:
            return 1
        else:
            return recursion(y-2)+recursion(y-1)
    for i in range(int(x)):
        fib_list.append(recursion(i))
    # print(fib_list)
    series.configure(text=fib_list)
    fib_list = []


#clear the screen
def click2():
    series.configure(text='fibonacci Series')



label = tk.Label(root,text='Fibonacci Series',font=("Andalus",20)).pack()
label2 = tk.Label(root,text='-----------------------------------------------',font=("Andalus",20)).pack()
series = tk.Label(root,text='fibonacci Series',font=("Andalus",20),fg="green")
series.pack()
entry = tk.Entry(root,width=50)
entry.place(x=100,y=150)
# entry.pack()
button = tk.Button(root,text="Fibonacci Numbers",cursor='heart',bd=2,bg="yellow",fg="green",font=("Andalus",10),command=click)
button.place(x=170,y=180)
# button.pack()
button2 = tk.Button(root,text="Clear",cursor='heart',bd=2,bg="yellow",fg="green",font=("Andalus",10),command=click2)
button2.place(x=300,y=180)
root.geometry("500x500+200+200")

root.mainloop()



