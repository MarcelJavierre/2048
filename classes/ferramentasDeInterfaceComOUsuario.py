# Importando a variável "platform" do módulo "sys" que indica qual sistema operacional está executando o código
from sys import platform

# Importando a função "system" do módulo "os" que permite utilizar comandos do terminal
from os import system

# Importando a função "sleep" do módulo "time" que pausa a execução do código por um dado tempo
from time import sleep

# Importando o módulo "tkinter"
from tkinter import *

class FerramentasDeInterfaceComOUsuario:
    '''
    Super classe com os métodos genéricos associados com a comunicação
    com o usuário.
    '''

    def __init__(self):
        '''
        Método construtor.

        Self -> None
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
            'limpaTela',
            'pausa',
            'mudaCorDeFundoDoBotao'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com
        todos os atributos e métodos da classe.

        Self -> str
        '''

        string = f'Classe FerramentasDeInterfaceComOUsuario:\n{FerramentasDeInterfaceComOUsuario.__doc__}\n\nAtributos:\n'

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

        Self -> set[str]
        '''
        return self.__atributos

    def getMetodos(self):
        '''
        Método que retorna o conjunto com todos os métodos da classe.

        Self -> set[str]
        '''
        return self.__metodos

    def manual(self):
        '''
        Método que retorna um dicionário com todos os atributos e
        métodos da classe com suas respectivas documentações.

        Self -> dict[str]
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
            'limpaTela': self.limpaTela.__doc__,
            'pausa': self.pausa.__doc__,
            'mudaCorDeFundoDoBotao': self.mudaCorDeFundoDoBotao.__doc__
        }

    def entradaDoUsuario(self, mensagem = ''):
        '''
        Método para receber o comando do usuário. Retorna uma string com
        a entrada do usuário.

        Self, str -> str
        '''
        return input(mensagem)

    def limpaTela(self, tela):
        '''
        Método para limpar a tela.

        Self, tkinter.Tk -> None
        '''
        # Verifica quais componentes estão na tela
        for componente in tela.winfo_children():
            # Esquece os componentes na tela
            componente.grid_forget()

    def pausa(self, tempo):
        '''
        Método para pausar a execução do código por um dado tempo em
        segundos.

        Self, float -> None
        '''
        sleep(tempo)

    def mudaCorDeFundoDoBotao(self, evento, botao, cor):
        '''
        Método que altera a cor do fundo botão passado.

        Self, tkinter.Event, tkinter.Button, str -> None
        '''
        botao['bg'] = cor
