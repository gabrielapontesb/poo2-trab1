from ifes.cdp.pessoa import Pessoa

class Pjuridica(Pessoa):

    def __init__(self, cod, nome, tel, end, cnpj):
        super(Pjuridica, self).__init__(cod, nome, tel, end)
        self.__cnpj = cnpj

    def get_cnpj(self):
        return self.__cnpj

    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj