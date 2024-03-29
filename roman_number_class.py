


from romano_funcional import RomanNumberError


class NumeroRomano:
    componentes = {
    
        1000:'M', 2000 : 'MM', 3000 : 'MMM',
    
    
        100 : 'C', 200 : 'CC', 300 : 'CCC',
        400 : 'CD', 500 : 'D', 600 : 'DC',
        700 : 'DCC', 800 : 'DCCC', 900 : 'CM',
    
    
        10 :'X', 20 : 'XX', 30 :'XXX',
        40 : 'XL', 50 : 'L', 60 : 'LX',
        70 : 'LXX', 80 : 'LXXX', 90 : 'XC',
    
        1 : 'I', 2: 'II', 3 : 'III',
        4 : 'IV', 5 : 'V', 6 : 'VI',
        7 : 'VII', 8 : 'VIII', 9 : 'IX'
    

    }

    simbolo_romano = {
    "M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1, "" : 0
    }

    def __init__(self, valor):

        if isinstance(valor, int):

            self.valor = valor
            self.representacion = self.entero_a_romano(valor)
        elif isinstance(valor, str):
            self.representacion = valor
            self.valor = self.romano_a_entero(valor)
        else:
            raise RomanNumberError("Valor debe ser cadena o entero")
    

    def entero_a_romano(self, valor):
        numero = "{:0>4d}".format(valor)
        digitos = list(numero)

        longitud = len(digitos)
        romano = ''
        for ix in range(len(numero)):
            longitud -= 1
            digitos[ix] = digitos[ix] + "0" * longitud
            romano += self.componentes.get(int(digitos[ix]), "")

        return romano
    
    def romano_a_entero(self, romano):
        r = 0
        caracter_anterior = ""
        cont_repes = 1
        compro = ""
        for caracter in romano:
            
            if caracter == caracter_anterior:
                cont_repes += 1
            else:
                cont_repes = 1

            if (caracter == "D" and caracter_anterior == "D") or (caracter == "L" and caracter_anterior == "L") or (caracter == "V" and caracter_anterior == "V"):
                raise RomanNumberError("No se puede repetir D o L o V mas de una vez")

            if cont_repes > 3:
                raise RomanNumberError("No se pueden dar mas de tres repeticiones")

            if self.simbolo_romano[caracter] > self.simbolo_romano[caracter_anterior]:
                if caracter_anterior == "I" and (caracter != "X" and caracter != "V"):
                    raise RomanNumberError("No se puede restar I a un valor distinto de X o V")
                if caracter_anterior == "X" and (caracter != "L" and caracter != "C"):
                    raise RomanNumberError("No se puede restar X a un valor distinto de L o C")
                if caracter_anterior == "C" and (caracter != "D" and caracter != "M"):
                    raise RomanNumberError("No se puede restar C a un valor distinto de D o M")
                if caracter_anterior == "V" or caracter_anterior == "L" or caracter_anterior == "D":
                    raise RomanNumberError("No se puede restar V o L o D")
                if caracter_anterior == compro and (caracter_anterior == "I" or caracter_anterior == "X" or caracter_anterior == "C"):
                    raise RomanNumberError("No se puede restar mas de dos veces I o C o X")
                

                
                r -= self.simbolo_romano[caracter_anterior] * 2
            compro = caracter_anterior

            r += self.simbolo_romano[caracter]
            caracter_anterior = caracter
            
        #print(r)
        return r
    
    def __add__(self, otro):
        if isinstance(otro, NumeroRomano):
            return NumeroRomano(self.valor + otro.valor)
        elif isinstance(otro, int):
            return NumeroRomano(self.valor + otro)
        elif isinstance(otro, float):
            return NumeroRomano(self.valor + int(otro))

    
    def __radd__(self, otro):
        if isinstance(otro, int):
            return NumeroRomano(otro + self.valor)
        elif isinstance(otro, float):
            return NumeroRomano(self.valor + int(otro))
        #return self__add__(otro)

    def __mul__(self, otro):
        if isinstance(otro, NumeroRomano):
            return NumeroRomano(self.valor * otro.valor)
        elif isinstance(otro, int):
            return NumeroRomano(self.valor * otro)
    
    def __rmul__(self, otro):
        if isinstance(otro, int):
            return NumeroRomano(otro * self.valor)

        




        
    def __repr__(self):
        return self.representacion  