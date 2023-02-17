import math
def divide_string(frase, operacion):
    if not isinstance(frase, str): #se verifica si el parámetro frase es string o no
        return "1342"
    if not isinstance(operacion, int): #se verifica si el parámetro operacion es integer o no
        return "2511"
    if operacion == 1:
        mayusculas = "" #string para contener los caracteres numéricos y las mayúsculas
        minusculas = "" #string para contener los caracteres no alfanuméricos y las minúsculas
        for caracter in frase: #con el for se recorre uno a uno los caracteres que forman la frase ingresada
            if caracter.isnumeric() or caracter.isupper(): #si el caracter es numérico o una mayúscula se agregan al string mayuscula 
                mayusculas += caracter
            else:
                minusculas += caracter
        return mayusculas, minusculas #la función devuelve los 2 strings formados
    elif operacion == 2:
        longitud = len(frase) #se utiliza para medir la longitud del string
        mitad = longitud // 2
        if longitud % 2 == 0: #si la cantidad de caracteres es par se ejecuta esta opción
            return (frase[:mitad], frase[mitad:]) #devuelve el string partido a la mitad
        else: #si la cantidad de caracteres es impar se ejecuta esta opción
            return (frase[:mitad+1], frase[mitad+1:]) #se divide el string de modo que la primera mitad tenga un caracter más que la segunda mitad
    else:
        return "1220"

def measure_area(parametro):
    if not isinstance(parametro, int): #se verifica si el parámetro es un número entero o no
        return "2511"  # Código de error único si el parámetro no es un número entero
    #si el parámetro es un número entero:
    areaSq = parametro ** 2 #cálculo del área del cuadrado usando parametro como medida del lado
    areaCir = math.pi * (parametro ** 2) #cálculo del área del círculo usando parametro como medida del radio
    return areaSq, areaCir

