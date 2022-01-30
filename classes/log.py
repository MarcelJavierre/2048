# Função do módulo time para obter a data atual
from time import localtime

# Função do módulo os para criar uma pasta
from os import mkdir

# Classe da seção log
class Log:
    '''Esta classe trata do armazenamento em arquivos de todos os dados que podem vir a ser de interesse do usuário, bem como todos os erros que ocorrerem durante a execução do jogo.'''

    def __init__(self):
        '''
        Método construtor. Cria as pastas para armazenar os arquivos salvos.
        self -> none
        '''

        # Cria a pasta "estatisticas"
        try:
            mkdir('estatisticas')

        # Caso a pasta já exista, não faz nada
        except FileExistsError:
            pass

        # Cria a pasta "partidasSalvas"
        try:
            mkdir('partidasSalvas')

        # Caso a pasta já exista, não faz nada
        except FileExistsError:
            pass

        # Cria a pasta "relatorioDeErros"
        try:
            mkdir('relatorioDeErros')

        # Caso a pasta já exista, não faz nada
        except FileExistsError:
            pass

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
            'apagarJogoSalvo',
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
            'apagarJogoSalvo': self.apagarJogoSalvo.__doc__,
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
        # Abre o arquivo
        arquivo = open('partidasSalvas/partidasSalvas', 'a')

        # Escreve no arquivo o conteúdo da partida
        arquivo.write(f'{localtime()[2]:02d}/{localtime()[1]:02d}/{localtime()[0]}    {localtime()[3]:02d}:{localtime()[4]:02d}\n{tamanhoDoTabuleiro}\n{pecaDaVitoria}\n{tabuleiro}\n{score}\n')
        
        # Fecha o arquivo
        arquivo.close()

    def carregarJogo(self):
        '''
        Método que carrega de um arquivo o jogo salvo.
        Retorna uma lista com o seguinte conteúdo:

        * 1ª índice [0]: Data e Hora do Salvamento;
        * 2ª índice [1]: Tamanho do Tabuleiro;
        * 3ª índice [2]: Objetivo da Partida;
        * 4ª índice [3]: Matriz do Tabuleiro;
        * 5ª índice [4]: Score.

        self -> list
        '''
        # Tenta abrir o arquivo
        try:
            arquivo = open('partidasSalvas/partidasSalvas', 'r')

        # Caso o arquivo não exista, cria e abre o arquivo
        except FileNotFoundError:
            arquivo = open('partidasSalvas/partidasSalvas', 'x')
            arquivo.close()
            arquivo = open('partidasSalvas/partidasSalvas', 'r')

        # Lê o conteúdo do arquivo
        conteudoDoArquivo = arquivo.readlines()

        # Fecha o arquivo
        arquivo.close()

        # Retorna o conteúdo do arquivo
        return conteudoDoArquivo

    def apagarJogoSalvo(self, indiceDaPartidaSalva):
        '''
        Método para apagar do arquivo com as partidas salvas um jogo salvo.
        self,int -> none
        '''
        # Abre o arquivo no modo leitura
        arquivo = open('partidasSalvas/partidasSalvas', 'r')

        # Lê o conteúdo do arquivo
        conteudoDoArquivo = arquivo.readlines()

        # Fecha o arquivo
        arquivo.close()

        # Remove os dados da partida salva
        conteudoDoArquivo.pop(indiceDaPartidaSalva)
        conteudoDoArquivo.pop(indiceDaPartidaSalva)
        conteudoDoArquivo.pop(indiceDaPartidaSalva)
        conteudoDoArquivo.pop(indiceDaPartidaSalva)
        conteudoDoArquivo.pop(indiceDaPartidaSalva)

        # Abre o arquivo no modo sobrescrever
        arquivo = open('partidasSalvas/partidasSalvas', 'w')

        # Escreve o conteúdo de volta no arquivo
        for i in range(len(conteudoDoArquivo)):
            arquivo.write(conteudoDoArquivo[i])

        # Fecha o arquivo
        arquivo.close()

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