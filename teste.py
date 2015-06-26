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
import shutil

class Imagem:

    def carregar(self):
        nome = raw_input("Informe o nome da imagem \n")
        self.nome = nome
        local = raw_input('informe o local do arquivo: \n')
        self.local = local
        arquivo = open(local + nome,"rb")

        tipo = arquivo.readline()
        self.tipo = tipo
        dimensao = arquivo.readline()
        tons = arquivo.readline()
        self.tons = tons

        valores = dimensao.split(" ")
        m, n = int(valores[0]), int(valores[1])

        dimen = (m,n)
        self.dimensao = dimen

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
        # print "antes"
        print self.vetor
        lista = []
        L = len(self.vetor)
        for i in range(L):
            valorAtual = self.vetor[i]
            novoValor = L - 1 - valorAtual
            lista.append(novoValor)
            self.vetor.put(i,novoValor)

        print self.vetor

    def realceContraste(self):
        print "realce de contraste aplicado."

    def equalizarHistograma(self):
        print "Histograma salvo."

    def salvar(self):
        # for i in range(256):
        #     byte = arquivo.read(1)
        #     unpacked = pack("b", byte)
        #     img_vet[i] = unpacked[0]
        self.arquivo = open(self.local + self.nome,"r+")
        self.arquivo.seek(1,2)
        self.arquivo.write("oi")
        print "Arquivo salvo"

    def salvarComo(self):
        nome = raw_input("Informe o nome da imagem \n")
        local = raw_input('informe o local do arquivo: \n')
        arquivoVelho = open(self.nome + self.local, "rb")
        arquivoNovo = open(local + nome,"w+")
        shutil.copyfileobj(arquivoVelho, arquivoNovo)
        arquivo = self.arquivo
        arquivo.close()
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
        print "Primeiro, carregue a imagem"
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
        if(podeLerComando(comando=comando, imagem=imagem)):
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
                
