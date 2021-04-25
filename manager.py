import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import random
from tkinter import scrolledtext as st

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

# ---------------------------- UI ------------------------------- #
raiz=Tk()
raiz.title("Manager")
raiz.geometry("450x350")
raiz.resizable(False,False)
#Página de Registro
ventana=Toplevel()
ventana.geometry("450x350")
ventana.title("Manager")
ventana.resizable(False,False)

Label(ventana, text="Bienvenido", bg='#a6d4f2', font=("Cambria", 20), width = "500", height = "4").pack()

Label(ventana, text ="Usuario :").pack()
caja1=Entry(ventana)
caja1.pack()
Label(ventana, text="Contraseña :").pack()
caja2=Entry(ventana, show="*")
caja2.pack()


db=sqlite3.connect("mdp.db")


try:
    db.execute("""create table usuarios (
                              Nombre text,
                              Apellidos text,
                              Email text,
                              Usuario text,
                              Pass text
                        )""")
    print("se creo la tabla usuarios")                        
except sqlite3.OperationalError:
    print("La tabla usuarios ya existe")                    
db.commit()

c=db.cursor()

def login():
     usuario=caja1.get()
     contr=caja2.get()
     c.execute("SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?", (usuario, contr))
     if c.fetchall():
          mb.showinfo(title="Login Correcto", message="Usuario y contraseña correctos")
          raiz.deiconify()
          ventana.destroy()
     else:
          mb.showinfo(title="Usuario o contraseña incorrecto", message="Porfavor vuelva a intentarlo")


