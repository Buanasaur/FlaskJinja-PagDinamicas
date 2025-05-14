class Curso:

    def __init__(self, nome, descricao):
        # os atributos estão públicos.
        self.nome = nome
        self.descricao = descricao

    def get_nome(self):
        return self.nome

    def get_descricao(self):
        return self.descricao