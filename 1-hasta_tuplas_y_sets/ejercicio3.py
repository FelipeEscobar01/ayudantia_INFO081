def revertir_tupla(tupla: tuple) -> tuple:
    return tupla[::-1]


def main():
    tupla = (1, "Holi", 'a', 1.5) 
    print(revertir_tupla(tupla))


if __name__ == "__main__":
    main()
