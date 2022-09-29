import tkinter
from tkinter import*
from tkinter import messagebox
from turtle import width
from itertools import cycle
import pymysql
import os
from os import walk
import logging
import subprocess
from subprocess import PIPE,Popen
import datetime
import webbrowser



def menu_pantalla():
    global pantalla
    pantalla=Tk ()
    pantalla.geometry("400x510")
    pantalla.title ("Bienvenido a Servicio de Salud")
    pantalla.iconbitmap("logoanto.ico")  #colocar un icono no olvidar

    
    barraMenu=Menu(pantalla)
    menuArchivo=Menu(barraMenu, tearoff=0)
    menuArchivo.add_command(label="bitacora usuario", command=acceso_bitacora)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Salir", command=pantalla.destroy)
    menuAyuda=Menu(barraMenu, tearoff=0)
    menuAyuda.add_command(label="manual de sistema", command=manual_sistema)
    menuAyuda.add_command(label="manual usuario", command=manual_usuario)
    barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
    barraMenu.add_cascade(label="Ayuda", menu=menuAyuda )
    
    pantalla.config(menu=barraMenu)
   


    image=PhotoImage(file="logoanto.gif")
    image=image.subsample(1,1)
    label=Label (image=image)
    label.pack()

    Label (text="acceso al sistema", bg="navy", fg="white", width ="300", height="3", font=("calibri", 15)) .pack()
    Label (text="").pack()

    Button (text="iniciar sesion", height="3", width="30", command=inicio_sesion ).pack()
    Label (text="").pack ()

    Button (text="Registrar usuario", height="3", width="30", command=registrar).pack()
    Label (text="").pack ()

    Button (text="Administrador", height="3", width="30", command=login_administrador).pack()

    pantalla.mainloop()

def manual_sistema():
    webbrowser.open_new("C:\Manual de Sistemas.pdf")

def manual_usuario():
    webbrowser.open_new("C:\Manual de usuario.pdf")
    
def acceso_bitacora():
    webbrowser.open_new("C:\bita.pdf")
    

def login_administrador ():
    global pantalla3
    pantalla3 = Toplevel(pantalla)
    pantalla3.geometry("400x480")
    pantalla3.title("inicio de sesion")
    pantalla3.iconbitmap("logoanto.ico")

    Label (pantalla3, text="ingresar usuario y contraseña Administrador", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)) .pack()
    Label (pantalla3, text="").pack()

    global adnombreusuario_verify
    global adcontrasenausuario_verify

    adnombreusuario_verify=StringVar()
    adcontrasenausuario_verify=StringVar()

    global adnombre_usuario_entry
    global adcontrasena_usuario_entry

    Label (pantalla3, text="usuario").pack()
    adnombre_usuario_entry=Entry(pantalla3, textvariable=adnombreusuario_verify)
    adnombre_usuario_entry.pack()
    Label(pantalla3).pack()

    Label (pantalla3, text="contraseña").pack()
    adcontrasena_usuario_entry=Entry(pantalla3, show="*", textvariable=adcontrasenausuario_verify)
    adcontrasena_usuario_entry.pack()
    Label(pantalla3).pack()

    Button(pantalla3, text="iniciar sesion", command=validacion_datos2).pack()    
                      
    


def inicio_sesion ():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x480")
    pantalla1.title("inicio de sesion")
    pantalla1.iconbitmap("logoanto.ico")

    Label (pantalla1, text="ingresar usuario y contraseña", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)) .pack()
    Label (pantalla1, text="").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label (pantalla1, text="usuario").pack()
    nombre_usuario_entry=Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label (pantalla1, text="contraseña").pack()
    contrasena_usuario_entry=Entry(pantalla1, show="*", textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="iniciar sesion", command=validacion_datos).pack()
    

