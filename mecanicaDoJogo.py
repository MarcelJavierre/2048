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