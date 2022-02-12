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

    # Reinicia a instância da mecânica do jogo
    mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

    # Limpa a tela
    interface.limpaTela(interface.janela)

    # Exibe o menu principal
    interface.menuPrincipal()

    # Configura o comando de cada botão
    interface.botaoNovoJogo['command'] = iniciaLoopDoJogo
    interface.botaoCarregarJogo['command'] = partidasSalvas

    # Loop do tkinter
    interface.janela.mainloop()

    # Recebendo a entrada do usuário
    entrada = interface.entradaDoUsuario()

    # Verifica qual opção o usuário escolheu
    # Novo Jogo
    if entrada == '1':
        # Inicia um novo jogo
        iniciaLoopDoJogo()

    # Carregar Jogo
    elif entrada == '2':
        # Loop para receber a entrada do usuário da tela de opções
        while True:
            # Limpa a tela
            interface.limpaTela(interface.janela)

            # Lê as partidas salvas
            dadosDasPartidasSalvas = log.carregarJogo()

            # Mostra a tela de carregamento
            interface.telaDeCarregamento(dadosDasPartidasSalvas)

            # Caso não exista nenhuma partida salva, volta para o menu principal
            if dadosDasPartidasSalvas == []:
                interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
                main()

            # Espera a entrada do usuário
            entrada = interface.entradaDoUsuario()

            # Seleciona uma ação de acordo com a entrada do usuário
            # Carregar jogo
            if entrada == '1':
                # Loop para receber a entrada do usuário
                while True:
                    entrada = interface.entradaDoUsuario('Insira o número da partida que deseja carregar ou "c" para cancelar:\n')

                    # Caso o usuário tenha inserido "c", quebra o loop
                    if entrada == 'c' or entrada == 'C':
                        break

                    # Tenta converter a entrada para o índice da partida salva
                    try:
                        indiceDaPartidaSalva = (int(entrada) - 1) * 5

                        # Verifica se o índice inserido é válido
                        try:
                            # Se não for, gera um erro
                            if indiceDaPartidaSalva < 0 or indiceDaPartidaSalva >= len(dadosDasPartidasSalvas):
                                raise ValueError('Nao existe partida salva com o numero inserido')

                            # Se for, carrega a partida salva
                            else:
                                # Atualiza as variáveis de configuração com os dados da partida salva
                                tamanhoDoTabuleiro = int(dadosDasPartidasSalvas[indiceDaPartidaSalva + 1])
                                objetivo = int(dadosDasPartidasSalvas[indiceDaPartidaSalva + 2])

                                # Reinicia a instância da mecânica do jogo
                                mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

                                # Atualiza o tabuleiro e o score com os dados da partida salva
                                mecanica.carregarJogo(eval(dadosDasPartidasSalvas[indiceDaPartidaSalva + 3]), int(dadosDasPartidasSalvas[indiceDaPartidaSalva + 4]))

                                # Reinicia o loop do jogo
                                iniciaLoopDoJogo()

                        # Caso o índice não seja válido, gera um relatório de erro, imprime uma mensagem na tela e repete o loop
                        except ValueError as mensagemDeErro:
                            log.relatorioDeErro(repr(mensagemDeErro))
                            print(mensagemDeErro)

                    # Caso o usuário tenha inserido algo diferente de um número, gera um relatório de erro e repete o loop
                    except ValueError as mensagemDeErro:
                        log.relatorioDeErro(repr(mensagemDeErro))
                        print('Entrada inválida')

            # Apagar partida salva
            elif entrada == '2':
                # Loop para receber a entrada do usuário
                while True:
                    entrada = interface.entradaDoUsuario('Insira o número da partida que deseja apagar ou "c" para cancelar:\n')

                    # Caso o usuário tenha inserido "c", quebra o loop
                    if entrada == 'c' or entrada == 'C':
                        break

                    # Tenta converter a entrada para int
                    try:
                        indiceDaPartidaSalva = int(entrada)

                        # Tenta apagar a partida salva
                        try:
                            # Apaga a partida salva
                            log.apagarJogoSalvo(indiceDaPartidaSalva)

                            # Quebra o loop
                            break

                        # Caso o índice não seja válido, gera um relatório de erro, imprime uma mensagem na tela e repete o loop
                        except ValueError as mensagemDeErro:
                            log.relatorioDeErro(repr(mensagemDeErro))
                            print(mensagemDeErro)

                    # Caso o usuário tenha inserido algo diferente de um número, gera um relatório de erro e repete o loop
                    except ValueError as mensagemDeErro:
                        log.relatorioDeErro(repr(mensagemDeErro))
                        print('Entrada inválida')

            # Voltar ao menu principal
            elif entrada == '3':
                main()

    # Opções
    elif entrada == '3':
        # Loop para receber a entrada do usuário da tela de opções
        while True:
            # Limpa a tela
            interface.limpaTela(interface.janela)

            # Mostra a tela de opções
            interface.telaDeOpcoes(tamanhoDoTabuleiro, objetivo)
            
            # Espera a entrada do usuário
            entrada = interface.entradaDoUsuario()

            # Seleciona uma ação de acordo com a entrada do usuário
            # Alterar o tamanho do tabuleiro
            if entrada == '1':
                # Variável para armazenar o tamanho antigo do tabuleiro
                tamanhoDoTabuleiroAntigo = tamanhoDoTabuleiro

                # Loop para receber a entrada do usuário na alteração do tamanho do tabuleiro
                while True:
                    # Espera a entrada do usuário
                    entrada = interface.entradaDoUsuario('Insira o novo tamanho do tabuleiro ou "c" para cancelar:\n')

                    # Caso o usuário tenha inserido "c", quebra o loop
                    if entrada == 'c' or entrada == 'C':
                        # Se o usuário cancelar a mudança, muda de volta para o tamanho do tabuleiro antigo
                        tamanhoDoTabuleiro = tamanhoDoTabuleiroAntigo

                        # Quebra o loop
                        break

                    # Tenta converter a entrada para int
                    try:
                        # Muda a variável com o novo tamanho do tabuleiro
                        tamanhoDoTabuleiro = int(entrada)

                        # Tenta reiniciar a instância da mecânica do jogo com o valor inserido
                        try:
                            # Reinicia a instância da mecânica do jogo com o novo parâmetro
                            mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

                            # Quebra o loop
                            break

                        # Caso o número inserido não seja válido, gera um relatório de erro, imprime uma mensagem na tela e repete o loop
                        except ValueError as mensagemDeErro:
                            log.relatorioDeErro(repr(mensagemDeErro))
                            print(mensagemDeErro)

                    # Caso o usuário tenha inserido algo diferente de um número, gera um relatório de erro e repete o loop
                    except ValueError as mensagemDeErro:
                        log.relatorioDeErro(repr(mensagemDeErro))
                        print('Entrada inválida')

            # Alterar o objetivo da partida
            elif entrada == '2':
                # Variável para armazenar o objetivo da partida antigo
                objetivoAntigo = objetivo

                # Loop para receber a entrada do usuário na alteração do objetivo da partida
                while True:
                    # Espera a entrada do usuário
                    entrada = interface.entradaDoUsuario('Insira o novo valor do objetivo ou "c" para cancelar:\n')

                    # Caso o usuário tenha inserido "c", quebra o loop
                    if entrada == 'c' or entrada == 'C':
                        # Se o usuário cancelar a mudança, muda de volta para o tamanho do tabuleiro antigo
                        objetivo = objetivoAntigo

                        # Quebra o loop
                        break

                    # Tenta converter a entrada para int
                    try:
                        # Muda a variável com o novo objetivo
                        objetivo = int(entrada)

                        # Tenta reiniciar a instância da mecânica do jogo com o valor inserido
                        try:
                            # Reinicia a instância da mecânica do jogo com o novo parâmetro
                            mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

                            # Quebra o loop
                            break

                        # Caso o número inserido não seja válido, gera um relatório de erro, imprime uma mensagem na tela e repete o loop
                        except ValueError as mensagemDeErro:
                            log.relatorioDeErro(repr(mensagemDeErro))
                            print(mensagemDeErro)

                    # Caso o usuário tenha inserido algo diferente de um número, gera um relatório de erro e repete o loop
                    except ValueError as mensagemDeErro:
                        log.relatorioDeErro(repr(mensagemDeErro))
                        print('Entrada inválida')

            # Voltar ao menu principal
            elif entrada == '3':
                main()

    # Estatísticas
    elif entrada == '4':
        # Limpa a tela
        interface.limpaTela(interface.janela)

        # Mostra a tela das estatísticas
        interface.telaDasEstatisticas(log.getEstatisticasDeJogadas(), log.getEstatisticasDePecas(), log.getEstatisticasDeScore())

        # Volta para o menu principal
        main()

    # Manual do Desenvolvedor
    elif entrada == '5':
        # Limpa a tela
        interface.limpaTela(interface.janela)

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
        # Limpa a tela
        interface.limpaTela(interface.janela)

        # Sai do jogo
        quit()

    # Caso o usuário insira qualquer outra coisa diferente do pedido, exibe novamente o menu principal
    else:
        main()

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

    str -> bool
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Atualiza a estatística de jogadas
    log.estatisticasDeJogadas(direcao)

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
        # Verifica se o alguma peça atingiu o objetivo
        # Se sim, atualiza as estatísticas e encerra o loop do jogo
        if mecanica.venceuOJogo() == True:
            # Atualiza a estatística de peças com o objetivo atingido
            log.estatisticasDePecas(objetivo)

            # Atualiza a estatística de score com o score da partida
            log.estatisticasDeScore(mecanica.getScore())

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
        # Se não possuir, atualiza as estatísticas e encerra o loop do jogo
        if mecanica.possuiMovimentosVailidos() == False:
            # Atualiza a estatística de peças com a maior peça no tabuleiro
            log.estatisticasDePecas(mecanica.getValorDaMaiorPeca())

            # Atualiza a estatística de score com o score da partida
            log.estatisticasDeScore(mecanica.getScore())

            # Encerra o loop do jogo e mostra a tela de fim de jogo
            fimDeJogo(False)

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

    # Mostra a tela de fim de jogo
    interface.pausa(interface.janela, 1500)
    interface.limpaTela(interface.janela)
    interface.telaDeFimDeJogo(venceuOJogo, mecanica.getScore())

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
    interface.botaoVoltarAoMenuPrincipalDaTelaDePause['command'] = main

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

def partidasSalvas():
    '''
    Função para mostrar a lista de partidas salvas na tela de carregar
    jogo.

    () -> None
    '''
    # Define o comando dos botão
    interface.botaoVoltarAoMenuPrincipalDaTelaDeCarregamento['command'] = main

    # Limpa a tela
    interface.limpaTela(interface.janela)

    # Lê as partidas salvas
    dadosDasPartidasSalvas = log.carregarJogo()

    # Mostra a tela de carregamento
    interface.telaDeCarregamento(dadosDasPartidasSalvas)

    # Loop do tkinter
    interface.janela.mainloop()

if __name__ == '__main__':
    main()
