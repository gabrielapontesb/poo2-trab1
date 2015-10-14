from ifes.util.PfisicaBuilder import PfisicaBuilder
from ifes.util.PjuridicaBuilder import PjuridicaBuilder



class Builder():


    def CriarPessoa(self,cod, nome, tel, end, tipo):
        if (tipo.upper() == "F"):
            cpf = input("CPF: ")
            return PfisicaBuilder.criarPessoa(self,cod, nome, tel, end, cpf)
        elif(tipo.upper() == "J"):
            cnpj = input("CNPJ: ")
            return PjuridicaBuilder.CriarPessoa(self,cod, nome, tel, end, cnpj)