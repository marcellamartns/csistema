# -*- coding: utf-8 -*-



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