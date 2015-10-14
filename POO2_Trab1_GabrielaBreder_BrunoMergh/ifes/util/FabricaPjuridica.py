from ifes.cdp.pjuridica import *

class FabricaPjuridica():

    def CriarPessoa(self,cod, nome, tel, end, cnpj):
        pj = Pjuridica(cod, nome, tel, end, cnpj)
        return pj