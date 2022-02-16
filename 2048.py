"""
2048
====

Introdução
----------

O objetivo deste projeto é o desenvolvimento do jogo 2048 em Python.

Finalidade
----------

A finalidade é deste projeto é ser utilizado como avaliação para a
disciplina de Computação II da Universidade Federal do Rio de Janeiro.

Sobre o jogo
------------

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
from secoes.interfaceComOUsuario import *
from secoes.mecanicaDoJogo import *
from secoes.log import *

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

    # Opção "Carregar Jogo"
    elif entrada == '2':
        # Mostra a tela com as partidas salvas
        partidasSalvas()

    # Opção "Opções"
    elif entrada == '3':
        # Mostra a tela com as partidas salvas
        opcoes()

    # Opção "Estatísticas"
    elif entrada == '4':
        estatisticas()

    # Opção "Manual do Desenvolvedor"
    elif entrada == '5':
        manual()

    # Opção "Sair do Jogo"
    else:
        # Limpa a tela
        interface.limpaTela()

        # Sai do jogo
        quit()

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

    # Atualiza a estatística de fusões com a quantidade de fusões da partida
    log.estatisticasDeFusoes(mecanica.getQuantidadeDeFusoes())

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

    # Atualiza a estatística de peças com a maior peça no tabuleiro
    log.estatisticasDePecas(mecanica.getValorDaMaiorPeca())

    # Atualiza a estatística de score com o score da partida
    log.estatisticasDeScore(mecanica.getScore())

    # Atualiza a estatística de fusões com a quantidade de fusões da partida
    log.estatisticasDeFusoes(mecanica.getQuantidadeDeFusoes())

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

    # Limpa a tela
    interface.limpaTela()

    # Lê as partidas salvas
    dadosDasPartidasSalvas = log.carregarJogo()

    # Mostra a tela de carregamento
    try:
        entrada = interface.telaDeCarregamento(dadosDasPartidasSalvas)

    # Caso a entrada não seja válida, gera o relatório de erro e retorna a tela de carregar jogo
    except ErroDeComando as mensagemDeErro:
        # Gera o relatório de erro
        log.relatorioDeErro(repr(mensagemDeErro))

        # Retorna a tela de carregar jogo
        partidasSalvas()

    # Caso não possua partidas salvas, retorna ao menu principal
    if dadosDasPartidasSalvas == []:
        main()

    # Verifica qual opção o usuário escolheu
    # Opção "Carregar Jogo"
    elif entrada == '1':
        carregarJogo(dadosDasPartidasSalvas)

    # Opção "Apagar Partida"
    elif entrada == '2':
        apagarPartidaSalva()

    # Voltar ao menu principal
    else:
        main()

def carregarJogo(dadosDasPartidasSalvas):
    '''
    Função que, dado a lista com os dados das partidas salvas, solicita
    ao usuário o índice da partida salva e reinicia o loop do jogo com
    os dados salvos.

    list[str] -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log

    # Solicita ao usuário o índice da partida salva
    entrada = interface.entradaDoUsuario('Insira o número da partida que deseja carregar ou "c" para cancelar:\n')

    # Caso o usuário tenha inserido "c" ou "C", retorna para a tela com as partidas salvas
    if entrada == 'c' or entrada == 'C':
        partidasSalvas()

    try:
        # Converte a entrada para o índice da partida salva
        indiceDaPartidaSalva = (int(entrada) - 1) * 5

        try:
            # Se o índice inserido não é válido, gera um erro
            if indiceDaPartidaSalva < 0 or indiceDaPartidaSalva >= len(dadosDasPartidasSalvas):
                raise ValueError('Nao existe partida salva com o numero inserido')

            # Atualiza as variáveis de configuração com os dados da partida salva
            tamanhoDoTabuleiro = int(dadosDasPartidasSalvas[indiceDaPartidaSalva + 1])
            objetivo = int(dadosDasPartidasSalvas[indiceDaPartidaSalva + 2])

            # Reinicia a instância da mecânica do jogo
            mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

            # Atualiza o tabuleiro e o score com os dados da partida salva
            mecanica.carregarJogo(eval(dadosDasPartidasSalvas[indiceDaPartidaSalva + 3]), int(dadosDasPartidasSalvas[indiceDaPartidaSalva + 4]))

            # Reinicia o loop do jogo
            iniciaLoopDoJogo()

        # Caso o índice não seja válido, gera um relatório de erro, imprime uma mensagem na tela e repete a função de carregar jogo
        except ValueError as mensagemDeErro:
            # Gera o relatório de erro
            log.relatorioDeErro(repr(mensagemDeErro))

            # Escreve na tela uma mensagem de erro
            print(mensagemDeErro)

            # Repete a função de carregar jogo
            carregarJogo(dadosDasPartidasSalvas)

    # Caso o usuário tenha inserido algo diferente de um número, gera um relatório de erro, imprime uma mensagem na tela e repete a função de carregar jogo
    except ValueError as mensagemDeErro:
        # Gera o relatório de erro
        log.relatorioDeErro(repr(mensagemDeErro))

        # Escreve na tela uma mensagem de erro
        print('Entrada inválida')

        # Repete a função de carregar jogo
        carregarJogo(dadosDasPartidasSalvas)

def apagarPartidaSalva():
    '''
    Função que apaga a partida salva.
    
    () -> None
    '''
    # Definindo a utilização das variáveis de configuração globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo a utilização das instâncias de cada seção globais
    global interface
    global mecanica
    global log
    
    # Solicita ao usuário o índice da partida salva
    entrada = interface.entradaDoUsuario('Insira o número da partida que deseja apagar ou "c" para cancelar:\n')

    # Caso o usuário tenha inserido "c" ou "C", retorna para a tela com as partidas salvas
    if entrada == 'c' or entrada == 'C':
        partidasSalvas()

    try:
        # Converte a entrada para int
        indiceDaPartidaSalva = int(entrada)

        try:
            # Apaga a partida salva
            log.apagarJogoSalvo(indiceDaPartidaSalva)

            # Retorna para a tela com as partidas salvas
            partidasSalvas()

        # Caso o índice não seja válido, gera um relatório de erro, imprime uma mensagem na tela e repete a função de apagar partida salva
        except ValueError as mensagemDeErro:
            # Gera o relatório de erro
            log.relatorioDeErro(repr(mensagemDeErro))

            # Escreve na tela uma mensagem de erro
            print(mensagemDeErro)

            # Repete a função de apagar partida salva
            apagarPartidaSalva()

    # Caso o usuário tenha inserido algo diferente de um número, gera um relatório de erro, imprime uma mensagem na tela e repete a função de apagar partida salva
    except ValueError as mensagemDeErro:
        # Gera o relatório de erro
        log.relatorioDeErro(repr(mensagemDeErro))

        # Escreve na tela uma mensagem de erro
        print('Entrada inválida')

        # Repete a função de apagar partida salva
        apagarPartidaSalva()

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

    # Limpa a tela
    interface.limpaTela()

    # Mostra a tela de opções
    try:
        entrada = interface.telaDeOpcoes(tamanhoDoTabuleiro, objetivo)

    # Caso a entrada não seja válida, gera o relatório de erro e retorna a tela de opções
    except ErroDeComando as mensagemDeErro:
        # Gera o relatório de erro
        log.relatorioDeErro(repr(mensagemDeErro))

        # Retorna a tela de opções
        opcoes()

    # Verifica qual opção o usuário escolheu
    # Opção "Alterar Tamanho"
    if entrada == '1':
        atualizaConfiguracao('tamanho')

    # Opção "Alterar Objetivo"
    elif entrada == '2':
        atualizaConfiguracao('objetivo')

    # Opção "Voltar ao Menu Principal"
    else:
        main()

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

        # Recebe a entrada do usuário
        entrada = interface.entradaDoUsuario('Insira o novo tamanho do tabuleiro ou "c" para cancelar:\n')

        # Caso o usuário tenha inserido "c", retorna a tela de opções
        if entrada == 'c' or entrada == 'C':
            opcoes()

        try:
            # Muda a variável com o novo tamanho do tabuleiro
            tamanhoDoTabuleiro = int(entrada)

            try:
                # Reinicia a instância da mecânica do jogo com o novo parâmetro
                mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

            # Caso o número inserido não seja válido, gera um relatório de erro, imprime uma mensagem na tela e repete a função de atualizar a configuração
            except ValueError as mensagemDeErro:
                # Gera o relatório de erro
                log.relatorioDeErro(repr(mensagemDeErro))

                # Escreve na tela uma mensagem de erro
                print(mensagemDeErro)

                # Restaura o valor anterior do tamanho do tabuleiro
                tamanhoDoTabuleiro = tamanhoDoTabuleiroAntigo

                # Repete a função de atualizar a configuração
                atualizaConfiguracao(opcao)

        # Caso o usuário tenha inserido algo diferente de um número, gera um relatório de erro, imprime uma mensagem na tela e repete a função de atualizar a configuração
        except ValueError as mensagemDeErro:
            # Gera o relatório de erro
            log.relatorioDeErro(repr(mensagemDeErro))

            # Escreve na tela uma mensagem de erro
            print('Entrada inválida')

            # Repete a função de atualizar a configuração
            atualizaConfiguracao(opcao)

    else:
        # Variável para armazenar o objetivo da partida antigo
        objetivoAntigo = objetivo

        # Recebe a entrada do usuário
        entrada = interface.entradaDoUsuario('Insira o novo valor do objetivo ou "c" para cancelar:\n')

        # Caso o usuário tenha inserido "c", retorna a tela de opções
        if entrada == 'c' or entrada == 'C':
            opcoes()

        try:
            # Muda a variável com o novo objetivo
            objetivo = int(entrada)

            try:
                # Reinicia a instância da mecânica do jogo com o novo parâmetro
                mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

            # Caso o número inserido não seja válido, gera um relatório de erro, imprime uma mensagem na tela e repete a função de atualizar a configuração
            except ValueError as mensagemDeErro:
                # Gera o relatório de erro
                log.relatorioDeErro(repr(mensagemDeErro))

                # Escreve na tela uma mensagem de erro
                print(mensagemDeErro)

                # Restaura o valor anterior do objetivo
                objetivo = objetivoAntigo

                # Repete a função de atualizar a configuração
                atualizaConfiguracao(opcao)

        # Caso o usuário tenha inserido algo diferente de um número, gera um relatório de erro, imprime uma mensagem na tela e repete a função de atualizar a configuração
        except ValueError as mensagemDeErro:
            # Gera o relatório de erro
            log.relatorioDeErro(repr(mensagemDeErro))

            # Escreve na tela uma mensagem de erro
            print('Entrada inválida')

            # Repete a função de atualizar a configuração
            atualizaConfiguracao(opcao)

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

    # Limpa a tela
    interface.limpaTela()

    try:
        # Mostra a tela das estatísticas
        interface.telaDasEstatisticas(log.getEstatisticasDeJogadas(), log.getEstatisticasDePecas(), log.getEstatisticasDeScore(), log.getEstatisticasDeFusoes())

    # Caso não possua estatísticas, gera um relatório de erro e retorna ao menu principal
    except ErroDeEstatistica as mensagemDeErro:
        # Gera o relatório de erro
        log.relatorioDeErro(repr(mensagemDeErro))

    # Volta para o menu principal
    main()

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

if __name__ == '__main__':
    main()
