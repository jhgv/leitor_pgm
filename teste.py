###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF968 -- Programacao 1
#
# Autor:    Caio Vieira
#               Diego de Holanda Goncalves
#               Lucas
#               Welligton Marinho de Oliveira Filho
# Email:    cv@cin.ufpe.br
#               dhg@cin.ufpe.br
#               lof@cin.ufpe.br
#               wmof@cin.ufpe.br
# Data:     2015-06-03
#
# Descricao:  Editor de fotos.
#
#
#
#
# Licenca: The MIT License (MIT)
#           Copyright(c) 2015 EDITOR CDLW
#
###############################################################################

# import matplotlib.pyplot as plt
from struct import unpack
import numpy as np

class Imagem:
    def __init__(self, nome=None, arquivo=None, vetor=None):
        
        self.nome = nome
        self.vetor = vetor

    def carregar(self):
        nome = raw_input("Informe o nome da imagem \n")
        local = raw_input('informe o local do arquivo: \n')
        arquivo = open(local + nome,"rb")

        tipo = arquivo.readline()
        dimensao = arquivo.readline()
        tons = int(arquivo.readline())

        valores = dimensao.split(" ")
        m, n = int(valores[0]), int(valores[1])

        dimen = (m,n)

        matriz = np.zeros(dimen)

        img_vet = np.empty((256), dtype="b")
        
        for i in range(len(img_vet)):
            byte = arquivo.read(1)
            unpacked = unpack("b", byte)
            img_vet[i] = unpacked[0]

        self.arquivo = arquivo

        self.vetor = img_vet

        print("Imagem Carregada...")


    def realceNegativo(self):
        vetorAux = self.vetor
        L = len(vetorAux)
        for i in range(L):
            novoValor = (L - 1) - i
            vetorAux[i] = novoValor

        self.vetor = vetorAux

    def realceContraste(self):
        print "realce de contraste aplicado."

    def equalizarHistograma(self):
        print "Histograma salvo."

    def salvar(self):
        self.arquivo.close()
        print "Arquivo salvo"

    def salvarComo(self):
        print "Arquivo salvo como"



def nome(): #Fun??o para pedir o nome do arquivo toda vez que for pedido.
    return raw_input('Digite o nome do arquivo: ')


# def carregar(): #Fun??o para carregar o arquivo.
#     #Pedindo ao usu?rio para informar o arquivo
#     # arq = nome()
#     #Pedindo ao usu?rio para informar o local

#     #Abrindo a imagem em Bin?rio
#     arquivo = open(lArq ,"rb")
#     # with open("exemplos_pgm/einstein.pgm",'rb') as f:
#     tipo = arquivo.readline()
#     dimensao = arquivo.readline()
#     tons = int(arquivo.readline())

#     valores = dimensao.split(" ")
#     m, n = int(valores[0]), int(valores[1])

#     dimen = (m,n)

#     matriz = np.zeros(dimen)

#     img_vet = np.empty((256), dtype="b")
    
#     for i in range(len(img_vet)):
#         byte = arquivo.read(1)
#         unpacked = unpack("b", byte)
#         img_vet[i] = unpacked[0]

#     print("Imagem Carregada...")
    return arquivo

def podeLerComando(imagem, comando):
    if comando > 1 and comando < 7 and imagem == None:
        return False
    else:
        return True

##Fun??o para salvar o arquivo.
# def salvar(arq):
#     #Usando close para fechar e, com isso, salvar o arquivo.
#     arq.close()
#     print ('Arquivo Salvo')

##Fun??o para salvar o arquivo em local definido pelo usu?rio.
# def salvarComo(arq):
#     print ('Para salvar como')
#     newArq = nome()
#     newLarq = local()

#     #Criando novo arquivo em bin?rio
#     newArq = open(newLarq,'wb')
#     arq.close()
#     newArq.close()




if __name__ == "__main__":

    imagem = None

    print "Digite umas das opcoes"
    print "1 - Carregar imagem"
    print "2 - Salvar imagem"
    print "3 - Salvar imagem como"
    print "4 - Aplicar realce negativo"
    print "5 - Aplicar realce de contraste"
    print "6 - Salvar histograma"
    print "7 - Sair"

    comando = input()

    while comando != 7:
        if(podeLerComando(comando, imagem)):
            if comando == 1:
                imagem = Imagem()
                imagem.carregar()
            elif comando == 2:
                imagem.salvar()
            elif comando == 3:
                imagem.salvarComo()
            elif comando == 4:
                imagem.realceNegativo()
            elif comando == 5:
                imagem.realceContraste()
            elif comando == 6:
                imagem.equalizarHistograma()

        comando = input("Digite uma nova opcao")
                
