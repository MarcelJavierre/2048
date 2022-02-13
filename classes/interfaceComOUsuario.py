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
        Método construtor. Inicia os componentes de todas as telas.

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

        # Atributo com a barra de rolagem
        self.barraDeRolagem = Scrollbar(master = self.janela)

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
        self.botaoNovoJogo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoNovoJogo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoNovoJogo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoNovoJogo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

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
        self.botaoCarregarJogo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoCarregarJogo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoCarregarJogo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoCarregarJogo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

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
        self.botaoOpcoes.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoOpcoes, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoOpcoes.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoOpcoes, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

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
        self.botaoEstatisticas.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoEstatisticas, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoEstatisticas.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoEstatisticas, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

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
        self.botaoManualDoDesenvolvedor.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoManualDoDesenvolvedor, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoManualDoDesenvolvedor.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoManualDoDesenvolvedor, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

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
        self.botaoSairDoJogo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoSairDoJogo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoSairDoJogo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoSairDoJogo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        # Atributos com os componentes da tela do tabuleiro
        self.quadroDaTelaDoTabuleiro = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela do tabuleiro

        self.score = Label( # Atributo com o score da partida na tela do tabuleiro
            master = self.quadroDaTelaDoTabuleiro,
            font = FONTE_TAMANHO_18,
            fg = BRANCO,
            bg = COR_DO_FUNDO
        )
        self.score.grid(row = 0, column = 0)

        self.objetivo = Label( # Atributo com o objetivo da partida na tela do tabuleiro
            master = self.quadroDaTelaDoTabuleiro,
            font = FONTE_TAMANHO_18,
            fg = BRANCO,
            bg = COR_DO_FUNDO
        )
        self.objetivo.grid(row = 1, column = 0)

        self.tabuleiro = Frame(master = self.quadroDaTelaDoTabuleiro, bg = COR_DA_BORDA_DO_TABULEIRO, borderwidth = 5) # Atributo com o quadro do tabuleiro
        self.tabuleiro.grid(row = 2, column = 0, pady = 20)

        # Atributos com os componentes da tela de fim de jogo
        self.quadroDaTelaDeVitoria = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela de vitória
        self.quadroDaTelaDeDerrota = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela de derrota

        self.vitoria = Label( # Atributo com o título da tela de vitória
            master = self.quadroDaTelaDeVitoria,
            text = 'Você Venceu!',
            font = FONTE_TAMANHO_32_EM_NEGRITO,
            fg = AMARELO,
            bg = COR_DO_FUNDO
        )
        self.vitoria.grid(row = 0, column = 0, pady = 20)

        self.scoreDaTelaDeVitoria = Label( # Atributo com o texto do score da tela de vitória
            master = self.quadroDaTelaDeVitoria,
            font = FONTE_TAMANHO_16,
            fg = AMARELO,
            bg = COR_DO_FUNDO
        )
        self.scoreDaTelaDeVitoria.grid(row = 1, column = 0)

        self.voltarAoMenuPrincipalDaTelaDeVitoria = Label( # Atributo com o texto da tela de vitória para voltar ao menu principal
            master = self.quadroDaTelaDeVitoria,
            text = 'Aperte Qualquer Tecla para Voltar ao Menu Principal',
            font = FONTE_TAMANHO_16,
            fg = AMARELO,
            bg = COR_DO_FUNDO
        )
        self.voltarAoMenuPrincipalDaTelaDeVitoria.grid(row = 2, column = 0, pady = 20)

        self.derrota = Label( # Atributo com o título da tela de derrota
            master = self.quadroDaTelaDeDerrota,
            text = 'Você Perdeu!',
            font = FONTE_TAMANHO_32_EM_NEGRITO,
            fg = VERMELHO,
            bg = COR_DO_FUNDO
        )
        self.derrota.grid(row = 0, column = 0, pady = 20)

        self.scoreDaTelaDeDerrota = Label( # Atributo com o texto do score da tela de derrota
            master = self.quadroDaTelaDeDerrota,
            font = FONTE_TAMANHO_16,
            fg = VERMELHO,
            bg = COR_DO_FUNDO
        )
        self.scoreDaTelaDeDerrota.grid(row = 1, column = 0)

        self.voltarAoMenuPrincipalDaTelaDeDerrota = Label( # Atributo com o texto da tela de derrota para voltar ao menu principal
            master = self.quadroDaTelaDeDerrota,
            text = 'Aperte Qualquer Tecla para Voltar ao Menu Principal',
            font = FONTE_TAMANHO_16,
            fg = VERMELHO,
            bg = COR_DO_FUNDO
        )
        self.voltarAoMenuPrincipalDaTelaDeDerrota.grid(row = 2, column = 0, pady = 20)

        # Atributos com os componentes da tela de pause
        self.quadroDaTelaDePause = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela de pause

        self.pause = Label( # Atributo com o título da tela de pause
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
        self.botaoVoltarAoJogo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoVoltarAoJogo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoVoltarAoJogo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoVoltarAoJogo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

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
        self.botaoSalvarOJogo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoSalvarOJogo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoSalvarOJogo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoSalvarOJogo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        self.botaoVoltarAoMenuPrincipalDaTelaDePause = Button( # Atributo com o botão "Voltar ao Menu Principal" da tela de pause
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
        self.botaoVoltarAoMenuPrincipalDaTelaDePause.grid(row = 3, column = 0) # Insere o botão no quadro
        self.botaoVoltarAoMenuPrincipalDaTelaDePause.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoVoltarAoMenuPrincipalDaTelaDePause, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoVoltarAoMenuPrincipalDaTelaDePause.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoVoltarAoMenuPrincipalDaTelaDePause, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

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

        # Atributos com os componentes da tela de carregamento
        self.canvasDaTelaDeCarregamento = Canvas( # Atributo com o "Canvas" da tela de carregamento
            master = self.janela,
            bg = COR_DO_FUNDO,
            highlightthickness = 0,
            yscrollcommand = self.barraDeRolagem.set
        )

        self.quadroDaTelaDeCarregamento = Frame(master = self.canvasDaTelaDeCarregamento, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela de carregamento
        self.canvasDaTelaDeCarregamento.create_window( # Adiciona o quadro da tela de carregamento no "Canvas" da tela de carregamento
            0,
            0,
            window = self.quadroDaTelaDeCarregamento,
            anchor = 'nw'
        )

        self.tituloDaTelaDeCarregamento = Label( # Atributo com o título da tela de carregamento
            master = self.quadroDaTelaDeCarregamento,
            text = 'Partidas Salvas',
            font = FONTE_TAMANHO_32_EM_NEGRITO,
            fg = CIANO,
            bg = COR_DO_FUNDO
        )
        self.tituloDaTelaDeCarregamento.grid(row = 0, column = 0, pady = 20)

        self.partidasSalvas = Frame(master = self.quadroDaTelaDeCarregamento, bg = COR_DO_FUNDO) # Atributo com o quadro das partidas salvas

        self.naoHaPartidasSalvas = Label( # Atributo com o texto indicando que não há partidas salvas
            master = self.quadroDaTelaDeCarregamento,
            text = 'Não Há Partidas Salvas!',
            font = FONTE_TAMANHO_16,
            fg = CIANO,
            bg = COR_DO_FUNDO
        )

        self.botaoVoltarAoMenuPrincipalDaTelaDeCarregamento = Button( # Atributo com o botão "Voltar ao Menu Principal" da tela de carregamento
            master = self.quadroDaTelaDeCarregamento,
            text = 'Voltar ao Menu Principal',
            font = FONTE_TAMANHO_14,
            fg = CIANO,
            activeforeground = CIANO_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoVoltarAoMenuPrincipalDaTelaDeCarregamento.grid(row = 2, column = 0, pady = 20) # Insere o botão no quadro
        self.botaoVoltarAoMenuPrincipalDaTelaDeCarregamento.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoVoltarAoMenuPrincipalDaTelaDeCarregamento, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoVoltarAoMenuPrincipalDaTelaDeCarregamento.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoVoltarAoMenuPrincipalDaTelaDeCarregamento, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        # Atributos com os componentes da tela de Opções
        self.quadroDaTelaDeOpcoes = Frame(master = self.janela, bg = COR_DO_FUNDO) # Atributo com o quadro para armazenar o conteúdo da tela de opções

        self.opcoes = Label( # Atributo com o título da tela de opções
            master = self.quadroDaTelaDeOpcoes,
            text = 'Opções',
            font = FONTE_TAMANHO_32_EM_NEGRITO,
            fg = AZUL,
            bg = COR_DO_FUNDO
        )
        self.opcoes.grid(row = 0, column = 0, pady = 20)

        self.tamanhoDoTabuleiro = StringVar() # Atributo para armazenar a entrada do usuário na seleção do tamanho do tabuleiro
        self.objetivoDaPartida = StringVar() # Atributo para armazenar a entrada do usuário na seleção do objetivo da partida

        self.textoDoTamanhoDoTabuleiro = Label( # Atributo com o texto do tamanho do tabuleiro da tela de opções
            master = self.quadroDaTelaDeOpcoes,
            font = FONTE_TAMANHO_16,
            fg = AZUL,
            bg = COR_DO_FUNDO
        )
        self.textoDoTamanhoDoTabuleiro.grid(row = 1, column = 0)

        self.entradaDoTamanhoDoTabuleiro = Entry( # Atributo com a entrada do tamanho do tabuleiro
            master = self.quadroDaTelaDeOpcoes,
            textvariable = self.tamanhoDoTabuleiro,
            font = FONTE_TAMANHO_14,
            fg = AZUL
        )
        self.entradaDoTamanhoDoTabuleiro.grid(row = 2, column = 0, pady = 5)

        self.botaoAlterarTamanho = Button( # Atributo com o botão "Alterar Tamanho" da tela de opções
            master = self.quadroDaTelaDeOpcoes,
            text = 'Alterar Tamanho',
            font = FONTE_TAMANHO_14,
            fg = AZUL,
            activeforeground = AZUL_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoAlterarTamanho.grid(row = 3, column = 0) # Insere o botão no quadro
        self.botaoAlterarTamanho.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoAlterarTamanho, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoAlterarTamanho.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoAlterarTamanho, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        self.espacoEntreAsOpcoes = Frame(master = self.quadroDaTelaDeOpcoes, bg = COR_DO_FUNDO) # Atributo com o quadro para espaçar as opções na tela de opções
        self.espacoEntreAsOpcoes.grid(row = 4, column = 0, pady = 20)

        self.textoDoObjetivo = Label( # Atributo com o texto do objetivo da tela de opções
            master = self.quadroDaTelaDeOpcoes,
            font = FONTE_TAMANHO_16,
            fg = AZUL,
            bg = COR_DO_FUNDO
        )
        self.textoDoObjetivo.grid(row = 5, column = 0)

        self.entradaDoObjetivo = Entry( # Atributo com a entrada do objetivo
            master = self.quadroDaTelaDeOpcoes,
            textvariable = self.objetivoDaPartida,
            font = FONTE_TAMANHO_14,
            fg = AZUL
        )
        self.entradaDoObjetivo.grid(row = 6, column = 0, pady = 5)

        self.botaoAlterarObjetivo = Button( # Atributo com o botão "Alterar Objetivo" da tela de opções
            master = self.quadroDaTelaDeOpcoes,
            text = 'Alterar Objetivo',
            font = FONTE_TAMANHO_14,
            fg = AZUL,
            activeforeground = AZUL_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoAlterarObjetivo.grid(row = 7, column = 0) # Insere o botão no quadro
        self.botaoAlterarObjetivo.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoAlterarObjetivo, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoAlterarObjetivo.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoAlterarObjetivo, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão
        
        self.botaoVoltarAoMenuPrincipalDaTelaDeOpcoes = Button( # Atributo com o botão "Voltar ao Menu Principal" da tela de opções
            master = self.quadroDaTelaDeOpcoes,
            text = 'Voltar ao Menu Principal',
            font = FONTE_TAMANHO_14,
            fg = AZUL,
            activeforeground = AZUL_CLARO,
            bg = COR_DO_FUNDO,
            activebackground = CINZA,
            relief = 'flat',
            borderwidth = 0
        )
        self.botaoVoltarAoMenuPrincipalDaTelaDeOpcoes.grid(row = 8, column = 0, pady = 20) # Insere o botão no quadro
        self.botaoVoltarAoMenuPrincipalDaTelaDeOpcoes.bind('<Enter>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoVoltarAoMenuPrincipalDaTelaDeOpcoes, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
        self.botaoVoltarAoMenuPrincipalDaTelaDeOpcoes.bind('<Leave>', lambda evento: self.mudaCorDeFundoDoBotao(self.botaoVoltarAoMenuPrincipalDaTelaDeOpcoes, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão

        # Conjunto com todos os atributos da classe
        self.__atributos = {
            'self.janela',
            'self.barraDeRolagem',
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
            'self.botaoVoltarAoMenuPrincipalDaTelaDePause',
            'self.quadroDaTelaDeSalvamento',
            'self.jogoSalvo',
            'self.canvasDaTelaDeCarregamento',
            'self.quadroDaTelaDeCarregamento',
            'self.tituloDaTelaDeCarregamento',
            'self.partidasSalvas',
            'self.naoHaPartidasSalvas',
            'self.botaoVoltarAoMenuPrincipalDaTelaDeCarregamento',
            'self.quadroDaTelaDeOpcoes',
            'self.opcoes',
            'self.tamanhoDoTabuleiro',
            'self.objetivoDaPartida',
            'self.textoDoTamanhoDoTabuleiro',
            'self.entradaDoTamanhoDoTabuleiro',
            'self.botaoAlterarTamanho',
            'self.espacoEntreAsOpcoes',
            'self.textoDoObjetivo',
            'self.entradaDoObjetivo',
            'self.botaoAlterarObjetivo',
            'self.botaoVoltarAoMenuPrincipalDaTelaDeOpcoes',
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
            'self.barraDeRolagem': 'Atributo com a barra de rolagem.',
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
            'self.score': 'Atributo com o score da partida na tela do tabuleiro.',
            'self.objetivo': 'Atributo com o objetivo da partida na tela do tabuleiro.',
            'self.tabuleiro': 'Atributo com o quadro do tabuleiro.',
            'self.quadroDaTelaDeVitoria': 'Atributo com o quadro para armazenar o conteúdo da tela de vitória.',
            'self.quadroDaTelaDeDerrota': 'Atributo com o quadro para armazenar o conteúdo da tela de derrota.',
            'self.vitoria': 'Atributo com o título da tela de vitória.',
            'self.scoreDaTelaDeVitoria': 'Atributo com o texto do score da tela de vitória.',
            'self.voltarAoMenuPrincipalDaTelaDeVitoria': 'Atributo com o texto da tela de vitória para voltar ao menu principal.',
            'self.derrota': 'Atributo com o título da tela de derrota.',
            'self.scoreDaTelaDeDerrota': 'Atributo com o texto do score da tela de derrota.',
            'self.voltarAoMenuPrincipalDaTelaDeDerrota': 'Atributo com o texto da tela de derrota para voltar ao menu principal.',
            'self.quadroDaTelaDePause': 'Atributo com o quadro para armazenar o conteúdo da tela de pause.',
            'self.pause': 'Atributo com o título da tela de pause.',
            'self.botaoVoltarAoJogo': 'Atributo com o botão "Voltar ao Jogo".',
            'self.botaoSalvarOJogo': 'Atributo com o botão "Salvar o Jogo".',
            'self.botaoVoltarAoMenuPrincipalDaTelaDePause': 'Atributo com o botão "Voltar ao Menu Principal" da tela de pause.',
            'self.quadroDaTelaDeSalvamento': 'Atributo com o quadro para armazenar o conteúdo da tela de salvamento.',
            'self.jogoSalvo': 'Atributo com o título da tela de salvamento.',
            'self.canvasDaTelaDeCarregamento': 'Atributo com o "Canvas" da tela de carregamento.',
            'self.quadroDaTelaDeCarregamento': 'Atributo com o quadro para armazenar o conteúdo da tela de carregamento.',
            'self.tituloDaTelaDeCarregamento': 'Atributo com o título da tela de carregamento.',
            'self.partidasSalvas': 'Atributo com o quadro das partidas salvas.',
            'self.naoHaPartidasSalvas': 'Atributo com o texto indicando que não há partidas salvas.',
            'self.botaoVoltarAoMenuPrincipalDaTelaDeCarregamento': 'Atributo com o botão "Voltar ao Menu Principal" da tela de carregamento.',
            'self.quadroDaTelaDeOpcoes': 'Atributo com o quadro para armazenar o conteúdo da tela de opções.',
            'self.opcoes': 'Atributo com o título da tela de opções.',
            'self.tamanhoDoTabuleiro': 'Atributo para armazenar a entrada do usuário na seleção do tamanho do tabuleiro.',
            'self.objetivoDaPartida': 'Atributo para armazenar a entrada do usuário na seleção do objetivo da partida.',
            'self.textoDoTamanhoDoTabuleiro': 'Atributo com o texto do tamanho do tabuleiro da tela de opções.',
            'self.entradaDoTamanhoDoTabuleiro': 'Atributo com a entrada do tamanho do tabuleiro.',
            'self.botaoAlterarTamanho': 'Atributo com o botão "Alterar Tamanho" da tela de opções.',
            'self.espacoEntreAsOpcoes': 'Atributo com o quadro para espaçar as opções na tela de opções.',
            'self.textoDoObjetivo': 'Atributo com o texto do objetivo da tela de opções.',
            'self.entradaDoObjetivo': 'Atributo com a entrada do objetivo.',
            'self.botaoAlterarObjetivo': 'Atributo com o botão "Alterar Objetivo" da tela de opções.',
            'self.botaoVoltarAoMenuPrincipalDaTelaDeOpcoes': 'Atributo com o botão "Voltar ao Menu Principal" da tela de opções.',
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

    def telaDeCarregamento(self, dadosDasPartidasSalvas):
        '''
        Método para exibir ao usuário a tela de carregamento das
        partidas salvas.

        Self, list[str] -> None
        '''
        # Configura a barra de rolagem para ser utilizada com a tela de carregamento
        self.barraDeRolagem.config(command = self.canvasDaTelaDeCarregamento.yview)

        # Passa por todos os botões contidos no "Frame" das partidas salvas
        for botao in self.partidasSalvas.winfo_children():
            # Remove o botão do "Frame" das partidas salvas
            botao.destroy()

        # Verifica se possui alguma partida salva
        # Caso possua, escreve na tela uma lista com todas as partidas salvas
        if dadosDasPartidasSalvas != []:
            self.naoHaPartidasSalvas.grid_forget()
            self.partidasSalvas.grid(row = 1, column = 0)

            # Passa por todas as partidas salvas
            for i in range(0, len(dadosDasPartidasSalvas), 5):
                # Converte o tabuleiro de string para list
                tabuleiro = eval(dadosDasPartidasSalvas[i + 3][: - 1])

                # Cria uma variável que armazena o tabuleiro em forma de string devidamente formatado
                # Inicia a string com o topo do tabuleiro
                tabuleiroFormatado = '┌──────' + '┬──────' * (len(tabuleiro[0]) - 1) + '┐\n'
                # Passa por todas as linhas do tabuleiro
                for linha in range(len(tabuleiro)):
                    # Adiciona o espaço entre a borda da casa e o número
                    tabuleiroFormatado += '│      ' * len(tabuleiro[0]) + '│\n'
                    # Passa por todas as colunas do tabuleiro
                    for coluna in range(len(tabuleiro[linha])):
                        tabuleiroFormatado += '│'
                        # Caso o valor da casa seja diferente de 0, adiciona na string o valor da casa
                        if tabuleiro[linha][coluna] != 0:
                            tabuleiroFormatado += f'{tabuleiro[linha][coluna]}'.center(6)
                        # Caso o valor seja 0, imprime um espaço em branco na casa
                        else:
                            tabuleiroFormatado += '      '
                    tabuleiroFormatado += '│\n'
                    # Adiciona mais um espaço entre a borda da casa e o número
                    tabuleiroFormatado += '│      ' * len(tabuleiro[0]) + '│\n'
                    # Caso seja a última iteração, não adiciona na string a divisão entre as casas do tabuleiro
                    if linha != (len(tabuleiro[linha]) - 1):
                        tabuleiroFormatado += '├──────' + '┼──────' * (len(tabuleiro[0]) - 1) + '┤\n'
                # Aciona na string o fundo do tabuleiro
                tabuleiroFormatado += '└──────' + '┴──────' * (len(tabuleiro[0]) - 1) + '┘'

                # Cria um botão para cada partida salva
                Button(
                    master = self.partidasSalvas,
                    text = f'{dadosDasPartidasSalvas[i]}\nOBJETIVO:    {dadosDasPartidasSalvas[i + 2]}\nSCORE:    {dadosDasPartidasSalvas[i + 4]}\n{tabuleiroFormatado}',
                    font = FONTE_MONOESPACADA_TAMANHO_12,
                    fg = CIANO,
                    activeforeground = CIANO_CLARO,
                    bg = COR_DO_FUNDO,
                    activebackground = CINZA,
                    relief = 'flat',
                    borderwidth = 0
                ).grid(column = 0, pady = 5)

            # Adiciona os eventos para mudar a cor dos botões ao passar o mouse por cima
            for i in range(len(self.partidasSalvas.winfo_children())):
                self.partidasSalvas.winfo_children()[i].bind('<Enter>', lambda evento, botao = self.partidasSalvas.winfo_children()[i]: self.mudaCorDeFundoDoBotao(botao, CINZA)) # Define o evento que muda a cor de fundo ao passar o mouse em cima do botão
                self.partidasSalvas.winfo_children()[i].bind('<Leave>', lambda evento, botao = self.partidasSalvas.winfo_children()[i]: self.mudaCorDeFundoDoBotao(botao, COR_DO_FUNDO)) # Define o evento que muda a cor de fundo ao tirar o mouse de cima do botão
                
            # Atualiza a janela
            self.janela.update()

        # Se não possuir, mostra uma tela diferente
        else:
            self.partidasSalvas.grid_forget()
            self.naoHaPartidasSalvas.grid(row = 1, column = 0)

        # Mostra a tela de carregamento junto com a barra de rolagem
        self.barraDeRolagem.pack(fill = 'y', side = 'right')
        self.canvasDaTelaDeCarregamento.pack(expand = True, fill = 'y')

        # Atualiza a área de rolagem
        self.canvasDaTelaDeCarregamento.configure(scrollregion = self.canvasDaTelaDeCarregamento.bbox('all'))

    def telaDeOpcoes(self, tamanhoDoTabuleiro, objetivo):
        '''
        Método para exibir ao usuário a tela de opções do jogo.

        Self, int, int -> None
        '''
        # Atualiza o texto dos títulos para os valores atuais de tamanho e objetivo
        self.textoDoTamanhoDoTabuleiro['text'] = f'Tamanho do Tabuleiro:\n{tamanhoDoTabuleiro}'
        self.textoDoObjetivo['text'] = f'Objetivo:\n{objetivo}'

        # Mostra a tela de opções
        self.quadroDaTelaDeOpcoes.grid()

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
