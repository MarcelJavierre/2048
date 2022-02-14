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
    interface.limpaTela()

    # Exibe o menu principal
    try:
        entrada = interface.menuPrincipal()

    # Caso a entrada não seja válida, gera o relatório de erro e retorna ao menu principal
    except ErroDeComando as mensagemDeErro:
        # Gera o relatório de erro
        log.relatorioDeErro(repr(mensagemDeErro))

        # Retorna ao menu principal
        main()

    # Verifica qual opção o usuário escolheu
    # Opção "Novo Jogo"
    if entrada == '1':
        # Mostra a tela dos controles
        interface.limpaTela()
        interface.telaDosControles()
        interface.entradaDoUsuario('Aperte Enter para Iniciar a Partida\n')

        # Inicia o Loop do jogo
        iniciaLoopDoJogo()

    # Carregar Jogo
    elif entrada == '2':
        # Loop para receber a entrada do usuário da tela de opções
        while True:
            # Limpa a tela
            interface.limpaTela()

            # Lê as partidas salvas
            listaComOsDadosDasPartidasSalvas = log.carregarJogo()

            # Mostra a tela de carregamento
            interface.telaDeCarregamento(listaComOsDadosDasPartidasSalvas)

            # Caso não exista nenhuma partida salva, volta para o menu principal
            if listaComOsDadosDasPartidasSalvas == []:
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
                            if indiceDaPartidaSalva < 0 or indiceDaPartidaSalva >= len(listaComOsDadosDasPartidasSalvas):
                                raise ValueError('Nao existe partida salva com o numero inserido')

                            # Se for, carrega a partida salva
                            else:
                                # Atualiza as variáveis de configuração com os dados da partida salva
                                tamanhoDoTabuleiro = int(listaComOsDadosDasPartidasSalvas[indiceDaPartidaSalva + 1])
                                objetivo = int(listaComOsDadosDasPartidasSalvas[indiceDaPartidaSalva + 2])

                                # Reinicia a instância da mecânica do jogo
                                mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

                                # Atualiza o tabuleiro e o score com os dados da partida salva
                                mecanica.carregarJogo(eval(listaComOsDadosDasPartidasSalvas[indiceDaPartidaSalva + 3]), int(listaComOsDadosDasPartidasSalvas[indiceDaPartidaSalva + 4]))

                                # Reinicia o loop do jogo
                                loopDoJogo()

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
            interface.limpaTela()

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
        interface.limpaTela()

        # Mostra a tela das estatísticas
        interface.telaDasEstatisticas(log.getEstatisticasDeJogadas(), log.getEstatisticasDePecas(), log.getEstatisticasDeScore())

        # Volta para o menu principal
        main()

    # Manual do Desenvolvedor
    elif entrada == '5':
        # Limpa a tela
        interface.limpaTela()

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
        interface.limpaTela()

        # Sai do jogo
        quit()

    # Caso o usuário insira qualquer outra coisa diferente do pedido, exibe novamente o menu principal
    else:
        main()

def iniciaLoopDoJogo():
    '''
    Função que exibe a tela do tabuleiro e recebe a entrada do usuário.

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
    interface.limpaTela()

    # Mostra o tabuleiro
    try:
        entrada = interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore(), objetivo, True)

    # Caso a entrada não seja válida, gera o relatório de erro e retorna ao início do loop do jogo
    except ErroDeComando as mensagemDeErro:
        # Gera o relatório de erro
        log.relatorioDeErro(repr(mensagemDeErro))

        # Retorna ao início do loop do jogo
        iniciaLoopDoJogo()

    # Caso a entrada do usuário tenha sido 'p', pausa a partida
    if entrada == 'p':
        pause()

    # Caso contrário, realiza o loop do jogo
    else:
        loopDoJogo(entrada)

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

    # Variável para indicar se alguma ação foi realizada
    houveMudanca = False

    # Loop para mover as peças do tabuleiro
    while mecanica.movePecas(direcao) == True:
        interface.pausa(0.1)
        interface.limpaTela()
        interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore(), objetivo)

        # Muda a variável para indicar que houve uma ação
        houveMudanca = True

    # Junta as peças do tabuleiro
    if mecanica.juntaPecas(direcao) == True:
        interface.pausa(0.1)
        interface.limpaTela()
        interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore(), objetivo)

        # Muda a variável para indicar que houve uma ação
        houveMudanca = True

    # Loop para mover as peças do tabuleiro
    while mecanica.movePecas(direcao) == True:
        interface.pausa(0.1)
        interface.limpaTela()
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
        interface.limpaTela()

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

    # Atualiza a estatística de peças com a maior peça no tabuleiro
    log.estatisticasDePecas(mecanica.getValorDaMaiorPeca())

    # Atualiza a estatística de score com o score da partida
    log.estatisticasDeScore(mecanica.getScore())

    # Mostra a tela de fim de jogo
    interface.pausa(1.5)
    interface.limpaTela()
    interface.telaDeFimDeJogo(venceuOJogo, mecanica.getScore())

    # Reinicia a instância da mecânica do jogo
    mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

    # Volta para o menu principal
    interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
    main()

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

    # Limpa a tela
    interface.limpaTela()

    # Mostra a tela de pause
    try:
        entrada = interface.telaDePause()

    # Caso a entrada não seja válida, gera o relatório de erro e retorna a tela de pause
    except ErroDeComando as mensagemDeErro:
        # Gera o relatório de erro
        log.relatorioDeErro(repr(mensagemDeErro))

        # Retorna a tela de pause
        pause()

    # Verifica qual opção o usuário escolheu
    # Opção "Voltar ao Jogo"
    if entrada == '1':
        # Retorna ao início do loop do jogo
        iniciaLoopDoJogo()

    # Opção "Salvar o Jogo"
    elif entrada == '2':
        # Salva a partida
        salvarOJogo()

    # Opção "Voltar ao Menu"
    else:
        # Volta ao menu principal
        voltarAoMenuPrincipal()

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
    interface.limpaTela()

    # Mostra a tela de salvamento
    interface.telaDeSalvamento()

    # Salva o jogo
    log.savarJogo(tamanhoDoTabuleiro, objetivo, mecanica.getTabuleiro().tolist(), mecanica.getScore())

    # Espera 1 segundo
    interface.pausa(1)

    # Volta para a tela de pause
    pause()

def voltarAoMenuPrincipal():
    '''
    Função que reinicia a instância da mecânica do jogo e retorna ao menu principal.

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

if __name__ == '__main__':
    main()
