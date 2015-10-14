from ifes.util import Fabrica

class PjuridicaBuilder():

    def criarPessoa(self,cod, nome, tel, end, cnpj):
        fpb = Fabrica.FabricaPfisica.CriarPessoa(self,cod, nome, tel, end, cnpj)
        return fpb
