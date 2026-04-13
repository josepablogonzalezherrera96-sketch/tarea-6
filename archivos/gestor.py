def guardar_archivos(todos_los_ejercicios):
    """Crea los archivos txt con los ejercicios y sus respuestas."""
    
    # Escribir archivo de práctica
    with open("practica.txt", "w", encoding="utf-8") as f_practica:
        for ej_sin_resolver, _ in todos_los_ejercicios:
            f_practica.write(ej_sin_resolver + "\n")
            
    # Escribir archivo de respuestas
    with open("respuestas.txt", "w", encoding="utf-8") as f_respuestas:
        for _, ej_resuelto in todos_los_ejercicios:
            f_respuestas.write(ej_resuelto + "\n")
            
    print("\n¡Archivos 'practica.txt' y 'respuestas.txt' generados con éxito!")
