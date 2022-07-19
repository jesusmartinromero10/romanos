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

"""
1. Crear una función que pase de entero > 0 y < 4000 a romano
2. Cualquier otra entrada debe dar error


"""

class RomanNumberError(Exception):
    pass

numero_romano = (
    (1000, 'M'), (500, 'D'), (100, 'C'), (50, 'D'), (10, 'X'), (5, 'V'), (1, 'I')
)

componentes = {
    
        1000:'M', 2000 : 'MM', 3000 : 'MMM',
    
    
        100 : 'C', 200 : 'CC', 300 : 'CCC',
        400 : 'CD', 500 : 'D', 600 : 'DC',
        700 : 'DCC', 800 : 'DCCC', 900 : 'CM',
    
    
        10 :'X', 20 : 'XX', 30 :'XXX',
        40 : 'XL', 50 : 'L', 60 : 'LX',
        70 : 'LXX', 80 : 'LXXX', 90 : 'XC',
    
        1 : 'I', 2: 'II', 3 : 'III',
        4 : 'IL', 5 : 'V', 6 : 'VI',
        7 : 'VII', 8 : 'VIII', 9 : 'IX'
    

}


def entero_a_romano(numero):
    """
    numero = str(numero)
    longitud = len(numero)

    if longitud < 4:
        numero = "{:0>4s}".format(numero)
    """
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    ix = 0
    longitud = len(digitos)
    romano = ""
    for n in numero:
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        romano = romano + componentes.get(int(digitos[ix]), "")
        ix += 1
    return romano



entero_a_romano(336)


