"""
2048
====

Sobre o jogo:
-------------

2048 é jogado em um tabuleiro de 4X4, com peças numéricas que deslizam
suavemente quando o jogador as move em um dos quatro sentidos
disponíveis: para cima, para baixo, à esquerda e à direita.

Cada vez, um novo número aparece aleatoriamente em um local vazio na
placa (com um valor de 2 ou 4).

Os blocos deslizam o mais longe possível na direção escolhida até que
eles sejam interrompidos por qualquer outro bloco ou a borda do
tabuleiro. Se duas peças do mesmo número colidem durante a movimentação,
elas irão se fundir em uma peça com o valor total das duas peças que
colidiram.

O jogo é vencido quando uma peça com o valor de 2048 aparece no
tabuleiro. Quando o jogador não tem movimentos legais (não há espaços
vazios e nem peças adjacentes com o mesmo valor), o jogo termina.
"""

# Propriedades do documento
__author__ = 'Marcel Javierre'
__copyright__ = 'Copyright 2022'
__credits__ = __author__
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = __author__
__email__ = 'javierremarcel@poli.ufrj.br'
__status__ = 'Production'

# Importando as classes de cada seção
from classes.interfaceComOUsuario import *
from classes.mecanicaDoJogo import *
from classes.log import *

# Definindo as configurações padrão do jogo
tamanhoDoTabuleiro = 4
objetivo = 2048

# Inicializando as instâncias de cada seção
interface = InterfaceComOUsuario()
mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)
log = Log()

def main():
    '''
    Função principal. Exibe o menu principal.

    () -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Limpa a tela
    interface.limpaTela(interface.janela)

    # Exibe o menu principal
    interface.menuPrincipal()

    # Configura o comando de cada botão
    interface.botaoNovoJogo['command'] = iniciaLoopDoJogo
    interface.botaoCarregarJogo['command'] = partidasSalvas
    interface.botaoOpcoes['command'] = opcoes
    interface.botaoEstatisticas['command'] = estatisticas
    interface.botaoManualDoDesenvolvedor['command'] = manual

    # Loop do tkinter
    interface.janela.mainloop()

def iniciaLoopDoJogo():
    '''
    Função que define os eventos da tela do tabuleiro.

    () -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Define os eventos das teclas do teclado
    interface.janela.bind('<Up>', lambda evento: loopDoJogo('cima'))
    interface.janela.bind('<Down>', lambda evento: loopDoJogo('baixo'))
    interface.janela.bind('<Left>', lambda evento: loopDoJogo('esquerda'))
    interface.janela.bind('<Right>', lambda evento: loopDoJogo('direita'))
    interface.janela.bind('<Escape>', lambda evento: pause())

    # Limpa a tela
    interface.limpaTela(interface.janela)

    # Mostra o tabuleiro
    interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore(), objetivo)

    # Loop do tkinter
    interface.janela.mainloop()

