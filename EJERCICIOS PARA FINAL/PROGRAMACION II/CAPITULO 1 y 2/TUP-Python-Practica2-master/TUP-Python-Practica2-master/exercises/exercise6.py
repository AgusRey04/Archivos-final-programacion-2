"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union
def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """
    numeros=[]
    string=[]
    for elemento in lista:
        if type(elemento) is int or  type(elemento) is float:
            numeros.append(elemento)
        else:
            string.append(elemento)
    # string.extend(numeros)
    # return  string
    return  string + numeros
print(numeros_al_final_basico([3, "a", 1, "b", 10, "j"]))
# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################
from typing import List, Union

def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """
    numeros = [x for x in lista if isinstance(x,int)]
    string = [x for x in lista if isinstance(x,str)]
    return string +numeros
    
print(numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]))
# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
