from ifes.cdp.pfisica import Pfisica
from ifes.cdp.pjuridica import Pjuridica
import os
from ifes.util.FabricaPessoa import FabricaPessoa
from ifes.util.FabricaProduto import FabricaProduto
from ifes.util.FabricaFornecedor import FabricaFornecedor
from ifes.util.FabricaVenda import FabricaVenda
from ifes.util.FabricaCompra import FabricaCompra

class Cadastro:

    @staticmethod
    def popular_banco_cliente():

        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/cliente.txt")
        lstcliente = []
        arqc = open(FILENAME, 'r')
        conteudo = arqc.readline()
        while conteudo != "":
            lstconteudo = conteudo.split(";")
            cod = int(lstconteudo[0])
            nome = lstconteudo[1]
            tel = int(lstconteudo[2])
            end = lstconteudo[3]
            tipo = lstconteudo[4]
            if tipo.upper() == "F":
                cpf = lstconteudo[5]
                p = Pfisica(cod, nome, tel, end, cpf)
                lstcliente.append(p)
            elif tipo.upper() == "J":
                cnpj = lstconteudo[5]
                p = Pjuridica(cod, nome, tel, end, cnpj)
                lstcliente.append(p)
            conteudo = arqc.readline()
        return lstcliente

    @staticmethod
    def popular_banco_produto():

        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/produto.txt")
        lstproduto = []
        arqp = open(FILENAME, 'r')
        conteudo = arqp.readline()
        while conteudo != "":
            lstconteudo = conteudo.split(';')
            cod = int(lstconteudo[0])
            desc = lstconteudo[1]
            estmin = int(lstconteudo[2])
            qtdatual = int(lstconteudo[3])
            custo = float(lstconteudo[4])
            pctlucro = float(lstconteudo[5])
            p = FabricaProduto.criar_produto(cod, desc, estmin, qtdatual, custo, pctlucro)
            lstproduto.append(p)
            conteudo = arqp.readline()
        return lstproduto

    @staticmethod
    def popular_banco_fornecedor():

        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/fornecedor.txt")
        lstfornecedor = []
        arqf = open(FILENAME, 'r')
        conteudo = arqf.readline()
        while conteudo != "":
            lstconteudo = conteudo.split(';')
            nome = lstconteudo[0]
            end = lstconteudo[1]
            tel = int(lstconteudo[2])
            cod = int(lstconteudo[3])
            cnpj = lstconteudo[4]
            f = FabricaFornecedor.criar_fornecedor(nome, end, tel, cod, cnpj)
            lstfornecedor.append(f)
            conteudo = arqf.readline()
        return lstfornecedor

    @staticmethod
    def popular_banco_venda():

        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/venda.txt")
        lstvenda = []
        arqv = open(FILENAME, 'r')
        conteudo = arqv.readline()
        while conteudo != "":
            lstconteudo = conteudo.split(';')
            cliente = int(lstconteudo[0])
            data = lstconteudo[1]
            produto = int(lstconteudo[2])
            qtd = int(lstconteudo[3])
            v = FabricaVenda.criar_venda(cliente, data, produto, qtd)
            lstvenda.append(v)
            conteudo = arqv.readline()
        return lstvenda

    @staticmethod
    def popular_banco_compra():

        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/compra.txt")
        lstcompra = []
        arqc = open(FILENAME, 'r')
        conteudo = arqc.readline()
        while conteudo != "":
            lstconteudo = conteudo.split(';')
            qtd = int(lstconteudo[0])
            notafiscal = lstconteudo[1]
            codfornec = int(lstconteudo[2])
            codprod = int(lstconteudo[3])
            dtcompra = lstconteudo[4]
            c = FabricaCompra.criar_compra(qtd, notafiscal, codfornec, codprod, dtcompra)
            lstcompra.append(c)
            conteudo = arqc.readline()
        return lstcompra

    @staticmethod
    def cadastra_pessoa():

        cod = int(input("Codigo: "))
        nome = input("Nome: ")
        tel = int(input("Telefone: "))
        end = input("Endereco: ")
        tipo = input("F para fisica e J para juridica: ")
        fabrica = FabricaPessoa.criar_pessoa(cod, nome, tel, end, tipo)
        return fabrica

    @staticmethod
    def cadastra_produto():

        cod = int(input("Codigo: "))
        desc = input("Descricao: ")
        estmin = int(input("Estoque minimo: "))
        qtdatual = int(input("Qtd atual: "))
        custo = float(input("Custo: "))
        pctlucro = int(input("Pct lucro: "))
        p = FabricaProduto.criar_produto(cod, desc, estmin, qtdatual, custo, pctlucro)
        return p

    @staticmethod
    def cadastra_fornecedor():
        nome = input("Nome do fornecedor: ")
        end = input("Endereco: ")
        tel = int(input("Telefone: "))
        cod = int(input("Codigo: "))
        cnpj = int(input("Cnpj: "))
        f = FabricaFornecedor.criar_fornecedor(nome, end, tel, cod, cnpj)
        return f

    @staticmethod
    def cadastra_venda():
        cliente = int(input("Codigo do cliente: "))
        dt = input("Data: ")
        prod = int(input("Codigo do produto: "))
        qtd = int(input("Quantidade: "))
        v = FabricaVenda.criar_venda(cliente, dt, prod, qtd)
        return v

    @staticmethod
    def cadastra_compra():
        qtd = int(input("Quantidade: "))
        notaf = int(input("Nota fiscal: "))
        codfornec = int(input("Codigo do fornecedor: "))
        codprod = int(input("Codigo do produto: "))
        dtcompra = input("Data: ")
        c = FabricaCompra.criar_compra(qtd, notaf, codfornec, codprod, dtcompra)
        return c
