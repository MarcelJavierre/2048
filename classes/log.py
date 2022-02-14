# Importando a função localtime do módulo time que retorna a data e a hora
from time import localtime

# Importando a função mkdir do módulo os que permite criar uma pasta
from os import mkdir

# Classe da seção log
class Log:
    '''
    Esta classe trata do armazenamento em arquivos de todos os dados que
    podem vir a ser de interesse do usuário, bem como todos os erros que
    ocorrerem durante a execução do jogo.
    '''

    def __init__(self):
        '''
        Método construtor. Cria as pastas e os arquivos para armazenar
        os dados salvos.

        Self -> None
        '''

        # Cria a pasta "estatisticas"
        try:
            mkdir('estatisticas')

        # Caso a pasta já exista, não faz nada
        except FileExistsError:
            pass

        # Cria a pasta "partidasSalvas"
        try:
            mkdir('partidasSalvas')

        # Caso a pasta já exista, não faz nada
        except FileExistsError:
            pass

        # Cria a pasta "relatorioDeErros"
        try:
            mkdir('relatorioDeErros')

        # Caso a pasta já exista, não faz nada
        except FileExistsError:
            pass

        # Cria o arquivo "partidasSalvas" dentro da pasta "partidasSalvas"
        try:
            arquivo = open('partidasSalvas/partidasSalvas', 'x')
            arquivo.close()

        # Caso o arquivo já exista, não faz nada
        except FileExistsError:
            pass

        # Cria o arquivo "estatisticasDeJogadas" dentro da pasta "estatisticas" com a estrutura para armazenar os dados
        try:
            # Cria o arquivo
            arquivo = open('estatisticas/estatisticasDeJogadas', 'x')
            arquivo.close()

            # Abre novamente o arquivo e escreve nele a estrutura para armazenar os dados
            arquivo = open('estatisticas/estatisticasDeJogadas', 'w')
            arquivo.write('Cima:\n')
            arquivo.write('0\n')
            arquivo.write('Baixo:\n')
            arquivo.write('0\n')
            arquivo.write('Esquerda:\n')
            arquivo.write('0\n')
            arquivo.write('Direita:\n')
            arquivo.write('0\n')
            arquivo.close()

        # Caso o arquivo já exista, não faz nada
        except FileExistsError:
            pass

        # Cria o arquivo "estatisticasDePecas" dentro da pasta "estatisticas" com a estrutura para armazenar os dados
        try:
            # Cria o arquivo
            arquivo = open('estatisticas/estatisticasDePecas', 'x')
            arquivo.close()

            # Abre novamente o arquivo e escreve nele a estrutura para armazenar os dados
            arquivo = open('estatisticas/estatisticasDePecas', 'w')
            arquivo.write('2:\n')
            arquivo.write('0\n')
            arquivo.write('4:\n')
            arquivo.write('0\n')
            arquivo.write('8:\n')
            arquivo.write('0\n')
            arquivo.write('16:\n')
            arquivo.write('0\n')
            arquivo.write('32:\n')
            arquivo.write('0\n')
            arquivo.write('64:\n')
            arquivo.write('0\n')
            arquivo.write('128:\n')
            arquivo.write('0\n')
            arquivo.write('256:\n')
            arquivo.write('0\n')
            arquivo.write('512:\n')
            arquivo.write('0\n')
            arquivo.write('1024:\n')
            arquivo.write('0\n')
            arquivo.write('2048:\n')
            arquivo.write('0\n')
            arquivo.write('Outros:\n')
            arquivo.write('0\n')
            arquivo.close()

        # Caso o arquivo já exista, não faz nada
        except FileExistsError:
            pass

        # Cria o arquivo "estatisticasDeScore" dentro da pasta "estatisticas"
        try:
            arquivo = open('estatisticas/estatisticasDeScore', 'x')
            arquivo.close()

        # Caso o arquivo já exista, não faz nada
        except FileExistsError:
            pass

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
            'savarJogo',
            'carregarJogo',
            'apagarJogoSalvo',
            'estatisticasDeJogadas',
            'estatisticasDePecas',
            'estatisticasDeScore',
            'getEstatisticasDeJogadas',
            'getEstatisticasDePecas',
            'getEstatisticasDeScore',
            'relatorioDeErro'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com
        todos os atributos e métodos da classe.

        Self -> str
        '''

        string = f'Classe Log:\n{Log.__doc__}\n\nAtributos:\n'

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
            '__init__': self.__init__.__doc__,
            '__str__': self.__str__.__doc__,
            'getAtributos': self.getAtributos.__doc__,
            'getMetodos': self.getMetodos.__doc__,
            'manual': self.manual.__doc__,
            'savarJogo': self.savarJogo.__doc__,
            'carregarJogo': self.carregarJogo.__doc__,
            'apagarJogoSalvo': self.apagarJogoSalvo.__doc__,
            'estatisticasDeJogadas': self.estatisticasDeJogadas.__doc__,
            'estatisticasDePecas': self.estatisticasDePecas.__doc__,
            'estatisticasDeScore': self.estatisticasDeScore.__doc__,
            'getEstatisticasDeJogadas': self.getEstatisticasDeJogadas.__doc__,
            'getEstatisticasDePecas': self.getEstatisticasDePecas.__doc__,
            'getEstatisticasDeScore': self.getEstatisticasDeScore.__doc__,
            'relatorioDeErro': self.relatorioDeErro.__doc__
        }

    def savarJogo(self, tamanhoDoTabuleiro, objetivo, tabuleiro, score):
        '''
        Método que armazena em um arquivo o estado atual do jogo. O
        arquivo de salvamento se encontra em
        "partidasSalvas/partidasSalvas". Cada partida salva ocupa 5
        linhas no arquivo, sendo elas:

        * 1ª Linha: Data e Hora do Salvamento;
        * 2ª Linha: Tamanho do Tabuleiro;
        * 3ª Linha: Objetivo da Partida;
        * 4ª Linha: Matriz do Tabuleiro;
        * 5ª Linha: Score.

        Self, int, int, list[int], int -> None
        '''
        # Abre o arquivo
        arquivo = open('partidasSalvas/partidasSalvas', 'a')

        # Escreve no arquivo o conteúdo da partida
        arquivo.write(f'{localtime()[2]:02d}/{localtime()[1]:02d}/{localtime()[0]}    {localtime()[3]:02d}:{localtime()[4]:02d}\n{tamanhoDoTabuleiro}\n{objetivo}\n{tabuleiro}\n{score}\n')
        
        # Fecha o arquivo
        arquivo.close()

    def carregarJogo(self):
        '''
        Método que carrega de um arquivo o jogo salvo. Retorna uma lista
        com o seguinte conteúdo:

        * 1ª índice [0]: Data e Hora do Salvamento;
        * 2ª índice [1]: Tamanho do Tabuleiro;
        * 3ª índice [2]: Objetivo da Partida;
        * 4ª índice [3]: Matriz do Tabuleiro;
        * 5ª índice [4]: Score.

        Self -> list[str]
        '''
        # Abre o arquivo
        arquivo = open('partidasSalvas/partidasSalvas', 'r')

        # Lê o conteúdo do arquivo
        conteudoDoArquivo = arquivo.readlines()

        # Fecha o arquivo
        arquivo.close()

        # Retorna o conteúdo do arquivo
        return conteudoDoArquivo

    def apagarJogoSalvo(self, indiceDaPartidaSalva):
        '''
        Método para apagar do arquivo com as partidas salvas um jogo
        salvo. Gera um "ValueError" caso o índice passado não seja
        válido.

        Self, int -> None
        '''
        # Abre o arquivo no modo leitura
        arquivo = open('partidasSalvas/partidasSalvas', 'r')

        # Lê o conteúdo do arquivo
        conteudoDoArquivo = arquivo.readlines()

        # Fecha o arquivo
        arquivo.close()

        # Converte o índice da partida salva passado para o índice da lista do conteúdo do arquivo
        indiceDoConteudoDoArquivo = (indiceDaPartidaSalva - 1) * 5

        # Verifica se o índice passado é válido
        if indiceDoConteudoDoArquivo < 0 or indiceDoConteudoDoArquivo >= len(conteudoDoArquivo):
            # Se não for, gera um erro
            raise ValueError('Nao existe partida salva com o numero passado')

        # Remove os dados da partida salva
        conteudoDoArquivo.pop(indiceDoConteudoDoArquivo)
        conteudoDoArquivo.pop(indiceDoConteudoDoArquivo)
        conteudoDoArquivo.pop(indiceDoConteudoDoArquivo)
        conteudoDoArquivo.pop(indiceDoConteudoDoArquivo)
        conteudoDoArquivo.pop(indiceDoConteudoDoArquivo)

        # Abre o arquivo no modo sobrescrever
        arquivo = open('partidasSalvas/partidasSalvas', 'w')

        # Escreve o conteúdo de volta no arquivo
        for i in range(len(conteudoDoArquivo)):
            arquivo.write(conteudoDoArquivo[i])

        # Fecha o arquivo
        arquivo.close()

    def estatisticasDeJogadas(self, jogada):
        '''
        Método que armazena em um arquivo a quantidade de jogadas para
        cada direção. A estrutura do arquivo é a seguinte:

        * 1ª linha: "Cima";
        * 2ª linha: Quantidade de jogadas realizadas para cima;
        * 3ª linha: "Baixo";
        * 4ª linha: Quantidade de jogadas realizadas para baixo;
        * 5ª linha: "Esquerda";
        * 6ª linha: Quantidade de jogadas realizadas para a esquerda;
        * 7ª linha: "Direita";
        * 8ª linha: Quantidade de jogadas realizadas para a direita.

        Self, str -> None
        '''
        # Abre o arquivo no modo leitura
        arquivo = open('estatisticas/estatisticasDeJogadas', 'r')

        # Lê o conteúdo do arquivo
        conteudoDoArquivo = arquivo.readlines()

        # Fecha o arquivo
        arquivo.close()

        # Abre o arquivo no modo sobrescrever
        arquivo = open('estatisticas/estatisticasDeJogadas', 'w')

        # Verifica qual jogada foi realizada e insere mais 1 na quantidade de jogadas realizadas para aquela direção
        if jogada == 'cima':
            conteudoDoArquivo[1] = f'{int(conteudoDoArquivo[1][: - 1]) + 1}\n'
        elif jogada == 'baixo':
            conteudoDoArquivo[3] = f'{int(conteudoDoArquivo[3][: - 1]) + 1}\n'
        elif jogada == 'esquerda':
            conteudoDoArquivo[5] = f'{int(conteudoDoArquivo[5][: - 1]) + 1}\n'
        else:
            conteudoDoArquivo[7] = f'{int(conteudoDoArquivo[7][: - 1]) + 1}\n'

        # Escreve o conteúdo de volta no arquivo
        for i in range(len(conteudoDoArquivo)):
            arquivo.write(conteudoDoArquivo[i])

        # Fecha o arquivo
        arquivo.close()

    def estatisticasDePecas(self, maiorPecaNoTabuleiro):
        '''
        Método que armazena em um arquivo a quantidade de vezes que
        aquela peça foi a maior no tabuleiro ao finalizar ou sair de uma
        partida. A estrutura do arquivo é a seguinte:

        * 1ª Linha: "2";
        * 2ª Linha: Quantidade de partidas encerradas com a peça no
                    valor 2 sendo a maior do tabuleiro;
        * 3ª Linha: "4";
        * 4ª Linha: Quantidade de partidas encerradas com a peça no
                    valor 4 sendo a maior do tabuleiro;
        * 5ª Linha: "8";
        * 6ª Linha: Quantidade de partidas encerradas com a peça no
                    valor 8 sendo a maior do tabuleiro;
        * 7ª Linha: "16";
        * 8ª Linha: Quantidade de partidas encerradas com a peça no
                    valor 16 sendo a maior do tabuleiro;

        .
        .
        .
        
        Self, int -> None
        '''
        # Abre o arquivo no modo leitura
        arquivo = open('estatisticas/estatisticasDePecas', 'r')

        # Lê o conteúdo do arquivo
        conteudoDoArquivo = arquivo.readlines()

        # Fecha o arquivo
        arquivo.close()

        # Abre o arquivo no modo sobrescrever
        arquivo = open('estatisticas/estatisticasDePecas', 'w')

        # Caso o valor da maior peça seja maior que 2048, muda seu valor para "Outros"
        if maiorPecaNoTabuleiro > 2048:
            maiorPecaNoTabuleiro = 'Outros'

        # Procura o índice da quantidade da peça no conteúdo do arquivo
        indice = conteudoDoArquivo.index(f'{maiorPecaNoTabuleiro}:\n') + 1

        # Insere mais 1 na quantidade
        conteudoDoArquivo[indice] = f'{int(conteudoDoArquivo[indice][: - 1]) + 1}\n'

        # Escreve o conteúdo de volta no arquivo
        for i in range(len(conteudoDoArquivo)):
            arquivo.write(conteudoDoArquivo[i])

        # Fecha o arquivo
        arquivo.close()

    def estatisticasDeScore(self, score):
        '''
        Método que armazena em um arquivo o histórico de score das
        partidas. A estrutura do arquivo consiste em cada linha conter o
        score de uma partida.

        Self, int -> None
        '''
        # Abre o arquivo
        arquivo = open('estatisticas/estatisticasDeScore', 'a')

        # Insere o score no final do arquivo
        arquivo.write(f'{score}\n')

        # Fecha o arquivo
        arquivo.close()

    def getEstatisticasDeJogadas(self):
        '''
        Método que retorna uma tupla na qual a primeira posição é uma
        lista com as direções (eixo x) e a segunda é uma lista com a
        quantidade (eixo y).

        Self -> tuple[list[str], list[int]]
        '''
        # Abre o arquivo no modo leitura
        arquivo = open('estatisticas/estatisticasDeJogadas', 'r')

        # Lê o conteúdo do arquivo
        conteudoDoArquivo = arquivo.readlines()

        # Fecha o arquivo
        arquivo.close()

        # Lista para armazenar as estatísticas
        eixoX = []
        eixoY = []

        # Passa por todas as linhas do arquivo
        for i in range(0, len(conteudoDoArquivo) - 1, 2):
            # Remove os caracteres ":" e "\n" e armazena na lista
            eixoX.append(conteudoDoArquivo[i][: - 2])

            # Remove o caractere "\n", converte para int e armazena na lista
            eixoY.append(int(conteudoDoArquivo[i + 1][: - 1]))

        return eixoX, eixoY

    def getEstatisticasDePecas(self):
        '''
        Método que retorna uma tupla na qual a primeira posição é uma
        lista com o valor das peças (eixo x) e a segunda é uma lista com
        a quantidade (eixo y).

        Self -> tuple[list[str], list[int]]
        '''
        # Abre o arquivo no modo leitura
        arquivo = open('estatisticas/estatisticasDePecas', 'r')

        # Lê o conteúdo do arquivo
        conteudoDoArquivo = arquivo.readlines()

        # Fecha o arquivo
        arquivo.close()

        # Lista para armazenar as estatísticas
        eixoX = []
        eixoY = []

        # Passa por todas as linhas do arquivo
        for i in range(0, len(conteudoDoArquivo) - 1, 2):
            # Remove os caracteres ":" e "\n" e armazena na lista
            eixoX.append(conteudoDoArquivo[i][: - 2])

            # Remove o caractere "\n", converte para int e armazena na lista
            eixoY.append(int(conteudoDoArquivo[i + 1][: - 1]))

        return eixoX, eixoY

    def getEstatisticasDeScore(self):
        '''
        Método que retorna uma tupla na qual a primeira posição é uma
        lista com a quantidade de partidas (eixo x) e a segunda é uma
        lista com os scores (eixo y).

        Self -> tuple[list[int]]
        '''
        # Abre o arquivo no modo leitura
        arquivo = open('estatisticas/estatisticasDeScore', 'r')

        # Lê o conteúdo do arquivo
        conteudoDoArquivo = arquivo.readlines()

        # Fecha o arquivo
        arquivo.close()

        # Lista para armazenar as estatísticas
        eixoX = []
        eixoY = []

        # Passa por todas as linhas do arquivo
        for i in range(len(conteudoDoArquivo)):
            # Adiciona na lista o número da partida
            eixoX.append(i + 1)

            # Remove o caractere "\n", converte para int e armazena na lista
            eixoY.append(int(conteudoDoArquivo[i][: - 1]))

        return eixoX, eixoY
    
    def relatorioDeErro(self, mensagemDeErro):
        '''
        Método que cria um arquivo de relatório sobre um possível erro
        que ocorra durante a execução do código. O nome do arquivo
        gerado é "relatorio-de-erro-AAAA-MM-DD-HH-MM-SS.txt".

        Self, str -> None
        '''
        # Cria o arquivo dentro da pasta "relatorioDeErros"
        arquivo = open(f'relatorioDeErros/relatorio-de-erro-{localtime()[0]}-{localtime()[1]:02d}-{localtime()[2]:02d}-{localtime()[3]:02d}-{localtime()[4]:02d}-{localtime()[5]:02d}.txt', 'w')

        # Escreve no arquivo a mensagem de erro
        arquivo.write(mensagemDeErro)

        # Fecha o arquivo
        arquivo.close()
