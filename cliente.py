# -*- coding: utf-8 -*-

from datetime import datetime
from bson.objectid import ObjectId

class Cliente(object):

    def __init__(self, id_=None, cadastro=None, nome_razao=None, cpf_cnpj=None, tipo=None,
                contatos=None, enderecos=None):

        self._id = id_ if id_ else ObjectId(id_)
        self._cadastro = cadastro if cadastro else datetime.now()
        self._nome_razao = nome_razao
        self._cpf_cnpj = cpf_cnpj
        self._tipo = tipo
        self._contatos = contatos if contatos else []
        self._enderecos = enderecos if enderecos else []

    @property
    def id_(self):
        return self._id

    @property
    def cadastro(self):
        return self._cadastro

    @property
    def nome_razao(self):
        return self._nome_razao

    @property
    def cpf_cnpj(self):
        return self._cpf_cnpj

    @property
    def tipo(self):
        return self._tipo

    @property
    def contatos(self):
        return self._contatos

    @property
    def enderecos(self):
        return self._enderecos

    @property
    def retorna_dicionario(self):

        return {
            "_id": self._id,
            "cadastro": self._cadastro,
            "nome_razao": self._nome_razao,
            "cpf_cnpj": self._cpf_cnpj,
            "tipo": self._tipo,
            "contatos": self._contatos,
            "enderecos": self._enderecos
        }