import os.path

#função para adicionar um jogador novo
def criaNovoJogo():
    nome = input("Digite o nome do novo jogador: ")
    #verifica se o jogador ja existe ou não
    if os.path.isfile("{}.txt".format(nome)):
        print("\njogador ja registrado\n")
    else:
        print("\nRegistrando o jogador {}\n".format(nome))
        f = open("{}.txt".format(nome), "w")
        f.write("0\n")#pontuacao/vitorias
        f.write(("0"))#derrotas
        f.close()

#função para excluir jogador
def excluiJogador():
    nome = input("Digite o nome do jogador a ser excluido: ")
    #verficia se o jogador a ser excluido existe
    if os.path.isfile("{}.txt".format(nome)):
        print("\nExcluindo o jogador {}\n".format(nome))
        os.remove("{}.txt".format(nome))
    else:
        print("\nJogador {} não existe\n".format(nome))

#le a pontuação do jogador
def lePontuacao():
    nome = input("Digite o nome do jogador: ")
    #se o jogador existe, leia a pontuação
    if os.path.isfile("{}.txt".format(nome)):
        f = open("{}.txt".format(nome), "r")
        print("\nPontuacao de {}: \n".format(nome))
        historico = f.readlines()#le as linhas do arquivo txt
        vitorias = historico[0]
        derrotas = historico[1]
        print("Vitorias: {}\nDerrotas: {}\n".format(vitorias, derrotas))
    else:
        print("\nJogador {} não existe\n".format(nome))

#Verifica se algum jogador ganhou
def VerificaSeGanhou(matriz,simbolo):
        #verifica se ganha, se ganhar executa as funçoes
        #horizontal
        for i in range(5):
            if (matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2] and matriz[i][2] == matriz[i][3] and matriz[i][0] != " " or matriz[i][1] == matriz[i][2] and matriz[i][2] == matriz[i][3] and matriz[i][3] == matriz[i][4] and matriz[i][1] != " " ):
                IniciarJogo()
                Ganhou(simbolo)
                Final()
        #vertical
        for i in range(5):
            if (matriz[0][i]== matriz[1][i] and matriz[1][i] == matriz[2][i] and matriz[2][i] == matriz[3][i] and matriz[0][i] != " " or matriz[1][i]== matriz[2][i] and matriz[2][i] == matriz[3][i] and matriz[3][i] == matriz[4][i] and matriz[1][i] != " "):
                IniciarJogo()
                Ganhou(simbolo)
                Final()
        #diagonal
        if (matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] and matriz[2][2] == matriz[3][3] and matriz[0][0] != " " or matriz[1][1] == matriz[2][2] and matriz[2][2] == matriz[3][3] and matriz[3][3] == matriz[4][4] and matriz[1][1] != " "):
            IniciarJogo()
            Ganhou(simbolo)
            Final()
        #diagonal
        if (matriz[0][4] == matriz[1][3] and matriz[1][3] == matriz[2][2] and matriz[2][2] == matriz[3][1] and matriz[0][4] != " " or matriz[4][0] == matriz[3][1] and matriz[3][1] == matriz[2][2] and matriz[2][2] == matriz[1][3] and matriz[4][0] != " "):
            IniciarJogo()
            Ganhou(simbolo)
            Final()
        #diagonal
        if (matriz[0][3] == matriz[1][2] and matriz[1][2] == matriz[2][1] and matriz[2][1] == matriz[3][0] and matriz[0][3] != " " or matriz[1][4] == matriz[2][3] and matriz[2][3] == matriz[3][2] and matriz[3][2] == matriz[4][1] and matriz[1][4] != " "):
            IniciarJogo()
            Ganhou(simbolo)
            Final()
        #diagonal
        if (matriz[0][1] == matriz[1][2] and matriz[1][2] == matriz[2][3] and matriz[2][3] == matriz[3][4] and matriz[0][1] != " " or matriz[1][0] == matriz[2][1] and matriz[2][1] == matriz[3][2] and matriz[3][2] == matriz[4][3] and matriz[1][0] != " "):
            IniciarJogo()
            Ganhou(simbolo)
            Final()

#Pergunta os nomes dos jogadores no começo da partida
def PerguntaNome():
        #recebe e cria variaveis globais para os nomes digitados
        global nome1
        nome1 = input("Nome do primeiro jogador: ")
        #se o nome existir passa para o proximo e depois inicia o jogo
        if os.path.isfile("{}.txt".format(nome1)):
            global nome2
            nome2 = input("Nome do segundo jogador: ")
            if os.path.isfile("{}.txt".format(nome2)):
                reset()
                jogo()
        else:
            print("Jogador não encontrado.")

