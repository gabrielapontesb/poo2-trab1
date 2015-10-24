from ifes.cdp.venda import Venda


class FabricaVenda():

    @staticmethod
    def criar_venda(cliente, dt, prod, qtd):
        return Venda(cliente, dt, prod, qtd)

