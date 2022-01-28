# Importando a super classe com os métodos genéricos associados com a mecânica do jogo
if __name__ == '__main__':
    from ferramentasDeMecanicaDoJogo import *

else:
    from classes.ferramentasDeMecanicaDoJogo import *

# Função do módulo copy para realizar uma cópia independente do objeto original
from copy import deepcopy

# Classe da seção mecânica do jogo
class MecanicaDoJogo(FerramentasDeMecanicaDoJogo):
    '''Esta classe contém todos os métodos responsável por alterar a tela e o estado do jogo de acordo com os comandos do jogador.'''

    def __init__(self, tamanhoDoTabuleiro = 4, pecaDaVitoria = 2048):
        '''
        Método construtor que inicializa o tabuleiro.
        Se nenhum parâmetro for passado, inicializa com o tamanho padrão 4X4 e com objetivo de atingir 2048.
        self,int,int -> none
        '''
        # Atributo que armazena a matriz do tabuleiro
        self.tabuleiro = self.geraMatriz(tamanhoDoTabuleiro, tamanhoDoTabuleiro)

        # Atributo que armazena o score
        self.score = 0

        # Atributo com o valor da peça do objetivo do jogo
        self.pecaDaVitoria = pecaDaVitoria

        # Atributo que armazena a lista com os números para serem sorteados e inseridos no tabuleiro a cada nova rodada
        # A cada nova rodada, 90% de chance da nova peça ser 2 e 10% de chance da nova peça ser 4
        self.listaComOsNumerosParaSeremSorteadosEInseridosACadaNovaRodada = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
        
        # Inicia o tabuleiro com 2 peças
        self.inserePeca(self.getCasasVazias())
        self.inserePeca(self.getCasasVazias())

        # Conjunto com todos os atributos da classe
        self.__atributos = {
            'self.__atributos',
            'self.__metodos',
            'self.tabuleiro',
            'self.score',
            'self.pecaDaVitoria',
            'self.listaComOsNumerosParaSeremSorteadosEInseridosACadaNovaRodada'
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
            'carregarJogo'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com todos os atributos e métodos da classe.
        self -> str
        '''

        string = f'Classe mecanicaDoJogo:\n{MecanicaDoJogo.__doc__}\n\nAtributos:\n'

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
            'self.tabuleiro': 'Atributo que armazena a matriz do tabuleiro.',
            'self.score': 'Atributo que armazena o score.',
            'self.pecaDaVitoria': 'Atributo com o valor da peça do objetivo do jogo',
            'self.listaComOsNumerosParaSeremSorteadosEInseridosACadaNovaRodada': 'Atributo que armazena a lista com os números para serem sorteados e inseridos no tabuleiro a cada nova rodada.',
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
            'carregarJogo': self.carregarJogo.__doc__
        }

    def inserePeca(self, listaComAsCasasVazias):
        '''
        Método que insere uma nova peça no tabuleiro em uma casa livre.
        self,list -> none
        '''
        # Sorteia a nova peça
        peca = self.geraElementoAleatorio(self.listaComOsNumerosParaSeremSorteadosEInseridosACadaNovaRodada)

        # Sorteia a casa vazia
        casa = self.geraElementoAleatorio(listaComAsCasasVazias)

        # Altera o atributo "tabuleiro" com a nova peça
        self.tabuleiro[int(casa[0])][int(casa[1])] = peca

    def movePecas(self, entradaDoUsuario):
        '''
        Método que move todas as peças do tabuleiro de acordo com a entrada do usuário. Retorna uma lista com todas as movimentações de peças realizadas.
        self,str -> list
        '''
        # Lista com as diferentes partes da movimentação das peças
        listaComAsMovimentacoes = []

        # Caso a entrada do usuário for "cima"
        if entradaDoUsuario == 'cima':
            # Loop para realizar todas as movimentações até não ter mais movimentos válidos
            while True:
                # Variável para indicar se ainda têm movimentos válidos
                pecaFoiMovida = False

                # Passa por todas as linhas, de cima para baixo
                for i in range(1, len(self.tabuleiro)):
                    # Passa por todas as colunas
                    for j in range(len(self.tabuleiro[i])):

                        # Caso a peça não seja "None"
                        if self.tabuleiro[i][j] != None:

                            # Verifica a casa da linha anterior
                            # Caso a casa esteja vazia (com uma peça "None"), move a peça para a casa de cima
                            if self.tabuleiro[i - 1][j] == None:
                                self.tabuleiro[i - 1][j] = self.tabuleiro[i][j]
                                self.tabuleiro[i][j] = None
                                pecaFoiMovida = True

                            # Caso a casa esteja com uma peça igual, junta as duas peças
                            elif self.tabuleiro[i - 1][j] == self.tabuleiro[i][j]:
                                self.tabuleiro[i - 1][j] += self.tabuleiro[i][j]
                                self.tabuleiro[i][j] = None

                                # Adiciona o valor da nova peça ao score
                                self.score += self.tabuleiro[i - 1][j]

                                pecaFoiMovida = True

                # Caso não possua mais nenhum movimento válido, encerra o loop
                if pecaFoiMovida == False:
                    break

                # Armazena as diferentes partes da movimentação das peças
                listaComAsMovimentacoes.append(deepcopy(self.tabuleiro))

        # Caso a entrada do usuário for "baixo"
        elif entradaDoUsuario == 'baixo':
            # Loop para realizar todas as movimentações até não ter mais movimentos válidos
            while True:
                # Variável para indicar se ainda têm movimentos válidos
                pecaFoiMovida = False

                # Passa por todas as linhas, de baixo para cima
                for i in range(len(self.tabuleiro) - 2, - 1, - 1):
                    # Passa por todas as colunas
                    for j in range(len(self.tabuleiro[i])):

                        # Caso a peça não seja "None"
                        if self.tabuleiro[i][j] != None:

                            # Verifica a casa da linha anterior
                            # Caso a casa esteja vazia (com uma peça "None"), move a peça para a casa de cima
                            if self.tabuleiro[i + 1][j] == None:
                                self.tabuleiro[i + 1][j] = self.tabuleiro[i][j]
                                self.tabuleiro[i][j] = None
                                pecaFoiMovida = True

                            # Caso a casa esteja com uma peça igual, junta as duas peças
                            elif self.tabuleiro[i + 1][j] == self.tabuleiro[i][j]:
                                self.tabuleiro[i + 1][j] += self.tabuleiro[i][j]
                                self.tabuleiro[i][j] = None

                                # Adiciona o valor da nova peça ao score
                                self.score += self.tabuleiro[i + 1][j]

                                pecaFoiMovida = True

                # Caso não possua mais nenhum movimento válido, encerra o loop
                if pecaFoiMovida == False:
                    break

                # Armazena as diferentes partes da movimentação das peças
                listaComAsMovimentacoes.append(deepcopy(self.tabuleiro))

        # Caso a entrada do usuário for "esquerda"
        elif entradaDoUsuario == 'esquerda':
            # Loop para realizar todas as movimentações até não ter mais movimentos válidos
            while True:
                # Variável para indicar se ainda têm movimentos válidos
                pecaFoiMovida = False

                # Passa por todas as linhas
                for i in range(len(self.tabuleiro)):
                    # Passa por todas as colunas, da esquerda para a direita
                    for j in range(1, len(self.tabuleiro[i])):

                        # Caso a peça não seja "None"
                        if self.tabuleiro[i][j] != None:

                            # Verifica a casa da coluna anterior
                            # Caso a casa esteja vazia (com uma peça "None"), move a peça para a casa de cima
                            if self.tabuleiro[i][j - 1] == None:
                                self.tabuleiro[i][j - 1] = self.tabuleiro[i][j]
                                self.tabuleiro[i][j] = None
                                pecaFoiMovida = True

                            # Caso a casa esteja com uma peça igual, junta as duas peças
                            elif self.tabuleiro[i][j - 1] == self.tabuleiro[i][j]:
                                self.tabuleiro[i][j - 1] += self.tabuleiro[i][j]
                                self.tabuleiro[i][j] = None

                                # Adiciona o valor da nova peça ao score
                                self.score += self.tabuleiro[i][j - 1]

                                pecaFoiMovida = True

                # Caso não possua mais nenhum movimento válido, encerra o loop
                if pecaFoiMovida == False:
                    break

                # Armazena as diferentes partes da movimentação das peças
                listaComAsMovimentacoes.append(deepcopy(self.tabuleiro))

        # Caso a entrada do usuário for "direita"
        else:
            # Loop para realizar todas as movimentações até não ter mais movimentos válidos
            while True:
                # Variável para indicar se ainda têm movimentos válidos
                pecaFoiMovida = False

                # Passa por todas as linhas
                for i in range(len(self.tabuleiro)):
                    # Passa por todas as colunas, da direita para a esquerda
                    for j in range(len(self.tabuleiro[i]) - 2, - 1, - 1):

                        # Caso a peça não seja "None"
                        if self.tabuleiro[i][j] != None:

                            # Verifica a casa da coluna anterior
                            # Caso a casa esteja vazia (com uma peça "None"), move a peça para a casa de cima
                            if self.tabuleiro[i][j + 1] == None:
                                self.tabuleiro[i][j + 1] = self.tabuleiro[i][j]
                                self.tabuleiro[i][j] = None
                                pecaFoiMovida = True

                            # Caso a casa esteja com uma peça igual, junta as duas peças
                            elif self.tabuleiro[i][j + 1] == self.tabuleiro[i][j]:
                                self.tabuleiro[i][j + 1] += self.tabuleiro[i][j]
                                self.tabuleiro[i][j] = None

                                # Adiciona o valor da nova peça ao score
                                self.score += self.tabuleiro[i][j + 1]

                                pecaFoiMovida = True

                # Caso não possua mais nenhum movimento válido, encerra o loop
                if pecaFoiMovida == False:
                    break

                # Armazena as diferentes partes da movimentação das peças
                listaComAsMovimentacoes.append(deepcopy(self.tabuleiro))

        # Retorna a lista com as diferentes partes da movimentação das peças
        return listaComAsMovimentacoes

    def venceuOJogo(self):
        '''
        Método que verifica todas as casas do tabuleiro.
        Retorna "True" se o tabuleiro possui uma peça com o valor definido como o objetivo (padrão 2048) ou "False" se não.
        self -> bool
        '''
        # Passa por todas as linhas do tabuleiro
        for i in range(len(self.tabuleiro)):
            # Passa por todas as colunas do tabuleiro
            for j in range(len(self.tabuleiro[i])):
                # Verifica se possui alguma peça com o valor do objetivo
                if self.tabuleiro[i][j] == self.pecaDaVitoria:
                    # Caso encontre, retorna "True"
                    return True

        # Caso passe por todas as casas e não encontre a peça com o valor do objetivo, retorna "False"
        return False

    def possuiMovimentosVailidos(self):
        '''
        Método que verifica todas as casas do tabuleiro.
        Retorna "True" se possui movimentos válidos ou "False" se não.
        self -> bool
        '''
        # Verifica as casas centrais
        # Passa pelas linhas, da segunda até a penúltima
        for i in range(1, len(self.tabuleiro) - 1):
            # Passa pelas colunas, da segunda até a penúltima
            for j in range(1, len(self.tabuleiro[i]) - 1):
                # Verifica se a casa pode se juntar com alguma outra casa ao redor
                # Se sim, retorna "True"
                if (
                    self.tabuleiro[i][j] == None or
                    self.tabuleiro[i][j] == self.tabuleiro[i + 1][j] or
                    self.tabuleiro[i][j] == self.tabuleiro[i - 1][j] or
                    self.tabuleiro[i][j] == self.tabuleiro[i][j + 1] or
                    self.tabuleiro[i][j] == self.tabuleiro[i][j - 1]
                ):
                    return True

        # Verifica as casas da borda superior
        # Passa pelas colunas, da segunda até a penúltima
        for j in range(1, len(self.tabuleiro[0]) - 1):
            # Verifica se a casa pode se juntar com alguma outra casa ao redor
                # Se sim, retorna "True"
                if (
                    self.tabuleiro[0][j] == None or
                    self.tabuleiro[0][j] == self.tabuleiro[0][j + 1] or
                    self.tabuleiro[0][j] == self.tabuleiro[0][j - 1]
                ):
                    return True
                    
        # Verifica as casas da borda inferior
        # Passa pelas colunas, da segunda até a penúltima
        for j in range(1, len(self.tabuleiro[0]) - 1):
            # Verifica se a casa pode se juntar com alguma outra casa ao redor
                # Se sim, retorna "True"
                if (
                    self.tabuleiro[len(self.tabuleiro) - 1][j] == None or
                    self.tabuleiro[len(self.tabuleiro) - 1][j] == self.tabuleiro[len(self.tabuleiro) - 1][j + 1] or
                    self.tabuleiro[len(self.tabuleiro) - 1][j] == self.tabuleiro[len(self.tabuleiro) - 1][j - 1]
                ):
                    return True

        # Verifica as casas da borda esquerda
        # Passa pelas linhas, da segunda até a penúltima
        for i in range(1, len(self.tabuleiro) - 1):
            # Verifica se a casa pode se juntar com alguma outra casa ao redor
                # Se sim, retorna "True"
                if (
                    self.tabuleiro[i][0] == None or
                    self.tabuleiro[i][0] == self.tabuleiro[i + 1][0] or
                    self.tabuleiro[i][0] == self.tabuleiro[i - 1][0]
                ):
                    return True

        # Verifica as casas da borda direita
        # Passa pelas linhas, da segunda até a penúltima
        for i in range(1, len(self.tabuleiro) - 1):
            # Verifica se a casa pode se juntar com alguma outra casa ao redor
                # Se sim, retorna "True"
                if (
                    self.tabuleiro[i][len(self.tabuleiro[0]) - 1] == None or
                    self.tabuleiro[i][len(self.tabuleiro[0]) - 1] == self.tabuleiro[i + 1][len(self.tabuleiro[0]) - 1] or
                    self.tabuleiro[i][len(self.tabuleiro[0]) - 1] == self.tabuleiro[i - 1][len(self.tabuleiro[0]) - 1]
                ):
                    return True

        # Caso não possua movimentos válidos, retorna "False"
        return False

    def getCasasVazias(self):
        '''
        Método que verifica todas as casas do tabuleiro.
        Retorna uma lista de strings com todas as posições de casas vazias.
        A primeira posição da string é a posição da linha e a segunda é a posição da coluna.
        self -> list
        '''
        # Lista para armazenar as posições vazias
        lista = []

        # Passa por todas as linhas
        for i in range(len(self.tabuleiro)):
            # Passa por todas as colunas
            for j in range(len(self.tabuleiro[i])):
                # Caso a casa possuir o elemento "None", adiciona na lista a posição da casa
                if self.tabuleiro[i][j] == None:
                    lista.append(f'{i}{j}')

        return lista

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

    def carregarJogo(self, tabuleiro, score):
        '''
        Método que atualiza os atributos com os dados do jogo salvo.
        self,list,int -> none
        '''
        self.tabuleiro = tabuleiro
        self.score = score