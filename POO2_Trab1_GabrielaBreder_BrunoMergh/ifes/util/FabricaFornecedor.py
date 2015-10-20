from ifes.cdp.fornecedor import Fornecedor


class FabricaFornecedor():


    def CriarFornecedor(self, nome, end, tel, cod, cnpj):
        return Fornecedor(nome, end, tel, cod, cnpj)

