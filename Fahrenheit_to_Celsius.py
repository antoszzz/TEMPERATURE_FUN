import tkinter as tk
from tkinter import filedialog
from tkinter.constants import *
import sys

def conv_FC(Far:str):
    Far = Far.replace(',','.')
    if not Far.replace('.','',1).isdigit():
        tk.messagebox.showinfo(title=None,message='Can work only with numbers' )
        return 
    Tf = float(Far)
    Tc = (Tf-32)*5/9
    info_box_C.delete(0,END)
    info_box_C.insert(0,Tc)
    return 
def conv_CF(Far:str):
    Far = Far.replace(',','.')
    if not Far.replace('.','',1).isdigit():
        tk.messagebox.showinfo(title=None,message='Can work only with numbers' )
        return 
    Tf = float(Far)
    Tc = Tf*9/5+32
    info_box_F.delete(0,END)
    info_box_F.insert(0,Tc)
    return 
def choose_action():
    if info_box_F.get()=='':
        conv_CF(info_box_C.get())
    else:
        conv_FC(info_box_F.get())

def close():
    a= tk.messagebox.askyesno(title=None,message='Do you wanna exit?')
    if a: sys.exit()
    return

#def main():
root=tk.Tk()
root.title("FARHNHEIT - CELCIUS CONVERTER")
root.geometry('250x150')
lbl_Tf = tk.Label(root,text='Temperature in Fahrenheits:')
lbl_Tf.grid(column=0,row=0, sticky="SW")
info_box_F = tk.Entry(root,width=20)
info_box_F.grid(column=0,row=1)
lbl_Tf = tk.Label(root,text='Temperature in Celsiuses:')
lbl_Tf.grid(column=0,row=2, sticky="SW")
info_box_C = tk.Entry(root,width=20)
info_box_C.grid(column=0,row=3)
f_rame = tk.Frame(root)
f_rame.grid(column=1,row = 2, sticky="NE")
b_start = tk.Button(f_rame,text='Convert',command=lambda: choose_action())
b_start.grid(column=0,row=0,ipadx=15)
b_exit = tk.Button(f_rame,text='Exit', command =lambda: close())
b_exit.grid(column=0,row=1,ipadx=25,pady=5)
#temp = input('Put the temperature in Fahrenheits\n')
#print(f'The temperature in Celcius:{conv_FC(temp)}')
root.mainloop()

#if __name__=='__main__':main()