#função do final da partida
def Final():

        #identifica qual jogador ganhou por 0 ou 1
        if Ganhou(simbolo)==1:
            #le o arquivo de texto, pega os valores de dentro e soma +1 para vitoria
            #mostra quem foi o vencedor
            print("\nQuem venceu foi: {}\n".format(nome1))
            f = open("{}.txt".format(nome1), "r")
            historico = f.readlines()
            derrot = historico[1]
            vitoria = int(historico[0])
            vitoria+= 1
            vi = str(vitoria)
            f.close()

            #escreve o mesmo valor de derrota e vitoria +1
            f = open("{}.txt".format(nome1), "w")
            f.write("{}\n".format(vi))
            f.write(derrot)
            f.close()

            #faz o mesmo para o usario que perdeu colocando +1 na derrota
            b = open("{}.txt".format(nome2), "r")
            historic = b.readlines()
            vitori = historico[0]
            derrota = int(historic[1])
            derrota+= 1
            b = open("{}.txt".format(nome2), "w")
            b.write(vitori)
            b.write(str(derrota))
            b.close()
            main()

        #identifica qual jogador ganhou por 0 ou 1
        elif Ganhou(simbolo)==0:
            #le o arquivo de texto, pega os valores de dentro e soma +1 para vitoria
            #mostra quem venceu
            print("\nQuem venceu foi: {}\n".format(nome2))
            f = open("{}.txt".format(nome2), "r")
            historico = f.readlines()
            derrot = historico[1]
            vitoria = int(historico[0])
            vitoria+= 1
            vi = str(vitoria)
            f.close()

            #escreve o mesmo valor de derrota e vitoria +1
            f = open("{}.txt".format(nome2), "w")
            f.write("{}\n".format(vi))
            f.write(derrot)
            f.close()

            #faz o mesmo para o usario que perdeu colocando +1 na derrota
            b = open("{}.txt".format(nome1), "r")
            historic = b.readlines()
            vitori = historico[0]
            derrota = int(historic[1])
            derrota+= 1
            b = open("{}.txt".format(nome1), "w")
            b.write(vitori)
            b.write(str(derrota))
            b.close()
            main()

#funcao que indica qual jogador ganhou (0 ou 1)
def Ganhou(simbolo):
    return simbolo


#reseta a matriz
def reset():
    global matriz
    matriz = [[' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ']]


#função para mostrar o tabuleiro
def IniciarJogo():

    tabuleiro = """
    {} | {} | {} | {} | {}
    --+---+---+---+---
    {} | {} | {} | {} | {}
    --+---+---+---+---
    {} | {} | {} | {} | {}
    --+---+---+---+---
    {} | {} | {} | {} | {}
    --+---+---+---+---
    {} | {} | {} | {} | {}
""".format(matriz[0][0],matriz[0][1],matriz[0][2],matriz[0][3],matriz[0][4],matriz[1][0],matriz[1][1],matriz[1][2],matriz[1][3],matriz[1][4],matriz[2][0],matriz[2][1],matriz[2][2],matriz[2][3],matriz[2][4],matriz[3][0],matriz[3][1],matriz[3][2],matriz[3][3],matriz[3][4],matriz[4][0],matriz[4][1],matriz[4][2],matriz[4][3],matriz[4][4],)
    print(tabuleiro) #printa o tabuleiro criado

#funcao do jogo para identificar qual linha e coluna o usuario escolhe
def jogo():
    jogadas = 0  # numero de jogadas
    global simbolo
    simbolo = 0  #var para verificar qual jogador joga
    while jogadas<25:  #enquanto as jogadas forem menor que 25 pergunte ao jogador onde ele quer jogar
        IniciarJogo()
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))

        #se na matriz for ' ' (sem nada) coloque o simbolo indicado
        #se estiver entre 0 e 4, prossiga
        if 0 <= int(linha) < 5 and 0 <= int(coluna) < 5:
            if matriz[linha][coluna] == ' ':
                #se simbolo for 0 coloque X
                if simbolo == 0:
                    matriz[linha][coluna] = "X"
                    jogadas += 1      #aumenta em 1 o numero de jogadas (max 25 total dos dois)
                    simbolo += 1      #aumenta em 1 o simbolo para passar pro proximo jogador
                    VerificaSeGanhou(matriz,simbolo)     #executa a função para verificar se ganha

                # se simbolo for 1 coloque O
                elif simbolo == 1:
                    if linha<5 and coluna<5:
                        matriz[linha][coluna] = "O"
                        jogadas += 1      #aumenta em 1 o numero de jogadas (max 25 total dos dois)
                        simbolo -= 1      #diminui em 1 o simbolo para passar pro proximo jogador (volta a ser 0 para o X jogar)
                        VerificaSeGanhou(matriz,simbolo,)    #executa a função para verificar se ganha

            #se não for " " (vazio) fale que ja esta ocupado
            else:
                print("O espaço ja esta ocupado!")
        else:
            print("\nNumero invalido!")
    #se passar 25 rodadas mostra empate
    print("Empate!!!")


#criar o menu
def main():
    while True:
        print("-----Menu-----")
        print("1 - Criar jogador")
        print("2 - Mostrar pontuação")
        print("3 - Excluir jogador")
        print("4 - Iniciar partida")

        #variavel para guardar escolha
        opcao = input("Escolha a opção desejada: ")

        #se for tal numero execute sua função
        if opcao == "1":
            criaNovoJogo()
        elif opcao == "2":
            lePontuacao()
        elif opcao == "3":
            excluiJogador()
        elif opcao == "4":
            PerguntaNome()
        else:
            print("Valor invalido.")



#inicia o programa
main()