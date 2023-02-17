import metodos
import math
import pytest

def prueba_divide_string():
    #Para todas las pruebas se iguala el resultado del método a la respuesta esperada, si este es igual se sabe que el método funciona correctamente.
    #Prueba 1: Verifica que en la operación 1, el string se divide en mayúsculas/numeros y minúsculas
    resultado = metodos.divide_string("AbcDEf12", 1)
    assert resultado == ('ADE12', 'bcf')
    
    #Prueba 2: Verifica que en la operación 2, el string se divide en mitades (#caracteres par)
    resultado = metodos.divide_string("AbcDEf12", 2)
    assert resultado == ('AbcD', 'Ef12')
    
    #Prueba 3: Verifica que en la operación 2, el string se divide en mitades (#caracteres impar)
    resultado = metodos.divide_string("M1cR0pr053s4D0r3s", 2)
    assert resultado == ('M1cR0pr05', '3s4D0r3s')
    
    #Prueba 4: Se emite un código de error cuando el parámetro 'frase' no es un string
    resultado = metodos.divide_string(1, 1)
    assert resultado == "Error: El parámetro 'frase' debe ser un string."
    
    #Prueba 5: Se emite un código de error cuando el parámetro 'operacion' no es un número entero
    resultado = metodos.divide_string("AbcDEf12", "1")
    assert resultado == "Error: El parámetro 'operacion' debe ser un número entero."
    
    #Prueba 6: El método devuelve un código de error cuando el parámetro 'operacion' no es 1 o 2
    resultado = metodos.divide_string("AbcDEf12", 3)
    assert resultado == "Error: El parámetro 'operacion' debe ser 1 o 2."

def prueba_measure_area():
    #Prueba 1: Verifica que la operación se haga correctamente
    resultado = metodos.measure_area(5)
    assert resultado[0] == 25
    assert math.isclose(resultado[1], math.pi*(5**2) , abs_tol=0)
    #Prueba 2: Parámetro no entero
    result = AreaCalculator.measure_area("hello")
    assert result == -1

    
