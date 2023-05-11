
---
### _Para hacer los ejercicios propongo dos formas, hacer uno mismo los archivos (son aleatorios), o descargar aquellos que yo generé, ¡dejaré el codigo para la primera opcion y un enlace para la segunda!_
---

## 🥑 **Ejercicio 1**

Tengo una empresa que separa el cuanto se ha vendido cada dia durante el ultimo mes en un archivo, este archivo esta distribuido de la siguiente manera, las columnas me indican que division de la empresa responsable de ese numero de ventas y las filas me indican cuantas ventas fueron ese dia.

### columnas -> divisiones [0..n]
### filas -> ventas en el dia [1..n]

Por ejemplo, viendolo como una matriz de python, la posicion "[0, 0]" me indicara cuanto vendio la division 0, el dia 1.

En base a esto responda las siguientes preguntas:

**1) ¿Cual es la division que más ha vendido durante el último mes?**

**2) ¿Cual es la division que menos ha vendido durante el último mes?**

**3) ¿Que dia vendieron mas las divisiones en conjunto?**

<br/>

## 🥑 **Ejercicio 2**

Tengo una farmacia que guarda cada mes, un archivo por dia indicando cuanto stock se sumo de 'x' remedio al stock general (No lo sabemos, solo sabemos cuanto se sumo), los archivos estan distribuidos de esta manera:

```
Remedio1-Stock_nuevo1
Remedio2-Stock_nuevo1
...
RemedioN-Stock_nuevoN
```

En base a esto desarrolle lo siguiente:

**1) Escriba en un nuevo archivo, cuantos remedios llegaron de cada uno durante el mes**

**2) ¿Qué dia fue el que llego mas Venlafaxina?**

**3) ¿Qué dia fue el que llego menos Venlafaxina?**

<br/>

# **Codigos para generar los archivos**

### **Ejercicio 1**

```
import os
import random


def main():
    ejecutar = input((f"Directorio actual: {os.getcwd()}\n" \
                      f"¿Esta bien? Ingrese 0 (No) o 1 (Si)\n> "))
    if (ejecutar == '1'): 
        with open("ejercicio1.txt", 'w') as archivo:
            i = 0
            while (True):
                j = 0
                while (j != 9):
                    archivo.write(f"{random.randint(0, 100)}-")
                    j += 1
                archivo.write(f"{random.randint(0, 100)}\n")
                i += 1
                if (i == 30):
                    break


if __name__ == "__main__":
    main()
```

### **Ejercicio 2**

```
import os
import random


remedios = ["Fluoxetina", "Citalopram", "Sertralina", "Paroxetina",
            "Escitalopram", "Clonazepam", "Quetiapina", "Zopiclona",
            "Venlafaxina", "Vortioxetina"]


def main():
    ejecutar = input((f"Directorio actual: {os.getcwd()}\n" \
                      f"¿Esta bien? Ingrese 0 (No) o 1 (Si)\n> "))
    if (ejecutar == '1'):
        for i in range(1, 31):
            if (i < 10):
                nombre_archivo = f"0{i}-04-2023" 
            else:
                nombre_archivo = f"{i}-04-2023"
            with open(nombre_archivo, 'w') as archivo:
                for drug in remedios:
                    archivo.write(f"{drug}-{random.randint(20, 50)}\n")


if __name__ == "__main__":
    main()
```

# **Archivos generados por mi**

### **Ejercicio 1**

https://drive.google.com/file/d/1XCcU5UiXPcizX7Rhj33eEhMMV7fjMxOe/view?usp=share_link

### **Ejercicio 2**

https://drive.google.com/file/d/1TWpUNUafkSFJ6IkdEICsqbV8gVwmwgh8/view?usp=share_link