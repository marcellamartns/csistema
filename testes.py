# -*- coding: utf-8 -*-


from cliente import Cliente
from contato import Contato
from endereco import Endereco
from conexao import Conexao
from pymongo import MongoClient


HOST =  "mongodb://localhost:27017/"
BANCO = "csistema"

# conexao com o banco
conexao_banco = MongoClient(HOST)
banco = conexao_banco[BANCO]
conexao = Conexao(banco)
print("PASSOU NO TESTE 1")

# criar os objetos cliente, contato e endereco
cli = Cliente(id_=None, cadastro=None, nome_razao="juju", cpf_cnpj="123344", tipo="juri", contatos=None, enderecos=None)
cont = Contato(id_=None, cadastro=None, nome="macela", email="marcella@1223", telefone="223344")
end = Endereco(id_=None, cadastro=None, rua="catira", numero="12349", bairro="jardi")
print("PASSOU NO TESTE 2")

# inserir cliente
conexao.inserir(cli)
print("PASSOU NO TESTE 3")

# atualizar cliente
conexao.atualizar(cli.id_, cli)
print("PASSOU NO TESTE 4")

# buscar um cliente
conexao.buscar(cli.id_)

# listar clientes
conexao.listar()
print("PASSOU NO TESTE 6")

# inserir contato
conexao.inserir_contato(cli.id_, cont)
print("PASSOU NO TESTE 7")

# atualizar contato
cont.email = "aaa"
conexao.atualizar_contato(cli.id_, cont)
print("PASSOU NO TESTE 8")

# excluir contato
conexao.excluir_contato(cli.id_, cont.id_)
print("PASSOU NO TESTE 9")

# inserir endereco
conexao.inserir_endereco(cli.id_, end)
print("PASSOU NO TESTE 10")

# atualizar endereco
end.rua = "asas"
conexao.atualizar_endereco(cli.id_, end)
print("PASSOU NO TESTE 11")

# excluir endereco
conexao.excluir_endereco(cli.id_, end.id_)
print("PASSOU NO TESTE 12")

# excluir cliente
conexao.excluir(cli.id_)
print("PASSOU NO ULTIMO TESTE")