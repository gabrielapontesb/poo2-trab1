from ifes.cdp.venda import Venda


class FabricaVenda():


    def CriarVenda(self, cliente, dt, prod, qtd):
        return Venda(cliente, dt, prod, qtd)

