import tkinter as tk
from tkinter import messagebox  

def on_click_gmail(event):
    if entrada_gmail.get() == "g-mail":
        entrada_gmail.delete(0, tk.END)
        entrada_gmail.config(fg="blue")

def on_leave_gmail(event):
    if entrada_gmail.get() == "":
        entrada_gmail.insert(0, "g-mail")
        entrada_gmail.config(fg="blue")

def on_click_senha(event):
    if entrada_senha.get() == "senha":
        entrada_senha.delete(0, tk.END)
        entrada_senha.config(fg="black", show="*")

def on_leave_senha(event):
    if entrada_senha.get() == "":
        entrada_senha.config(show="")
        entrada_senha.insert(0, "senha")
        entrada_senha.config(fg="gray")

def abrir_proxima_pagina():

    gmail_digitado = entrada_gmail.get()
    senha_digitada = entrada_senha.get()
    
    gmail_correto = "caiogay@gmail.com"
    senha_correta = "512137"
    

    if gmail_digitado == gmail_correto and senha_digitada == senha_correta:
        
        
        entrada_gmail.delete(0, tk.END)
        entrada_gmail.insert(0, "g-mail:")
        entrada_gmail.config(fg="blue")
        
        entrada_senha.delete(0, tk.END)
        entrada_senha.config(show="")
        entrada_senha.insert(0, "senha:")
        entrada_senha.config(fg="blue")
        
        janela.focus()

      
        nova_janela = tk.Toplevel(janela)
        nova_janela.geometry("600x400")
        nova_janela.title("Nova Página")
        nova_janela.configure(bg="black")
        
        tk.Label(nova_janela, text="Bem-vindo ao sistema!", font=("Arial", 20, "bold"), bg="white", fg="green").pack(pady=150)
        
    else:
        messagebox.showerror("Erro de Login", "G-mail ou senha incorretos. Tente novamente.")


janela = tk.Tk()
janela.geometry("1920x1080")
janela.configure(bg="white")

minha_imagem = tk.PhotoImage(file="image 1.png")  
label_imagem = tk.Label(janela, image=minha_imagem, bg="white")
label_imagem.image = minha_imagem  
label_imagem.pack(pady=(100, 40))

entrada_gmail = tk.Entry(janela, font=("Arial", 16), bg="#7A7575", fg="white", relief="flat", justify="left", width=45)
entrada_gmail.insert(0, "g-mail")
entrada_gmail.pack(pady=10, ipady=20)
entrada_gmail.bind("<FocusIn>", on_click_gmail)
entrada_gmail.bind("<FocusOut>", on_leave_gmail)

entrada_senha = tk.Entry(janela, font=("Arial", 16), bg="#7A7575", fg="white", relief="flat", justify="left", width=45)
entrada_senha.insert(0, "senha")
entrada_senha.pack(pady=10, ipady=20)
entrada_senha.bind("<FocusIn>", on_click_senha)
entrada_senha.bind("<FocusOut>", on_leave_senha)

botao_acessar = tk.Button(janela, text="ACESSAR", font=("Arial", 14, "bold"), bg="#005B90", fg="white", relief="flat", width=32, command=abrir_proxima_pagina)
botao_acessar.pack(pady=20, ipady=20)

janela.focus()
janela.mainloop()