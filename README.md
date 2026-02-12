# AFD – Autómata Finito Determinista en Python

Este repositorio implementa un **Autómata Finito Determinista (AFD)** en Python que evalúa cadenas binarias (`0` y `1`) leídas desde un archivo de texto.

---

##  Descripción

El autómata:

- Tiene como estado inicial `q1`
- Tiene como estado de aceptación `q2`
- Procesa cadenas binarias
- Determina si una cadena es **ACEPTADA** o **NO ACEPTADA**

---

##  Lenguaje que reconoce

El AFD acepta **todas las cadenas binarias que comienzan con `0`**.

### Ejemplos

| Cadena | Resultado |
|--------|-----------|
| 0      | ACEPTA    |
| 01     | ACEPTA    |
| 0111   | ACEPTA    |
| 1      | NO ACEPTA |
| 10     | NO ACEPTA |

---

##  Estructura del Autómata

### Estados:
- `q1` → Estado inicial  
- `q2` → Estado de aceptación  
- `q3` → Estado trampa  

### Transiciones:

| Estado | 0  | 1  |
|--------|----|----|
| q1     | q2 | q3 |
| q2     | q2 | q2 |
| q3     | q3 | q3 |

---

##  Uso del programa

En el repositorio ya se incluyen:

- `AFD.py` → Programa principal  
- `entrada.txt` → Archivo de entrada con las cadenas  

 Ambos archivos deben permanecer en la **misma carpeta**.

No es necesario crear ningún archivo adicional.

###  Ejecutar el programa

Desde la carpeta donde están los archivos:

```bash
python afd.py cadenas.txt
