# -*- coding: utf-8 -*-

from bson.objectid import ObjectId
from contato import Contato
from cliente import Cliente
from endereco import Endereco

NOME_COLECAO = "clientes"

class Conexao(object):

    def __init__(self, banco):

        self._colecao = banco[NOME_COLECAO]

    def inserir(self, cliente):

        self._colecao.insert_one(cliente.retorna_dicionario)

    def atualizar(self, codigo_cliente, cliente):

        qry = {"_id": ObjectId(codigo_cliente)}
        fld = {"$set":
                    {"nome_razao": cliente.nome_razao,
                    "cpf_cnpj": cliente.cpf_cnpj,
                    "tipo": cliente.tipo
        }}

        self._colecao.update_one(qry, fld)

    def buscar(self, codigo_cliente):

        qry = {"_id": ObjectId(codigo_cliente)}

        cliente = self._colecao.find_one(qry)
        lista_contato = []

        for cli in cliente["contatos"]:
            contat = Contato(cli["_id"], cli["cadastro"], cli["nome"], cli["email"], cli["telefone"])
            lista_contato.append(contat)

        client = Cliente(cliente["_id"], cliente["cadastro"], cliente["nome_razao"], cliente["cpf_cnpj"], cliente["tipo"], lista_contato)

        return client

    def listar(self):

        clientes = self._colecao.find()
        lista_cont, lista_end, lista_final = [], [], []

        for c in clientes:
            for cont in c["contatos"]:

                contat = Contato(cont["_id"], cont["cadastro"], cont["nome"], cont["email"], cont["telefone"])
                lista_cont.append(contat)

            for end in c["enderecos"]:

                ende = Endereco(end["_id"], end["cadastro"], end["rua"], end["numero"], end["bairro"])
                lista_end.append(ende)

        client = Cliente(c["_id"], c["cadastro"], c["nome_razao"], c["cpf_cnpj"], c["tipo"], lista_cont, lista_end)
        lista_final.append(client)
        return lista_final

    def excluir(self, codigo_cliente):

        self._colecao.delete_one({"_id": ObjectId(codigo_cliente)})


    def inserir_contato(self, codigo_cliente, contato):

        qry = {"_id": ObjectId(codigo_cliente)}
        fld = {"$push": {"contatos": contato.transforma_dicionario}}

        self._colecao.update_one(qry, fld)

    def atualizar_contato(self, codigo_cliente, contato):

        qry = {"_id": codigo_cliente, "contatos._id": contato.id_}
        fld = {"$set": {
            "contatos.$.nome": contato.nome,
            "contatos.$.email": contato.email,
            "contatos.$.telefone": contato.telefone
        }}
        self._colecao.update_one(qry, fld)

    def excluir_contato(self, codigo_cliente, codigo_contato):

        qry = {"_id": ObjectId(codigo_cliente)}
        fld = {"$pull": {"contatos": {"_id": ObjectId(codigo_contato)}}}

        self._colecao.update_one(qry, fld)

    def inserir_endereco(self, codigo_cliente, endereco):

        qry = {"_id": ObjectId(codigo_cliente)}
        fld = {"$push": {"enderecos": endereco.transforma_dicionario}}

        self._colecao.update_one(qry, fld)

    def atualizar_endereco(self, codigo_cliente, endereco):

        qry = {"_id": codigo_cliente, "enderecos._id": endereco.id_}
        fld = {"$set": {
            "enderecos.$.rua": endereco.rua,
            "enderecos.$.numero": endereco.numero,
            "enderecos.$.bairro": endereco.bairro
        }}

        self._colecao.update_one(qry, fld)

    def excluir_endereco(self, codigo_cliente, codigo_endereco):

        qry = {"_id": ObjectId(codigo_cliente)}
        fld = {"$pull": {"enderecos": {"_id": ObjectId(codigo_endereco)}}}

        self._colecao.update_one(qry, fld)