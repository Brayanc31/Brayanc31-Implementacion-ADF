import sys


def AFD(cadena):
    transicion = {
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q3',
        ('q2', '0'): 'q2',
        ('q2', '1'): 'q2',
        ('q3', '0'): 'q3',
        ('q3', '1'): 'q3'
    }
    
    estado_inicial = 'q1'
    estados_aceptacion = ['q2']
    estado_actual = estado_inicial
    
    for simbolo in cadena:
        if simbolo not in ['0', '1']:
            return "NO ACEPTA"
        
        estado_actual = transicion[(estado_actual, simbolo)]
    
    if estado_actual in estados_aceptacion:
        return "ACEPTA"
    else:
        return "NO ACEPTA"


def main():
    archivo_entrada = sys.argv[1]
    
    with open(archivo_entrada, 'r') as archivo:
        lineas = archivo.readlines()
    
    for linea in lineas:
        cadena = linea.strip()
        if cadena:
            resultado = AFD(cadena)
            print(resultado)


if __name__ == "__main__":
    main()
