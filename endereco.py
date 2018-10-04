# -*- coding: utf-8 -*-


from datetime import datetime
from bson.objectid import ObjectId

class Endereco(object):

    def __init__(self, id_=None, cadastro=None, rua=None, numero=None, bairro=None):

        self._id = id_ if id_ else ObjectId(id_)
        self._cadastro = cadastro if cadastro else datetime.now()
        self._rua = rua
        self._numero = numero
        self._bairro = bairro

    @property
    def id_(self):
        return self._id

    @property
    def cadastro(self):
        return self._cadastro

    @property
    def rua(self):
        return self._rua

    @rua.setter
    def rua(self, value):
        self._rua = value

    @property
    def numero(self):
        return self._numero

    @property
    def bairro(self):
        return self._bairro

    @property
    def transforma_dicionario(self):

        return {
            "_id": self._id,
            "cadastro": self._cadastro,
            "rua": self._rua,
            "numero": self._numero,
            "bairro": self._bairro
        }