def newventana():
     newventana=Toplevel(ventana)
     newventana.title("Registro de Usuario")
     newventana.geometry("400x320")
     newventana.resizable(False, False)
     Label(newventana, text="Nombre :").pack()
     caja3=Entry(newventana)
     caja3.pack()
     Label(newventana, text="Apellidos :").pack()
     caja4=Entry(newventana)
     caja4.pack()
     Label(newventana, text="Email :").pack()
     caja5=Entry(newventana)
     caja5.pack()
     Label(newventana, text="Usuario :").pack()
     caja6=Entry(newventana)
     caja6.pack()
     Label(newventana, text="Contraseña :").pack()
     caja7=Entry(newventana, show="*")
     caja7.pack()
     Label(newventana, text="Repita la Contraseña :").pack()
     caja8=Entry(newventana, show="*")
     caja8.pack()


     def registro():
          Nombre=caja3.get()
          Apellidos=caja4.get()
          Email=caja5.get()
          Usr_reg=caja6.get()
          Contra_reg=caja7.get()
          Contra_reg2=caja8.get()
          if(Contra_reg==Contra_reg2):
               c.execute("INSERT INTO usuarios values(\'"+Nombre+"\',\'"+Apellidos+"\',\'"+Email+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
               db.commit()
               mb.showinfo(title="Registro Correcto",message="!!Hola "+Usr_reg+" ¡¡ \nSu registro fue exitoso.")
               newventana.destroy()
          else:
               mb.showerror(title="Contraseña Incorrecta",message="!!!Error¡¡¡ \nLas contraseñas no coinciden.")
     buttons=tk.Button(newventana, text="Registrarse",bg='#a6d4f2', command=registro, font=("Arial Rounded MT Bold",10)).pack(side="bottom")


Label(ventana,text=" ").pack()
Button(ventana, text=" ENTRAR ",command=login,bg='#a6d4f2',font=("Arial Rounded MT Bold",10)).pack()
Label(ventana,text=" ").pack()
Label(ventana,text="¿No tienes una cuenta?  ").pack()
boton1=Button(ventana,text="REGÍSTRATE AQUÍ",bg='#a6d4f2',command=newventana,font=("Arial Rounded MT Bold",10)).pack()



#Página principal
pestañas=ttk.Notebook(raiz)

PassManager=ttk.Frame(pestañas)
pestañas.add(PassManager, text="PassManager")

motdb=sqlite3.connect("mdp.db")


try:
    db.execute("""create table mots (
                              Web text,
                              Usuario text,
                              Email text,
                              Pass text
                        )""")
    print("se creo la tabla mots")                        
except sqlite3.OperationalError:
    print("La tabla mots ya existe")  
motdb.cursor()
# ---------------------------- save pass ------------------------------- #
def save():
     website = website_entry.get()
     user = user_entry.get()
     email = email_entry.get()
     password = password_entry.get()

     if len(website) == 0 or len(password) == 0:
          mb.showinfo(title="Oops", message="Please make sure that each and every field is filled up")
     else:
          is_ok = mb.askokcancel(title=website, message=f"These are the details entered : \nEmail: {email} \nPassword: {password} \nAre you sure you want to save this? " )

     if is_ok:
          motdb.execute("INSERT INTO mots values(\'"+website+"\',\'"+user+"\',\'"+email+"\',\'"+password+"')")
          motdb.commit()
          mb.showinfo(title="Registro Correcto",message="Guardado correctamente")
          website_entry.delete(0, END)
          user_entry.delete(0, END)
          email_entry.delete(0, END)
          password_entry.delete(0, END)

# ---------------------------- UI ------------------------------- #
passgen_frame = LabelFrame(PassManager, text="Record")
passgen_frame.pack(fill="both", expand="yes", padx=20)

# labels
website_label = Label(passgen_frame, text="Website :")
website_label.grid(row=1, column=0, padx=10, pady=10)
user_label = Label(passgen_frame, text="User :")
user_label.grid(row=2, column=0, padx=10, pady=10)
email_label = Label(passgen_frame, text="Email :")
email_label.grid(row=3, column=0, padx=10, pady=10)
password_label = Label(passgen_frame, text="Password :")
password_label.grid(row=4, column=0, padx=10, pady=10)

# Entries
website_entry = Entry(passgen_frame, width=53)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
user_entry = Entry(passgen_frame, width=53)
user_entry.grid(row=2, column=1, columnspan=2)
email_entry = Entry(passgen_frame, width=53)
email_entry.grid(row=3, column=1, columnspan=2)
password_entry = Entry(passgen_frame, width=35)
password_entry.grid(row=4, column=1)

# Buttons
generate_password = Button(passgen_frame, text="Generate Password", width=14, command=generate_password)
generate_password.grid(row=4, column=2)
add_button = Button(passgen_frame, text="Add", width=36, command=save)
add_button.grid(row=5, column=1, columnspan=2)

def consulta(datos):
     try:
          cone= sqlite3.connect("mdp.db")
          cursor=cone.cursor()
          sql="select Usuario, Email, Pass from mots where Web=?"
          cursor.execute(sql, datos)
          return cursor.fetchall()
     finally:
          cone.close()


def consultar():
     datos=(web.get(), )
     respuesta=consulta(datos)
     if len(respuesta)>0:
          email.set(respuesta[0][1])
          user.set(respuesta[0][0])
          password.set(respuesta[0][2])
     else:
          email.set('')
          user.set('')
          password.set('')
          mb.showinfo("Información", "No existe un usuario o mail para esta web")


busqueda=ttk.Frame(pestañas)
pestañas.add(busqueda, text="Búsqueda Única")

wrappframe = ttk.LabelFrame(busqueda)
wrappframe.grid(sticky="nsew")

labelframe2=ttk.LabelFrame(wrappframe, text="Información")
labelframe2.grid(column=0, row=0, padx=5, pady=10)

label1=ttk.Label(labelframe2, text="Web:")
label1.grid(column=0, row=0, padx=4, pady=4)
web=tk.StringVar()
entryweb=ttk.Entry(labelframe2, textvariable=web)
entryweb.grid(column=1, row=0, padx=4, pady=4)

label2=ttk.Label(labelframe2, text="Email:")        
label2.grid(column=0, row=1, padx=4, pady=4)
email=tk.StringVar()
entryemail=ttk.Entry(labelframe2, textvariable=email, state="readonly")
entryemail.grid(column=1, row=1, padx=4, pady=4)

label3=ttk.Label(labelframe2, text="User:")        
label3.grid(column=0, row=2, padx=4, pady=4)
user=tk.StringVar()
entryuser=ttk.Entry(labelframe2, textvariable=user, state="readonly")
entryuser.grid(column=1, row=2, padx=4, pady=4)

label4=ttk.Label(labelframe2, text="Password:")        
label4.grid(column=0, row=3, padx=4, pady=4)
password=tk.StringVar()
entrypassword=ttk.Entry(labelframe2, textvariable=password, state="readonly")
entrypassword.grid(column=1, row=3, padx=4, pady=4)

boton1=ttk.Button(labelframe2, text="Consultar", command=consultar)
boton1.grid(column=1, row=4, padx=4, pady=4)



def update():
     website = entry_mod_web.get()
     user = entry_mod_user.get()
     email = entry_mod_email.get()
     password = entry_mod_password.get()

     
     cone= sqlite3.connect("mdp.db")
     cursor=cone.cursor()
     cursor.execute("UPDATE mots SET Usuario=?, Email=?, Pass=? WHERE Web=?",(user, email, password, website))
     cone.commit()
     cone.close()
     # Output Messages 
     mb.showinfo("Modificación", "Se ha modificado correctamente el usuario")
     entry_mod_web.delete(0, END)
     entry_mod_user.delete(0, END)
     entry_mod_email.delete(0, END)
     entry_mod_password.delete(0, END)

labelframe3=ttk.LabelFrame(wrappframe, text="Modificar")
labelframe3.grid(column=1, row=0, padx=5, pady=10)

label_mod_1=ttk.Label(labelframe3, text="Web:")
label_mod_1.grid(column=1, row=0, padx=4, pady=4)

entry_mod_web=ttk.Entry(labelframe3, textvariable=web)
entry_mod_web.grid(column=2, row=0, padx=4, pady=4)

label_mod_2=ttk.Label(labelframe3, text="Email:")        
label_mod_2.grid(column=1, row=1, padx=4, pady=4)

entry_mod_email=ttk.Entry(labelframe3, textvariable=email)
entry_mod_email.grid(column=2, row=1, padx=4, pady=4)

label_mod_3=ttk.Label(labelframe3, text="User:")        
label_mod_3.grid(column=1, row=2, padx=4, pady=4)

entry_mod_user=ttk.Entry(labelframe3, textvariable=user)
entry_mod_user.grid(column=2, row=2, padx=4, pady=4)

label_mod_4=ttk.Label(labelframe3, text="Password:")        
label_mod_4.grid(column=1, row=3, padx=4, pady=4)

entry_mod_password=ttk.Entry(labelframe3, textvariable=password)
entry_mod_password.grid(column=2, row=3, padx=4, pady=4)

boton_mod=ttk.Button(labelframe3, text="Editar", command=update)
boton_mod.grid(column=2, row=4, padx=4, pady=4)

def delete():
     website = website_entry.get()

     cone= sqlite3.connect("mdp.db")
     cursor=cone.cursor()
     cursor.execute("DELETE from mots WHERE Web= "+ website_entry.get())
     cone.commit()
     cone.close()
     # Output Messages 
     mb.showinfo("Eliminación", "Se ha eliminado correctamente el usuario")
     website_entry.delete(0, END)
     user_entry.delete(0, END)
     email_entry.delete(0, END)
     password_entry.delete(0, END)


delete_button = Button(wrappframe, text="Borrar", width=50, command=delete)
delete_button.grid(row=5, column=0, columnspan=2,padx=4, pady=4)






informacion=ttk.Frame(pestañas)
pestañas.add(informacion, text="Información")

def recuperar_todos():
     try:
          cone = sqlite3.connect("mdp.db")
          cursor=cone.cursor()
          sql="select Web, Usuario, Email, Pass from mots"
          cursor.execute(sql)
          return cursor.fetchall()
     finally:
          cone.close()

def listar():
     respuesta=recuperar_todos()
     scrolledtext1.delete("1.0", tk.END)        
     for fila in respuesta:
          scrolledtext1.insert(tk.END, "web: "+str(fila[0])+"\nusuario: "+fila[1]+"\nemail: "+str(fila[2])+"\npass: "+fila[3]+"\n\n")
          #scrolledtext1.configure(state ='disabled')

pag_info = ttk.LabelFrame(informacion, text="Información")
pag_info.grid(column=0, row=0, padx=5, pady=10)
boton1=ttk.Button(pag_info, text="Listado completo", command=listar)
boton1.grid(column=0, row=0, padx=4, pady=4)
scrolledtext1=st.ScrolledText(pag_info, width=30, height=10, font = ("Times New Roman",15))
scrolledtext1.grid(column=0,row=1, padx=10, pady=10)






pestañas.pack()
raiz.withdraw()
raiz.mainloop()