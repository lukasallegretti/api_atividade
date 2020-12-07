from models import Pessoas

def inserePessoas(nome,idade):
    pessoa = Pessoas(nome=nome,idade=idade)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)

def filtro(nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    print(pessoa.nome)
    print(pessoa.idade)

def altera_pessoa(nome=None,nova_idade=None):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.nome = nome
    pessoa.idade =  nova_idade
    pessoa.save()

def exclui_pessoa(nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.delete()

if __name__ == '__main__':
    #inserePessoas('Lukas',24)
    altera_pessoa('Lukas',24)
    filtro('Lukas')
    exclui_pessoa('Lukas')
    consulta()