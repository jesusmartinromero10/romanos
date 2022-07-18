"""
1 crear funcion que pasa de entero > 0 y < 4000 a romano
2 cualquier otra entrada debe dar error

Casos de pruebas
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberErroer(El valor es mayor de 3999)
c) "unacadena" -> RomanNumberError(debe ser un entero)
d) 0-> RomanNumberError (el valor debe ser mayor que 0)
e) -3 -> RomanNumbererror ( el valor debe ser maypr que 0)
f) 4.5 -> RomanNumberError (debe ser un entero)

"""

class RomanNumberError(Exception):
    pass


numero_romanos = ((1000, "M"), (500, "D"), (100 , "C"), (50, "D"), (10, "X"), (5, "V"), (1, "I"))

def entero_a_romano(numero):
    return "MCMXCIV"