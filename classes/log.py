# Função do módulo time para obter a data atual
from time import localtime

# Classe da seção log
class Log:
    '''Esta classe trata do armazenamento em arquivos de todos os dados que podem vir a ser de interesse do usuário, bem como todos os erros que ocorrerem durante a execução do jogo.'''

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
            'savarJogo',
            'carregarJogo',
            'estatisticasDeJogadas',
            'estatisticasDePecas',
            'relatorioDeErro'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com todos os atributos e métodos da classe.
        self -> str
        '''

        string = f'Classe Log:\n{Log.__doc__}\n\nAtributos:\n'

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
            'savarJogo': self.savarJogo.__doc__,
            'carregarJogo': self.carregarJogo.__doc__,
            'estatisticasDeJogadas': self.estatisticasDeJogadas.__doc__,
            'estatisticasDePecas': self.estatisticasDePecas.__doc__,
            'relatorioDeErro': self.relatorioDeErro.__doc__
        }

    def savarJogo(self, tamanhoDoTabuleiro, pecaDaVitoria, tabuleiro, score):
        '''
        Método que armazena em um arquivo o estado atual do jogo.
        O arquivo de salvamento se encontra em "partidasSalvas/partidasSalvas".
        Cada partida salva ocupa 5 linhas no arquivo, sendo elas:

        * 1ª Linha: Data e Hora do Salvamento;
        * 2ª Linha: Tamanho do Tabuleiro;
        * 3ª Linha: Objetivo da Partida;
        * 4ª Linha: Matriz do Tabuleiro;
        * 5ª Linha: Score.

        self,int,int,list,int -> none
        '''
        arquivo = open('partidasSalvas/PartidasSalvas', 'a')
        arquivo.write(f'{localtime()[2]:02d}/{localtime()[1]:02d}/{localtime()[0]}\t{localtime()[3]:02d}:{localtime()[4]:02d}\n{tamanhoDoTabuleiro}\n{pecaDaVitoria}\n{tabuleiro}\n{score}\n')
        arquivo.close()

    def carregarJogo(self):
        '''
        Método que carrega de um arquivo o jogo salvo. Retorna uma tupla com a matriz do tabuleiro e o score.
        self -> tuple
        '''
        pass

    def estatisticasDeJogadas(self):
        '''
        Método que armazena em um arquivo todos os movimentos do usuário.
        self -> none
        '''
        pass

    def estatisticasDePecas(self):
        '''
        Método que armazena em um arquivo a quantidade total de peças formadas durante as partidas.
        self -> none
        '''
        pass
    
    def relatorioDeErro(self):
        '''
        Método que cria um arquivo de relatório sobre um possível erro que ocorra durante a execução do código.
        self -> none
        '''
        pass