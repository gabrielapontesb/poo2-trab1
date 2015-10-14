from ifes.util.FabricaPfisica import FabricaPfisica
from ifes.util.FabricaPjuridica import FabricaPjuridica


class Fabrica():


    def CriarPessoa(self,cod, nome, tel, end, tipo):
        if (tipo.upper() == "F"):
            cpf = input("CPF: ")
            return FabricaPfisica.CriarPessoa(self,cod, nome, tel, end, cpf)
        elif(tipo.upper() == "J"):
            cnpj = input("CNPJ: ")
            return FabricaPjuridica.CriarPessoa(self,cod, nome, tel, end, cnpj)
