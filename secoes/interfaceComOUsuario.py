'''
Módulo com a definição da classe InterfaceComOUsuario responsável pela
seção interface com o usuário.
'''

# Importando a função get_terminal_size do módulo os que retorna as dimensões do terminal
from os import get_terminal_size

# Importando o módulo matplotlib.pyplot com o apelido plt
import matplotlib.pyplot as plt

# Importando a super classe FerramentasDeInterfaceComOUsuario com os métodos genéricos associados com a comunicação com o usuário
from ferramentas.ferramentasDeInterfaceComOUsuario import *

# Importando a exceção ErroDeComando
from excecoes.erroDeComando import *

class InterfaceComOUsuario(FerramentasDeInterfaceComOUsuario):
    '''
    Classe responsável por toda a interação com o usuário. Tudo que é
    pedido ao usuário ou mostrado para ele é função desta classe.
    '''

    def __init__(self, tamanhoDoTabuleiro = 4):
        '''
        Método construtor.

        Self, int -> None
        '''
        # Atributo que armazena o tamanho do tabuleiro
        self.tamanhoDoTabuleiro = tamanhoDoTabuleiro

        # Atributos com as strings para construção do tabuleiro
        self.topoDaBordaDoTabuleiro = '┌──────' + '┬──────' * (self.tamanhoDoTabuleiro - 1) + '┐' # Atributo com a borda do topo do tabuleiro
        self.centroDaBordaDoTabuleiro = '├──────' + '┼──────' * (self.tamanhoDoTabuleiro - 1) + '┤' # Atributo com a borda do espaço entre os números do tabuleiro
        self.fundoDaBordaDoTabuleiro = '└──────' + '┴──────' * (self.tamanhoDoTabuleiro - 1) + '┘' # Atributo com a borda do fundo do tabuleiro
        self.espacoEntreOsNumeros = '│      ' * self.tamanhoDoTabuleiro + '│' # Atributo com o espaço entre os números do tabuleiro

        # Define o estilo dos gráficos
        plt.style.use('dark_background')

        # Conjunto com todos os atributos da classe
        self.__atributos = {
            'self.__atributos',
            'self.__metodos',
            'self.tamanhoDoTabuleiro',
            'self.topoDaBordaDoTabuleiro',
            'self.centroDaBordaDoTabuleiro',
            'self.fundoDaBordaDoTabuleiro',
            'self.espacoEntreOsNumeros'
        }

        # Conjunto com todos os métodos da classe
        self.__metodos = {
            '__init__',
            '__str__',
            'getAtributos',
            'getMetodos',
            'manual',
            'entradaDoUsuario',
            'limpaTela',
            'pausa',
            'menuPrincipal',
            'telaDePause',
            'telaDeSalvamento',
            'telaDeCarregamento',
            'telaDeOpcoes',
            'telaDoManual',
            'telaDasEstatisticas',
            'telaDoTabuleiro',
            'telaDeFimDeJogo',
            'telaDosControles'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com
        todos os atributos e métodos da classe.

        Self -> str
        '''

        string = f'Classe InterfaceComOUsuario:\n{InterfaceComOUsuario.__doc__}\n\nAtributos:\n'

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
            'self.tamanhoDoTabuleiro': 'Atributo que armazena o tamanho do tabuleiro.',
            'self.topoDaBordaDoTabuleiro': 'Atributo com a borda do topo do tabuleiro.',
            'self.centroDaBordaDoTabuleiro': 'Atributo com a borda do espaço entre os números do tabuleiro.',
            'self.fundoDaBordaDoTabuleiro': 'Atributo com a borda do fundo do tabuleiro.',
            'self.espacoEntreOsNumeros': 'Atributo com o espaço entre os números do tabuleiro.',
            '__init__': self.__init__.__doc__,
            '__str__': self.__str__.__doc__,
            'getAtributos': self.getAtributos.__doc__,
            'getMetodos': self.getMetodos.__doc__,
            'manual': self.manual.__doc__,
            'entradaDoUsuario': self.entradaDoUsuario.__doc__,
            'limpaTela': self.limpaTela.__doc__,
            'pausa': self.pausa.__doc__,
            'menuPrincipal': self.menuPrincipal.__doc__,
            'telaDePause': self.telaDePause.__doc__,
            'telaDeSalvamento': self.telaDeSalvamento.__doc__,
            'telaDeCarregamento': self.telaDeCarregamento.__doc__,
            'telaDeOpcoes': self.telaDeOpcoes.__doc__,
            'telaDoManual': self.telaDoManual.__doc__,
            'telaDasEstatisticas': self.telaDasEstatisticas.__doc__,
            'telaDoTabuleiro': self.telaDoTabuleiro.__doc__,
            'telaDeFimDeJogo': self.telaDeFimDeJogo.__doc__,
            'telaDosControles': self.telaDosControles.__doc__
        }

    def menuPrincipal(self):
        '''
        Método para exibir ao usuário o menu principal do jogo. Retorna
        a entrada do usuário. Gera um ErroDeComando caso entrada não
        seja válida.

        Self -> str
        '''
        # Mostra a tela do menu principal
        print('\n' * (int((get_terminal_size().lines - 28) / 2)), end = '') # Centraliza verticalmente a tela do menu principal
        print('\x1b[0;33m', end = '')
        print("┌──────────────────┐┌──────────────────┐┌──────────────────┐┌──────────────────┐".center(get_terminal_size().columns))
        print("│ ┌──────────────┐ ││ ┌──────────────┐ ││ ┌──────────────┐ ││ ┌──────────────┐ │".center(get_terminal_size().columns))
        print("│ │    _____     │ ││ │     ____     │ ││ │   _    _     │ ││ │     ____     │ │".center(get_terminal_size().columns))
        print("│ │   / ___ `.   │ ││ │   .'    '.   │ ││ │  │ │  │ │    │ ││ │   .' __ '.   │ │".center(get_terminal_size().columns))
        print("│ │  │_/___) │   │ ││ │  │  .--.  │  │ ││ │  │ │__│ │_   │ ││ │   │ (__) │   │ │".center(get_terminal_size().columns))
        print("│ │   .'____.'   │ ││ │  │ │    │ │  │ ││ │  │____   _│  │ ││ │   .`____'.   │ │".center(get_terminal_size().columns))
        print("│ │  / /____     │ ││ │  │  `--'  │  │ ││ │      _│ │_   │ ││ │  │ (____) │  │ │".center(get_terminal_size().columns))
        print("│ │  │_______│   │ ││ │   '.____.'   │ ││ │     │_____│  │ ││ │  `.______.'  │ │".center(get_terminal_size().columns))
        print("│ │              │ ││ │              │ ││ │              │ ││ │              │ │".center(get_terminal_size().columns))
        print("│ └──────────────┘ ││ └──────────────┘ ││ └──────────────┘ ││ └──────────────┘ │".center(get_terminal_size().columns))
        print("└──────────────────┘└──────────────────┘└──────────────────┘└──────────────────┘".center(get_terminal_size().columns))
        print('')
        print('')
        print('\x1b[0;32m', end = '')
        print('┌───┬─────────────────────────┐'.center(get_terminal_size().columns))
        print('│ 1 │         Novo Jogo       │'.center(get_terminal_size().columns))
        print('\x1b[0;96m', end = '')
        print('├───┼─────────────────────────┤'.center(get_terminal_size().columns))
        print('│ 2 │      Carregar Jogo      │'.center(get_terminal_size().columns))
        print('\x1b[0;34m', end = '')
        print('├───┼─────────────────────────┤'.center(get_terminal_size().columns))
        print('│ 3 │          Opções         │'.center(get_terminal_size().columns))
        print('\x1b[0;35m', end = '')
        print('├───┼─────────────────────────┤'.center(get_terminal_size().columns))
        print('│ 4 │       Estatísticas      │'.center(get_terminal_size().columns))
        print('\x1b[0;31m', end = '')
        print('├───┼─────────────────────────┤'.center(get_terminal_size().columns))
        print('│ 5 │ Manual do Desenvolvedor │'.center(get_terminal_size().columns))
        print('├───┼─────────────────────────┤'.center(get_terminal_size().columns))
        print('\x1b[0;38;5;130m', end = '')
        print('│ 6 │       Sair do Jogo      │'.center(get_terminal_size().columns))
        print('└───┴─────────────────────────┘'.center(get_terminal_size().columns))
        print('')
        print('\x1b[0;0m')

        # Recebe a entrada do usuário
        entrada = self.entradaDoUsuario()

        # Verifica se a entrada é válida
        if entrada not in ('1', '2', '3', '4', '5', '6'):
            # Se não for, gera o erro "ErroDeComando"
            raise ErroDeComando(f'A entrada "{entrada}" nao e valida')

        else:
            # Se for, retorna a entrada
            return entrada

    def telaDePause(self):
        '''
        Método para exibir ao usuário a tela de pause do jogo. Retorna a
        entrada do usuário. Gera um ErroDeComando caso entrada não seja
        válida.

        Self -> str
        '''
        # Mostra a tela de pause
        print('\n' * (int((get_terminal_size().lines - 10) / 2)), end = '') # Centraliza verticalmente a tela de pause
        print('\x1b[0;33m', end = '')
        print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│   │   │   │   │   │   │ P │ A │ U │ S │ E │   │   │   │   │   │   │'.center(get_terminal_size().columns))
        print('├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'.center(get_terminal_size().columns))
        print('│ 1 │   │ V │ O │ L │ T │ A │ R │   │ A │ O │   │ J │ O │ G │ O │   │'.center(get_terminal_size().columns))
        print('├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'.center(get_terminal_size().columns))
        print('│ 2 │   │ S │ A │ L │ V │ A │ R │   │ O │   │ J │ O │ G │ O │   │   │'.center(get_terminal_size().columns))
        print('├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'.center(get_terminal_size().columns))
        print('│ 3 │   │ V │ O │ L │ T │ A │ R │   │ A │ O │   │ M │ E │ N │ U │   │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print('\x1b[0;0m')

        # Recebe a entrada do usuário
        entrada = self.entradaDoUsuario()

        # Verifica se a entrada é válida
        if entrada not in ('1', '2', '3'):
            # Se não for, gera o erro "ErroDeComando"
            raise ErroDeComando(f'A entrada "{entrada}" nao e valida')

        else:
            # Se for, retorna a entrada
            return entrada

    def telaDeSalvamento(self):
        '''
        Método para exibir ao usuário a tela de salvamento do jogo.

        Self -> None
        '''
        print('\n' * (int((get_terminal_size().lines - 3) / 2)), end = '') # Centraliza verticalmente a tela de salvamento
        print('\x1b[0;96m', end = '')
        print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│ J │ O │ G │ O │   │ S │ A │ L │ V │ O │ ! │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print('\x1b[0;0m', end = '')

    def telaDeCarregamento(self, dadosDasPartidasSalvas):
        '''
        Método para exibir ao usuário a tela de carregamento das
        partidas salvas.

        Self, list[str] -> str
        '''
        print('\x1b[0;96m')
        print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│ P │ A │ R │ T │ I │ D │ A │ S │   │ S │ A │ L │ V │ A │ S │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print('')

        # Verifica se possui alguma partida salva
        # Caso possua, escreve na tela uma lista com todas as partidas salvas
        if dadosDasPartidasSalvas != []:
            # Passa por todas as partidas salvas
            # De 7 em 7 por causa da quantidade de linhas que cada partida salva ocupa
            for x in range(0, len(dadosDasPartidasSalvas), 7):
                # Escreve na tela o índice da partida salva
                print(f'{int(x / 5 + 1)}'.center(get_terminal_size().columns))
                print('─────────────────────────────────────────────'.center(get_terminal_size().columns))

                # Escreve na tela a data e hora da partida salva
                print(dadosDasPartidasSalvas[x][: - 1].center(get_terminal_size().columns))

                # Escreve na tela o objetivo da partida salva
                print(f'OBJETIVO:    {dadosDasPartidasSalvas[x + 2][: - 1]}'.center(get_terminal_size().columns))

                # Escreve na tela o score da partida salva
                print(f'SCORE:    {dadosDasPartidasSalvas[x + 4][: - 1]}'.center(get_terminal_size().columns))

                # Escreve na tela o tabuleiro da partida salva
                # Converte a string do tabuleiro de volta para lista
                tabuleiro = eval(dadosDasPartidasSalvas[x + 3][: - 1])

                # Strings com as bordas do tabuleiro
                topoDaBordaDoTabuleiro = '┌──────' + '┬──────' * (len(tabuleiro[0]) - 1) + '┐'
                centroDaBordaDoTabuleiro = '├──────' + '┼──────' * (len(tabuleiro[0]) - 1) + '┤'
                fundoDaBordaDoTabuleiro = '└──────' + '┴──────' * (len(tabuleiro[0]) - 1) + '┘'
                espacoEntreOsNumeros = '│      ' * len(tabuleiro[0]) + '│'

                # Escreve na tela o tabuleiro
                print(topoDaBordaDoTabuleiro.center(get_terminal_size().columns))
                # Passa por todas as linhas
                for i in range(len(tabuleiro)):
                    print(espacoEntreOsNumeros.center(get_terminal_size().columns))

                    # Variável para armazenar a linha do tabuleiro
                    linhaComOValorDasPecas = ''

                    # Passa por todas as colunas
                    for j in range(len(tabuleiro[i])):
                        # Determina o espaço do número dependendo de quantas casas o número possui
                        if tabuleiro[i][j] == 0:
                            linhaComOValorDasPecas += f'│      '

                        elif len(str(tabuleiro[i][j])) == 1:
                            linhaComOValorDasPecas += f'│  {tabuleiro[i][j]}   '

                        elif len(str(tabuleiro[i][j])) == 2:
                            linhaComOValorDasPecas += f'│  {tabuleiro[i][j]}  '

                        elif len(str(tabuleiro[i][j])) == 3:
                            linhaComOValorDasPecas += f'│ {tabuleiro[i][j]}  '

                        elif len(str(tabuleiro[i][j])) == 4:
                            linhaComOValorDasPecas += f'│ {tabuleiro[i][j]} '

                        elif len(str(tabuleiro[i][j])) == 5:
                            linhaComOValorDasPecas += f'│{tabuleiro[i][j]} '

                        else:
                            linhaComOValorDasPecas += f'│{tabuleiro[i][j]}'

                    linhaComOValorDasPecas += '│'

                    print(linhaComOValorDasPecas.center(get_terminal_size().columns))
                    print(espacoEntreOsNumeros.center(get_terminal_size().columns))

                    # Caso seja a última iteração, não escreve na tela o centro do tabuleiro
                    if i != (len(tabuleiro[i]) - 1):
                        print(centroDaBordaDoTabuleiro.center(get_terminal_size().columns))
                print(fundoDaBordaDoTabuleiro.center(get_terminal_size().columns))
                print('')

            print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
            print('│ 1 │   │ C │ A │ R │ R │ E │ G │ A │ R │   │ J │ O │ G │ O │   │'.center(get_terminal_size().columns))
            print('├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'.center(get_terminal_size().columns))
            print('│ 2 │   │ A │ P │ A │ G │ A │ R │   │ P │ A │ R │ T │ I │ D │ A │'.center(get_terminal_size().columns))
            print('├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'.center(get_terminal_size().columns))
            print('│ 3 │   │ V │ O │ L │ T │ A │ R │   │ A │ O │   │ M │ E │ N │ U │'.center(get_terminal_size().columns))
            print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
            print('\x1b[0;0m')

            # Recebe a entrada do usuário
            entrada = self.entradaDoUsuario()

            # Verifica se a entrada é válida
            if entrada not in ('1', '2', '3'):
                # Se não for, gera o erro "ErroDeComando"
                raise ErroDeComando(f'A entrada "{entrada}" nao e valida')

            else:
                # Se for, retorna a entrada
                return entrada

        # Se não possuir, mostra uma tela diferente
        else:
            print('Não há partidas salvas!'.center(get_terminal_size().columns))
            print('─────────────────────────────────────────────'.center(get_terminal_size().columns))
            print('\x1b[0;0m')

            return self.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')

    def telaDeOpcoes(self, tamanhoDoTabuleiro, objetivo):
        '''
        Método para exibir ao usuário a tela de opções do jogo. Retorna
        a entrada do usuário. Gera um ErroDeComando caso entrada não
        seja válida.

        Self, int, int -> str
        '''
        # Mostra a tela de opções
        print('\n' * (int((get_terminal_size().lines - 24) / 2)), end = '') # Centraliza verticalmente a tela de opções
        print('\x1b[0;34m', end = '')
        print('┌───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│ O │ P │ Ç │ Õ │ E │ S │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print('')

        print('\x1b[0;94m', end = '')
        print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│ T │ A │ M │ A │ N │ H │ O │   │ D │ O │   │ T │ A │ B │ U │ L │ E │ I │ R │ O │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print(f'{tamanhoDoTabuleiro}'.center(get_terminal_size().columns))
        print('─────────────────────────────────────────────────'.center(get_terminal_size().columns))
        print('')

        print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│   │   │ O │ B │ J │ E │ T │ I │ V │ O │   │ D │ O │   │ J │ O │ G │ O │   │   │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print(f'{objetivo}'.center(get_terminal_size().columns))
        print('─────────────────────────────────────────────────'.center(get_terminal_size().columns))
        print('')

        print('\x1b[0;34m', end = '')
        print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│ 1 │   │ A │ L │ T │ E │ R │ A │ R │   │ T │ A │ M │ A │ N │ H │ O │   │'.center(get_terminal_size().columns))
        print('├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'.center(get_terminal_size().columns))
        print('│ 2 │   │ A │ L │ T │ E │ R │ A │ R │   │ O │ B │ J │ E │ T │ I │ V │ O │'.center(get_terminal_size().columns))
        print('├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'.center(get_terminal_size().columns))
        print('│ 3 │   │ V │ O │ L │ T │ A │ R │   │ A │ O │   │ M │ E │ N │ U │   │   │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print('\x1b[0;0m')

        # Recebe a entrada do usuário
        entrada = self.entradaDoUsuario()

        # Verifica se a entrada é válida
        if entrada not in ('1', '2', '3'):
            # Se não for, gera o erro "ErroDeComando"
            raise ErroDeComando(f'A entrada "{entrada}" nao e valida')

        else:
            # Se for, retorna a entrada
            return entrada

    def telaDoManual(self):
        '''
        Método para exibir ao usuário a tela do manual do jogo.

        Self -> None
        '''
        print('\x1b[0;31m')
        print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│   │   │ M │ A │ N │ U │ A │ L │   │ D │ O │   │   │'.center(get_terminal_size().columns))
        print('├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'.center(get_terminal_size().columns))
        print('│ D │ E │ S │ E │ N │ V │ O │ L │ V │ E │ D │ O │ R │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print('\x1b[0;0m')

    def telaDasEstatisticas(self, estatisticasDeJogadas, estatisticasDePecas, estatisticasDeScore, estatisticasDeFusoes):
        '''
        Método para exibir ao usuário a tela de estatísticas do jogo.

        Self,
        tuple[numpy.ndarray[str], numpy.ndarray[int]],
        tuple[numpy.ndarray[str], numpy.ndarray[int]],
        tuple[numpy.ndarray[int]] -> None
        '''
        # Define o formato 2x2 para a organização dos gráficos
        FORMATO = (2, 2)

        # Define a figura dos gráficos
        figura = plt.figure('2048 - Estatísticas', (15, 8))

        # Define os eixos
        eixoDasEstatisticasDeJogadas = plt.subplot2grid(FORMATO, (0, 0), fig = figura)
        eixoDasEstatisticasDePecas = plt.subplot2grid(FORMATO, (0, 1), fig = figura)
        eixoDasEstatisticasDeScore = plt.subplot2grid(FORMATO, (1, 0), fig = figura)
        eixoDasEstatisticasDeFusoes = plt.subplot2grid(FORMATO, (1, 1), fig = figura)

        # Ajusta o espaçamento entre os gráficos
        plt.subplots_adjust(hspace = 0.5)

        # Gráfico das estatísticas de jogadas
        eixoDasEstatisticasDeJogadas.pie(
            estatisticasDeJogadas[1],
            labels = estatisticasDeJogadas[0],
            colors = ('red', 'green', 'blue', 'purple'),
            autopct = lambda porcentagem: f'{porcentagem: .2f}%' if porcentagem > 0 else ''
        )
        eixoDasEstatisticasDeJogadas.set_title('Jogadas')

        # Gráfico das estatísticas de peças
        eixoDasEstatisticasDePecas.bar(estatisticasDePecas[0], estatisticasDePecas[1], color = 'yellow')
        eixoDasEstatisticasDePecas.set_xlabel('Peça')
        eixoDasEstatisticasDePecas.set_ylabel('Quantidade')
        eixoDasEstatisticasDePecas.set_title('Maior Peça de Cada Partida')

        # Gráfico das estatísticas de scores
        eixoDasEstatisticasDeScore.plot(estatisticasDeScore[0], estatisticasDeScore[1], 'orange')
        eixoDasEstatisticasDeScore.set_xlabel('Partidas')
        eixoDasEstatisticasDeScore.set_ylabel('Score')
        eixoDasEstatisticasDeScore.set_title('Histórico de Score')

        # Gráfico das estatísticas de fusões
        eixoDasEstatisticasDeFusoes.plot(estatisticasDeFusoes[0], estatisticasDeFusoes[1], color = 'cyan')
        eixoDasEstatisticasDeFusoes.set_xlabel('Partidas')
        eixoDasEstatisticasDeFusoes.set_ylabel('Fusões')
        eixoDasEstatisticasDeFusoes.set_title('Total de Fusões')

        # Mostra o gráfico
        plt.show()

    def telaDoTabuleiro(self, tabuleiro, score, objetivo, recebeEntradaDoUsuario = False):
        '''
        Método para exibir a tela do tabuleiro do jogo. Caso o parâmetro
        "recebeEntradaDoUsuario" for "True", retorna a entrada do
        usuário. Gera um ErroDeComando caso entrada não seja válida.

        Self, numpy.ndarray[int], int, int, bool -> str | None
        '''
        # Escreve na tela os dados da partida
        print('\x1b[0;0m')
        print(f'OBJETIVO:    {objetivo}'.center(get_terminal_size().columns))
        print(f'SCORE:    {score}'.center(get_terminal_size().columns))
        print(('─' * len(self.topoDaBordaDoTabuleiro)).center(get_terminal_size().columns))

        # Escreve na tela o tabuleiro
        # Variável para centralizar o tabuleiro
        margem = int((get_terminal_size().columns - len(self.topoDaBordaDoTabuleiro)) / 2)

        # Escreve na tela o topo da borda do tabuleiro
        print(' ' * margem, end = '')
        print(self.topoDaBordaDoTabuleiro)

        # Passa por todas as linhas
        for i in range(self.tamanhoDoTabuleiro):
            # Escreve o espaço entre a borda e os números
            print(' ' * margem, end = '')
            print(self.espacoEntreOsNumeros)

            # Variável para armazenar a linha do tabuleiro
            linhaComOValorDasPecas = ''

            # Passa por todas as colunas
            for j in range(self.tamanhoDoTabuleiro):
                # Determina o espaço do número dependendo de quantas casas o número possui
                if tabuleiro[i][j] == 0:
                    linhaComOValorDasPecas += f'│      '

                elif len(str(tabuleiro[i][j])) == 1:
                    linhaComOValorDasPecas += f'│  {tabuleiro[i][j]}   '

                elif len(str(tabuleiro[i][j])) == 2:
                    linhaComOValorDasPecas += f'│  \x1b[0;31m{tabuleiro[i][j]}\x1b[0;0m  '

                elif len(str(tabuleiro[i][j])) == 3:
                    linhaComOValorDasPecas += f'│ \x1b[0;33m{tabuleiro[i][j]}\x1b[0;0m  '

                elif len(str(tabuleiro[i][j])) == 4:
                    linhaComOValorDasPecas += f'│ \x1b[0;33m{tabuleiro[i][j]}\x1b[0;0m '

                elif len(str(tabuleiro[i][j])) == 5:
                    linhaComOValorDasPecas += f'│\x1b[0;32m{tabuleiro[i][j]}\x1b[0;0m '

                else:
                    linhaComOValorDasPecas += f'│\x1b[0;34m{tabuleiro[i][j]}\x1b[0;0m'

            linhaComOValorDasPecas += '│'

            # Escreve na tela a linha com os números das casas
            print(' ' * margem, end = '')
            print(linhaComOValorDasPecas)

            # Escreve o espaço entre a borda e os números
            print(' ' * margem, end = '')
            print(self.espacoEntreOsNumeros)

            # Caso seja a última iteração, não escreve na tela o centro do tabuleiro
            if i != (self.tamanhoDoTabuleiro - 1):
                print(' ' * margem, end = '')
                print(self.centroDaBordaDoTabuleiro)

        # Escreve na tela o fundo da borda do tabuleiro
        print(' ' * margem, end = '')
        print(self.fundoDaBordaDoTabuleiro)

        # Caso o parâmentro "recebeEntradaDoUsuario" for "True", recebe a entrada do usuário
        if recebeEntradaDoUsuario == True:
            # Recebe a entrada do usuário
            entrada = self.entradaDoUsuario()

            # Verifica se a entrada é válida
            if entrada not in ('w', 'a', 's', 'd', 'p'):
                # Se não for, gera o erro "ErroDeComando"
                raise ErroDeComando(f'A entrada "{entrada}" nao e valida')

            else:
                # Se for, retorna a entrada
                if entrada == 'w':
                    return 'cima'
                elif entrada == 'a':
                    return 'esquerda'
                elif entrada == 's':
                    return 'baixo'
                elif entrada == 'd':
                    return 'direita'
                else:
                    return entrada

        # Caso contrário, retorna "None"
        else:
            return None

    def telaDeFimDeJogo(self, foiVencedor, score, valorDaMaiorPeca, quantidadeDeFusoes):
        '''
        Método para exibir a tela de fim de jogo.

        Self, bool, int, int, int -> None
        '''
        print('\n' * (int((get_terminal_size().lines - 10) / 2)), end = '') # Centraliza verticalmente a tela de fim de jogo

        # Se foi vencedor, exibe "VOCÊ VENCEU!"
        if foiVencedor == True:
            print('\x1b[0;33m', end = '')
            print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
            print('│ V │ O │ C │ Ê │   │ V │ E │ N │ C │ E │ U │ ! │'.center(get_terminal_size().columns))

        # Se não, exibe "VOCÊ PERDEU!"
        else:
            print('\x1b[0;31m', end = '')
            print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
            print('│ V │ O │ C │ Ê │   │ P │ E │ R │ D │ E │ U │ ! │'.center(get_terminal_size().columns))

        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print('\x1b[0;32m')

        # Exibe as estatísticas da partida
        print('───────────────────────────────────'.center(get_terminal_size().columns))
        print(f'SCORE:    {score}'.center(get_terminal_size().columns))
        print(f'MAIOR PEÇA NO TABULEIRO:    {valorDaMaiorPeca}'.center(get_terminal_size().columns))
        print(f'QUANTIDADE DE FUSÕES:    {quantidadeDeFusoes}'.center(get_terminal_size().columns))
        print('───────────────────────────────────'.center(get_terminal_size().columns))
        print('\x1b[0;0m')

    def telaDosControles(self):
        '''
        Método para exibir a tela com os controles do jogo.

        Self -> None
        '''
        print('\n' * (int((get_terminal_size().lines - 20) / 2)), end = '') # Centraliza verticalmente a tela de fim de controles
        print('\x1b[0;33m', end = '')
        print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│ C │ O │ N │ T │ R │ O │ L │ E │ S │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print('')

        print('Movimentação'.center(get_terminal_size().columns))
        print('─────────────────────────────────────'.center(get_terminal_size().columns))
        print('    ┌───┐                   ┌──────┐ '.center(get_terminal_size().columns))
        print('    │ W │         ┌───┐     │      │ '.center(get_terminal_size().columns))
        print('┌───┼───┼───┐     │ + │     └┐Enter│ '.center(get_terminal_size().columns))
        print('│ A │ S │ D │     └───┘      │     │ '.center(get_terminal_size().columns))
        print('└───┴───┴───┘                └─────┘ '.center(get_terminal_size().columns))
        print('')

        print('Pause'.center(get_terminal_size().columns))
        print('─────────────────────────────────────'.center(get_terminal_size().columns))
        print('                            ┌──────┐ '.center(get_terminal_size().columns))
        print('    ┌───┐         ┌───┐     │      │ '.center(get_terminal_size().columns))
        print('    │ P │         │ + │     └┐Enter│ '.center(get_terminal_size().columns))
        print('    └───┘         └───┘      │     │ '.center(get_terminal_size().columns))
        print('                             └─────┘ '.center(get_terminal_size().columns))
        print('\x1b[0;0m')
