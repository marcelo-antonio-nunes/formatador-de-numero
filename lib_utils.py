import os
from platform import system


def clear_all() -> None:
    '''
        Indentifica o sistem, e limpa o terminal com o comando correspondente
    '''
    if system() == 'Windows':
        os.system('cls')
    elif system() == 'Linux':
        os.system('clear')


def marcador(marcador: str, tamanho: int) -> str:
    '''
        marcador('caracter da escolha',comprimento do linha em)
        ex:marcador('=',10)
        saida: ==========
    '''
    return marcador * tamanho


def title_program(texto: str) -> None:
    '''
        title_program("Titulo do programa")
    '''
    comprimento = len(texto)+9
    print(f"{marcador('*',comprimento)}\n\
    {texto}\n{marcador('*',comprimento)}\n\n")


def filtra_numbers(numbers: str) -> str:
    '''
        so deixa passar numeros inteiros, elimina espaços e qualquer
        caracter que não seja numeros inteiros 
    '''
    result = ""
    for d in numbers:
        if d.isdigit():
            result += d
    return result


def format_numbers(entrada: str, casas: int) -> str:
    numbers: str = filtra_numbers(entrada)
    comprimento = casas + 2
    result = ''
    for i, d in enumerate(numbers):
        if i % casas == 0:
            result += '\n'+marcador('=', comprimento)+'\n'
        result += d
    return result+'\n\n'


def pause() -> None:
    input('Enter\n')


def menu() -> str:
    title_program('OPÇÔES')
    ops: str = '''
1)-Salvar\n
===========\n
2)-Inicio\n
===========\n
3)-Sair\n
===========\n
'''
    result = input(ops)
    return result


def menu2() -> str:
    title_program('OPÇÔES')
    ops2: str = '''
1)-Inicio\n
============\n
2)-Sair\n
============\n
'''
    result = input(ops2)
    return result


def dados() -> str:
    clear_all()
    nome_arquivo = input("arquivo  :").upper() or 'ARQUIVO'
    seu_nome = input("Seu None :").title() or 'não informado'
    telefone = input("Telefone :") or 'não informado'
    prefixo = f'{telefone[0]}{telefone[1]}'
    if  prefixo !='11':
       telefone = telefone.replace(telefone,'(11)'+telefone)
    else:
        telefone = telefone.replace(telefone,f'({prefixo}){telefone[2:]}')
    return nome_arquivo, seu_nome, telefone


def salvar(saida: str) -> str:
    arq, nome, tel = dados()
    ds = f'NOME:{nome}\nTELEFONE:{tel}\n\n{saida}\n\n'
    clear_all()
    if saida != "":
        if system() == 'Windows':
            os.chdir(r'C:\Users\Public\Documents')
        elif system() == 'Linux':
            os.chdir(r'~/')
        try:
            with open(f'{arq}.txt', 'w', encoding='utf-8') as f:
                f.write(ds)
            print(f'{ds}\n{arq} SALVO COM SUCESSO!!\n')
            pause()
            clear_all()
            result = menu2()
        except:
            print(f'ERRO AO TENTAR SALVAR O ARQUIVO {arq}')
    else:
        print(f'{arq} ESTÁ VASIO!!')
    return result


def sair() -> None:
    clear_all()
    exit()


def exec(fnc) -> None:
    '''
        Executa uma funcão passada como parametro
    '''
    fnc()
