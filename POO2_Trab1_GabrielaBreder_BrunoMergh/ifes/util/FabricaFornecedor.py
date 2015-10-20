from ifes.cdp.fornecedor import Fornecedor


class FabricaFornecedor():

    @staticmethod
    def criar_fornecedor(nome, end, tel, cod, cnpj):
        return Fornecedor(nome, end, tel, cod, cnpj)

