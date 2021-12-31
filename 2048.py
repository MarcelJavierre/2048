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
__maintainer__ = 'Marcel_Javierre'
__email__ = 'javierremarcel@poli.ufrj.br'
__status__ = 'Production'

# Classe da seção mecânica do jogo
class mecanicaDoJogo:
    'Esta classe é responsável por alterar a tela e o estado do jogo de acordo com os comandos do jogador'
    pass

# Classe da seção interface com o usuário
class interfaceComOUsuario:
    'Classe responsável por toda a interação com o usuário. Tudo que é pedido ao usuário ou mostrado para ele é função desta classe'
    def menuPrincipal():
        'Método para exibir ao usuário o menu principal do jogo'
        pass

    def telaDePause():
        'Método para exibir ao usuário a tela de pause do jogo'
        pass

    def telaDeSalvamentoCarregamento():
        'Método para exibir ao usuário a tela de salvamento/carregamento do jogo'
        pass

    def telaDeOpcoes():
        'Método para exibir ao usuário a tela de opções do jogo'
        pass

    def telaDoManual():
        'Método para exibir ao usuário a tela do manual do jogo'
        pass

    def telaDasEstatisticas():
        'Método para exibir ao usuário a tela de estatísticas do jogo'
        pass

# Classe da seção log
class log:
    'Esta classe trata do armazenamento em arquivos de todos os dados que podem vir a ser de interesse do usuário, bem como todos os erros que ocorrerem durante a execução do jogo'
    pass