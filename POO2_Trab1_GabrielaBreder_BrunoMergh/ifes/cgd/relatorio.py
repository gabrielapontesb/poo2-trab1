import os

class Relatorio:

    @staticmethod
    def apagar(lstfornec, lstprod, lstcomp):

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "WriteApagar.txt")
        #valor devido aos fornecedores
        arquivo = open(path, 'w')
        arquivo.write("Fornecedor;quantia a pagar\n")
        total = 0
        for i in range(len(lstfornec)):
            for j in range(len(lstcomp)):
                if lstfornec[i].get_cod() == lstcomp[j].get_codfornec():
                    for k in range(len(lstprod)):
                        if lstcomp[j].get_codprod() == lstprod[k].get_cod():
                            valor = lstprod[k].get_custo() * lstcomp[j].get_qtd()
                            break

                    total += valor
                    valor = 0

            arquivo.write(str(lstfornec[i].get_cod()) + ";" + str(round(total,2)) + "\n")
            total = 0

    @staticmethod
    def areceber(lstpessoa, lstvendas, lstprod):
        #valor total de vendas

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "WriteAreceber.txt")
        arquivo = open(path, 'w')
        arquivo.write("Cliente;quantia a receber\n")

        total = 0
        for i in range(len(lstpessoa)):
            total = 0
            for j in range(len(lstvendas)):
                if lstpessoa[i].get_cod() == lstvendas[j].get_cliente():
                    for k in range(len(lstprod)):
                        if lstvendas[j].get_prod() == lstprod[k].get_cod():
                            valor = (((lstprod[k].get_pctlucro()/100) * lstprod[k].get_custo()) + lstprod[k].get_custo()) * lstvendas[j].get_qtd()
                            break
                    total += valor
                    valor = 0
            arquivo.write(str(lstpessoa[i].get_nome()) + ";" + str(round(total,2)) + "\n")

    @staticmethod
    def vendasprod(lstprod, lstvendas):

        #vendas e lucro por produto

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "WriteVendasPorProd.txt")
        arquivo = open(path, 'w')
        arquivo.write("Descricao do Produto;Total de venda bruta;Total de lucro\n")

        total= totalp = 0
        for i in range(len(lstprod)):
            for j in range(len(lstvendas)):
                if lstprod[i].get_cod() == lstvendas[j].get_prod():

                    valor = (((lstprod[i].get_pctlucro()/100) * lstprod[i].get_custo()) + lstprod[i].get_custo()) * lstvendas[j].get_qtd()
                    perc = ((lstprod[i].get_pctlucro()/100) * lstprod[i].get_custo()) * lstvendas[j].get_qtd()

                total += valor
                totalp += perc
                valor = 0
                perc = 0
            arquivo.write(str(lstprod[i].get_desc()) + ";" + str(round(total, 2)) + ";" + str(round(totalp, 2)) + "\n")
            total = totalp = 0

    @staticmethod
    def estoque(lstprod, lstvendas, lstcomp):

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "WriteEstoque.txt")
        arquivo = open(path, 'w')

        for i in range(len(lstprod)):
            for j in range(len(lstcomp)):
                if lstprod[i].get_cod() == lstcomp[j].get_codprod():
                    lstprod[i].set_qtdatual(lstprod[i].get_qtdatual() + lstcomp[j].get_qtd())

        for i in range(len(lstprod)):
            for j in range(len(lstvendas)):
                if lstprod[i].get_cod() == lstvendas[j].get_prod():
                    lstprod[i].set_qtdatual(lstprod[i].get_qtdatual() - lstvendas[j].get_qtd())

        arquivo.write("Codigo;Descricao;Quantidade Atual; \n")
        for i in range(len(lstprod)):
            if lstprod[i].get_qtdatual() < lstprod[i].get_estmin():
                arquivo.write(str(lstprod[i].get_cod()) + ";" + str(lstprod[i].get_desc())  + ";" + str(lstprod[i].get_qtdatual()) + ";COMPRAR MAIS")
                arquivo.write("\n")
            else:
                arquivo.write(str(lstprod[i].get_cod()) + ";" + str(lstprod[i].get_desc())  + ";" + str(lstprod[i].get_qtdatual()) +  ";")
                arquivo.write("\n")