def loopDoJogo(direcao):
    '''
    Função do loop do jogo. Move as peças do tabuleiro, insere novas
    peças e verifica se o jogador venceu ou perdeu a partida.

    str -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Remove os eventos da tela do tabuleiro
    interface.removeEvento(interface.janela, '<Up>')
    interface.removeEvento(interface.janela, '<Down>')
    interface.removeEvento(interface.janela, '<Left>')
    interface.removeEvento(interface.janela, '<Right>')
    interface.removeEvento(interface.janela, '<Escape>')


    # Variável para indicar se alguma ação foi realizada
    houveMudanca = False

    # Loop para mover as peças do tabuleiro
    while mecanica.movePecas(direcao) == True:
        interface.pausa(interface.janela, 100)
        interface.limpaTela(interface.janela)
        interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore(), objetivo)

        # Muda a variável para indicar que houve uma ação
        houveMudanca = True

    # Junta as peças do tabuleiro
    if mecanica.juntaPecas(direcao) == True:
        interface.pausa(interface.janela, 100)
        interface.limpaTela(interface.janela)
        interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore(), objetivo)

        # Muda a variável para indicar que houve uma ação
        houveMudanca = True

    # Loop para mover as peças do tabuleiro
    while mecanica.movePecas(direcao) == True:
        interface.pausa(interface.janela, 100)
        interface.limpaTela(interface.janela)
        interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore(), objetivo)

        # Muda a variável para indicar que houve uma ação
        houveMudanca = True

    # Caso houve alguma mudança no tabuleiro, continua o loop do jogo
    if houveMudanca == True:
        # Atualiza a estatística de jogadas
        log.estatisticasDeJogadas(direcao)
        
        # Verifica se o alguma peça atingiu o objetivo
        # Se sim, encerra o loop do jogo
        if mecanica.venceuOJogo() == True:
            # Encerra o loop do jogo e mostra a tela de fim de jogo
            fimDeJogo(True)

        # Verifica quais são as casas vazias do tabuleiro
        casasVazias = mecanica.getCasasVazias()

        # Caso o tabuleiro possua casas vazias, insere um nova peça
        if len(casasVazias) != 0:
            mecanica.inserePeca(casasVazias)

        # Limpa a tela
        interface.limpaTela(interface.janela)

        # Mostra o tabuleiro
        interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore(), objetivo)

        # Verifica se ainda tem jogadas válidas
        # Se não possuir, encerra o loop do jogo
        if mecanica.possuiMovimentosVailidos() == False:
            # Encerra o loop do jogo e mostra a tela de fim de jogo
            fimDeJogo(False)

    iniciaLoopDoJogo()

def fimDeJogo(venceuOJogo):
    '''
    Função para mostrar a tela de fim de jogo.

    bool -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Remove os eventos da tela do tabuleiro
    interface.removeEvento(interface.janela, '<Up>')
    interface.removeEvento(interface.janela, '<Down>')
    interface.removeEvento(interface.janela, '<Left>')
    interface.removeEvento(interface.janela, '<Right>')
    interface.removeEvento(interface.janela, '<Escape>')

    # Atualiza a estatística de peças com a maior peça no tabuleiro
    log.estatisticasDePecas(mecanica.getValorDaMaiorPeca())

    # Atualiza a estatística de score com o score da partida
    log.estatisticasDeScore(mecanica.getScore())

    # Mostra a tela de fim de jogo
    interface.pausa(interface.janela, 1500)
    interface.limpaTela(interface.janela)
    interface.telaDeFimDeJogo(venceuOJogo, mecanica.getScore())

    # Reinicia a instância da mecânica do jogo
    mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

    # Volta para o menu principal
    interface.janela.bind('<KeyRelease>', lambda evento: interface.removeEvento(interface.janela, '<KeyRelease>'), '+')
    interface.janela.bind('<KeyRelease>', lambda evento: main(), '+')

    # Loop do tkinter
    interface.janela.mainloop()

def pause():
    '''
    Função para mostrar a tela de pause.

    () -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Remove os eventos da tela do tabuleiro
    interface.removeEvento(interface.janela, '<Up>')
    interface.removeEvento(interface.janela, '<Down>')
    interface.removeEvento(interface.janela, '<Left>')
    interface.removeEvento(interface.janela, '<Right>')
    interface.removeEvento(interface.janela, '<Escape>')

    # Define os comandos dos botões
    interface.botaoVoltarAoJogo['command'] = iniciaLoopDoJogo
    interface.botaoSalvarOJogo['command'] = salvarOJogo
    interface.botaoVoltarAoMenuPrincipalDaTelaDePause['command'] = voltarAoMenuPrincipal

    # Limpa a tela
    interface.limpaTela(interface.janela)

    # Mostra a tela de pause
    interface.telaDePause()

    # Loop do tkinter
    interface.janela.mainloop()

def salvarOJogo():
    '''
    Função para salvar o jogo.

    () -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Limpa a tela
    interface.limpaTela(interface.janela)

    # Mostra a tela de salvamento
    interface.telaDeSalvamento()

    # Salva o jogo
    log.savarJogo(tamanhoDoTabuleiro, objetivo, mecanica.getTabuleiro().tolist(), mecanica.getScore())

    # Espera 1 segundo
    interface.pausa(interface.janela, 1000)

    # Volta para a tela de pause
    pause()

