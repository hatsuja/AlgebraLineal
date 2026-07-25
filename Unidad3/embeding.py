from sentence_transformers import SentenceTransformer
# 1. Cargar el modelo multilingüe en español
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
# 2. Documentos de Robótica y Programación
documentos = [
    "Brazo robótico con servomotores y sensores",
    "Robot seguidor de línea con Arduino",
    "Código en Python para algoritmos",
    "Desarrollo de software y lógica",
    "Programación de sensores para un robot"
]
# 3. Consulta de búsqueda
consulta = ["Cómo construir un robot con servomotores"]
# 4. Generar los Embeddings (Vectores)
vectores_docs = model.encode(documentos)
vector_consulta = model.encode(consulta)
# 5. Mostrar los primeros 5 elementos del embedding de cada documento
print("===============================================================")
print("PRIMEROS 5 ELEMENTOS DEL EMBEDDING DE CADA DOCUMENTO:")
print("===============================================================\n")
for i, doc_vector in enumerate(vectores_docs):
    print(f"Documento {i+1} ('{documentos[i]}'):")
    print(f"  Embedding (primeros 5 valores): {doc_vector[:5]}\n")
# 6. Mostrar los primeros 5 elementos del embedding de la consulta
print("===============================================================")
print("PRIMEROS 5 ELEMENTOS DEL EMBEDDING DE LA CONSULTA:")
print("===============================================================\n")
print(f"Consulta: '{consulta[0]}'")
print(f"  Embedding (primeros 5 valores): {vector_consulta[0][:5]}")

