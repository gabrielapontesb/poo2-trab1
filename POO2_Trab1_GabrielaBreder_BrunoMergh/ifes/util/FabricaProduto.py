from ifes.cdp.produto import Produto


class FabricaProduto():

    @staticmethod
    def criar_produto(cod, desc, estmin, qtdatual, custo, pctlucro):
        return Produto(cod, desc, estmin, qtdatual, custo, pctlucro)

