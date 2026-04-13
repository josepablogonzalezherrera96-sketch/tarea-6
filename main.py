from operaciones import generador
from archivos import gestor

def mostrar_menu():
    print("\n--- Generador de Operaciones - Profesor Jirafales ---")
    
    try:
        cant_sumas = int(input("¿Cuántas sumas desea generar? "))
        cant_restas = int(input("¿Cuántas restas desea generar? "))
        cant_mult = int(input("¿Cuántas multiplicaciones desea generar? "))
        cant_div = int(input("¿Cuántas divisiones desea generar? "))
        
        todos_los_ejercicios = []
        
        # Generar cada bloque de ejercicios
        todos_los_ejercicios.extend(generador.generar_ejercicios('suma', cant_sumas))
        todos_los_ejercicios.extend(generador.generar_ejercicios('resta', cant_restas))
        todos_los_ejercicios.extend(generador.generar_ejercicios('multiplicacion', cant_mult))
        todos_los_ejercicios.extend(generador.generar_ejercicios('division', cant_div))
        
        # Guardar en los archivos correspondientes
        gestor.guardar_archivos(todos_los_ejercicios)
        
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    mostrar_menu()
  
