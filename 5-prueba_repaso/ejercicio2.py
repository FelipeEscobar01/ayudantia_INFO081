
palabra = {127 : 'N', 293 : 'e', 145 : 'e',
           297 : 's', 373 : 't', 319 : 'i',
           504 : 'o', 531 : ' ', 199 : 'c',
           541 : 'd', 592 : 'o', 810 : 'á',
           679 : 'm', 664 : 'r', 712 : 'i',
           759 : 'r', 771 : ' ', 790 : 'm',
           816 : 's'}

def descrifra_mensaje(palabra: dict) -> None:
    llaves = list(palabra.keys())
    llaves.sort()
    for key in llaves:
        print(palabra[key], end='')

def main():
    descrifra_mensaje(palabra) 

if __name__ == "__main__":
    main()
