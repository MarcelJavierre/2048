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
__copyright__ = 'Copyright_2022'
__credits__ = __author__
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = __author__
__email__ = 'javierremarcel@poli.ufrj.br'
__status__ = 'Production'

# Importando as classes
from classes.interfaceComOUsuario import *
from classes.mecanicaDoJogo import *
from classes.log import *

# Função principal
def main():
    # Inicializando as instâncias de cada seção
    interface = InterfaceComOUsuario()
    mecanica = MecanicaDoJogo()
    log = Log()

    # Exibindo o menu principal
    interface.limpaTela()
    interface.menuPrincipal()

    # Recebendo a entrada do usuário
    entrada = interface.entradaDoUsuario()

    # Limpa a tela
    interface.limpaTela()

    # Verifica qual opção o usuário escolheu
    # Novo Jogo
    if entrada == '1':
        # Loop do jogo
        while True:
            # Mostra o tabuleiro
            interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore())

            # Espera a entrada do usuário
            entrada = interface.entradaDoUsuario()

            # Seleciona uma ação de acordo com a entrada do usuário
            if entrada == 'w':
                listaComAsMovimentacoes = mecanica.movePecas('cima')
            elif entrada == 'a':
                listaComAsMovimentacoes = mecanica.movePecas('esquerda')
            elif entrada == 's':
                listaComAsMovimentacoes = mecanica.movePecas('baixo')
            else:
                listaComAsMovimentacoes = mecanica.movePecas('direita')

            # Mostra na tela toda a movimentação das peças
            for i in range(len(listaComAsMovimentacoes)):
                interface.pausa(0.1)
                interface.limpaTela()
                interface.telaDoTabuleiro(listaComAsMovimentacoes[i], mecanica.getScore())

            # Verifica se o alguma peça atingiu o objetivo
            if mecanica.venceuOJogo() == True:
                # Se sim, coloca a variável "venceuOJogo" como "True" e encerra o loop do jogo
                venceuOJogo = True
                break

            # Verifica quais são as casas vazias do tabuleiro
            casasVazias = mecanica.getCasasVazias()

            # Caso o tabuleiro possua casas vazias, insere um nova peça
            if casasVazias != []:
                mecanica.inserePeca(casasVazias)

            # Caso não possua, verifica se ainda têm jogadas válidas
            else:
                # Verifica se ainda tem jogadas válidas
                if mecanica.possuiMovimentosVailidos() == False:
                    # Se não possuir, coloca a variável "venceuOJogo" como "False" e encerra o loop do jogo
                    venceuOJogo = False
                    break

            # Limpa a tela
            interface.limpaTela()

        # Volta para o menu principal
        interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
        main()

    # Carregar Jogo
    elif entrada == '2':
        print('Não Implementado')

        # Volta para o menu principal
        interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
        main()

    # Opções
    elif entrada == '3':
        print('Não Implementado')

        # Volta para o menu principal
        interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
        main()

    # Estatísticas
    elif entrada == '4':
        print('Não Implementado')

        # Volta para o menu principal
        interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
        main()

    # Manual do Desenvolvedor
    elif entrada == '5':
        # Mostra o título da tela
        interface.telaDoManual()
        
        # Escreve na tela a documentação de todas as classes do jogo
        print(interface, end = '')
        print(mecanica, end = '')
        print(log, end = '')

        # Volta para o menu principal
        interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
        main()

    # Sair do Jogo
    elif entrada == '6':
        quit()

    # Caso o usuário insira qualquer outra coisa diferente do pedido, exibe novamente o menu principal
    else:
        main()

if __name__ == '__main__':
    main()