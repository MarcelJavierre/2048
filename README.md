# 2048

<p align = "center" width = "100%">
    <img alt = "Logo do Jogo 2048" src = "imagens/logo.png" width = "300" height = "300">
    <img alt = "Partida de 2048 em Andamento" src = "imagens/partidaEmAndamento.png" width = "300" height = "300">
</p>

## Introdução

O objetivo deste projeto é o desenvolvimento do jogo 2048 em Python.

## Finalidade

A finalidade é deste projeto é ser utilizado como avaliação para a disciplina de Computação II da Universidade Federal do Rio de Janeiro.

## Sobre o Jogo

2048 é jogado em um tabuleiro de 4X4, com peças numéricas que deslizam suavemente quando o jogador as move em um dos quatro sentidos disponíveis: para cima, para baixo, à esquerda e à direita.

Cada vez, um novo número aparece aleatoriamente em um local vazio na placa (com um valor de 2 ou 4).

Os blocos deslizam o mais longe possível na direção escolhida até que eles sejam interrompidos por qualquer outro bloco ou a borda do tabuleiro. Se duas peças do mesmo número colidem durante a movimentação, elas irão se fundir em uma peça com o valor total das duas peças que colidiram.

O jogo é vencido quando uma peça com o valor de 2048 aparece no tabuleiro. Quando o jogador não tem movimentos legais (não há espaços vazios e nem peças adjacentes com o mesmo valor), o jogo termina.

## Sobre o Desenvolvimento do Jogo

O código do jogo foi feito 100% em python e utilizando programação orientada a objetos.

A primeira prova consistia na modelagem do código, na qual só era necessário a definição dos métodos e atributos das classes e suas documentações. O código dessa primeira parte se encontra [aqui](https://github.com/MarcelJavierre/2048/releases/tag/Prova_1).

A segunda prova consistia na criação de arquivos para persistência de dados, tratamento de exceções e criação de estatísticas com os módulos numpy e matplotlib. O código dessa segunda parte se encontra [aqui](https://github.com/MarcelJavierre/2048/releases/tag/Prova_2) e a versão com interface gráfica se encontra [aqui](https://github.com/MarcelJavierre/2048/releases/tag/Prova_2_tkinter).

A entrega final do projeto consistia na finalização do jogo, com todas as funções completas. O código da entrega final se encontra [aqui](https://github.com/MarcelJavierre/2048/releases/tag/Prova_3) e a versão com interface gráfica se encontra [aqui](https://github.com/MarcelJavierre/2048/releases/tag/Prova_3_tkinter).
