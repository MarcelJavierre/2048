'''
Módulo com a definição da classe MecanicaDoJogo responsável pela seção
mecânica do jogo.
'''

# Importando a função log2 do módulo math para calcular logaritmos na base 2
from math import log2

# Importando a super classe FerramentasDeMecanicaDoJogo com os métodos genéricos associados com a mecânica do jogo
from ferramentas.ferramentasDeMecanicaDoJogo import *

class MecanicaDoJogo(FerramentasDeMecanicaDoJogo):
    '''
    Esta classe contém todos os métodos responsável por alterar a tela e
    o estado do jogo de acordo com os comandos do jogador.
    '''

    def __init__(self, tamanhoDoTabuleiro = 4, objetivo = 2048):
        '''
        Método construtor que inicializa o tabuleiro. Se nenhum
        parâmetro for passado, inicializa com o tamanho padrão 4X4 e com
        objetivo de atingir 2048. Caso o tamanho do tabuleiro passado
        for menor ou igual a 1 ou o objetivo não for uma potência de 2,
        gera um "ValueError".

        Self, int, int -> None
        '''
        # Verifica se o tamanho do tabuleiro passado é válido
        if tamanhoDoTabuleiro <= 1:
            # Se não for, retorna um "ValueError"
            raise ValueError(f'Nao e possivel gerar um tabuleiro com o tamanho {tamanhoDoTabuleiro}')

        # Verifica se o objetivo passado é válido
        if (objetivo <= 1) or (objetivo > 524288) or (not log2(objetivo).is_integer()):
            # Se não for, retorna um "ValueError"
            raise ValueError(f'O valor {objetivo} nao e um objetivo valido')

        # Atributo que armazena o tamanho do tabuleiro
        self.tamanhoDoTabuleiro = tamanhoDoTabuleiro

        # Atributo que armazena a matriz do tabuleiro
        self.tabuleiro = self.geraMatriz(tamanhoDoTabuleiro, tamanhoDoTabuleiro)

        # Atributo que armazena o score
        self.score = 0

        # Atributo com o valor da peça do objetivo do jogo
        self.objetivo = objetivo

        # Atributo que armazena o vetor com os números para serem sorteados e inseridos no tabuleiro a cada nova rodada
        self.numerosParaSeremSorteados = np.array((2, 4), int)

        # Atributo que armazena o vetor com a probabilidade do sorteio
        # A cada nova rodada, 90% de chance da nova peça ser 2 e 10% de chance da nova peça ser 4
        self.probabilidade = np.array((0.9, 0.1), float)

        # Atributo que armazena a quantidade de vezes que duas peças foram fundidas durante a partida
        self.quantidadeDeFusoes = 0
        
        # Inicia o tabuleiro com 2 peças
        self.inserePeca(self.getCasasVazias())
        self.inserePeca(self.getCasasVazias())

        # Conjunto com todos os atributos da classe
        self.__atributos = {
            'self.__atributos',
            'self.__metodos',
            'self.tamanhoDoTabuleiro',
            'self.tabuleiro',
            'self.score',
            'self.objetivo',
            'self.numerosParaSeremSorteados',
            'self.probabilidade',
            'self.quantidadeDeFusoes'
        }

        # Conjunto com todos os métodos da classe
        self.__metodos = {
            '__init__',
            '__str__',
            'getAtributos',
            'getMetodos',
            'manual',
            'geraMatriz',
            'geraElementoAleatorio',
            'inserePeca',
            'movePecas',
            'juntaPecas',
            'venceuOJogo',
            'possuiMovimentosVailidos',
            'getCasasVazias',
            'getTabuleiro',
            'getScore',
            'getValorDaMaiorPeca',
            'getQuantidadeDeFusoes',
            'carregarJogo'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com
        todos os atributos e métodos da classe.

        Self -> str
        '''

        string = f'Classe MecanicaDoJogo:\n{MecanicaDoJogo.__doc__}\n\nAtributos:\n'

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
            'self.tamanhoDoTabuleiro': 'Atributo que armazena o tamanho do tabuleiro',
            'self.tabuleiro': 'Atributo que armazena a matriz do tabuleiro.',
            'self.score': 'Atributo que armazena o score.',
            'self.objetivo': 'Atributo com o valor da peça do objetivo do jogo',
            'self.numerosParaSeremSorteados': 'Atributo que armazena o vetor com os números para serem sorteados e inseridos no tabuleiro a cada nova rodada.',
            'self.probabilidade': 'Atributo que armazena o vetor com a probabilidade do sorteio',
            'self.quantidadeDeFusoes': 'Atributo que armazena a quantidade de vezes que duas peças foram fundidas durante a partida.',
            '__init__': self.__init__.__doc__,
            '__str__': self.__str__.__doc__,
            'getAtributos': self.getAtributos.__doc__,
            'getMetodos': self.getMetodos.__doc__,
            'manual': self.manual.__doc__,
            'geraMatriz': self.geraMatriz.__doc__,
            'geraElementoAleatorio': self.geraElementoAleatorio.__doc__,
            'inserePeca': self.inserePeca.__doc__,
            'movePecas': self.movePecas.__doc__,
            'juntaPecas': self.juntaPecas.__doc__,
            'venceuOJogo': self.venceuOJogo.__doc__,
            'possuiMovimentosVailidos': self.possuiMovimentosVailidos.__doc__,
            'getCasasVazias': self.getCasasVazias.__doc__,
            'getTabuleiro': self.getTabuleiro.__doc__,
            'getScore': self.getScore.__doc__,
            'getValorDaMaiorPeca': self.getValorDaMaiorPeca.__doc__,
            'getQuantidadeDeFusoes': self.getQuantidadeDeFusoes.__doc__,
            'carregarJogo': self.carregarJogo.__doc__
        }

    def inserePeca(self, casasVazias):
        '''
        Método que insere uma nova peça no tabuleiro em uma casa livre.

        Self, numpy.ndarray[str] -> None
        '''
        # Sorteia a nova peça
        peca = self.geraElementoAleatorio(self.numerosParaSeremSorteados, self.probabilidade)

        # Sorteia a casa vazia
        casa = self.geraElementoAleatorio(casasVazias)

        # Altera o atributo "tabuleiro" com a nova peça
        self.tabuleiro[int(casa[0])][int(casa[1])] = peca

    def movePecas(self, entradaDoUsuario):
        '''
        Método que move todas as peças do tabuleiro de acordo com a
        entrada do usuário. Retorna "True" se alguma peça foi deslocada
        ou "False" se não. O parâmetro "entradaDoUsuario" precisa ser
        "w", "a", "s" ou "d".

        Self, str -> bool
        '''
        # Variável para indicar se alguma peça foi movida
        pecaFoiMovida = False

        # Caso a entrada do usuário for para cima
        if entradaDoUsuario == 'w':
            # Passa da segunda até a última linha
            for i in range(1, self.tamanhoDoTabuleiro):
                # Passa por todas as colunas
                for j in range(self.tamanhoDoTabuleiro):
                    # Caso a peça não seja 0
                    if self.tabuleiro[i][j] != 0:
                        # Verifica a casa da linha anterior
                        # Caso a casa esteja vazia (com uma peça 0), move a peça para a casa de cima
                        if self.tabuleiro[i - 1][j] == 0:
                            self.tabuleiro[i - 1][j] = self.tabuleiro[i][j]
                            self.tabuleiro[i][j] = 0
                            pecaFoiMovida = True

        # Caso a entrada do usuário for para baixo
        elif entradaDoUsuario == 's':
            # Passa da penúltima até a primeira linha
            for i in range(self.tamanhoDoTabuleiro - 2, - 1, - 1):
                # Passa por todas as colunas
                for j in range(self.tamanhoDoTabuleiro):
                    # Caso a peça não seja 0
                    if self.tabuleiro[i][j] != 0:
                        # Verifica a casa da linha anterior
                        # Caso a casa esteja vazia (com uma peça 0), move a peça para a casa de cima
                        if self.tabuleiro[i + 1][j] == 0:
                            self.tabuleiro[i + 1][j] = self.tabuleiro[i][j]
                            self.tabuleiro[i][j] = 0
                            pecaFoiMovida = True

        # Caso a entrada do usuário for para a esquerda
        elif entradaDoUsuario == 'a':
            # Passa por todas as linhas
            for i in range(self.tamanhoDoTabuleiro):
                # Passa da segunda até a última coluna
                for j in range(1, self.tamanhoDoTabuleiro):
                    # Caso a peça não seja 0
                    if self.tabuleiro[i][j] != 0:
                        # Verifica a casa da coluna anterior
                        # Caso a casa esteja vazia (com uma peça 0), move a peça para a casa de cima
                        if self.tabuleiro[i][j - 1] == 0:
                            self.tabuleiro[i][j - 1] = self.tabuleiro[i][j]
                            self.tabuleiro[i][j] = 0
                            pecaFoiMovida = True

        # Caso a entrada do usuário for para a direita
        else:
            # Passa por todas as linhas
            for i in range(self.tamanhoDoTabuleiro):
                # Passa da penúltima até a primeira coluna
                for j in range(self.tamanhoDoTabuleiro - 2, - 1, - 1):
                    # Caso a peça não seja 0
                    if self.tabuleiro[i][j] != 0:
                        # Verifica a casa da coluna anterior
                        # Caso a casa esteja vazia (com uma peça 0), move a peça para a casa de cima
                        if self.tabuleiro[i][j + 1] == 0:
                            self.tabuleiro[i][j + 1] = self.tabuleiro[i][j]
                            self.tabuleiro[i][j] = 0
                            pecaFoiMovida = True

        # Retorna a variável que indica se alguma peça foi movida ou não
        return pecaFoiMovida

    def juntaPecas(self, entradaDoUsuario):
        '''
        Método que junta todas as peças vizinhas iguais do tabuleiro de
        acordo com a entrada do usuário. Retorna "True" se alguma peça
        foi juntada ou "False" se não. O parâmetro "entradaDoUsuario"
        precisa ser "w", "a", "s" ou "d".

        Self, str -> bool
        '''
        # Variável para indicar se alguma peça foi movida
        pecaFoiJuntada = False

        # Caso a entrada do usuário for para cima
        if entradaDoUsuario == 'w':
            # Passa da primeira até a penúltima linha
            for i in range(self.tamanhoDoTabuleiro - 1):
                # Passa por todas as colunas
                for j in range(self.tamanhoDoTabuleiro):
                    # Caso a peça não seja 0
                    if self.tabuleiro[i][j] != 0:
                        # Verifica a casa da linha de baixo
                        # Caso a casa esteja com uma peça igual, junta as duas peças
                        if self.tabuleiro[i][j] == self.tabuleiro[i + 1][j]:
                            self.tabuleiro[i][j] += self.tabuleiro[i + 1][j]
                            self.tabuleiro[i + 1][j] = 0

                            # Adiciona o valor da nova peça ao score
                            self.score += self.tabuleiro[i][j]

                            # Adiciona + 1 no contador de fusões
                            self.quantidadeDeFusoes += 1

                            pecaFoiJuntada = True

        # Caso a entrada do usuário for para baixo
        elif entradaDoUsuario == 's':
            # Passa da última até a segunda linha
            for i in range(self.tamanhoDoTabuleiro - 1, 0, - 1):
                # Passa por todas as colunas
                for j in range(self.tamanhoDoTabuleiro):
                    # Caso a peça não seja 0
                    if self.tabuleiro[i][j] != 0:
                        # Verifica a casa da linha de cima
                        # Caso a casa esteja com uma peça igual, junta as duas peças
                        if self.tabuleiro[i][j] == self.tabuleiro[i - 1][j]:
                            self.tabuleiro[i][j] += self.tabuleiro[i - 1][j]
                            self.tabuleiro[i - 1][j] = 0

                            # Adiciona o valor da nova peça ao score
                            self.score += self.tabuleiro[i][j]

                            # Adiciona + 1 no contador de fusões
                            self.quantidadeDeFusoes += 1

                            pecaFoiJuntada = True

        # Caso a entrada do usuário for para a esquerda
        elif entradaDoUsuario == 'a':
            # Passa por todas as linhas
            for i in range(self.tamanhoDoTabuleiro):
                # Passa da primeira até a penúltima coluna
                for j in range(self.tamanhoDoTabuleiro - 1):
                    # Caso a peça não seja 0
                    if self.tabuleiro[i][j] != 0:
                        # Verifica a casa da coluna anterior
                        # Caso a casa esteja com uma peça igual, junta as duas peças
                        if self.tabuleiro[i][j] == self.tabuleiro[i][j + 1]:
                            self.tabuleiro[i][j] += self.tabuleiro[i][j + 1]
                            self.tabuleiro[i][j + 1] = 0

                            # Adiciona o valor da nova peça ao score
                            self.score += self.tabuleiro[i][j]

                            # Adiciona + 1 no contador de fusões
                            self.quantidadeDeFusoes += 1

                            pecaFoiJuntada = True

        # Caso a entrada do usuário for para a direita
        else:
            # Passa por todas as linhas
            for i in range(self.tamanhoDoTabuleiro):
                # Passa da última até a segunda coluna
                for j in range(self.tamanhoDoTabuleiro - 1, 0, - 1):
                    # Caso a peça não seja 0
                    if self.tabuleiro[i][j] != 0:
                        # Verifica a casa da coluna anterior
                        # Caso a casa esteja com uma peça igual, junta as duas peças
                        if self.tabuleiro[i][j] == self.tabuleiro[i][j - 1]:
                            self.tabuleiro[i][j] += self.tabuleiro[i][j - 1]
                            self.tabuleiro[i][j - 1] = 0

                            # Adiciona o valor da nova peça ao score
                            self.score += self.tabuleiro[i][j]

                            # Adiciona + 1 no contador de fusões
                            self.quantidadeDeFusoes += 1

                            pecaFoiJuntada = True

        # Retorna a variável que indica se alguma peça foi movida ou não
        return pecaFoiJuntada

    def venceuOJogo(self):
        '''
        Método que verifica todas as casas do tabuleiro. Retorna "True"
        se o tabuleiro possui uma peça com o valor definido como o
        objetivo (padrão 2048) ou "False" se não.

        Self -> bool
        '''
        return (self.objetivo in self.tabuleiro)

    def possuiMovimentosVailidos(self):
        '''
        Método que verifica todas as casas do tabuleiro. Retorna "True"
        se possui movimentos válidos ou "False" se não.

        Self -> bool
        '''
        # Caso o tabuleiro possua alguma casa vazia, retorna "True"
        if 0 in self.tabuleiro:
            return True

        # Verifica se tem movimentos válidos na vertical
        # Passa da primeira até a penúltima linha
        for i in range(self.tamanhoDoTabuleiro - 1):
            # Passa por todas as colunas
            for j in range(self.tamanhoDoTabuleiro):
                # Caso a casa possua uma peça igual a casa de baixo, retorna "True"
                if self.tabuleiro[i][j] == self.tabuleiro[i + 1][j]:
                    return True

        # Verifica se tem movimentos válidos na horizontal
        # Passa por todas as linhas
        for i in range(self.tamanhoDoTabuleiro):
            # Passa da primeira até a penúltima coluna
            for j in range(self.tamanhoDoTabuleiro - 1):
                # Caso a casa possua uma peça igual a casa ao lado, retorna "True"
                if self.tabuleiro[i][j] == self.tabuleiro[i][j + 1]:
                    return True
                    
        # Caso não possua movimentos válidos, retorna "False"
        return False

    def getCasasVazias(self):
        '''
        Método que verifica todas as casas do tabuleiro. Retorna um
        vetor de strings com todas as posições de casas vazias. A
        primeira posição da string é o índice da linha e a segunda é o
        índice da coluna.

        Self -> numpy.ndarray[str]
        '''
        # Cria dois vetores com os índices das casas vazias
        indicesDasLinhas, indicesDasColunas = np.where(self.tabuleiro == 0)

        # Converte os dois vetores de int para vetores de strings
        indicesDasLinhas = indicesDasLinhas.astype(str)
        indicesDasColunas = indicesDasColunas.astype(str)

        # Retorna os dois vetores concatenados
        return np.char.add(indicesDasLinhas, indicesDasColunas)

    def getTabuleiro(self):
        '''
        Método que retorna a matriz do tabuleiro.

        Self -> numpy.ndarray[int]
        '''
        return self.tabuleiro

    def getScore(self):
        '''
        Método que retorna o score.

        Self -> int
        '''
        return self.score

    def getValorDaMaiorPeca(self):
        '''
        Método que retorna o valor da maior peça no tabuleiro.

        Self -> int
        '''
        return np.max(self.tabuleiro)

    def getQuantidadeDeFusoes(self):
        '''
        Método que retorna o valor da quantidade de fusões.

        Self -> int
        '''
        return self.quantidadeDeFusoes

    def carregarJogo(self, tabuleiro, score):
        '''
        Método que atualiza os atributos com os dados do jogo salvo.

        Self, list[int], int -> None
        '''
        self.tabuleiro = np.array(tabuleiro, int)
        self.score = score
