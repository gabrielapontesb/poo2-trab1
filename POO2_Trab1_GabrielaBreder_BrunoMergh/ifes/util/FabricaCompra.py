from ifes.cdp.compra import Compra


class FabricaCompra():


    def CriarCompra(self, qtd, notaf, codfornec, codprod, dtcompra):
        return Compra(qtd, notaf, codfornec, codprod, dtcompra)

