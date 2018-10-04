# -*- coding: utf-8 -*-


from datetime import datetime
from bson.objectid import ObjectId

class Contato(object):

    def __init__(self, id_=None, cadastro=None, nome=None, email=None, telefone=None):

        self._id = id_ if id_ else ObjectId(id_)
        self._cadastro = cadastro if cadastro else datetime.now()
        self._nome = nome
        self._email = email
        self._telefone = telefone

    @property
    def id_(self):
        return self._id

    @property
    def cadastro(self):
        return self._cadastro

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def telefone(self):
        return self._telefone

    @property
    def transforma_dicionario(self):

        return {
            "_id": self._id,
            "cadastro": self._cadastro,
            "nome": self._nome,
            "email": self._email,
            "telefone": self._telefone
        }