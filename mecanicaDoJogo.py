# Importando a super classe com os métodos genéricos associados com a mecânica do jogo
import ferramentasDeMecanicaDoJogo

# Classe da seção mecânica do jogo
class mecanicaDoJogo(ferramentasDeMecanicaDoJogo):
    '''Esta classe contém todos os métodos responsável por alterar a tela e o estado do jogo de acordo com os comandos do jogador'''

    def __init__(self, tamanhoDoTabuleiro = 4):
        '''
        Inicializa o tabuleiro. Se nenhum parâmetro for passado, inicializa com o tamanho padrão 4X4.
        self,int -> none
        '''
        self.tabuleiro = ferramentasDeMecanicaDoJogo.geraMatriz(self, tamanhoDoTabuleiro, tamanhoDoTabuleiro)
        self.score = 0

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
        return None

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