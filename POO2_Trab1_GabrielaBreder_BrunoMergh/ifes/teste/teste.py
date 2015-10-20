import unittest
import os

from ifes.cdp.pessoa import Pessoa
from ifes.cdp.produto import Produto
from ifes.cdp.fornecedor import Fornecedor
from ifes.cdp.compra import Compra
from ifes.cdp.venda import Venda
from ifes.util.FabricaCompra import FabricaCompra
from ifes.util.FabricaProduto import FabricaProduto
from ifes.util.FabricaFornecedor import FabricaFornecedor
from ifes.util.FabricaVenda import FabricaVenda


class TestGeral(unittest.TestCase):

    def set_up(self):
        self.pessoa = Pessoa(0, "Bruno", 27997743714, "Rua qualquer")
        self.produto = Produto(0,"miojo",3,5,3.2,40)
        self.fornecedor = Fornecedor("Casas Bahia","Rua 1", 999, 0, 122)
        self.compra = Compra(1,111,0,0,"12/01/2015")
        self.venda = Venda(0,"13/01/2015",0,1)
        self.fabricac = FabricaCompra.criar_compra(1,111,0,0,"12/01/2015")
        self.fabricavenda = FabricaVenda.criar_venda(0,"13/01/2015",0,1)
        self.fabricap = FabricaProduto.criar_produto(0,"miojo",3,5,3.2,40)




    def test_atributos_pessoa(self):
        self.assertEqual(self.pessoa.get_cod(), 0)
        self.assertEqual(self.pessoa.get_nome(), "Bruno")
        self.assertEqual(self.pessoa.get_tel(), 27997743714)
        self.assertEqual(self.pessoa.get_end(), "Rua qualquer")

    def test_atributos_produto(self):
        self.assertEqual(self.produto.get_cod(), 0)
        self.assertEqual(self.produto.get_desc(), "miojo")
        self.assertEqual(self.produto.get_estmin(), 3)
        self.assertEqual(self.produto.get_qtdatual(), 5)
        self.assertEqual(self.produto.get_custo(), 3.2)
        self.assertEqual(self.produto.get_pctlucro(), 40)

    def test_atributos_fornecedor(self):
         self.assertEqual(self.fornecedor.get_nome(), "Casas Bahia")
         self.assertEqual(self.fornecedor.get_end(), "Rua 1")
         self.assertEqual(self.fornecedor.get_tel(), 999)
         self.assertEqual(self.fornecedor.get_cod(), 0)
         self.assertEqual(self.fornecedor.get_cnpj(), 122)

    def test_atributos_compra(self):
        self.assertEqual(self.compra.get_qtd(), 1)
        self.assertEqual(self.compra.get_notaf(), 111)
        self.assertEqual(self.compra.get_codfornec(), 0)
        self.assertEqual(self.compra.get_codprod(), 0)
        self.assertEqual(self.compra.get_dtcompra(), "12/01/2015")

    def test_atributos_venda(self):
        self.assertEqual(self.venda.get_cliente(), 0)
        self.assertEqual(self.venda.get_dt(), "13/01/2015")
        self.assertEqual(self.venda.get_prod(), 0)
        self.assertEqual(self.venda.get_qtd(), 1)

    def test_apagar(self):

        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/WriteApagar.txt")
        arqc = open(FILENAME, 'r')
        conteudo = arqc.read()
        self.assertEqual(conteudo, "Fornecedor;quantia a pagar\n0;3.81\n1;2.4\n2;1.68\n")

    def test_areceber(self):
        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/WriteAreceber.txt")
        arqc = open(FILENAME, 'r')
        conteudo = arqc.read()
        self.assertEqual(conteudo, "Cliente;quantia a receber\nBruno;4.79\nAna;4.51\nGabi;4.16\nJoao;2.77\nPedro;5.87\nGuilherme;9.22\n")

    def test_vendasprod(self):
        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/WriteVendasPorProduto.txt")
        arqc = open(FILENAME, 'r')
        conteudo = arqc.read()
        self.assertEqual(conteudo, "Descricao do Produto;Total de venda bruta;Total de lucro\nleite;9.9;3.3\npao doce;2.73;0.78\npao de sal;2.77;0.93\npo de cafe;12.6;4.2\nmiojo;3.31;1.47\n")

    def test_estoque(self):
        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/WriteEstoque.txt")
        arqc = open(FILENAME, 'r')
        conteudo = arqc.read()
        self.assertEqual(conteudo, "Codigo;Descricao;Quantidade Atual; \n0;leite;4;\n1;pao doce;5;\n2;pao de sal;6;\n3;po de cafe;3;\n4;miojo;5;\n")

    def test_fabrica_compra(self):
        self.assertEqual(self.fabricac.get_qtd(), 1)
        self.assertEqual(self.fabricac.get_notaf(), 111)
        self.assertEqual(self.fabricac.get_codfornec(), 0)
        self.assertEqual(self.fabricac.get_codprod(), 0)
        self.assertEqual(self.fabricac.get_dtcompra(), "12/01/2015")

    def test_fabrica_venda(self):
        self.assertEqual(self.fabricavenda.get_cliente(), 0)
        self.assertEqual(self.fabricavenda.get_dt(), "13/01/2015")
        self.assertEqual(self.fabricavenda.get_prod(), 0)
        self.assertEqual(self.fabricavenda.get_qtd(), 1)

    def test_fabrica_fornecedor(self):
        self.ff = FabricaFornecedor.criar_fornecedor("JorgeSA", "Rua 1", 1111,1,"121212")
        self.assertEqual(self.ff.get_nome(), "JorgeSA")
        self.assertEqual(self.ff.get_end(), "Rua 1")
        self.assertEqual(self.ff.get_tel(), 1111)
        self.assertEqual(self.ff.get_cod(), 1)
        self.assertEqual(self.ff.get_cnpj(), "121212")

    def test_fabrica_produto(self):
        self.assertEqual(self.fabricap.get_cod(), 0)
        self.assertEqual(self.fabricap.get_desc(), "miojo")
        self.assertEqual(self.fabricap.get_estmin(), 3)
        self.assertEqual(self.fabricap.get_qtdatual(), 5)
        self.assertEqual(self.fabricap.get_custo(), 3.2)
        self.assertEqual(self.fabricap.get_pctlucro(), 40)


if __name__ == "__main__":
    unittest.main()
