from ifes.cdp.pfisica import Pfisica
from ifes.cdp.pjuridica import Pjuridica


class Fabrica():


    def CriarPessoa(self,cod, nome, tel, end, tipo):
        if (tipo.upper() == "F"):
            cpf = input("CPF: ")
            return Pfisica(cod, nome, tel, end, cpf)
        elif(tipo.upper() == "J"):
            cnpj = input("CNPJ: ")
            return Pjuridica(cod, nome, tel, end, cnpj)
