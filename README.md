# Ejercicio en clase - Generador de Árbol de Derivaciones

Este repositorio contiene un código en Python que genera y visualiza el árbol de derivaciones de una gramática matemática a partir de un archivo de texto.

## Instrucciones para clonar el repositorio y ejecutar el código

### 1. Clonar el repositorio

Para obtener el código, puedes clonar el repositorio de GitHub utilizando el siguiente comando en tu terminal o consola de comandos:

```bash
git clone https://github.com/MalianR/Ejercicio-en-clase.git
```

Esto descargará todos los archivos del repositorio a tu máquina local.

2. Acceder al directorio del proyecto
Una vez que hayas clonado el repositorio, accede al directorio donde se encuentra el proyecto:
```bash
cd Ejercicio-en-clase
```
3. Asegurarse de tener las dependencias necesarias
Este código utiliza las bibliotecas networkx y matplotlib. Si no las tienes instaladas, puedes instalarlas con pip:
```bash
pip install networkx matplotlib
```
4. Crear o modificar el archivo de gramática (Gramma.txt)
El archivo de entrada de la gramática debe estar en el mismo directorio que el archivo Python y debe tener el siguiente formato (El txt tiene esta gramatica):
```bash
E -> E + T | E - T | T
T -> T * F | T / F | F
F -> ( E ) | n
```
Este archivo define una gramática que sigue las siguientes reglas:

E: Expresión
T: Término
F: Factor

(**Update**)
Ir a la linea 76 del codigo donde esta la ubicacion de el .txt y modificar la ubicacion de donde esta ubicado este 
```bash
ruta_archivo = r"C:\Users\jrinc\Desktop\Leng de prog y trans\Ejercicio en clase Netx\Gramaa.txt"
```

5. Ejecutar el script
Para generar el árbol de derivaciones a partir de la gramática que definiste en el archivo Gramma.txt, puedes ejecutar el siguiente comando en la terminal:
```bash
python Gramaticaarbol.py Gramma.txt
```
Donde:
  Gramaticaarbol.py es el archivo que contiene el código Python.
  Gramma.txt es el archivo que contiene la gramática que deseas analizar.

6. Qué hace el código
El código realiza las siguientes acciones:

Carga la gramática: Lee el archivo de texto con las reglas de la gramática.
Genera el árbol de derivaciones: Crea un grafo dirigido donde cada nodo representa un símbolo de la gramática y las aristas representan las reglas de derivación.
Visualiza el árbol: Utiliza matplotlib y networkx para dibujar y mostrar el árbol de derivaciones.
Muestra las derivaciones: Muestra en la consola todas las posibles derivaciones desde cada símbolo de la gramática.

7. Ejemplo de salida
Un ejemplo de salida en la consola podría ser:

Aparte del grafico utilizando networkx en la terminal generaria algo parecido a lo siguiente 
```bash
Resultados de derivación:

Derivaciones desde E:
- E -> E + T
- E -> E - T
- E -> T

No hay derivaciones desde E + T

No hay derivaciones desde E - T

Derivaciones desde T:
- T -> T * F
- T -> T / F
- T -> F

No hay derivaciones desde T * F

No hay derivaciones desde T / F

Derivaciones desde F:
- F -> ( E )
- F -> n

No hay derivaciones desde ( E )

No hay derivaciones desde n
```
