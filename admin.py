from tkinter import *
from tkinter.ttk import *
from tkinter import font
import movieDB
import tkinter as tk
import chart 


class adminView(tk.Tk):
    def info(self):
            us1 = self.e.get()
            ps2 = self.f.get()
            return us1+"\n"+ps2
            print("args"+us1+ps2)
            
    def on_button(self):
        validate(self)
           
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Login")
        self.configure(background=('cornsilk'))
        self.height = 100
        self.width = 100
        self.a = tk.Label(self ,text="username",foreground="blue",background="cornsilk").grid(row=0,column = 0)
        self.b = tk.Label(self ,text="password",foreground="blue",background="cornsilk").grid(row=1,column=0)
        
        self.e = tk.Entry(self)
        self.e.grid(row=0,column=1)
        self.f = tk.Entry(self,show='*')
        self.f.grid(row=1,column=1)
 #       self.e.pack()
 #      self.f.pack()
        self.c = tk.Button(self,command=self.on_button,text="LOGIN")
        self.c.grid(row=2,column=0)
 #       self.c.bind('<Button-1>',on_button)
        
        


def validate(gui):
    string = gui.info()
    us1 = string.split("\n")[0]
    ps2 = string.split("\n")[1]
    if us1== "admin" and ps2=="password":
        i=Label(gui,text='Login success').grid(row=6,column=0)
        char = chart.chart()
        gui.destroy()
        gui.quit()
        print("login success")
    else:
        print("wrong password")
        j=Label(gui,text='Login failed').grid(row=6,column=0)
                
         

    


