# Importando a função "choice" do módulo "random" que sorteia um elemento aleatório de uma dada lista
from random import choice

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

        string = f'Classe FerramentasDeMecanicaDoJogo:\n{FerramentasDeMecanicaDoJogo.__doc__}\n\nAtributos:\n'

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
            'geraMatriz': self.geraMatriz.__doc__,
            'geraElementoAleatorio': self.geraElementoAleatorio.__doc__
        }

    def geraMatriz(self, numeroDeLinhas, numeroDeColunas):
        '''
        Método para gerar uma matriz. Retorna uma lista de listas
        (matriz).

        Self, int, int -> list[None]
        '''
        # Cria uma lista vazia
        matriz = []

        # Passa por todas as linhas adicionando uma lista vazia
        for i in range(numeroDeLinhas):
            matriz.append([])
            # Passa por todas as colunas adicionando "None" em cada posição
            for j in range(numeroDeColunas):
                matriz[i].append(None)

        return matriz

    def geraElementoAleatorio(self, lista):
        '''
        Método para sortear um elemento aleatório de uma dada lista.
        Retorna o elemento sorteado.

        Self, list[Any] -> Any
        '''
        return choice(lista)
