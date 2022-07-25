from turtle import st
import pytest


from romano_funcional import RomanNumberError, entero_a_romano, romano_a_entero2

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

def test_romano_a_entero_no_mas_de_tres():

    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero2("LIIII")
    assert str(exceptionInfo.value) == "No se pueden dar mas de tres repeticiones"

def test_romano_a_entero_resta_si_soy_mayor_anterior():
    assert romano_a_entero2("IV") == 4

def test_romano_a_entero_d_l_v_mas_de_dos_veces():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero2("LVV")
    assert str(exceptionInfo.value) == "No se puede repetir D o L o V mas de una vez"

def test_romano_a_entero_restar_X_a_V_C():
    with pytest.raises(RomanNumberError) as exceptionInfo:
            romano_a_entero2("XD")
    assert str(exceptionInfo.value) == "No se puede restar X a un valor distinto de L o C"

def test_romano_a_entero_restar_I_a_V_X():
    with pytest.raises(RomanNumberError) as exceptioninfo:
        romano_a_entero2("MIL")
    assert str(exceptioninfo.value) == "No se puede restar I a un valor distinto de X o V"

def test_romano_a_entero_restar_V_L_D():
    with pytest.raises(RomanNumberError) as exceptionInfo:
            romano_a_entero2("VX")
    assert str(exceptionInfo.value) == "No se puede restar V o L o D"

def test_romano_a_entero_restar_I_X_C():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero2("IIV")
    assert str(exceptionInfo.value) == "No se puede restar mas de dos veces I o C o X"

