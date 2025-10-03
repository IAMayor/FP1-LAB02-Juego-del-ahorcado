import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    # TODO: Implementa esta función (y elimina la instrucción pass)
    texto=cadena.lower() #todo minusculas
    texto=texto.strip() #quitar espacios delante y detrás
    texto2=""
    for c in texto:
        if c in "áä" :
            c="a"
        elif c in 'éë':
            c='e' 
        elif c in 'íï':
            c='i' 
        elif c in 'óö':
            c='o' 
        elif c in 'úü':
            c='u'
        texto2+=c
  

    return texto2 


def ocultar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    # TODO: Implementa esta función (y elimina la instrucción pass)
    texto=""
    for c in palabra_secreta:
        if c in letras_usadas:
            texto+=c 
        else:
            texto+="_"
    return texto 


def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    # TODO: Implementa esta función (y elimina la instrucción pass)
    if "_" in palabra_enmascarada:
        return False
    else:
        return True


# TODO: Implementa la función mostrar_estado
def mostrar_estado(palabra, letras, intentos_restan):
    '''
    la función `mostrar_estado` que usaremos durante el juego 
    para mostrar
    al jugador información sobre el transcurso del juego. 

    La función recibe por parámetros 
    palabra: la palabra enmascarada, 
    letras: las letras ya usadas y 
    intentos_restan: los intentos restantes. 

    Un ejemplo de la salida mostrada en el terminal al llamar a la función 
    sería el siguiente:
    '''
    print (f"Estado :{" ".join(palabra)} ")  

    if letras=="":
        print ("Letras usadas: ninguna")
    else:
        print ("Letras usadas: ",letras)
    print (" Intentos restantes: ", intentos_restan)
    return None

# TODO: Implementa la función pedir_letra

# TODO: Implementa la función jugar

# TODO: Escribe el programa principal
