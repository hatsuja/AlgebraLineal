import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)  # Para que los datos sean fijos y repetibles
n_datos = 100
X_datos = np.random.uniform(40, 150, n_datos)
ruido = np.random.normal(0, 12, n_datos) # Imita las variaciones del mercado
Y_datos = 2.1212 + (2.2303 * X_datos) + ruido
columna_unos = np.ones((n_datos, 1))
X_matriz = np.column_stack((columna_unos, X_datos))
Y_vector = Y_datos.reshape(-1, 1)
Matriz_A = X_matriz.T.dot(X_matriz)
Vector_B = X_matriz.T.dot(Y_vector)
Matriz_A_inversa = np.linalg.inv(Matriz_A)
Coeficientes = Matriz_A_inversa.dot(Vector_B)
A_intercepto = Coeficientes[0][0]
B_pendiente = Coeficientes[1][0]
print("==================================================")
print("       RESULTADOS DE LA REGRESIÓN MATRICIAL        ")
print("==================================================")
print(f"Valor calculado para A (Intercepto Base): {A_intercepto:.4f}")
print(f"Valor calculado para B (Costo por m²):    {B_pendiente:.4f}")
print("\nTu ecuación final queda estructurada como:")
print(f"Y = {A_intercepto:.4f} + {B_pendiente:.4f}X")
print("==================================================")
plt.figure(figsize=(9, 6))
plt.scatter(X_datos, Y_datos, color='royalblue', alpha=0.7, label='Departamentos reales (100 datos)')
X_linea = np.linspace(40, 150, 100)
Y_linea = A_intercepto + B_pendiente * X_linea
plt.plot(X_linea, Y_linea, color='red', linewidth=2.5, label=f'Recta de Regresión: Y = {A_intercepto:.2f} + {B_pendiente:.2f}X')
plt.title('Proyecto Inmobiliario: Regresión Lineal Matricial', fontsize=14, fontweight='bold')
plt.xlabel('Metros Cuadrados (Variable X)', fontsize=12)
plt.ylabel('Precio en Miles de USD (Variable Y)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
