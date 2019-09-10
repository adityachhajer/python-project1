import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("tiktik")


clk = True
def checker(buttons):
    global clk
    if buttons["text"]==" " and clk == True:
        buttons["text"] = "X"
        clk = False
    elif buttons["text"]==" " and clk == False:
        buttons["text"] = "O"
        clk = True

    if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or
        b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or
        b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" or
        b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or
        b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" or
        b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or
        b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or
        b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" ):
        messagebox.showinfo("winner X","u have just won a game")


    elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or
          b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or
          b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or
          b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or
          b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" or
          b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or
          b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or
          b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O"):
        messagebox.showinfo("winner O", "u have just won a game")


b1 = tk.Button(bd=10,width = 10,height = 2,text = " ",bg = "pink",fg = "white",activebackground = "yellow",activeforeground = "red", command = lambda:checker(b1))
b1.grid(row=0,column = 0)
b2 = tk.Button(bd=10,width = 10,height = 2,text = " ",bg = "pink",fg = "white",activebackground = "yellow",activeforeground = "red", command = lambda:checker(b2))
b2.grid(row=0,column = 1)

b3 = tk.Button(bd=10,width = 10,height = 2,text = " ",bg = "pink",fg = "white",activebackground = "yellow",activeforeground = "red", command = lambda:checker(b3))
b3.grid(row=0,column = 2)
b4 = tk.Button(bd=10,width = 10,height = 2,text = " ",bg = "pink",fg = "white",activebackground = "yellow",activeforeground = "red", command = lambda:checker(b4))
b4.grid(row=1,column = 0)

b5 = tk.Button(bd=10,width = 10,height = 2,text = " ",bg = "pink",fg = "white",activebackground = "yellow",activeforeground = "red", command = lambda:checker(b5))
b5.grid(row=1,column = 1)
b6 = tk.Button(bd=10,width = 10,height = 2,text = " ",bg = "pink",fg = "white",activebackground = "yellow",activeforeground = "red", command = lambda:checker(b6))
b6.grid(row=1,column = 2)

b7 = tk.Button(bd=10,width = 10,height = 2,text = " ",bg = "pink",fg = "white",activebackground = "yellow",activeforeground = "red", command = lambda:checker(b7))
b7.grid(row=2,column = 0)
b8 = tk.Button(bd=10,width = 10,height = 2,text = " ",bg = "pink",fg = "white",activebackground = "yellow",activeforeground = "red", command = lambda:checker(b8))
b8.grid(row=2,column = 1)

b9 = tk.Button(bd=10,width = 10,height = 2,text = " ",bg = "pink",fg = "white",activebackground = "yellow",activeforeground = "red", command = lambda:checker(b9))
b9.grid(row=2,column = 2)


root.mainloop()
