from lib_utils import *


def main() -> None:
    titulo = 'Formatador de numeros'
    clear_all()
    title_program(titulo)
    numeros = input('Numeros :')
    saida = format_numbers(numeros, 5)
    print(saida)
    pause()
    clear_all()
    op = menu()
    if op == '1':
        op2 = salvar(saida)
        if op2 == '1':
            exec(main)
        elif op2 == '2':
            sair()
    if op == '2':
        exec(main)
    elif op == '3':
        sair()


if __name__ == '__main__':
    main()
