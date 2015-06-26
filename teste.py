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
        # Le nome do arquivo
        nome = raw_input("Informe o nome da imagem \n")
        self.nome = nome
         # Le local do arquivo
        local = raw_input('informe o local do arquivo: \n')
        self.local = local

        # cria instancia para o arquivo em pgm (formato binario)
        arquivo = open(local + nome,"rb")

        # capta os parametros da imagem: tipo, dimensao e tons
        tipo = arquivo.readline()
        self.tipo = tipo
        dimensao = arquivo.readline()
        tons = arquivo.readline()
        self.tons = tons

        valores = dimensao.split(" ")
        m, n = int(valores[0]), int(valores[1])
        dimen = (m,n)
        self.dimensao = dimen
        #-----------------------------------------------------

        # Vetor em formato binario para trabalhar com a imagem
        img_vet = np.empty((256), dtype="b")
        
        # Armazenas a iamgem em binario no vetor do numpy
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

def podeLerComando(imagem, comando):
    if comando > 1 and comando < 7 and imagem == None:
        print "Primeiro, carregue a imagem"
        return False
    else:
        return True



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
        # Verifica se a imagem ja foi carregada
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
                
