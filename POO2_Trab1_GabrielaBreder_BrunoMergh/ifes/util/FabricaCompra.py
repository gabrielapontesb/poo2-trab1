from ifes.cdp.compra import Compra

class FabricaCompra():

    @staticmethod
    def criar_compra(qtd, notaf, codfornec, codprod, dtcompra):
        return Compra(qtd, notaf, codfornec, codprod, dtcompra)

