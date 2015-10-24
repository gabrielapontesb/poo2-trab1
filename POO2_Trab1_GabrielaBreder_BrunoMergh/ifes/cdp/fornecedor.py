class Fornecedor:

    def __init__(self, nome, end, tel, cod, cnpj):
        self.__nome = nome
        self.__end = end
        self.__tel = tel
        self.__cod = cod
        self.__cnpj = cnpj


    def get_nome(self):
            return self.__nome

    def set_nome(self, nome):
            self.__nome = nome

    def get_end(self):
            return self.__end

    def set_end(self, end):
            self.__end = end

    def get_tel(self):
            return self.__tel

    def set_tel(self, tel):
            self.__tel = tel

    def get_cod(self):
            return self.__cod

    def set_cod(self, cod):
            self.__cod = cod

    def get_cnpj(self):
            return self.__cnpj

    def set_cnpj(self, cnpj):
            self.__cnpj = cnpj
