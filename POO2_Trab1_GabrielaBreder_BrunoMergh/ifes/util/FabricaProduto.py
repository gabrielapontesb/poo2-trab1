from ifes.cdp.produto import Produto


class FabricaProduto():


    def CriarProduto(self,cod, desc, estmin, qtdatual, custo, pctlucro):
        return Produto(cod, desc, estmin, qtdatual, custo, pctlucro)

