# Importando a função "get_terminal_size" do módulo "os" que retorna as dimensões do terminal
from os import get_terminal_size

# Importando o módulo "matplotlib.pyplot" com o apelido "plt"
import matplotlib.pyplot as plt

# Importando a super classe "FerramentasDeInterfaceComOUsuario" com os métodos genéricos associados com a comunicação com o usuário
if __name__ == '__main__':
    from ferramentasDeInterfaceComOUsuario import *

else:
    from classes.ferramentasDeInterfaceComOUsuario import *

# Importando as definições das cores utilizadas
from configuracoes.cores import *

# Importando as definições das fontes utilizadas
from configuracoes.fontes import *

# Classe da seção interface com o usuário
class InterfaceComOUsuario(FerramentasDeInterfaceComOUsuario):
    '''
    Classe responsável por toda a interação com o usuário. Tudo que é
    pedido ao usuário ou mostrado para ele é função desta classe.
    '''

    def __init__(self):
        '''
        Método construtor. Inicializa os componentes de todas as telas.

        Self -> None
        '''
        # Atributo com a janela do jogo
        self.janela = Tk()

        # Configurações da janela
        self.janela.title('2048') # Define o título "2048" para a janela
        self.janela.geometry('1280x720') # Define o tamanho "1280x720" para a janela
        self.janela.configure(bg = COR_DO_FUNDO) # Define a cor de fundo da janela
        self.janela.rowconfigure(0, weight = 1) # Configura o posicionamento da linha com o redimensionamento da janela
        self.janela.columnconfigure(0, weight = 1) # Configura o posicionamento da coluna com o redimensionamento da janela

        # Atributos com os componentes do menu principal
        self.quadroDoMenuPrincipal = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo do menu principal

        self.logo = PhotoImage(file = 'imagens/logo.png') # Atributo com a imagem da logo
        self.titulo = Canvas( # Atributo com o título do menu principal
            master = self.quadroDoMenuPrincipal,
            width = self.logo.width(),
            height = self.logo.height(),
            background = COR_DO_FUNDO,
            highlightthickness = 0
        )
        self.titulo.create_image(0, 0, image = self.logo, anchor = 'nw') # Insere a logo no título
        self.titulo.grid(row = 0, column = 0, pady = 20) # Insere o título no quadro

        self.botaoNovoJogo = Button( # Atributo com o botão "Novo Jogo"
            master = self.quadroDoMenuPrincipal,
            text = 'Novo Jogo',
            font = FONTE_TAMANHO_14,
            fg = VERDE,
            activeforeground = VERDE_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoNovoJogo.grid(row = 1, column = 0) # Insere o botão no quadro
        self.botaoNovoJogo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoNovoJogo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoNovoJogo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoNovoJogo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        self.botaoCarregarJogo = Button( # Atributo com o botão "Carregar Jogo"
            master = self.quadroDoMenuPrincipal,
            text = 'Carregar Jogo',
            font = FONTE_TAMANHO_14,
            fg = CIANO,
            activeforeground = CIANO_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoCarregarJogo.grid(row = 2, column = 0) # Insere o botão no quadro
        self.botaoCarregarJogo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoCarregarJogo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoCarregarJogo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoCarregarJogo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        self.botaoOpcoes = Button( # Atributo com o botão "Opções"
            master = self.quadroDoMenuPrincipal,
            text = 'Opções',
            font = FONTE_TAMANHO_14,
            fg = AZUL,
            activeforeground = AZUL_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoOpcoes.grid(row = 3, column = 0) # Insere o botão no quadro
        self.botaoOpcoes.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoOpcoes, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoOpcoes.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoOpcoes, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        self.botaoEstatisticas = Button( # Atributo com o botão "Estatísticas"
            master = self.quadroDoMenuPrincipal,
            text = 'Estatísticas',
            font = FONTE_TAMANHO_14,
            fg = ROXO,
            activeforeground = ROXO_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoEstatisticas.grid(row = 4, column = 0) # Insere o botão no quadro
        self.botaoEstatisticas.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoEstatisticas, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoEstatisticas.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoEstatisticas, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        self.botaoManualDoDesenvolvedor = Button( # Atributo com o botão "Manual do Desenvolvedor"
            master = self.quadroDoMenuPrincipal,
            text = 'Manual do Desenvolvedor',
            font = FONTE_TAMANHO_14,
            fg = VERMELHO,
            activeforeground = VERMELHO_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoManualDoDesenvolvedor.grid(row = 5, column = 0) # Insere o botão no quadro
        self.botaoManualDoDesenvolvedor.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoManualDoDesenvolvedor, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoManualDoDesenvolvedor.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoManualDoDesenvolvedor, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        self.botaoSairDoJogo = Button( # Atributo com o botão "Sair do Jogo"
            master = self.quadroDoMenuPrincipal,
            text = 'Sair do Jogo',
            font = FONTE_TAMANHO_14,
            fg = LARANJA,
            activeforeground = LARANJA_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0,
            command = quit
        )
        self.botaoSairDoJogo.grid(row = 6, column = 0) # Insere o botão no quadro
        self.botaoSairDoJogo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoSairDoJogo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoSairDoJogo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoSairDoJogo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        # Atributos com os componentes da tela do tabuleiro
        self.quadroDaTelaDoTabuleiro = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela do tabuleiro

        self.score = Label( # Atributo com a "Label" do score
            master = self.quadroDaTelaDoTabuleiro,
            font = FONTE_TAMANHO_18,
            fg = VERDE,
            bg = COR_DO_FUNDO
        )
        self.score.grid(row = 0, column = 0)

        self.objetivo = Label( # Atributo com a "Label" do objetivo
            master = self.quadroDaTelaDoTabuleiro,
            font = FONTE_TAMANHO_18,
            fg = VERDE,
            bg = COR_DO_FUNDO
        )
        self.objetivo.grid(row = 1, column = 0)

        self.tabuleiro = Frame(master = self.quadroDaTelaDoTabuleiro, bg = '#a39489', borderwidth = 5) # Atributo com o "Frame" do tabuleiro
        self.tabuleiro.grid(row = 2, column = 0, pady = 20)

        # Atributos com os componentes da tela de fim de jogo
        self.quadroDaTelaDeVitoria = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela de vitória
        self.quadroDaTelaDeDerrota = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela de derrota

        self.vitoria = Label( # Atributo com a "Label" do título da tela de vitória
            master = self.quadroDaTelaDeVitoria,
            text = 'Você Venceu!',
            font = FONTE_TAMANHO_32_EM_NEGRITO,
            fg = AMARELO,
            bg = COR_DO_FUNDO
        )
        self.vitoria.grid(row = 0, column = 0, pady = 20)

        self.scoreDaTelaDeVitoria = Label( # Atributo com a "Label" do score da tela de vitória
            master = self.quadroDaTelaDeVitoria,
            font = FONTE_TAMANHO_16,
            fg = CIANO,
            bg = COR_DO_FUNDO
        )
        self.scoreDaTelaDeVitoria.grid(row = 1, column = 0)

        self.voltarAoMenuPrincipalDaTelaDeVitoria = Label( # Atributo com a "Label" da tela de vitória para voltar ao menu principal
            master = self.quadroDaTelaDeVitoria,
            text = 'Aperte Qualquer Tecla para Voltar ao Menu Principal',
            font = FONTE_TAMANHO_16,
            fg = ROXO,
            bg = COR_DO_FUNDO
        )
        self.voltarAoMenuPrincipalDaTelaDeVitoria.grid(row = 2, column = 0, pady = 20)

        self.derrota = Label( # Atributo com a "Label" do título da tela de derrota
            master = self.quadroDaTelaDeDerrota,
            text = 'Você Perdeu!',
            font = FONTE_TAMANHO_32_EM_NEGRITO,
            fg = VERMELHO,
            bg = COR_DO_FUNDO
        )
        self.derrota.grid(row = 0, column = 0, pady = 20)

        self.scoreDaTelaDeDerrota = Label( # Atributo com a "Label" do score da tela de derrota
            master = self.quadroDaTelaDeDerrota,
            font = FONTE_TAMANHO_16,
            fg = VERDE,
            bg = COR_DO_FUNDO
        )
        self.scoreDaTelaDeDerrota.grid(row = 1, column = 0)

        self.voltarAoMenuPrincipalDaTelaDeDerrota = Label( # Atributo com a "Label" da tela de derrota para voltar ao menu principal
            master = self.quadroDaTelaDeDerrota,
            text = 'Aperte Qualquer Tecla para Voltar ao Menu Principal',
            font = FONTE_TAMANHO_16,
            fg = AZUL,
            bg = COR_DO_FUNDO
        )
        self.voltarAoMenuPrincipalDaTelaDeDerrota.grid(row = 2, column = 0, pady = 20)

        # Atributos com os componentes da tela de pause
        self.quadroDaTelaDePause = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela de pause

        self.pause = Label( # Atributo com a "Label" do título da tela de pause
            master = self.quadroDaTelaDePause,
            text = 'Pause',
            font = FONTE_TAMANHO_32_EM_NEGRITO,
            fg = AMARELO,
            bg = COR_DO_FUNDO
        )
        self.pause.grid(row = 0, column = 0, pady = 20)

        self.botaoVoltarAoJogo = Button( # Atributo com o botão "Voltar ao Jogo"
            master = self.quadroDaTelaDePause,
            text = 'Voltar ao Jogo',
            font = FONTE_TAMANHO_14,
            fg = ROXO,
            activeforeground = ROXO_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoVoltarAoJogo.grid(row = 1, column = 0) # Insere o botão no quadro
        self.botaoVoltarAoJogo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoVoltarAoJogo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoVoltarAoJogo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoVoltarAoJogo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        self.botaoSalvarOJogo = Button( # Atributo com o botão "Salvar o Jogo"
            master = self.quadroDaTelaDePause,
            text = 'Salvar o Jogo',
            font = FONTE_TAMANHO_14,
            fg = ROXO,
            activeforeground = ROXO_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoSalvarOJogo.grid(row = 2, column = 0) # Insere o botão no quadro
        self.botaoSalvarOJogo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoSalvarOJogo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoSalvarOJogo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoSalvarOJogo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        self.botaoVoltarAoMenuPrincipal = Button( # Atributo com o botão "Voltar ao Menu Principal"
            master = self.quadroDaTelaDePause,
            text = 'Voltar ao Menu Principal',
            font = FONTE_TAMANHO_14,
            fg = ROXO,
            activeforeground = ROXO_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoVoltarAoMenuPrincipal.grid(row = 3, column = 0) # Insere o botão no quadro
        self.botaoVoltarAoMenuPrincipal.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoVoltarAoMenuPrincipal, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoVoltarAoMenuPrincipal.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(evento, self.botaoVoltarAoMenuPrincipal, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        # Atributos com os componentes da tela de salvamento
        self.quadroDaTelaDeSalvamento = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela de salvamento

        self.jogoSalvo = Label( # Atributo com o título da tela de salvamento
            master = self.quadroDaTelaDeSalvamento,
            text = 'Jogo Salvo!',
            font = FONTE_TAMANHO_32_EM_NEGRITO,
            fg = CIANO,
            bg = COR_DO_FUNDO
        )
        self.jogoSalvo.grid(row = 0, column = 0)

        # Conjunto com todos os atributos da classe
        self.__atributos = {
            'self.janela',
            'self.quadroDoMenuPrincipal',
            'self.logo',
            'self.titulo',
            'self.botaoNovoJogo',
            'self.botaoCarregarJogo',
            'self.botaoOpcoes',
            'self.botaoEstatisticas',
            'self.botaoManualDoDesenvolvedor',
            'self.botaoSairDoJogo',
            'self.quadroDaTelaDoTabuleiro',
            'self.score',
            'self.objetivo',
            'self.tabuleiro',
            'self.quadroDaTelaDeVitoria',
            'self.quadroDaTelaDeDerrota',
            'self.vitoria',
            'self.scoreDaTelaDeVitoria',
            'self.voltarAoMenuPrincipalDaTelaDeVitoria',
            'self.derrota',
            'self.scoreDaTelaDeDerrota',
            'self.voltarAoMenuPrincipalDaTelaDeDerrota',
            'self.quadroDaTelaDePause',
            'self.pause',
            'self.botaoVoltarAoJogo',
            'self.botaoSalvarOJogo',
            'self.botaoVoltarAoMenuPrincipal',
            'self.quadroDaTelaDeSalvamento',
            'self.jogoSalvo',
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
            'removeEvento',
            'pausa',
            'mudaCorDeFundoDoBotao',
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
            'self.janela': 'Atributo com a janela do jogo.',
            'self.quadroDoMenuPrincipal': 'Atributo com o quadro para armazenar o conteúdo do menu principal.',
            'self.logo': 'Atributo com a imagem da logo.',
            'self.titulo': 'Atributo com o título do menu principal.',
            'self.botaoNovoJogo': 'Atributo com o botão "Novo Jogo".',
            'self.botaoCarregarJogo': 'Atributo com o botão "Carregar Jogo".',
            'self.botaoOpcoes': 'Atributo com o botão "Opções".',
            'self.botaoEstatisticas': 'Atributo com o botão "Estatísticas".',
            'self.botaoManualDoDesenvolvedor': 'Atributo com o botão "Manual do Desenvolvedor".',
            'self.botaoSairDoJogo': 'Atributo com o botão "Sair do Jogo".',
            'self.quadroDaTelaDoTabuleiro': 'Atributo com o quadro para armazenar o conteúdo da tela do tabuleiro.',
            'self.score': 'Atributo com a "Label" do score.',
            'self.objetivo': 'Atributo com a "Label" do objetivo.',
            'self.tabuleiro': 'Atributo com o "Frame" do tabuleiro.',
            'self.quadroDaTelaDePause': 'Atributo com o quadro para armazenar o conteúdo da tela de pause.',
            'self.pause': 'Atributo com a "Label" do título da tela de pause.',
            'self.botaoVoltarAoJogo': 'Atributo com o botão "Voltar ao Jogo".',
            'self.botaoSalvarOJogo': 'Atributo com o botão "Salvar o Jogo".',
            'self.botaoVoltarAoMenuPrincipal': 'Atributo com o botão "Voltar ao Menu Principal".',
            'self.quadroDaTelaDeSalvamento': 'Atributo com o quadro para armazenar o conteúdo da tela de salvamento.',
            'self.jogoSalvo': 'Atributo com o título da tela de salvamento.',
            'self.quadroDaTelaDeVitoria': 'Atributo com o quadro para armazenar o conteúdo da tela de vitória.',
            'self.quadroDaTelaDeDerrota': 'Atributo com o quadro para armazenar o conteúdo da tela de derrota.',
            'self.vitoria': 'Atributo com a "Label" do título da tela de vitória.',
            'self.scoreDaTelaDeVitoria': 'Atributo com a "Label" do score da tela de vitória.',
            'self.voltarAoMenuPrincipalDaTelaDeVitoria': 'Atributo com a "Label" da tela de vitória para voltar ao menu principal.',
            'self.derrota': 'Atributo com a "Label" do título da tela de derrota.',
            'self.scoreDaTelaDeDerrota': 'Atributo com a "Label" do score da tela de derrota.',
            'self.voltarAoMenuPrincipalDaTelaDeDerrota': 'Atributo com a "Label" da tela de derrota para voltar ao menu principal.',
            'self.__atributos': 'Conjunto com todos os atributos da classe.',
            'self.__metodos': 'Conjunto com todos os métodos da classe.',
            '__init__': self.__init__.__doc__,
            '__str__': self.__str__.__doc__,
            'getAtributos': self.getAtributos.__doc__,
            'getMetodos': self.getMetodos.__doc__,
            'manual': self.manual.__doc__,
            'entradaDoUsuario': self.entradaDoUsuario.__doc__,
            'limpaTela': self.limpaTela.__doc__,
            'removeEvento': self.removeEvento.__doc__,
            'pausa': self.pausa.__doc__,
            'mudaCorDeFundoDoBotao': self.mudaCorDeFundoDoBotao.__doc__,
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

        Self -> None
        '''
        self.quadroDoMenuPrincipal.grid()

    def telaDePause(self):
        '''
        Método para exibir ao usuário a tela de pause do jogo.

        Self -> None
        '''
        self.quadroDaTelaDePause.grid()

    def telaDeSalvamento(self):
        '''
        Método para exibir ao usuário a tela de salvamento do jogo.

        Self -> None
        '''
        # Mostra a tela de salvamento
        self.quadroDaTelaDeSalvamento.grid()

        # Atualiza a janela
        self.janela.update()

    def telaDeCarregamento(self, listaComOsDadosDasPartidasSalvas):
        '''
        Método para exibir ao usuário a tela de carregamento das
        partidas salvas.

        Self, list[str] -> None
        '''
        print('\x1b[0;96m')
        print('┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐'.center(get_terminal_size().columns))
        print('│ P │ A │ R │ T │ I │ D │ A │ S │   │ S │ A │ L │ V │ A │ S │'.center(get_terminal_size().columns))
        print('└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘'.center(get_terminal_size().columns))
        print('')

        # Verifica se possui alguma partida salva
        # Caso possua, escreve na tela uma lista com todas as partidas salvas
        if listaComOsDadosDasPartidasSalvas != []:
            # Passa por todas as partidas salvas
            # De 5 em 5 por causa da quantidade de linhas que cada partida salva ocupa
            for x in range(0, len(listaComOsDadosDasPartidasSalvas), 5):
                # Escreve na tela o índice da partida salva
                print(f'{int(x / 5 + 1)}'.center(get_terminal_size().columns))
                print('─────────────────────────────────────────────'.center(get_terminal_size().columns))

                # Escreve na tela a data e hora da partida salva
                print(listaComOsDadosDasPartidasSalvas[x][: - 1].center(get_terminal_size().columns))

                # Escreve na tela o objetivo da partida salva
                print(f'OBJETIVO:    {listaComOsDadosDasPartidasSalvas[x + 2][: - 1]}'.center(get_terminal_size().columns))

                # Escreve na tela o score da partida salva
                print(f'SCORE:    {listaComOsDadosDasPartidasSalvas[x + 4][: - 1]}'.center(get_terminal_size().columns))

                # Escreve na tela o tabuleiro da partida salva
                # Converte a string do tabuleiro de volta para lista
                tabuleiro = eval(listaComOsDadosDasPartidasSalvas[x + 3][: - 1])

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

                        else:
                            linhaComOValorDasPecas += f'│ {tabuleiro[i][j]} '

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

        # Se não possuir, mostra uma tela diferente
        else:
            print('Não há partidas salvas!'.center(get_terminal_size().columns))
            print('─────────────────────────────────────────────'.center(get_terminal_size().columns))
            print('\x1b[0;0m')

    def telaDeOpcoes(self, tamanhoDoTabuleiro, objetivo):
        '''
        Método para exibir ao usuário a tela de opções do jogo.

        Self, int, int -> None
        '''
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
        print(f'{tamanhoDoTabuleiro}X{tamanhoDoTabuleiro}'.center(get_terminal_size().columns))
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

    def telaDasEstatisticas(self, estatisticasDeJogadas, estatisticasDePecas, estatisticasDeScore):
        '''
        Método para exibir ao usuário a tela de estatísticas do jogo.

        Self,
        tuple[list[str], list[int]],
        tuple[list[str], list[int]],
        tuple[list[int]] -> None
        '''
        # Define o estilo do gráfico
        plt.style.use('dark_background')

        # Define a organização dos gráficos com um "grid" no formato 2x2
        grid = (2, 2)

        # Define a figura
        fig = plt.figure('2048 - Estatísticas', (15, 8))

        # Define os eixos
        eixoDasEstatisticasDeJogadas = plt.subplot2grid(grid, (0, 0))
        eixoDasEstatisticasDePecas = plt.subplot2grid(grid, (0, 1))
        eixoDasEstatisticasDeScore = plt.subplot2grid(grid, (1, 0), colspan = 2)

        # Gráfico das estatísticas de jogadas
        eixoDasEstatisticasDeJogadas.pie(estatisticasDeJogadas[1], labels = estatisticasDeJogadas[0], colors = ('red', 'green', 'blue', 'purple'), autopct = '%1.1f%%')
        eixoDasEstatisticasDeJogadas.set_title('Estatísticas de Jogadas')

        # Gráfico das estatísticas de peças
        eixoDasEstatisticasDePecas.bar(estatisticasDePecas[0], estatisticasDePecas[1], color = 'yellow')
        eixoDasEstatisticasDePecas.set_xlabel('Peça')
        eixoDasEstatisticasDePecas.set_ylabel('Quantidade')
        eixoDasEstatisticasDePecas.set_title('Estatísticas da Maior Peça de Cada Partida')

        # Gráfico das estatísticas de scores
        eixoDasEstatisticasDeScore.plot(estatisticasDeScore[0], estatisticasDeScore[1], 'cyan')
        eixoDasEstatisticasDeScore.set_xlabel('Partidas')
        eixoDasEstatisticasDeScore.set_ylabel('Score')
        eixoDasEstatisticasDeScore.set_title('Estatísticas de Score')

        # Mostra o gráfico
        plt.show()

    def telaDoTabuleiro(self, tabuleiro, score, objetivo):
        '''
        Método para exibir a tela do tabuleiro do jogo.

        Self, numpy.ndarray[int], int, int -> None
        '''
        # Altera o texto dos atributos para incluir o valor do score e do objetivo atualizado
        self.score['text'] = f'SCORE:    {score}'
        self.objetivo['text'] = f'OBJETIVO:    {objetivo}'

        # Passa por todas as "Labels" contidas no "Frame" do tabuleiro
        for label in self.tabuleiro.winfo_children():
            # Remove a "Label" do "Frame" do tabuleiro
            label.destroy()

        # Insere o valor de cada casa do tabuleiro na tela
        # Passa por todas as linhas
        for i in range(len(tabuleiro)):
            # Passa por todas as colunas
            for j in range(len(tabuleiro[i])):
                # Insere uma "Label" com o valor da peça
                Label(
                    master = self.tabuleiro,
                    text = f'{tabuleiro[i][j]}',
                    font = FONTE_TAMANHO_24_EM_NEGRITO,
                    fg = COR_DO_NUMERO_DAS_PECAS[tabuleiro[i][j]],
                    bg = COR_DO_FUNDO_DAS_PECAS[tabuleiro[i][j]],
                    width = 5,
                    height = 3
                ).grid(row = i, column = j, padx = 5, pady = 5)

        # Mostra a tela do tabuleiro
        self.quadroDaTelaDoTabuleiro.grid()

        # Atualiza a janela
        self.janela.update()

    def telaDeFimDeJogo(self, foiVencedor, score):
        '''
        Método para exibir a tela de fim de jogo.

        Self, bool, int -> None
        '''

        # Se foi vencedor, exibe a tela de vencedor
        if foiVencedor == True:
            # Atualiza o atributo com o score
            self.scoreDaTelaDeVitoria['text'] = f'SCORE:    {score}'

            # Exibe a tela de vitória
            self.quadroDaTelaDeVitoria.grid()

            # Atualiza a janela
            self.janela.update()

        # Se não, exibe a tela de perdedor
        else:
            # Atualiza o atributo com o score
            self.scoreDaTelaDeDerrota['text'] = f'SCORE:    {score}'

            # Exibe a tela de derrota
            self.quadroDaTelaDeDerrota.grid()

            # Atualiza a janela
            self.janela.update()