def voltarAoMenuPrincipal():
    '''
    Função que reinicia a instância da mecânica do jogo e retorna ao
    menu principal.

    () -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Reinicia a instância da mecânica do jogo
    mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

    # Volta ao menu principal
    main()

def partidasSalvas():
    '''
    Função para mostrar a lista de partidas salvas na tela de carregar
    jogo.

    () -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Define o comando do botão
    interface.botaoVoltarAoMenuPrincipalDaTelaDeCarregamento['command'] = main

    # Limpa a tela
    interface.limpaTela(interface.janela)

    # Lê as partidas salvas
    dadosDasPartidasSalvas = log.carregarJogo()

    # Mostra a tela de carregamento
    interface.telaDeCarregamento(dadosDasPartidasSalvas)

    # Define os eventos dos botões com as partidas salvas
    for i in range(len(interface.partidasSalvas.winfo_children())):
        # Botão esquerdo do mouse carrega a partida salva
        interface.partidasSalvas.winfo_children()[i]['command'] = lambda indiceDaPartidaSalva = i: carregarJogo(dadosDasPartidasSalvas, indiceDaPartidaSalva)

        # Botão direito do mouse apaga a partida salva
        interface.partidasSalvas.winfo_children()[i].bind('<Button-3>', lambda evento, indiceDaPartidaSalva = i: apagarPartidaSalva(indiceDaPartidaSalva))

    # Loop do tkinter
    interface.janela.mainloop()

def carregarJogo(dadosDasPartidasSalvas, indiceDaPartidaSalva):
    '''
    Função que, dado a lista com os dados das partidas salvas e o índice
    da partida salva, reinicia o loop do jogo com os dados salvos.

    list[str], int -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Converte o índice da partida salva passado para o índice da lista com o conteúdo do arquivo
    indiceDaPartidaSalva *= 5

    # Atualiza as variáveis de configuração com os dados da partida salva
    tamanhoDoTabuleiro = int(dadosDasPartidasSalvas[indiceDaPartidaSalva + 1])
    objetivo = int(dadosDasPartidasSalvas[indiceDaPartidaSalva + 2])

    # Reinicia a instância da mecânica do jogo
    mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

    # Atualiza o tabuleiro e o score com os dados da partida salva
    mecanica.carregarJogo(eval(dadosDasPartidasSalvas[indiceDaPartidaSalva + 3]), int(dadosDasPartidasSalvas[indiceDaPartidaSalva + 4]))

    # Reinicia o loop do jogo
    iniciaLoopDoJogo()

def apagarPartidaSalva(indiceDaPartidaSalva):
    '''
    Função que, dado o índice da partida salva, apaga a partida salva.
    
    int -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log
    
    # Apaga a partida salva
    log.apagarJogoSalvo(indiceDaPartidaSalva)

    # Volta para a tela de partidas salvas
    partidasSalvas()

