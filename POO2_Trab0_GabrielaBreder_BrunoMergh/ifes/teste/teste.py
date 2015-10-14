import unittest
import os

from ifes.cdp.pessoa import Pessoa
from ifes.cdp.produto import Produto
from ifes.cdp.fornecedor import Fornecedor
from ifes.cdp.compra import Compra
from ifes.cdp.venda import  Venda
from ifes.util.Fabrica import Fabrica


class TestGeral(unittest.TestCase):
    def setUp(self):
        self.pessoa = Pessoa(0, "Bruno", 27997743714, "Rua qualquer")
        self.produto = Produto(0,"miojo",3,5,3.2,40)
        self.fornecedor = Fornecedor("Casas Bahia","Rua 1", 999, 0, 122)
        self.compra = Compra(1,111,0,0,"12/01/2015")
        self.venda = Venda(0,"13/01/2015",0,1)




    def testAtributosPessoa(self):
        self.assertEqual(self.pessoa.getCod(), 0)
        self.assertEqual(self.pessoa.getNome(), "Bruno")
        self.assertEqual(self.pessoa.getTel(), 27997743714)
        self.assertEqual(self.pessoa.getEnd(), "Rua qualquer")

    def testAtributosProduto(self):
        self.assertEqual(self.produto.getCod(), 0)
        self.assertEqual(self.produto.getDesc(), "miojo")
        self.assertEqual(self.produto.getEstmin(), 3)
        self.assertEqual(self.produto.getQtdatual(), 5)
        self.assertEqual(self.produto.getCusto(), 3.2)
        self.assertEqual(self.produto.getPctlucro(), 40)

    def testAtributosFornecedor(self):
         self.assertEqual(self.fornecedor.getNome(), "Casas Bahia")
         self.assertEqual(self.fornecedor.getEnd(), "Rua 1")
         self.assertEqual(self.fornecedor.getTel(), 999)
         self.assertEqual(self.fornecedor.getCod(), 0)
         self.assertEqual(self.fornecedor.getCnpj(), 122)

    def testAtributosCompra(self):
        self.assertEqual(self.compra.getQtd(), 1)
        self.assertEqual(self.compra.getNotaf(), 111)
        self.assertEqual(self.compra.getCodfornec(), 0)
        self.assertEqual(self.compra.getCodprod(), 0)
        self.assertEqual(self.compra.getDtcompra(), "12/01/2015")

    def testAtributosVenda(self):
        self.assertEqual(self.venda.getCliente(), 0)
        self.assertEqual(self.venda.getDt(), "13/01/2015")
        self.assertEqual(self.venda.getProd(), 0)
        self.assertEqual(self.venda.getQtd(), 1)

    def testApagar(self):
        FILENAME = os.path.expanduser("~/Documents/GitHub/poo2-trab0/POO2_Trab0_GabrielaBreder_BrunoMergh/ifes/arquivos/WriteApagar.txt")
        arqC = open(FILENAME, 'r')
        conteudo = arqC.read()
        self.assertEqual(conteudo, "Fornecedor;quantia a pagar\n0;3.81\n1;2.4\n2;1.68\n")

    def testAreceber(self):
        FILENAME = os.path.expanduser("~/Documents/GitHub/poo2-trab0/POO2_Trab0_GabrielaBreder_BrunoMergh/ifes/arquivos/WriteAreceber.txt")
        arqC = open(FILENAME, 'r')
        conteudo = arqC.read()
        self.assertEqual(conteudo, "Cliente;quantia a receber\nBruno;4.79\nAna;4.51\nGabi;4.16\nJoao;2.77\nPedro;5.87\nGuilherme;9.22\n")

    def testVendasprod(self):
        FILENAME = os.path.expanduser("~/Documents/GitHub/poo2-trab0/POO2_Trab0_GabrielaBreder_BrunoMergh/ifes/arquivos/WriteVendasPorProduto.txt")
        arqC = open(FILENAME, 'r')
        conteudo = arqC.read()
        self.assertEqual(conteudo, "Descricao do Produto;Total de venda bruta;Total de lucro\nleite;9.9;3.3\npao doce;2.73;0.78\npao de sal;2.77;0.93\npo de cafe;12.6;4.2\nmiojo;3.31;1.47\n")

    def testEstoque(self):
        FILENAME = os.path.expanduser("~/Documents/GitHub/poo2-trab0/POO2_Trab0_GabrielaBreder_BrunoMergh/ifes/arquivos/WriteEstoque.txt")
        arqC = open(FILENAME, 'r')
        conteudo = arqC.read()
        self.assertEqual(conteudo, "Codigo;Descricao;Quantidade Atual; \n0;leite;4;\n1;pao doce;5;\n2;pao de sal;6;\n3;po de cafe;3;\n4;miojo;5;\n")

    def testFabrica(self):

        self.assertEqual(Fabrica.CriarPessoa(self,11, "bernardo", 12121, "rua dois", "J"), 1 )

if __name__ == "__main__":
    unittest.main()
