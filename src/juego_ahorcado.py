import random

def elige_palabra(fichero="..\palabras.txt"):
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
    print (f"{"-"*10}")
    print (f"Estado :{" ".join(palabra)} ")  

    if letras=="":
        print ("Letras usadas: ninguna")
    else:
        print ("Letras usadas: ",letras)
    print (" Intentos restantes: ", intentos_restan)
    return None

# TODO: Implementa la función pedir_letra
def pedir_letra (letras_antes:str):
    '''
    Implementa la función `pedir_letra`, que solicita al jugador que introduzca una letra y se asegura de que la entrada proporcionada 
    por el jugador sea válida. Debe escribir la cabecera de la función y su cadena de documentación.
    
    Para que la entrada recibida del usuario sea válida debe cumplirse que:
    - Sea una letra (y solo una)
    - No sea una letra que ya se ha pedido anteriormente

    La función recibe un parámetro con las letras ya solicitadas anteriormente. Si el jugador no introduce una entrada válida, 
    la función le informa y se la vuelve a pedir, hasta que el jugador introduzca una letra válida. 
    En ese momento, la función devuelve dicha letra, **siempre en minúculas**.

    Una posible salida en el terminal de una llamada a la función sería esta 
    (suponiendo que las letras usadas incluyen sólo a la letra `a`)
    '''
    sigue=True
    while sigue: #en realidad saldrá del bucle con el return
        letra=input("Introduce una letra: ").lower()
        if len(letra)>1:
            print ("Debes introducir una única letra")   
        elif not letra.isalpha():
            print ("Debes introducir una letra")
        elif letra in letras_antes:
            print ("Esa letra ya la has utilizado")
        else: 
            return letra
    return None 


# TODO: Implementa la función jugar
def jugar(palabra_secreta, intentos=6):
    '''
    La función `jugar` recibe la palabra secreta que hay que adivinar y el número máximo de intentos (por defecto, será 6).
    1. **Inicialización**:  
    - Normalizamos la palabra mediante la función `normalizar`.  
    - Si la palabra está vacía, devolvemos `None` (y el juego termina).  
    - Enmascaramos la palabra mediante la función `ocultar`.  
    - Inicializamos una variable con el número máximo de intentos.  
    - Inicializamos una variable con las letras usadas hasta el momento (cadena vacía).  

    2. **Bucle principal**:  
    - Mientras el jugador tenga intentos restantes y no haya ganado:  
        - Muestra el estado del juego usando `mostrar_estado`.  
        - Pide una nueva letra usando `pedir_letra`.  
        - Añade a las letras usadas la que acabas de leer.  
        - Si la letra recibida no pertenece a la palabra secreta:              
            - Muestra un mensaje indicándolo.  
            - Resta 1 a los intentos.  
        - Si la letra recibida sí pertenece a la palabra secreta:  
            - Muestra un mensaje indicándolo.  
            - Actualiza la palabra enmascarada mediante la función `ocultar`.  

    3. **Fin del juego**: muestra un mensaje indicando si el jugador ha ganado o ha perdido, y cuál era la palabra original.

    '''
    palabra=normalizar(palabra_secreta)
    if palabra=="":
        return None 
    mascara=ocultar(palabra)
    veces=0
    letras=""
    no_gana=True
    while veces<intentos and no_gana:
        mostrar_estado(mascara,letras,intentos-veces)
        nueva_letra=pedir_letra(letras)
        letras+=nueva_letra
        if nueva_letra in palabra:
            print(f"La letra '{nueva_letra}' ESTÄ en la palabra secreta ✅ \n ")
            mascara=ocultar(palabra,letras)
            if "_" not in mascara:
                no_gana=False
        else:
            print(f"La letra '{nueva_letra}' no se encuentra en la palabra secreta ❌ \n")
            veces+=1
    print ("*** Fin del juego ***") 
    if no_gana:
        print (f"Lo siento has superado el máximo de intentos la palabra secreta era {palabra}")
    else:
        print (f"🎉¡¡¡ ENHORABUENA !!! has ACERTADO la palabra secreta {palabra.upper()} 🎉")
    return None

# TODO: Escribe el programa principal
palabra_alea=elige_palabra()
jugar(palabra_alea)
