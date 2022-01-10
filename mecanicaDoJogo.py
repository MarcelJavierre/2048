# Importando a super classe com os métodos genéricos associados com a mecânica do jogo
from ferramentasDeMecanicaDoJogo import *

# Classe da seção mecânica do jogo
class mecanicaDoJogo(ferramentasDeMecanicaDoJogo):
    '''Esta classe contém todos os métodos responsável por alterar a tela e o estado do jogo de acordo com os comandos do jogador.'''

    def __init__(self, tamanhoDoTabuleiro = 4):
        '''
        Método construtor que inicializa o tabuleiro. Se nenhum parâmetro for passado, inicializa com o tamanho padrão 4X4.
        self,int -> none
        '''
        # Atributo que armazena a matriz do tabuleiro
        self.tabuleiro = self.geraMatriz(tamanhoDoTabuleiro, tamanhoDoTabuleiro)

        # Atributo que armazena o score
        self.score = 0

        # Conjunto com todos os atributos da classe
        self.__atributos = {
            'self.__atributos',
            'self.__metodos',
            'self.tabuleiro',
            'self.score'
        }

        # Conjunto com todos os métodos da classe
        self.__metodos = {
            '__init__',
            '__str__',
            'getAtributos',
            'getMetodos',
            'manual',
            'geraMatriz',
            'geraNumeroAleatorio',
            'inserePeca',
            'movePecas',
            'getTabuleiro',
            'getScore'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com todos os atributos e métodos da classe.
        self -> str
        '''

        string = f'Classe mecanicaDoJogo:\n{mecanicaDoJogo.__doc__}\n\nAtributos:\n'

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
            'self.tabuleiro': 'Atributo que armazena a matriz do tabuleiro',
            'self.score': 'Atributo que armazena o score',
            '__init__': self.__init__.__doc__,
            '__str__': self.__str__.__doc__,
            'getAtributos': self.getAtributos.__doc__,
            'getMetodos': self.getMetodos.__doc__,
            'manual': self.manual.__doc__,
            'geraMatriz': self.geraMatriz.__doc__,
            'geraNumeroAleatorio': self.geraNumeroAleatorio.__doc__,
            'inserePeca': self.inserePeca.__doc__,
            'movePecas': self.movePecas.__doc__,
            'getTabuleiro': self.getTabuleiro.__doc__,
            'getScore': self.getScore.__doc__
        }

    def inserePeca(self):
        '''
        Método que insere uma nova peça no tabuleiro.
        Retorna True se uma peça foi inserida ou False se não há casas vazias sobrando (fim de jogo).
        self -> bool
        '''

    def movePecas(self, entradaDoUsuário):
        '''
        Método que move todas as peças do tabuleiro de acordo com a entrada do usuário.
        Retorna True se alguma peça virou 2048, ou False se nenhuma peça virou 2048.
        self,str -> bool
        '''
        pass

    def getTabuleiro(self):
        '''
        Método que retorna a matriz do tabuleiro.
        self -> list
        '''
        return self.tabuleiro

    def getScore(self):
        '''
        Método que retorna o score.
        self -> int
        '''
        return self.score