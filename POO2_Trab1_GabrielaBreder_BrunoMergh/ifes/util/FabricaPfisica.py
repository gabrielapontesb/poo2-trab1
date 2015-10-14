from ifes.cdp.pfisica import *

class FabricaPfisica():

    def CriarPessoa(self,cod, nome, tel, end, cpf):
        pf = Pfisica(cod, nome, tel, end, cpf)
        return pf

