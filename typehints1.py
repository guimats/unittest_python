from typing import (
    Any, NewType, Callable, Sequence, Iterable, TypeVar
)

# Primitivos
numero: int = 10
flutuante: float = 10.5
boolean: bool = False
string: str = 'Luiz Otavio'

# ---------------------------------------------------
# Sequências
tupla: tuple = (1, 2, 3, 'Luiz')
# Se quiser especificar o tipo do item tem que especificar cada um dos itens
tupla_str_int: tuple[int, int, int, str] = (1, 2, 3, 'Luiz')

# Na lista, você pode especificar o tipo apenas uma vez para varios itens
lista: list[int] = [1, 2, 3]
lista_str_int: list[int | str] = [1, 2, 3, 'Luiz']


# ---------------------------------------------------
# Dicionarios e conjuntos(sets)

# Meu tipo -> jogando um tipo em uma variavel
MeuDict = dict[str, str | int | list[int | str]]  # Se chama 'Alias'

# No dict, você pode especificar somente uma vez o tipo das chaves e valores
pessoa: dict[str, str | int] = {'nome': 'Luiz Otavio',
                                'sobrenome': 'Miranda', 'idade': 30}

pessoa2: MeuDict = {
    'nome': 'Luiz Otavio',
    'sobrenome': 'Miranda', 'idade': 30, 'lista': [1, 2, 'endereço']
}

# Pode se usar o any para falar que qualquer tipo é aceito (MÁ PRATICA)
pessoa3: dict[str, Any] = {'nome': 'Luiz Otavio',
                           'sobrenome': 'Miranda', 'idade': 30}


# CRIANDO NOVOS TIPOS
UserId = NewType('UserId', int)
user_id = UserId(312312312)


# tipagem de funções
# Callabe = primeiro argumento: tipos parametros recebidos
# Callabe = segundo argumento: tipo retorno da função

# função que não recebe argumento e retornada nada:
# def retorna_funcao(funcao: Callable[[], None]) -> Callable:
#     return funcao


# def fala_oi() -> None:
#     print('Oi')

# retorna_funcao(fala_oi)()


# função que recebe argumentos e retorna algo:
def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


# def soma(x: int, y: int) -> int:
#     return x + y


# print(retorna_funcao(soma)(10, 20))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


def iterar(sequencia: Sequence[int]):
    return [x for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x for x in sequencia]


# print(iterar([1, 2, 3]))
# print(iterar((1, 2, 3)))

# print(iterar2([1, 2, 3]))
# print(iterar2((1, 2, 3)))

# None pode ser usado para parametros que podem não ser enviados
def soma(x: int, y: float | None = None) -> float:
    # Pode precisar usar isinstance quando utilizar None na tipagem
    if isinstance(y, float | int):
        return x + y
    return x + x


print(soma(1, 5))

# Tipo dinâmico
T = TypeVar('T')

# Se comporta dependendo do que é enviado


def get_item(list: list[T], index: int) -> T:
    return list[index]


list_int = get_item([1, 2, 3], 1)  # list fica com tipo int
list_str = get_item(['a', 'b', 'c'], 1)  # list fica com tipo str
