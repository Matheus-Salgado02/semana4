class Restaurante:
    restaurantes = []


    def __init__(self,nome,categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome} | {restaurante.categoria} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return 'true' if self._ativo else 'false'
    
    def alterar_estado(self):
        self._ativo = not self._ativo
    





