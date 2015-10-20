class Compra:

	def __init__(self, qtd, notaf, codfornec, codprod, dtcompra):
		self.__qtd = qtd
		self.__notaf = notaf
		self.__codfornec = codfornec
		self.__codprod = codprod
		self.__dtcompra = dtcompra

	def get_qtd(self):
		return self.__qtd

	def set_qtd(self, qtd):
		self.__qtd = qtd

	def get_notaf(self):
		return self.__notaf

	def set_notaf(self, notaf):
		self.__notaf = notaf

	def get_codfornec(self):
		return self.__codfornec

	def set_codfornec(self, codfornec):
		self.__codfornec = codfornec

	def get_codprod(self):
		return self.__codprod

	def set_codprod(self, codprod):
		self.__codprod = codprod

	def get_dtcompra(self):
		return self.__dtcompra

	def set_dtcompra(self, dtcompra):
		self.__dtcompra = dtcompra