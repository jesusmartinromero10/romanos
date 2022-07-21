
from romano_funcional import entero_a_romano, romano_a_entero2

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



def test_error_si_entero_mayor_de_3999():
    assert entero_a_romano(1994) == "MCMXCIV"

#def test_error_romano_entero():
    #assert romano_a_entero("MCMXCIV") == 1994

def test_romano_a_entero_ordenados():
    assert romano_a_entero2("I") == 1
    assert romano_a_entero2("MDCCXIII") == 1713