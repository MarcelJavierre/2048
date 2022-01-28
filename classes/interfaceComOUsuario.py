# Importando a super classe com os métodos genéricos associados com a comunicação com o usuário
if __name__ == '__main__':
    from ferramentasDeInterfaceComOUsuario import *

else:
    from classes.ferramentasDeInterfaceComOUsuario import *

# Função do módulo os para verificar as dimensões do terminal
from os import get_terminal_size

# Classe da seção interface com o usuário
class InterfaceComOUsuario(FerramentasDeInterfaceComOUsuario):
    '''Classe responsável por toda a interação com o usuário. Tudo que é pedido ao usuário ou mostrado para ele é função desta classe.'''

    def __init__(self):
        '''
        Método construtor.
        self -> none
        '''

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
            'telaDeFimDeJogo'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com todos os atributos e métodos da classe.
        self -> str
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
            'telaDeFimDeJogo': self.telaDeFimDeJogo.__doc__
        }

    def menuPrincipal(self):
        '''
        Método para exibir ao usuário o menu principal do jogo.
        self -> none
        '''
        print('\x1b[0;33m')
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

    def telaDePause(self):
        '''
        Método para exibir ao usuário a tela de pause do jogo.
        self -> none
        '''
        print('\n' * (int((get_terminal_size().lines - 9) / 2))) # Centraliza verticalmente a tela de pause
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
        print('\x1b[0;0m', end = '')

    def telaDeSalvamento(self):
        '''
        Método para exibir ao usuário a tela de salvamento do jogo.
        self -> none
        '''
        pass

    def telaDeCarregamento(self):
        '''
        Método para exibir ao usuário a tela de carregamento do jogo.
        self -> none
        '''
        pass

    def telaDeOpcoes(self):
        '''
        Método para exibir ao usuário a tela de opções do jogo.
        self -> none
        '''
        pass

    def telaDoManual(self):
        '''
        Método para exibir ao usuário a tela do manual do jogo.
        self -> none
        '''
        print('\x1b[0;31m')
        print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│   │   │ M │ A │ N │ U │ A │ L │   │ D │ O │   │   │'.center(get_terminal_size().columns))
        print('├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤'.center(get_terminal_size().columns))
        print('│ D │ E │ S │ E │ N │ V │ O │ L │ V │ E │ D │ O │ R │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print('\x1b[0;0m')

    def telaDasEstatisticas(self):
        '''
        Método para exibir ao usuário a tela de estatísticas do jogo.
        self -> none
        '''
        pass

    def telaDoTabuleiro(self, tabuleiro, score):
        '''
        Método para exibir a tela do tabuleiro do jogo.
        self,list,int -> none
        '''

        # Strings com as bordas do tabuleiro
        topoDaBordaDoTabuleiro = '┌──────' + '┬──────' * (len(tabuleiro[0]) - 1) + '┐'
        centroDaBordaDoTabuleiro = '├──────' + '┼──────' * (len(tabuleiro[0]) - 1) + '┤'
        fundoDaBordaDoTabuleiro = '└──────' + '┴──────' * (len(tabuleiro[0]) - 1) + '┘'
        espacoEntreOsNumeros = '│      ' * len(tabuleiro[0]) + '│'

        # Escreve na tela o score
        print('\n\n')
        print(f'Score:  {score}'.center(get_terminal_size().columns))
        print('\n\n')

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
                if tabuleiro[i][j] == None:
                    linhaComOValorDasPecas += f'│      '

                elif len(str(tabuleiro[i][j])) == 1:
                    linhaComOValorDasPecas += f'│  {tabuleiro[i][j]}   '

                elif len(str(tabuleiro[i][j])) == 2:
                    linhaComOValorDasPecas += f'│  {tabuleiro[i][j]}  '

                elif len(str(tabuleiro[i][j])) == 3:
                    linhaComOValorDasPecas += f'│ {tabuleiro[i][j]}  '

                else:
                    linhaComOValorDasPecas += f'│ {tabuleiro[i][j]} '

            linhaComOValorDasPecas += '│'

            print(linhaComOValorDasPecas.center(get_terminal_size().columns))
            print(espacoEntreOsNumeros.center(get_terminal_size().columns))

            # Caso seja a última iteração, não escreve na tela o centro do tabuleiro
            if i != (len(tabuleiro[i]) - 1):
                print(centroDaBordaDoTabuleiro.center(get_terminal_size().columns))
        print(fundoDaBordaDoTabuleiro.center(get_terminal_size().columns))

    def telaDeFimDeJogo(self, foiVencedor, score):
        '''
        Método para exibir a tela de fim de jogo.
        self,bool,int -> none
        '''

        # Se foi vencedor, exibe a tela de vencedor
        if foiVencedor == True:
            pass

        # Se não, exibe a tela de perdedor
        else:
            pass