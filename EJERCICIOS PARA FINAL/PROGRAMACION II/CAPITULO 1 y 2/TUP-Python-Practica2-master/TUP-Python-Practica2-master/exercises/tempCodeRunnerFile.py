from typing import Any, Iterable
def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando la funcion any.

    Restricciones:
        - No utilizar bucles.
        - Utilizar una comprensión.
        - La solución debe tener 1 línea.

    Referencia: https://docs.python.org/3/library/functions.html#any
    """
    return (x for x in lista_1 if x in lista_2)

# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
print(superposicion_any(test_list, (2, "world", 35.20)))