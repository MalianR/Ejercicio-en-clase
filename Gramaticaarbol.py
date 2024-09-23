import networkx as nx
import matplotlib.pyplot as plt

def cargar_gramatica_desde_archivo(ruta_archivo):
    """Lee el archivo de gramática y retorna su contenido."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            gramatica = archivo.read()
        return gramatica
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encuentra.")
        return None
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

def validar_y_corregir_gramatica(gramatica):
    """Valida las reglas gramaticales y corrige las que no cumplen el formato A -> B."""
    reglas = gramatica.split('\n')
    reglas_validas = []
    reglas_corregidas = []
    reglas_invalidas = []

    for regla in reglas:
        regla = regla.strip()
        if not regla:
            continue
        if '->' in regla:
            reglas_validas.append(regla)
        else:
            # Intentar corregir la regla mal formateada
            partes = regla.split()
            if len(partes) > 1:
                simbolo_izquierdo = partes[0]
                simbolos_derechos = ' '.join(partes[1:])
                regla_corregida = f"{simbolo_izquierdo} -> {simbolos_derechos}"
                reglas_corregidas.append(regla_corregida)
            else:
                reglas_invalidas.append(regla)

    if reglas_invalidas:
        print(f"\nSe encontraron reglas que no pudieron ser corregidas y se ignorarán:")
        for regla in reglas_invalidas:
            print(f" - {regla}")

    return reglas_validas + reglas_corregidas

def extraer_simbolo_inicial(gramatica):
    """Extrae el símbolo inicial de la primera regla gramatical válida."""
    for regla in gramatica.split('\n'):
        if '->' in regla:
            simbolo_inicial = regla.split('->')[0].strip()
            return simbolo_inicial
    return None

def generar_arbol_derivaciones(gramatica):
    """Genera el árbol de derivaciones basado en las reglas gramaticales."""
    G = nx.DiGraph()
    
    simbolo_inicial = extraer_simbolo_inicial(gramatica)
    if not simbolo_inicial:
        print("Error: No se encontró un símbolo inicial.")
        return None
    
    G.add_node(simbolo_inicial)
    
    for regla in validar_y_corregir_gramatica(gramatica):
        regla = regla.replace('"', '')
        simbolo_izquierdo, simbolos_derechos = regla.split('->')
        simbolo_izquierdo = simbolo_izquierdo.strip()
        simbolos_derechos = simbolos_derechos.split('|')
        
        for simbolo_derecho in simbolos_derechos:
            simbolos = simbolo_derecho.strip().split()
            for simbolo in simbolos:
                G.add_node(simbolo)
                G.add_edge(simbolo_izquierdo, simbolo)

    return G

def visualizar_arbol_derivaciones(G, titulo="Árbol de derivaciones", guardar=False, ruta_salida="arbol_derivaciones.png"):
    if G is None:
        print("No se puede visualizar un árbol vacío.")
        return
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=1500, font_size=10, arrowsize=20, arrowstyle='->')
    
    plt.title(titulo)
    plt.axis('off')
    plt.show()
    
    if guardar:
        plt.savefig(ruta_salida)
        print(f"El árbol de derivaciones ha sido guardado en '{ruta_salida}'.")

def mostrar_derivaciones(G):
    if G is None:
        print("No hay derivaciones que mostrar.")
        return
    
    print("\nResultados de derivación:")
    for start_node in G.nodes():
        successors = list(G.successors(start_node))
        if successors:
            print(f"\nDerivaciones desde {start_node}:")
            for end_node in successors:
                print(f"- {start_node} -> {end_node}")
        else:
            print(f"\nNo hay derivaciones desde {start_node}")

# Ejemplo de uso
ruta_archivo = r"C:\Users\jrinc\Desktop\Leng de prog y trans\Ejercicio en clase Netx\Gramaa.txt"
ruta_archivo_falla = r"C:\Users\jrinc\Desktop\Leng de prog y trans\Ejercicio en clase Netx\Falla.txt"

gramatica = cargar_gramatica_desde_archivo(ruta_archivo_falla)

if gramatica:
    G = generar_arbol_derivaciones(gramatica)
    visualizar_arbol_derivaciones(G, "Árbol de derivaciones para la gramática (con correcciones)", guardar=True)
    mostrar_derivaciones(G)
