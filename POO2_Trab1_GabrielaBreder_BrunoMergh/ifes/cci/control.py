from ifes.cgd.cadastro import Cadastro
from ifes.cgd.relatorio import Relatorio

class Control:

    def __init__(self):
        self.__lstcliente = []
        self.__lstproduto = []
        self.__lstfornecedor = []
        self.__lstcompra =[]
        self.__lstvenda = []

    def controle(self, opcao, opcao2):

        cad = Cadastro()
        relatorio = Relatorio()


        if opcao == 1:
            if opcao2 == 1:
                p = cad.cadastra_pessoa()
                achou = False
                for cliente in range(len(self.__lstcliente)):
                    if p.get_cod() == self.__lstcliente[cliente].get_cod():
                        print("Cliente ja cadastrado\n")
                        achou = True
                        break
                if achou == False:
                    self.__lstcliente.append(p)
                    print("Cliente cadastrado com sucesso\n")

            elif opcao2 == 2:
                p = cad.cadastra_fornecedor()
                achou = False
                for fornecedor in range(len(self.__lstfornecedor)):
                    if p.get_cod() == self.__lstfornecedor[fornecedor].get_cod():
                        print("Fornecedor ja cadastrado\n")
                        achou = True
                        break

                if achou == False:
                    self.__lstfornecedor.append(p)
                    print("Fornecedor cadastrado com sucesso\n")

            elif opcao2 == 3:
                p = cad.cadastra_produto()
                achou = False
                for produto in range(len(self.__lstproduto)):
                    if p.get_cod() == self.__lstproduto[produto].get_cod() and p.get_desc() == self.__lstproduto[produto].get_desc():
                        self.__lstproduto[produto].set_qtdatual(self.__lstproduto[produto].get_qtdatual() + p.get_qtdatual())
                        print("Produto ja cadastrado. Qtd atual incrementada\n")
                        achou = True
                        break

                    elif p.get_cod() == self.__lstproduto[produto].get_cod() and p.get_desc() != self.__lstproduto[produto].get_desc():
                        print("O produto " + self.__lstproduto[produto].get_desc() + " ja utiliza esse codigo")
                        achou = True
                        break

                if achou == False:
                    self.__lstproduto.append(p)
                    print("Produto cadastrado com sucesso\n")

            elif opcao2 == 4:
                p = cad.cadastra_venda()
                self.__lstvenda.append(p)

            elif opcao2 == 5:
                p = cad.cadastra_compra()
                self.__lstcompra.append(p)

        elif opcao == 2:
            if opcao2 == 1:
                relatorio.apagar(self.__lstfornecedor, self.__lstproduto, self.__lstcompra)
            elif opcao2 == 2:
                relatorio.areceber(self.__lstcliente, self.__lstvenda, self.__lstproduto)
            elif opcao2 == 3:
                relatorio.vendasprod(self.__lstproduto, self.__lstvenda)
            elif opcao2 == 4:
                relatorio.estoque(self.__lstproduto, self.__lstvenda, self.__lstcompra)
            elif opcao2 == 5:
                relatorio.estoque(self.__lstproduto, self.__lstvenda, self.__lstcompra)
                relatorio.apagar(self.__lstfornecedor, self.__lstproduto, self.__lstcompra)
                relatorio.areceber(self.__lstcliente, self.__lstvenda, self.__lstproduto)
                relatorio.vendasprod(self.__lstproduto, self.__lstvenda)
        elif opcao == 3:
            self.__lstcliente = cad.popular_banco_cliente()
            self.__lstfornecedor = cad.popular_banco_fornecedor()
            self.__lstproduto = cad.popular_banco_produto()
            self.__lstcompra = cad.popular_banco_compra()
            self.__lstvenda = cad.popular_banco_venda()

__author__ = 'Bruno'
