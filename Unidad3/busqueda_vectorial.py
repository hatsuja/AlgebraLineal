import numpy as np
from sentence_transformers import SentenceTransformer

# ==============================================================================
# 10. CARGA DEL MODELO MULTILINGÜE
# Se utiliza el modelo 'paraphrase-multilingual-MiniLM-L12-v2' que genera
# embeddings de 384 dimensiones optimizados para capturar la semántica en español.
# ==============================================================================
print("Cargando el modelo Transformer...")
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
print("¡Modelo cargado exitosamente!\n")

# ==============================================================================
# 9. COLECCIÓN DE 50 DOCUMENTOS (Frases sobre Tecnología, Robótica y Programación)
# ==============================================================================
documentos = [
    # Categoria 1: Robótica y Hardware (1 - 15)
    "Brazo robótico con servomotores y sensores",
    "Robot seguidor de línea con Arduino",
    "Diseño de circuitos electrónicos para microcontroladores",
    "Mecatrónica aplicada a la automatización industrial",
    "Control de motores a paso con Raspberry Pi",
    "Construcción de drones autónomos de exploración",
    "Ensamblaje de chasis para robots móviles",
    "Uso de sensores ultrasónicos para evadir obstáculos",
    "Sensores de temperatura y humedad en sistemas embebidos",
    "Implementación de servos de alto torque para robótica",
    "Arquitectura de hardware para robots antropomórficos",
    "Sistemas de navegación para aspiradoras robóticas",
    "Baterías de litio para drones y vehículos terrestres",
    "Módulos de comunicación Bluetooth para Arduino",
    "Mantenimiento preventivo de componentes mecatrónicos",

    # Categoria 2: Programación, Software y Algoritmos (16 - 30)
    "Código en Python para algoritmos de ordenamiento",
    "Desarrollo de software y lógica de programación",
    "Estructuras de datos avanzadas en C y C++",
    "Desarrollo de aplicaciones web responsivas",
    "Creación de APIs RESTful con Node.js y Express",
    "Bases de datos relacionales SQL y optimización de consultas",
    "Programación orientada a objetos en Java",
    "Desarrollo de videojuegos con motores gráficos como Unity",
    "Patrones de diseño de software e arquitectura limpia",
    "Automatización de scripts en entornos Linux",
    "Pruebas unitarias e integración continua en desarrollo",
    "Control de versiones utilizando Git y GitHub",
    "Programación concurrente y multihilo en Python",
    "Desarrollo frontend utilizando el framework React",
    "Optimización del rendimiento en sistemas backend",

    # Categoria 3: Inteligencia Artificial y Ciencia de Datos (31 - 40)
    "Entrenamiento de redes neuronales convolucionales con PyTorch",
    "Modelos de inteligencia artificial para procesamiento de lenguaje natural",
    "Algoritmos de aprendizaje supervisado y clasificación de datos",
    "Modelos Transformers para visión por computadora",
    "Análisis exploratorio de datos mediante Pandas y NumPy",
    "Implementación de modelos de Regresión Lineal",
    "Redes neuronales recurrentes para análisis de series temporales",
    "Ajuste de hiperparámetros en modelos de Deep Learning",
    "Uso de Scikit-Learn para aprendizaje automático",
    "Despliegue de modelos de machine learning en la nube",

    # Categoria 4: Sistemas y Ciberseguridad (41 - 50)
    "Seguridad informática y pruebas de penetración en redes",
    "Configuración de servidores y redes de comunicación",
    "Computación en la nube e infraestructura como código",
    "Criptografía aplicada a la protección de datos",
    "Administración de contenedores utilizando Docker y Kubernetes",
    "Detección de intrusos y análisis de malware",
    "Protocolos de comunicación de red TCP y IP",
    "Seguridad en aplicaciones web e inyección SQL",
    "Monitoreo de rendimiento de servidores en tiempo real",
    "Sistemas operativos y gestión de memoria principal"
]

# Justificación del cálculo de embeddings:
# Se utiliza la librería Transformer que mapea cada uno de los 50 textos
# a un vector continuo de 384 dimensiones en un espacio semántico denso.
print("Generando vectores (embeddings) para los 50 documentos...")
vectores_docs = model.encode(documentos)
print(f"¡Vectores generados! Tamaño del corpus: {len(vectores_docs)} vectores de dimensión {len(vectores_docs[0])}.\n")

# ==============================================================================
# 11, 12, 13, 14 y 15. FUNCIÓN PRINCIPAL DE BÚSQUEDA VECTORIAL
# ==============================================================================
def realizar_busqueda(texto_consulta):
    # 12. Convertir la consulta en vector usando el mismo modelo Transformer
    vector_consulta = model.encode(texto_consulta)
    
    # Cálculo de la norma del vector de la consulta: ||Q||
    norma_consulta = np.linalg.norm(vector_consulta)
    
    resultados = []
    
    # 13 y 15. Recorrer los 50 documentos para calcular Producto Punto, Norma y Similitud Coseno
    for i, vector_doc in enumerate(vectores_docs):
        # 15. Producto punto: Q · D
        prod_punto = np.dot(vector_consulta, vector_doc)
        
        # 15. Norma del documento: ||D||
        norma_doc = np.linalg.norm(vector_doc)
        
        # 13 y 15. Similitud coseno: (Q · D) / (||Q|| * ||D||)
        similitud = prod_punto / (norma_consulta * norma_doc)
        
        resultados.append({
            'id': i + 1,
            'texto': documentos[i],
            'prod_punto': prod_punto,
            'norma_doc': norma_doc,
            'similitud': similitud
        })
    
    # 14. Ordenar los resultados de MAYOR a MENOR similitud coseno
    resultados.sort(key=lambda x: x['similitud'], reverse=True)
    
    # 14 y 15. Mostrar en pantalla el TOP 5 con todos los detalles matemáticos
    print("=" * 80)
    print(f"RESULTADOS PARA LA CONSULTA: '{texto_consulta}'")
    print(f"Norma del Vector Consulta ||Q||: {norma_consulta:.4f}")
    print("=" * 80)
    print(f"{'Rank':<5} | {'Doc ID':<7} | {'Similitud':<10} | {'Prod. Punto':<11} | {'Norma D':<9} | Texto del Documento")
    print("-" * 80)
    
    for rank, res in enumerate(resultados[:5], 1):
        print(f"{rank:<5} | D_{res['id']:<5} | {res['similitud']:<10.4f} | {res['prod_punto']:<11.4f} | {res['norma_doc']:<9.4f} | {res['texto']}")
    print("=" * 80 + "\n")

# ==============================================================================
# 11 y 16. MODO INTERACTIVO Y PRUEBA DE CONSULTAS (Mínimo 3 consultas)
# ==============================================================================
if __name__ == "__main__":
    print("----------------------------------------------------------------------")
    print("SISTEMA DE BÚSQUEDA VECTORIAL INTERACTIVO")
    print("----------------------------------------------------------------------\n")
    
    # 11. Ingreso de consulta por teclado
    while True:
        consulta_usuario = input("Ingrese su consulta de búsqueda (o escriba 'salir' para finalizar): ")
        if consulta_usuario.lower().strip() == 'salir':
            print("\n¡Programa finalizado!")
            break
        elif consulta_usuario.strip() == "":
            print("Por favor, ingrese un texto válido.\n")
            continue
            
        realizar_busqueda(consulta_usuario)
