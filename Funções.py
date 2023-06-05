def dizer_ola():
    print("Olá, Mundo!")


def exibir_saudacoes(nome: str, periodo: int):
    if periodo == 1:
        print(f'Bom dia, {nome}')
    elif periodo == 2:
        print(f'Boa tarde, {nome}')
    else:
        print(f'Boa noite, {nome}')


dizer_ola()
exibir_saudacoes("Guilherme", 1)
exibir_saudacoes(periodo=1, nome='José')
