# Módulo da biblioteca sys para verificar qual sistema operacional está executando o código
from sys import platform
# Módulo da biblioteca os para utilizar comandos do terminal
from os import system

class ferramentasDeInterfaceComOUsuario:
    '''Super classe com os métodos genéricos associados com a comunicação com o usuário.'''

    def entradaDoUsuario(self):
        '''
        Método para receber o comando do usuário.
        self -> none
        '''
        pass

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