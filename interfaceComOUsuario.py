# Importando a super classe com os métodos genéricos associados com a comunicação com o usuário
import ferramentasDeInterfaceComOUsuario

# Classe da seção interface com o usuário
class interfaceComOUsuario(ferramentasDeInterfaceComOUsuario):
    '''Classe responsável por toda a interação com o usuário. Tudo que é pedido ao usuário ou mostrado para ele é função desta classe'''

    def menuPrincipal(self):
        '''
        Método para exibir ao usuário o menu principal do jogo.
        self -> none
        '''
        pass

    def telaDePause(self):
        '''
        Método para exibir ao usuário a tela de pause do jogo.
        self -> none
        '''
        pass

    def telaDeSalvamentoCarregamento(self):
        '''
        Método para exibir ao usuário a tela de salvamento/carregamento do jogo.
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
        pass

    def telaDasEstatisticas(self):
        '''
        Método para exibir ao usuário a tela de estatísticas do jogo.
        self -> none
        '''
        pass

    def telaDoTabuleiro(self, matrizDoTabuleiro, score):
        '''
        Método para exibir a tela do tabuleiro do jogo.
        self,list,int -> none
        '''
        pass

    def telaDeFimDeJogo(self, score, foiVencedor):
        '''
        Método para exibir a tela de fim de jogo.
        self,int,bool -> none
        '''

        # Se foi vencedor, exibe a tela de vencedor
        if foiVencedor == True:
            pass

        # Se não, exibe a tela de perdedor
        else:
            pass