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


numero_romanos = ((1000, "M"), (500, "D"), (100 , "C"), (50, "D"),
 (10, "X"), (5, "V"), (1, "I"))

centenas = (
    (100, "C"), (200, "CC"), (300, "CCC"), (400, "CD"), (500, "D"), 
    (600, "DC"), (700, "DCC"), (800, "DCCC"), (900, "CM")
)

decenas = (
    (10, "X"), (20, "XX"), (30, "XXX"), (40, "XL"), (50, "L"), 
    (60, "LX"), (70, "LXX"), (80, "LXXX"), (90, "XC"))

unidades = (
    (1, "I"), (2, "II"), (3, "III"), (4, "IV"), (5, "V"), 
    (6, "VI"), (7, "VII"), (8, "VIII"), (9, "IX"))


"""
primer metodo
"""

def entero_a_romano(numero):
   
    numero = "{:0>4d}".format(numero)

    digitos = list(numero)
    ix = 0
    longitud = 4
    for n in numero:
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        ix += 1
        return digitos 

