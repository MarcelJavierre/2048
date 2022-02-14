# Importando o módulo "numpy" com o apelido "np"
import numpy as np

class FerramentasDeMecanicaDoJogo:
    '''
    Super classe com métodos genéricos associados com a mecânica do
    jogo.
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
            'geraMatriz',
            'geraElementoAleatorio'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com
        todos os atributos e métodos da classe.

        Self -> str
        '''

        string = f'Classe FerramentasDeMecanicaDoJogo:\n{FerramentasDeMecanicaDoJogo.__doc__}\n\nAtributos:\n\n'

        # Passa por todos os atributos e insere na string
        for i in self.__atributos:
            string += '        ' + i + ': ' + self.manual()[i] + '\n'

        string += '\nMétodos:\n\n'

        # Passa por todos os métodos e insere na string
        for i in self.__metodos:
            string += '        ' + i + ': ' + self.manual()[i] + '\n'

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
            'geraMatriz': self.geraMatriz.__doc__,
            'geraElementoAleatorio': self.geraElementoAleatorio.__doc__
        }

    def geraMatriz(self, numeroDeLinhas, numeroDeColunas):
        '''
        Método para gerar uma matriz. Retorna uma matriz numpy com todas
        as posições contendo o valor 0.

        Self, int, int -> numpy.ndarray[int]
        '''
        return np.zeros((numeroDeLinhas, numeroDeColunas), int)

    def geraElementoAleatorio(self, vetor, probabilidade = None):
        '''
        Método para sortear um elemento aleatório de um dado vetor.
        Retorna o elemento sorteado.

        Self, numpy.ndarray[Any], numpy.ndarray[float] -> Any
        '''
        return np.random.choice(vetor, 1, p = probabilidade)[0]
