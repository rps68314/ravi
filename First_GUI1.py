from tkinter import *
import math


start = Tk()


start.geometry("450x200")
start.title("Find Transmission Voltage")
start.config(bg="skyblue")


L = 0
P = 0
R = 0
k = 0
result = StringVar()


def cl():
    global result
    global Length
    global Power
    result = result.set(0)
    Length = Length.set("")
    Power = Power.set("")


def pr():
    global L
    global P
    global R
    global k

    ls = [11, 33, 66, 132, 220, 400]
    L = float(Length.get())
    P = float(Power.get())
    R = str(round(math.sqrt(5.5*(L/1.6+P/100))))
    if int(R) <= ls[0]:
        k =str(ls[0])
        result.set(k)
    elif int(R) <= ls[1]:
        k = str(ls[1])
        result.set(k)
    elif int(R) <= ls[2]:
        k = str(ls[2])
        result.set(k)
    elif int(R) <= ls[3]:
        k = str(ls[3])
        result.set(k)
    elif int(R) <= ls[4]:
        k = str(ls[4])
        result.set(k)
    elif int(R) >= ls[5]:
        k = str(ls[5])
        result.set(k)


l1 = Label(start, text="Welcome !", fg="Blue", font="bold 20", bg="skyblue")
l1.grid(row=1, column= 2,)
l3 = Label(start, text="Enter transmission Length (Km): ", bg="skyblue", anchor="nw")
l3.grid(row=2, column=1)
l4 = Label(start, text="Enter transmission Power (KVA): ", bg="skyblue", anchor="nw")
l4.grid(row=3, column=1)
l5 = Label(start, text="Suitable transmission Voltage is (Kv): ", bg="skyblue", anchor="nw")
l5.grid(row=4, column=1)
l6 = Label(start, bg = "white", fg = "blue", width = 15, textvariable = result, anchor="nw",font= "bold")
l6.grid(row=4, column=2)


Length = StringVar()
Power = StringVar()

E1 = Entry(start, textvariable=Length)
E1.grid(row=2, column=2)
E2 = Entry(start, textvariable=Power)
E2.grid(row=3, column=2)


B1 = Button(text="   Submit  ", fg="green", command=pr,)
B1.grid(row=6, column=2)
B2 = Button(text="Clear", fg="green", command=cl)
B2.grid(row=7, column=2,)

start.mainloop()


