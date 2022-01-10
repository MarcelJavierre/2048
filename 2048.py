"""
- Nome do jogo:
    2048

- Sobre o jogo:

    2048 é jogado em um tabuleiro de 4X4, com peças numéricas que deslizam suavemente quando o jogador as move em um dos quatro sentidos disponíveis: para cima, para baixo, à
    esquerda e à direita.

    Cada vez, um novo número aparece aleatoriamente em um local vazio na placa (com um valor de 2 ou 4).

    Os blocos deslizam o mais longe possível na direção escolhida até que eles sejam interrompidos por qualquer outro bloco ou a borda do tabuleiro. Se duas peças do mesmo número
    colidem durante a movimentação, elas irão se fundir em uma peça com o valor total das duas peças que colidiram.

    O jogo é vencido quando uma peça com o valor de 2048 aparece no tabuleiro. Quando o jogador não tem movimentos legais (não há espaços vazios e nem peças adjacentes com o mesmo
    valor), o jogo termina.
"""

# Propriedades do documento
__author__ = 'Marcel_Javierre'
__copyright__ = 'Copyright_2021'
__credits__ = __author__
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = __author__
__email__ = 'javierremarcel@poli.ufrj.br'
__status__ = 'Production'

# Importando as classes
from interfaceComOUsuario import *
from mecanicaDoJogo import *
from log import *

# Função principal
def main():
    pass

if __name__ == '__main__':
    main()