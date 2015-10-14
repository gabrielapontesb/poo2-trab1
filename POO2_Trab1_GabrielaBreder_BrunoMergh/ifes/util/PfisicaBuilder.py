from ifes.util import Fabrica

class PfisicaBuilder():

    def criarPessoa(self,cod, nome, tel, end, cpf):
        fpb = Fabrica.FabricaPfisica.CriarPessoa(self,cod, nome, tel, end, cpf)
        return fpb