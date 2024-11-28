import tkinter as tk
from tkinter import messagebox
from contatos import Contato, ListaTelefonica

# Instanciando a lista telefônica
lista_telefonica = ListaTelefonica()

# Classe da interface
class Aplicativo:
    # Construtor completo (iniciando a janela)
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Lista Telefônica")
        self.janela.geometry("385x420")

        # Labels
        self.label_nome = tk.Label(janela, text="Nome:", font=('Arial',15))
        self.label_nome.grid(row=0, column=0, sticky="w", padx=15, pady=5)
        
        self.label_telefone = tk.Label(janela, text="Telefone:", font=('Arial',15))
        self.label_telefone.grid(row=1, column=0, sticky="w", padx=15, pady=5)
        
        self.label_email = tk.Label(janela, text="Email:", font=('Arial',15))
        self.label_email.grid(row=2, column=0, sticky="w", padx=15, pady=5)

        # Entrys
        self.entry_nome = tk.Entry(janela, font=('Arial',15))
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)
        
        self.entry_telefone = tk.Entry(janela, font=('Arial',15))
        self.entry_telefone.grid(row=1, column=1, padx=10, pady=5)
        
        self.entry_email = tk.Entry(janela, font=('Arial',15))
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        self.button_adicionar = tk.Button(janela, text="Adicionar Contato", font=('Arial',15), command=self.adicionar_contato)
        self.button_adicionar.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_excluir = tk.Button(janela, text="Excluir Contato", font=('Arial',15), command=self.excluir_contato)
        self.button_excluir.grid(row=5, column=0, columnspan=2, pady=5)

        # Listbox
        self.lst = tk.Listbox(janela, width=40, height=10)
        self.lst.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Método para adiconar contatos
    def adicionar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()

        if nome and telefone and email:
            novo_contato = Contato(nome, telefone, email)
            lista_telefonica.adicionar_contato(novo_contato)
            messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
            self.limpar_campos()
            self.listar_contatos()  # Atualiza a lista
        else:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")

    # Método para listar contatos
    def listar_contatos(self):
        contatos = lista_telefonica.listar_contatos()
        self.lst.delete(0, tk.END)  # Limpa a lista

        if contatos:
            for contato in contatos:
                self.lst.insert(tk.END, str(contato) + "\n")
        else:
            self.lst.insert(tk.END, "Nenhum contato encontrado.")

    # Método para excluir um contato
    def excluir_contato(self):
        nome = self.entry_nome.get()

        if nome:
            if lista_telefonica.excluir_contato(nome):
                messagebox.showinfo("Sucesso", f"Contato {nome} excluído com sucesso!")
                self.limpar_campos()
                self.listar_contatos()  # Atualiza a lista
            else:
                messagebox.showwarning("Aviso", f"Contato {nome} não encontrado.")
        else:
            messagebox.showwarning("Aviso", "Digite o nome do contato a ser excluído.")

    # Método para limpar os campos
    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

# Criação da janela principal
janela = tk.Tk()
app = Aplicativo(janela)

# Iniciar o loop da interface gráfica
janela.mainloop()
