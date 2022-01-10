# Importando a super classe com os métodos genéricos associados com a comunicação com o usuário
from ferramentasDeInterfaceComOUsuario import *

# Classe da seção interface com o usuário
class interfaceComOUsuario(ferramentasDeInterfaceComOUsuario):
    '''Classe responsável por toda a interação com o usuário. Tudo que é pedido ao usuário ou mostrado para ele é função desta classe.'''

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
            'limpaTela',
            'menuPrincipal',
            'telaDePause',
            'telaDeSalvamentoCarregamento',
            'telaDeOpcoes',
            'telaDoManual',
            'telaDasEstatisticas',
            'telaDoTabuleiro',
            'telaDeFimDeJogo'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com todos os atributos e métodos da classe.
        self -> str
        '''

        string = f'Classe interfaceComOUsuario:\n{interfaceComOUsuario.__doc__}\n\nAtributos:\n'

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
            'limpaTela': self.limpaTela.__doc__,
            'menuPrincipal': self.menuPrincipal.__doc__,
            'telaDePause': self.telaDePause.__doc__,
            'telaDeSalvamentoCarregamento': self.telaDeSalvamentoCarregamento.__doc__,
            'telaDeOpcoes': self.telaDeOpcoes.__doc__,
            'telaDoManual': self.telaDoManual.__doc__,
            'telaDasEstatisticas': self.telaDasEstatisticas.__doc__,
            'telaDoTabuleiro': self.telaDoTabuleiro.__doc__,
            'telaDeFimDeJogo': self.telaDeFimDeJogo.__doc__
        }

    def menuPrincipal(self):
        '''
        Método para exibir ao usuário o menu principal do jogo.
        self -> none
        '''
        pass

    def telaDePause(self):
        '''
        Método para exibir ao usuário a tela de pause do jogo.
        self -> none
        '''
        pass

    def telaDeSalvamentoCarregamento(self):
        '''
        Método para exibir ao usuário a tela de salvamento/carregamento do jogo.
        self -> none
        '''
        pass

    def telaDeOpcoes(self):
        '''
        Método para exibir ao usuário a tela de opções do jogo.
        self -> none
        '''
        pass

    def telaDoManual(self):
        '''
        Método para exibir ao usuário a tela do manual do jogo.
        self -> none
        '''
        pass

    def telaDasEstatisticas(self):
        '''
        Método para exibir ao usuário a tela de estatísticas do jogo.
        self -> none
        '''
        pass

    def telaDoTabuleiro(self, matrizDoTabuleiro, score):
        '''
        Método para exibir a tela do tabuleiro do jogo.
        self,list,int -> none
        '''
        pass

    def telaDeFimDeJogo(self, foiVencedor, score):
        '''
        Método para exibir a tela de fim de jogo.
        self,bool,int -> none
        '''

        # Se foi vencedor, exibe a tela de vencedor
        if foiVencedor == True:
            pass

        # Se não, exibe a tela de perdedor
        else:
            pass