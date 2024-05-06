import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.title("LOGIN")
window.geometry("800x500")
window.configure(background="#59FBAC")
window.resizable(False, False)

def mensaje():
    
    usuario = Usuario_entrada.get() 
    
    contraseña = Contraseña_entrada.get() 
    
    if Usuario_entrada.get() == Contraseña_entrada.get() :  
        messagebox.showinfo("LOGIN", "Bienvenido")
    else:
        messagebox.showerror("LOGIN", "Usuario o contraseña incorrectos")

imagen = tk.PhotoImage(file="bienvenido.png")
imagen = imagen.subsample(2)
imagen_l = tk.Label(image=imagen)
imagen_l.place(x=-30,y=1)
imagen_l.pack

Login = tk.Label(text="Sign In",font=("Arial",20))
Login.place(x=585, y=115)

Usuario = tk.Label(text="User",font=("Arial",15))
Usuario.place(x=607, y=165)
Usuario_entrada = tk.Entry()
Usuario_entrada.place(x=567, y=200)

Contraseña = tk.Label(text="Password",font=("Arial",15),)
Contraseña.place(x=584, y=230)
Contraseña_entrada = tk.Entry()
Contraseña_entrada.place(x=567, y=265)

login = tk.Button(text="Get In",font=("Arial",15), command=mensaje) 
login.place(x=595, y=295)

tk.mainloop()