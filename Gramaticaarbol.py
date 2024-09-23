import networkx as nx
import matplotlib.pyplot as plt

def cargar_gramatica_desde_archivo(ruta_archivo):
    # Intentar abrir el archivo y manejar posibles errores
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

def generar_arbol_derivaciones(gramatica):
    # Creamos un grafo dirigido vacío
    G = nx.DiGraph()
    
    # Agregamos el nodo inicial (símbolo inicial de la gramática)
    simbolo_inicial = "E"
    G.add_node(simbolo_inicial)
    
    # Procesamos cada regla en la gramática, ignorando líneas vacías
    for regla in gramatica.split('\n'):
        regla = regla.strip().replace('"', '')
        
        # Ignoramos las reglas vacías o mal formateadas
        if not regla:
            continue
        
        # Verificamos que la regla tenga el separador "->"
        if '->' in regla:
            simbolo_izquierdo, simbolos_derechos = regla.split('->')
            simbolo_izquierdo = simbolo_izquierdo.strip()
            simbolos_derechos = simbolos_derechos.split('|')
            
            # Agregamos los nodos y aristas para cada símbolo derecho
            for simbolo_derecho in simbolos_derechos:
                simbolo_derecho = simbolo_derecho.strip()
                if simbolo_derecho:  # Evitar agregar nodos vacíos
                    G.add_node(simbolo_derecho)
                    G.add_edge(simbolo_izquierdo, simbolo_derecho)
        else:
            print(f"Regla mal formateada (se espera '->'): {regla}")
    
    return G

def visualizar_arbol_derivaciones(G, titulo="Árbol de derivaciones"):
    # Generar una disposición de los nodos usando spring_layout
    pos = nx.spring_layout(G)  
    
    # Dibujamos el grafo con configuraciones mejoradas
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=1500, font_size=10, arrowsize=20, arrowstyle='->')
    
    # Configuraciones adicionales del gráfico
    plt.title(titulo)
    plt.axis('off')  # Ocultar las marcas del eje
    plt.show()

def mostrar_derivaciones(G):
    # Mostrar las derivaciones desde cada nodo
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

# Intentar cargar la gramática
gramatica = cargar_gramatica_desde_archivo(ruta_archivo)

if gramatica:
    # Generar el árbol de derivaciones
    G = generar_arbol_derivaciones(gramatica)

    # Visualizar el árbol
    visualizar_arbol_derivaciones(G, "Árbol de derivaciones para la gramática matemática")

    # Mostrar las derivaciones
    mostrar_derivaciones(G)
