# Importando a super classe "FerramentasDeMecanicaDoJogo" com os métodos genéricos associados com a mecânica do jogo
from audioop import add


if __name__ == '__main__':
    from ferramentasDeMecanicaDoJogo import *

else:
    from classes.ferramentasDeMecanicaDoJogo import *

# Classe da seção mecânica do jogo
class MecanicaDoJogo(FerramentasDeMecanicaDoJogo):
    '''
    Esta classe contém todos os métodos responsável por alterar a tela e
    o estado do jogo de acordo com os comandos do jogador.
    '''

    def __init__(self, tamanhoDoTabuleiro = 4, objetivo = 2048):
        '''
        Método construtor que inicializa o tabuleiro. Se nenhum
        parâmetro for passado, inicializa com o tamanho padrão 4X4 e com
        objetivo de atingir 2048.

        Self, int, int -> None
        '''
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
            'self.probabilidade'
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
            'getCasasVazias',
            'getTabuleiro',
            'getScore',
            'getValorDaMaiorPeca',
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
            '__init__': self.__init__.__doc__,
            '__str__': self.__str__.__doc__,
            'getAtributos': self.getAtributos.__doc__,
            'getMetodos': self.getMetodos.__doc__,
            'manual': self.manual.__doc__,
            'geraMatriz': self.geraMatriz.__doc__,
            'geraElementoAleatorio': self.geraElementoAleatorio.__doc__,
            'inserePeca': self.inserePeca.__doc__,
            'movePecas': self.movePecas.__doc__,
            'getCasasVazias': self.getCasasVazias.__doc__,
            'getTabuleiro': self.getTabuleiro.__doc__,
            'getScore': self.getScore.__doc__,
            'getValorDaMaiorPeca': self.getValorDaMaiorPeca.__doc__,
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
        "cima", "baixo", "esquerda" ou "direita".

        Self, str -> bool
        '''
        # Variável para indicar se alguma peça foi movida
        pecaFoiMovida = False

        # Caso a entrada do usuário for "cima"
        if entradaDoUsuario == 'cima':
            # Passa por todas as linhas, de cima para baixo
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

                        # Caso a casa esteja com uma peça igual, junta as duas peças
                        elif self.tabuleiro[i - 1][j] == self.tabuleiro[i][j]:
                            self.tabuleiro[i - 1][j] += self.tabuleiro[i][j]
                            self.tabuleiro[i][j] = 0
                            # Adiciona o valor da nova peça ao score
                            self.score += self.tabuleiro[i - 1][j]
                            pecaFoiMovida = True

        # Caso a entrada do usuário for "baixo"
        elif entradaDoUsuario == 'baixo':
            # Passa por todas as linhas, de baixo para cima
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

                        # Caso a casa esteja com uma peça igual, junta as duas peças
                        elif self.tabuleiro[i + 1][j] == self.tabuleiro[i][j]:
                            self.tabuleiro[i + 1][j] += self.tabuleiro[i][j]
                            self.tabuleiro[i][j] = 0
                            # Adiciona o valor da nova peça ao score
                            self.score += self.tabuleiro[i + 1][j]
                            pecaFoiMovida = True

        # Caso a entrada do usuário for "esquerda"
        elif entradaDoUsuario == 'esquerda':
            # Passa por todas as linhas
            for i in range(self.tamanhoDoTabuleiro):
                # Passa por todas as colunas, da esquerda para a direita
                for j in range(1, self.tamanhoDoTabuleiro):
                    # Caso a peça não seja 0
                    if self.tabuleiro[i][j] != 0:
                        # Verifica a casa da coluna anterior
                        # Caso a casa esteja vazia (com uma peça 0), move a peça para a casa de cima
                        if self.tabuleiro[i][j - 1] == 0:
                            self.tabuleiro[i][j - 1] = self.tabuleiro[i][j]
                            self.tabuleiro[i][j] = 0
                            pecaFoiMovida = True

                        # Caso a casa esteja com uma peça igual, junta as duas peças
                        elif self.tabuleiro[i][j - 1] == self.tabuleiro[i][j]:
                            self.tabuleiro[i][j - 1] += self.tabuleiro[i][j]
                            self.tabuleiro[i][j] = 0
                            # Adiciona o valor da nova peça ao score
                            self.score += self.tabuleiro[i][j - 1]
                            pecaFoiMovida = True

        # Caso a entrada do usuário for "direita"
        else:
            # Passa por todas as linhas
            for i in range(self.tamanhoDoTabuleiro):
                # Passa por todas as colunas, da direita para a esquerda
                for j in range(self.tamanhoDoTabuleiro - 2, - 1, - 1):
                    # Caso a peça não seja 0
                    if self.tabuleiro[i][j] != 0:
                        # Verifica a casa da coluna anterior
                        # Caso a casa esteja vazia (com uma peça 0), move a peça para a casa de cima
                        if self.tabuleiro[i][j + 1] == 0:
                            self.tabuleiro[i][j + 1] = self.tabuleiro[i][j]
                            self.tabuleiro[i][j] = 0
                            pecaFoiMovida = True

                        # Caso a casa esteja com uma peça igual, junta as duas peças
                        elif self.tabuleiro[i][j + 1] == self.tabuleiro[i][j]:
                            self.tabuleiro[i][j + 1] += self.tabuleiro[i][j]
                            self.tabuleiro[i][j] = 0
                            # Adiciona o valor da nova peça ao score
                            self.score += self.tabuleiro[i][j + 1]
                            pecaFoiMovida = True

        # Retorna a variável que indica se alguma peça foi movida ou não
        return pecaFoiMovida

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
        # Verifica as casas centrais
        # Passa pelas linhas, da segunda até a penúltima
        for i in range(1, self.tamanhoDoTabuleiro - 1):
            # Passa pelas colunas, da segunda até a penúltima
            for j in range(1, self.tamanhoDoTabuleiro - 1):
                # Verifica se a casa pode se juntar com alguma outra casa ao redor
                # Se sim, retorna "True"
                if (
                    self.tabuleiro[i][j] == 0 or
                    self.tabuleiro[i][j] == self.tabuleiro[i + 1][j] or
                    self.tabuleiro[i][j] == self.tabuleiro[i - 1][j] or
                    self.tabuleiro[i][j] == self.tabuleiro[i][j + 1] or
                    self.tabuleiro[i][j] == self.tabuleiro[i][j - 1]
                ):
                    return True

        # Verifica as casas da borda superior
        # Passa pelas colunas, da segunda até a penúltima
        for j in range(1, self.tamanhoDoTabuleiro - 1):
            # Verifica se a casa pode se juntar com alguma outra casa ao redor
                # Se sim, retorna "True"
                if (
                    self.tabuleiro[0][j] == 0 or
                    self.tabuleiro[0][j] == self.tabuleiro[0][j + 1] or
                    self.tabuleiro[0][j] == self.tabuleiro[0][j - 1]
                ):
                    return True
                    
        # Verifica as casas da borda inferior
        # Passa pelas colunas, da segunda até a penúltima
        for j in range(1, self.tamanhoDoTabuleiro - 1):
            # Verifica se a casa pode se juntar com alguma outra casa ao redor
                # Se sim, retorna "True"
                if (
                    self.tabuleiro[self.tamanhoDoTabuleiro - 1][j] == 0 or
                    self.tabuleiro[self.tamanhoDoTabuleiro - 1][j] == self.tabuleiro[self.tamanhoDoTabuleiro - 1][j + 1] or
                    self.tabuleiro[self.tamanhoDoTabuleiro - 1][j] == self.tabuleiro[self.tamanhoDoTabuleiro - 1][j - 1]
                ):
                    return True

        # Verifica as casas da borda esquerda
        # Passa pelas linhas, da segunda até a penúltima
        for i in range(1, self.tamanhoDoTabuleiro - 1):
            # Verifica se a casa pode se juntar com alguma outra casa ao redor
                # Se sim, retorna "True"
                if (
                    self.tabuleiro[i][0] == 0 or
                    self.tabuleiro[i][0] == self.tabuleiro[i + 1][0] or
                    self.tabuleiro[i][0] == self.tabuleiro[i - 1][0]
                ):
                    return True

        # Verifica as casas da borda direita
        # Passa pelas linhas, da segunda até a penúltima
        for i in range(1, self.tamanhoDoTabuleiro - 1):
            # Verifica se a casa pode se juntar com alguma outra casa ao redor
                # Se sim, retorna "True"
                if (
                    self.tabuleiro[i][self.tamanhoDoTabuleiro - 1] == 0 or
                    self.tabuleiro[i][self.tamanhoDoTabuleiro - 1] == self.tabuleiro[i + 1][self.tamanhoDoTabuleiro - 1] or
                    self.tabuleiro[i][self.tamanhoDoTabuleiro - 1] == self.tabuleiro[i - 1][self.tamanhoDoTabuleiro - 1]
                ):
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

    def carregarJogo(self, tabuleiro, score):
        '''
        Método que atualiza os atributos com os dados do jogo salvo.

        Self, list[int], int -> None
        '''
        self.tabuleiro = np.array(tabuleiro, int)
        self.score = score