def opcoes():
    '''
    Função para trocar as opções.

    () -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Define os comandos dos botões
    interface.botaoAlterarTamanho['command'] = lambda: atualizaConfiguracao('tamanho')
    interface.botaoAlterarObjetivo['command'] = lambda: atualizaConfiguracao('objetivo')
    interface.botaoVoltarAoMenuPrincipalDaTelaDeOpcoes['command'] = main

    # Limpa a tela
    interface.limpaTela(interface.janela)

    # Mostra a tela de opções
    interface.telaDeOpcoes(tamanhoDoTabuleiro, objetivo)

    # Loop do tkinter
    interface.janela.mainloop()

def atualizaConfiguracao(opcao):
    '''
    Função que atualiza as variáveis globais de configuração.

    str -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Verifica qual parâmetro é para ser atualizado
    if opcao == 'tamanho':
        # Armazena o valor do tamanho anterior
        tamanhoDoTabuleiroAntigo = tamanhoDoTabuleiro

        try:
            # Recebe o novo valor do tamanho e atualiza a variável global
            tamanhoDoTabuleiro = int(interface.tamanhoDoTabuleiro.get())

            try:
                # Reinicia a instância da mecânica do jogo com o novo parâmetro
                mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

            # Caso o número passado não seja válido (<= 1), gera um relatório de erro
            except ValueError as mensagemDeErro:
                # Gera o relatório de erro
                log.relatorioDeErro(repr(mensagemDeErro))

                # Restaura o valor anterior do tamanho do tabuleiro
                tamanhoDoTabuleiro = tamanhoDoTabuleiroAntigo

        # Caso o usuário tenha inserido algo diferente de um número, gera um relatório de erro
        except ValueError as mensagemDeErro:
            # Gera o relatório de erro
            log.relatorioDeErro(repr(mensagemDeErro))

            # Restaura o valor anterior do tamanho do tabuleiro
            tamanhoDoTabuleiro = tamanhoDoTabuleiroAntigo
    
        # Apaga o texto na caixa de entrada
        interface.entradaDoTamanhoDoTabuleiro.delete(0, 'end')

    else:
        # Armazena o valor do objetivo anterior
        objetivoAntigo = objetivo

        try:
            # Recebe o novo valor do objetivo e atualiza a variável global
            objetivo = int(interface.objetivoDaPartida.get())

            try:
                # Reinicia a instância da mecânica do jogo com o novo parâmetro
                mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

            # Caso o número passado não seja válido, gera um relatório de erro
            except ValueError as mensagemDeErro:
                # Gera o relatório de erro
                log.relatorioDeErro(repr(mensagemDeErro))

                # Restaura o valor anterior do objetivo
                objetivo = objetivoAntigo

        # Caso o usuário tenha inserido algo diferente de um número, gera um relatório de erro
        except ValueError as mensagemDeErro:
            # Gera o relatório de erro
            log.relatorioDeErro(repr(mensagemDeErro))

            # Restaura o valor anterior do objetivo
            objetivo = objetivoAntigo

        # Apaga o texto na caixa de entrada
        interface.entradaDoObjetivo.delete(0, 'end')

    # Volta para a tela de opções
    opcoes()

def estatisticas():
    '''
    Função para mostrar as estatísticas.

    () -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Define o comando do botão
    interface.botaoVoltarAoMenuPrincipalDaTelaDeEstatisticas['command'] = main

    # Limpa a tela
    interface.limpaTela(interface.janela)

    # Mostra a tela das estatísticas
    interface.telaDasEstatisticas(log.getEstatisticasDeJogadas(), log.getEstatisticasDePecas(), log.getEstatisticasDeScore())

    # Loop do tkinter
    interface.janela.mainloop()

def manual():
    '''
    Função para mostrar o manual do desenvolvedor.

    () -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Define o comando do botão
    interface.botaoVoltarAoMenuPrincipalDaTelaDoManual['command'] = main

    # Limpa a tela
    interface.limpaTela(interface.janela)

    # Mostra o título da tela
    interface.telaDoManual()

    # Insere na tela a documentação de todas as classes do jogo
    interface.textoDoManualDoDesenvolvedor.insert('end', interface.__str__())
    interface.textoDoManualDoDesenvolvedor.insert('end', mecanica.__str__())
    interface.textoDoManualDoDesenvolvedor.insert('end', log.__str__())

    # Loop do tkinter
    interface.janela.mainloop()

if __name__ == '__main__':
    main()
