# Classe contato
class Contato:
    # Construtor completo
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    # Métodos get/set
    def set_nome(self,nome):
        self.__nome = nome
    def set_telefone(self,telefone):
        self.__telefone = telefone
    def set_email(self,email):
        self.__email = email
    def get_nome(self):
        return self.__nome
    def get_telefone(self):
        return self.__telefone
    def get_email(self):
        return self.__email

    # Método __str__ para imprimir um contato
    def __str__(self):
        return f"Nome: {self.__nome}, Telefone: {self.__telefone}, Email: {self.__email}"

# Lista telefonica composta por uma coleçao de objetos contato
class ListaTelefonica:
    # Construtor completo
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        return self.contatos

    def excluir_contato(self, nome):
        for contato in self.contatos:
            if contato.get_nome() == nome:
                self.contatos.remove(contato)
                return True
        return False
