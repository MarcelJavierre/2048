# Variável do módulo sys para verificar qual sistema operacional está executando o código
from sys import platform

# Função do módulo os para utilizar comandos do terminal
from os import system

class FerramentasDeInterfaceComOUsuario:
    '''Super classe com os métodos genéricos associados com a comunicação com o usuário.'''

    def __init__(self):
        '''
        Método construtor.
        self -> none
        '''

        # Conjunto com todos os atributos da classe
        self.__atributos = {
            'self.__atributos',
            'self.__metodos'
        }

        # Conjunto com todos os métodos da classe
        self.__metodos = {
            '__init__',
            '__str__',
            'getAtributos',
            'getMetodos',
            'manual',
            'entradaDoUsuario',
            'limpaTela'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com todos os atributos e métodos da classe.
        self -> str
        '''

        string = f'Classe ferramentasDeInterfaceComOUsuario:\n{FerramentasDeInterfaceComOUsuario.__doc__}\n\nAtributos:\n'

        # Passa por todos os atributos e insere na string
        for i in self.__atributos:
            string += '\t' + i + ': ' + self.manual()[i] + '\n'

        string += '\nMétodos:\n'

        # Passa por todos os métodos e insere na string
        for i in self.__metodos:
            string += '\t' + i + ': ' + self.manual()[i] + '\n'

        return string

    def getAtributos(self):
        '''
        Método que retorna o conjunto com todos os atributos da classe.
        self -> set
        '''
        return self.__atributos

    def getMetodos(self):
        '''
        Método que retorna o conjunto com todos os métodos da classe.
        self -> set
        '''
        return self.__metodos

    def manual(self):
        '''
        Método que retorna um dicionário com todos os atributos e métodos da classe com suas respectivas documentações.
        self -> dict
        '''
        return {
            'self.__atributos': 'Conjunto com todos os atributos da classe.',
            'self.__metodos': 'Conjunto com todos os métodos da classe.',
            '__init__': self.__init__.__doc__,
            '__str__': self.__str__.__doc__,
            'getAtributos': self.getAtributos.__doc__,
            'getMetodos': self.getMetodos.__doc__,
            'manual': self.manual.__doc__,
            'entradaDoUsuario': self.entradaDoUsuario.__doc__,
            'limpaTela': self.limpaTela.__doc__
        }

    def entradaDoUsuario(self):
        '''
        Método para receber o comando do usuário.
        self -> str
        '''
        return input()

    def limpaTela(self):
        '''
        Método para limpar a tela do terminal.
        self -> none
        '''

        # Verifica qual é o sistema operacional executando o código
        # Se for windows, utiliza o comando cls para limpar a tela
        if platform == 'win32':
            system('cls')

        # Se for linux, utiliza o comando clear
        elif platform == 'linux':
            system('clear')

        # Se não for nenhum dos dois, não faz nada
        else:
            pass