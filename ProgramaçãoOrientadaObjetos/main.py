from app import Restaurante

restaurante_praca=Restaurante('praça','Gourmet')
restaurante_mexicano=Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa','Japonesa')

restaurante_mexicano.alterar_estado()

def main():

    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
