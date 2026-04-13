import random

def generar_numero_dos_digitos():
    """Genera un número aleatorio de dos dígitos."""
    return random.randint(10, 99)

def generar_ejercicios(tipo, cantidad):
    """Genera una lista de tuplas con el formato (ejercicio_str, respuesta_str)."""
    ejercicios = []
    
    for _ in range(cantidad):
        a = generar_numero_dos_digitos()
        b = generar_numero_dos_digitos()
        
        if tipo == 'suma':
            ejercicios.append((f"{a}+{b}=", f"{a}+{b}={a+b}"))
        
        elif tipo == 'resta':
            # Para evitar resultados negativos en primaria, aseguramos que a >= b
            if a < b:
                a, b = b, a
            ejercicios.append((f"{a}-{b}=", f"{a}-{b}={a-b}"))
            
        elif tipo == 'multiplicacion':
            ejercicios.append((f"{a}*{b}=", f"{a}*{b}={a*b}"))
            
        elif tipo == 'division':
            # Para asegurar división exacta y operandos de dos dígitos
            divisor = random.randint(10, 99)
            cociente = random.randint(1, 9) # Cociente pequeño para que el dividendo no pase de 999
            dividendo = divisor * cociente
            
            # Si el dividendo no es de dos dígitos, ajustamos la lógica para cumplir la regla
            while dividendo > 99:
                divisor = random.randint(10, 49)
                cociente = random.randint(1, 2)
                dividendo = divisor * cociente
                
            ejercicios.append((f"{dividendo}/{divisor}=", f"{dividendo}/{divisor}={cociente}"))
            
    return ejercicios
