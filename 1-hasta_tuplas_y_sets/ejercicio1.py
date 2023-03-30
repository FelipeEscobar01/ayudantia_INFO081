import random

def set_aleatorio(largo: int, rango: tuple):
    set1 = set()
    for i in range(0, largo):
        set1.add(random.randint(min(rango), max(rango) + 1))
    return set1


def una_transforme_lista_ordene(set1: set, set2: set, revertir = False):
    set1.update(set2)
    set1 = list(set1)
    if revertir:
        set1.sort(reverse=True)
    else:
        set1.sort()
    return set1

def main():
    set1, set2 = set_aleatorio(10, (1, 100)), set_aleatorio(10, (1, 100))
    print(una_transforme_lista_ordene(set1, set2))



if __name__ == "__main__":
    main()