def registrar():
    global pantalla2
    global pantalla3
    pantalla2 = Toplevel(pantalla)
    pantalla2.geometry("400x480")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("logoanto.ico")
    
    global nombreusuario_entry
    global contrasena_entry
    global rutusuario_entry
    
    nombreusuario_entry= StringVar()
    contrasena_entry=StringVar()
    rutusuario_entry=StringVar()

    Label (pantalla2, text="Ingresar Usuario Nuevo \n  ", bg="navy", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label (pantalla2, text="").pack()

    Label (pantalla2, text="Nombre Completo").pack()
    nombreusuario_entry =Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label (pantalla2, text="Rut").pack()
    rutusuario_entry =Entry(pantalla2)
    rutusuario_entry.pack()
    Label(pantalla2).pack()

    Label (pantalla2, text="contraseña").pack()
    contrasena_entry =Entry(pantalla2, show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar", command=inserta_datos).pack()
    Button(pantalla2, text="Eliminar",  command=eliminar).pack()
    Button(pantalla2, text="Editar a traves del rut",  command=actualizar).pack()
    Button(pantalla2, text="backup", command=backup_cmd).pack()
    Button(pantalla2, text="Restaurar backup", command=restaurar_backup).pack()
    
def backup_cmd():
    os.system("cmd--mysqldump---h localhost ---u root --base_de_datos_gestorSSA-->C:\respaldo\nuevo3.sql")
    
def restaurar_backup():
    os.system('cmd')
    

def eliminar ():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="base_de_datos_gestorSSA"
        )
    fcursor=bd.cursor()
            
    sql="DELETE FROM login WHERE usuario='"+nombreusuario_entry.get()+"'"

    try:
        fcursor.execute(sql)
        bd.commit() 
        messagebox.showinfo(message="borrado Exitoso", title="Aviso")
   
    except:
        bd.rollback()
        messagebox.showinfo(message="No eliminado", title="Aviso")

    bd.close()

def actualizar():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="base_de_datos_gestorSSA"
        )
    fcursor=bd.cursor()
            
    sql="UPDATE login SET usuario='"+nombreusuario_entry.get()+"' WHERE rut='"+rutusuario_entry.get()+"'"

    try:
        fcursor.execute(sql)
        bd.commit()
        nombreusuario_entry.delete(0, 'end')
        bitacora()
        messagebox.showinfo(message="Actualizacion Exitosa", title="Aviso")
        
    except:
        bd.rollback()
        messagebox.showinfo(message=" No Actualizada", title="Aviso")

    bd.close()


def inserta_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="base_de_datos_gestorSSA"
        )
    fcursor=bd.cursor()
            
    sql="INSERT INTO login (usuario, rut, contrasena) VALUES ('{0}', '{1}', '{2}')". format(nombreusuario_entry.get(), rutusuario_entry.get(), contrasena_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        bitacora()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
   
    except:
        bd.rollback()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")

    bd.close()

def validacion_datos():
        bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="base_de_datos_gestorSSA"    
        )
        fcursor=bd.cursor()
    
        fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreusuario_verify.get()+"' and contrasena='"+contrasenausuario_verify.get()+"'")
        if  fcursor.fetchall():
             messagebox.showinfo(title="inicio de sesion correcto", message="Usuario y Contraseña correcta")
        else:
             messagebox.showinfo(title="inicio de sesion incorrecto", message="Usuario y Contraseña incorrecta")

        bd.close()
        
def validacion_datos2():
        bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="base_de_datos_gestorSSA"    
        )
        fcursor=bd.cursor()
    
        fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+adnombreusuario_verify.get()+"' and contrasena='"+adcontrasenausuario_verify.get()+"'")
        if  fcursor.fetchall():
             messagebox.showinfo(title="inicio de sesion correcto", message="Usuario y Contraseña administrador correcta")
        else:
             messagebox.showinfo(title="inicio de sesion incorrecto", message="Usuario y Contraseña administrador incorrecta")

        bd.close()
    
menu_pantalla()
